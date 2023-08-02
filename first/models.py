from django.db import models

# Create your models here.
class Name(models.Model):
    name=models.CharField(max_length=122)
class Name2(models.Model):
    name=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
