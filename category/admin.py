from django.contrib import admin
#from django.db import models
from .models import Category


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)} #This will populate the slug field automatically with the category name
    list_display = ('category_name', 'slug')


admin.site.register(Category, CategoryAdmin)