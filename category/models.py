from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=180)
    limit = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)