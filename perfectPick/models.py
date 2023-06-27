from email.policy import default
from tkinter import W
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField, IntegerField
from django.template import base
from django_mysql.models import ListTextField
from django.contrib.auth.models import AbstractUser
#Looked up usage of ListTextField and other List fields

# Create your models here.
class Integer(models.Model):
    movieID = models.IntegerField()

class Users(AbstractUser, models.Model):
    pass
    watchlist = models.ManyToManyField(Integer, related_name="watchlistItems")
    liked = models.ManyToManyField(Integer, related_name="liked")
