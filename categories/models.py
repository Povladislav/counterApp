from django.db import models


class Category(models.Model):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
    name_of_category = models.CharField(max_length=50)
    spent_sum = models.IntegerField(default=0)

    def __str__(self):
        return self.name_of_category
