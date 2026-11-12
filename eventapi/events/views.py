from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from.permissions import IsOrganizerOrReadOnly
from django.shortcuts import get_object_or_404

class Eventlistcreate(APIView):
    permission_classes=[TokenAuthentication]
    permission_classes=[IsOrganizerOrReadOnly]
    def get(self,request):
        e=Event.objects.all()
        serializer_instance=EventSerializer(e,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer_instance = EventSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(organizer=request.user)
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)



class EventRetrieveUpdateDelete(APIView):

    permission_classes=[TokenAuthentication]
    permission_classes=[IsOrganizerOrReadOnly]

    def get(self, request, i):
        e = get_object_or_404(Event, id=i)
        serializer_instance = EventSerializer(e) 
        return Response(serializer_instance.data, status=status.HTTP_200_OK)

    def put(self, request, i):
        e = get_object_or_404(Event, id=i)
        serializer_instance = EventSerializer(e, data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_200_OK)
        return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, i):
        e = Event.objects.get(id=i)
        serializer_instance = EventSerializer(e, request.data, partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, i):
        e = get_object_or_404(Event, id=i)
        e.delete()
        return Response({"Message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)




