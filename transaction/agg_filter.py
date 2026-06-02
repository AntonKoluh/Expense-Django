import django_filters
from .models import Transaction


class TransactionFilter(django_filters.FilterSet):
    from_date = django_filters.DateFilter(
        field_name="transaction_date",
        lookup_expr="gte"
    )
    to_date = django_filters.DateFilter(
        field_name="transaction_date",
        lookup_expr="lte"
    )
    category = django_filters.NumberFilter(
        field_name="categories__id"
    )

    class Meta:
        model = Transaction
        fields = ["from_date", "to_date", "category"]