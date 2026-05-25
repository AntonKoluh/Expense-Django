from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    http_method_names = ["get", "post"]

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)
    
    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminUser()]

        return [IsAuthenticated()]
