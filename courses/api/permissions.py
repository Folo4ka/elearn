from rest_framework.permissions import BasePermission
from ..models import Content


class IsEnrolled(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.students.filter(id=request.user.id).exists()
