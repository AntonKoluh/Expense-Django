from .models import Transaction
from category.models import Category
from rest_framework import serializers


class TransactionSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.none()
    )

    category_names = serializers.SlugRelatedField(
        source="categories",
        many=True,
        read_only=True,
        slug_field="name"
    )

    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Transaction
        fields = [
            "id",
            "amount",
            "type",
            "notes",
            "user",
            "categories",
            "category_names",
            "transaction_date",
        ]

    def validate_amount(self, amount):
        if amount < 0:
            raise serializers.ValidationError("Amount cannot be negative")
        
        max_limit = max([x.limit for x in self.categories])

        if amount > max_limit:
            raise serializers.ValidationError("Cannot exceed set limit")
        
        return amount

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get("request")

        if request and request.user.is_authenticated:
            queryset = Category.objects.filter(user=request.user)

            self.fields["categories"].child_relation.queryset = queryset