from django.db.models.signals import post_save,post_delete
from .models import Booking
import uuid
from django.dispatch import receiver

@receiver(post_save,sender=Booking)
def update_after_status_changes(sender,instance,created,**kwrgs):
    if instance.status=="confirmed" and not(instance.ticket_code):
        code=f"TICK-{uuid.uuid4().hex[:8]}"
        instance.ticket_code=code
        instance.save(update_fields=["ticket_code"])

        event=instance.event
        event.available_seats -= instance.seats
        event.save(update_fields=['available_seats'])

    elif instance.status == "cancelled":
        if instance.ticket_code:
            event=instance.event
            event.available_seats += instance.seats
            event.save(update_fields=['available_seats'])
            instance.ticket_code=" "
            instance.save(update_fields=['ticket_code'])

@receiver(post_delete,sender=Booking)
def updated_seats_after_deletion(sender,instance,**kwargs):
    if instance.status=="confirmed" and instance.ticket_code==" ":
        event=instance.event
        event.available_seats+=instance.seats
        event.save(update_fields=["available_seats"])
        





