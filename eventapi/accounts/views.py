from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated 

class Register(APIView):
    def post(self, request):
        serializer_instance = UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

class Logout(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        self.request.user.auth_token.delete()
        return Response({'message': 'Logged out successfully'},status=status.HTTP_200_OK)