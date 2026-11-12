from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields="__all__"

        read_only_fields=['user','status','amount','created_at']

    def validate(self,data):
        event=data['event']
        seats=data['seats']
        if event.available_seats<seats:
            raise serializers.ValidationError("Seats are unavailable")
        return data