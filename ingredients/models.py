from django.db import models


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    price_per_unit = models.CharField(max_length=50)
    main_unit = models.CharField(max_length=15)
    available = models.IntegerField()
