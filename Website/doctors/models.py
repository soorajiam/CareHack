from django.db import models
from timezone_field import TimeZoneField
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from datetime import datetime
from pytz import timezone, utc
from django.conf import settings

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    count=models.IntegerField(default=0)

    def __str__(self):
        return 'Department #{0} - {1}'.format(self.pk, self.name)

class Doctor(models.Model):
    name = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None, null=True)
    qualifiaction=models.CharField(max_length=200,null=True)

    def __str__(self):
        return 'Doctor #{0} - {1}'.format(self.pk, self.name)

class Appointment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None,null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,default=None,null=True)
    time = models.DateTimeField()
    time_zone = TimeZoneField(default='US/Pacific')

    # Additional fields not visible to users
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Appointment #{0}'.format(self.pk)

    def get_absolute_url(self):
        return reverse('view_appointment', args=[str(self.id)])

    def get_time(self):
        TZ = timezone(settings.TIME_ZONE)
        appoint = Appointment.objects.get(pk=1)
        aptime = appoint.time
        todatetime = datetime(aptime.year, aptime.month, aptime.day, aptime.hour, aptime.minute, aptime.second)
        time = TZ.localize(todatetime.replace(microsecond=0)).astimezone(utc).replace(tzinfo=None).isoformat() + 'Z'
        strin = ''.join(e for e in str(time) if e.isalnum())
        return strin
