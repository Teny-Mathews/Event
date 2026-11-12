from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    role_choice=[('organizer','Organizer'),('customer','Customer')]
    role=models.CharField(max_length=20,choices=role_choice)
    phone = models.CharField(max_length=20, null=True)



    

