from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    bio = models.TextField()
    city = models.CharField( max_length = 20 )
    country = models.CharField( max_length = 20 )
    phonenumber = PhoneNumberField()
    birth_date = models.DateField()