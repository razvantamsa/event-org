from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='profile' )
    bio = models.TextField(null=True)
    city = models.CharField( max_length = 20, null=True )
    country = models.CharField( max_length = 20, null=True )
    phonenumber = PhoneNumberField(null=True)
    birth_date = models.DateField(null=True)
    profile_picture = models.ImageField(upload_to='images/')