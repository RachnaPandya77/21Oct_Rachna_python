from django.db import models

# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.username

