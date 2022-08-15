from django.contrib import admin

from .models import Recipe, Ingredient, Profile, Category
# Register your models here.
myModels = [Recipe, Ingredient, Profile, Category]
admin.site.register(myModels)

