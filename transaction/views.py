from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Transaction
from .serializer import TransactionSerializer
from django_filters.rest_framework import DjangoFilterBackend

from transaction.agg_filter import TransactionFilter

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

class AggregateView(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend]
    filterset_class = TransactionFilter

    def get_queryset(self):
        return (
            Transaction.objects
            .filter(user=self.request.user)
            .prefetch_related("categories")
        )

    def list(self, request, *args, **knwargs):
        queryset = self.filter_queryset(self.get_queryset()).distinct()

        total = queryset.aggregate(total=Sum("amount"))["total"] or 0

        return Response({
            "total": total
        })