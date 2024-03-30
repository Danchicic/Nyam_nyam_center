from django.db import models


# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=100)
    count_of_dishes = models.IntegerField()

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=50)
    base_servings = models.IntegerField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    image_path = models.ImageField(null=True)
    recipe_link = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    final_price = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    address = models.SlugField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name


class Process_Description(models.Model):
    process_description = models.TextField(null=True, blank=True)
    time = models.CharField(max_length=50, blank=True, null=True)
    ingredient = models.CharField(max_length=25)
    quantity = models.FloatField()
    unit = models.CharField(max_length=15)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    def __str__(self):
        return self.dish.name
