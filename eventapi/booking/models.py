from django.db import models
from events.models import Event
from accounts.models import CustomUser
from datetime import datetime,time,timedelta

class Booking(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    seats=models.IntegerField()
    amount=models.IntegerField()
    status_choices=[('pending','Pending'),('confirmed','Confirmed'),('expired','Expired'),('cancelled','Cancelled')]
    status=models.CharField(max_length=20,choices=status_choices,default="pending")
    ticket_code=models.CharField(max_length=50,unique=True,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def check_and_update_expiration(self):
        booking_time=self.created_at+timedelta(minutes=15)
        if datetime.now()>booking_time:
            self.status="expired"
            self.save()
        return

    
    
