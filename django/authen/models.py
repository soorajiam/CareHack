from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    phone = models.IntegerField()
    verfied = models.BooleanField(default=False)
    pincode = models.IntegerField(null=True,blank=True)

    def is_verfied(self):
        return self.verfied

    def __str__(self):
        return self.user.username

