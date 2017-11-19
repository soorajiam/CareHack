from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignUpForm, VerifyForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import random
from django.conf import settings
import urllib.request
import urllib.parse


# Create your views here.

def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)


@login_required
def home(request):
    if request.user.profile.is_verfied():
        return render(request,"home.html")
    else:
        return redirect('verify')

def send_pin(request):
    resp = sendSMS(settings.API_KEY, request.user.profile.phone,
                   'TXTLCL', 'Your PIN is: {0}'.format(request.user.profile.pincode))
    print(resp)
    form = VerifyForm()
    return render(request, 'verify.html', {'form': form})

@login_required
def verify(request):
    if not request.user.profile.is_verfied():
        if request.method == 'POST':
            form = VerifyForm(request.POST)
            print(form.data.get('verno'))
            print(request.user.profile.pincode)
            if(request.user.profile.pincode == int(form.data.get('verno'))):
                profile = request.user.profile
                profile.verfied = True
                profile.save()
                return HttpResponse("Success")
        else:
            form = VerifyForm()
        return render(request, 'verify.html', {'form': form})
    else:
        return redirect('home')

def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            phoneno = form.cleaned_data.get('phoneno')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password,
                                     email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            pin = random.sample(range(10**(5-1), 10**5), 1)[0]
            Profile.objects.create(user = user, phone = phoneno, pincode = pin)
            # redirect to a new URL:
            resp = sendSMS(settings.API_KEY, request.user.profile.phone,
                           'TXTLCL', 'Your PIN is: {0}'.format(request.user.profile.pincode))
            return HttpResponseRedirect('/authen')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})



