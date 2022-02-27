from distutils.command.upload import upload
from pyexpat import model
from turtle import title
from django.db import models

class Mandate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images")
    desription = models.TextField(max_length=500)
