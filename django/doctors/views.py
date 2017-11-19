from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Doctor,Appointment,Department
from .forms import AppointmentForm
# Create your views here.

@login_required
def view_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/view_doctors.html', {'doctors': doctors})

@login_required
def view_doctor(request, pk):
    doctor = Doctor.objects.get(pk=pk)
    return render(request, 'doctors/view_doctor.html', {'doctor': doctor})

@login_required
def create_appointment(request, pk):
    doctor = Doctor.objects.get(pk=pk)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AppointmentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            time = form.cleaned_data.get('time')
            time_zone = form.cleaned_data.get('time_zone')
            Appointment.objects.create(user=request.user, doctor=doctor,time=time,time_zone=time_zone)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AppointmentForm()

    return render(request, 'appointment_form.html', {'form': form})


def main(request):
    dept=Department.objects.all()
    doc=Doctor.objects.all()
    app=Appointment.objects.all(user=request.user)
    return render(request,'main.html',{'dept':dept,'doc':doc,'app':app})
