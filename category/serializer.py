from .models import Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "limit", "user"]