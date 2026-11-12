from django.db import models
from accounts.models import CustomUser

class Event(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField(max_length=200)
    date=models.DateField()
    time=models.TimeField()
    venue=models.CharField(max_length=30)
    amount=models.IntegerField()
    organizer=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    total_seats=models.IntegerField()
    available_seats=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
