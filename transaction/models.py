from django.db import models
from category.models import Category
from django.contrib.auth.models import User

TYPE_CHOICE = [
    ('E', 'expense'),
    ('I', 'income')
]

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(choices=TYPE_CHOICE, default='expense')
    notes = models.TextField(null=True, blank=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)