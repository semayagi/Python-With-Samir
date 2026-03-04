from django.db import models

# Inherits models.Model - it provides a structured way to define the fields and behaviors of our database objects
# Blueprint for our database table
# Django's ORM (Object Relational Mapping) takes care of all the CRUD operations: Create Read Update Delete
# Django always adds ID automatically (self.id)
# Also Django increments it automatically (1st object has ID=1, 2nd has ID=2, ...)
class Tour(models.Model):
    # Character fields:
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()
    
    # This is a string representation of the tours
    def __str__(self):
        return (f"ID={self.id}: From {self.origin_country} To {self.destination_country}, {self.number_of_nights} nights costs ${self.price}")