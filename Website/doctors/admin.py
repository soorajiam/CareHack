from django.contrib import admin
from .models import Doctor,Appointment,Department

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Department)
