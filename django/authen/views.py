from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignUpForm, VerifyForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import random
from twilio.rest import Client
from django.conf import settings

# Create your views here.

def _send_pin(pin):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    client.messages.create(to="+919447712257",
                           from_="+12193019189",
                           body="Hello your pin is {0}!".format(pin))


@login_required
def home(request):
    if request.user.profile.is_verfied():
        return render(request,"home.html")
    else:
        return redirect('verify')

def send_pin(request):
    _send_pin(request.user.profile.pincode)
    form = VerifyForm()
    return render(request, 'verify.html', {'form': form})

@login_required
def verify(request):             #Post data username 'username' , password 'password'
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
            _send_pin(pin)
            return HttpResponseRedirect('/authen')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})



