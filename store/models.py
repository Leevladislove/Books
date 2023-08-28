from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.CharField(max_length=200)

    def __str__(self):
        return f'id {self.id}: {self.name}'
