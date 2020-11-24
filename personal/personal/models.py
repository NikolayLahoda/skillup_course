from django.db import models





class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)

class Book(models.Model):
    name = models.CharField(max_length=100)
    year_issued = models.PositiveSmallIntegerField()
    authors = models.
