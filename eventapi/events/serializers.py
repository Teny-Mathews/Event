from rest_framework import serializers
from events.models import Event
from datetime import datetime


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields="__all__"

        read_only_fields=['organizer','created_at']

    def validate(self,data):
        date=data['date']
        todays_date=datetime.today().date()
        # year=datetime.today().year()
        # month=datetime.today().month()
        if date<todays_date:
            raise serializers.ValidationError("Invalid data")
        
        return data