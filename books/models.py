from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
