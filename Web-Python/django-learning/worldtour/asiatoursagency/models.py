from django.db import models

# Inherits models.Model - it provides a structured way to define the fields and behaviors of our database objects
# Blueprint for our database table
# Django's ORM (Object Relational Mapping) takes care of all the CRUD operations: Create Read Update Delete
class Tour(models.Model):
    # Character fields:
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()