from rest_framework import permissions
from accounts.models import CustomUser

class IsOrganizerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method=="GET":
            return True
        else:
            return request.user.is_authenticated and request.user.role=="organizer"
    

    def has_object_permission(self, request, view, obj):
        if request.method=="GET":
            return True
        else:
            return obj.organizer==request.user