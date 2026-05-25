from rest_framework import viewsets
from .models import Category
from .serializer import CategorySerializer
from rest_framework.permissions import IsAuthenticated

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    http_method_names = ["get", "post"]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Category.objects.all()
        return Category.objects.filter(user_id=self.request.user.id)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)