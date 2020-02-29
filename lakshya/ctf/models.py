from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default='example@gmail.com')
    phone = models.CharField(max_length=10)
    clg = models.CharField(max_length=10)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, null=True)
    dept = models.CharField(max_length=100)
    year = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


