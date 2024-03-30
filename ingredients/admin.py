from django.contrib import admin
from .models import Ingredient
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class AdminIngredient(ImportExportModelAdmin, admin.ModelAdmin):
    pass


admin.site.register(Ingredient, AdminIngredient)
