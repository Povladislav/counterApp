from django.db import models


class Category(models.Model):
    name_of_category = models.CharField(max_length=50, unique=True)
    spent_sum = models.IntegerField(null=True)

    def __str__(self):
        return self.name_of_category
