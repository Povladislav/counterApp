from django.db import models


class Category(models.Model):
    name_of_category = models.CharField(max_length=50, unique=True, blank=True)

