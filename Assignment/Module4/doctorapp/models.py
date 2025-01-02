from django.db import models

# Create your models here.

class Doctor(models.Model):
    name=models.CharField(max_length=20)
    specialization=models.CharField(max_length=20)
    experience=models.IntegerField()
    address=models.TextField()
    mobile=models.BigIntegerField()
