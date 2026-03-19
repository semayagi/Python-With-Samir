from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)    # automatically increments
                                                       # primary_key = Unique Identifier
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)  # stock keeping unit
                                            # a unique ID, too
    price = models.FloatField()
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=100)

    def __str__(self):
        return self.name
