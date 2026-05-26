from rest_framework import viewsets
from .models import Transaction
from .serializer import TransactionSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class TransactionView(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    http_method_names = ["get", "post"]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Transaction.objects.all()
        return Transaction.objects.filter(user_id=self.request.user.id)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)