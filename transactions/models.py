from django.db import models
from django.utils import timezone


class Transaction(models.Model):
    sum = models.IntegerField()
    time = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('categories.Category', related_name='related_transaction', on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Transaction{self.id}"
