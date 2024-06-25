from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here
# Users -> id, name, email, gender, address

# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)  
#     email = models.CharField(max_length=255)
#     address = models.CharField(max_length=255, null=True, blank=True)
#     gender = models.CharField(max_length=255)


class User(AbstractUser):
    address = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.username
