from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class ProcessDescriptionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...


class CategoriesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...


class DishAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...


# Register your models here.
admin.site.register(Process_Description, ProcessDescriptionAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Dish, DishAdmin)
