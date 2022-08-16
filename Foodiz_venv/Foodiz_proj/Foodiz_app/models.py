from asyncio.windows_events import NULL
from email.mime import image
from pyexpat import model
from unicodedata import category
from django.db import models


#  https://www.youtube.com/watch?v=VJo-LNav6rU // Django - Models + Relationships

from django.contrib.auth.models import User
"""
IN_CLASS_VARIABLE = models.OneToOneField(
    CLASS_NAME_RELASHIN, on_delete=models.CASCADE, related_name="NAME_OF_THE_CLASS"
    
    IN_CLASS_VARIABLE = models.ManyToManyField(CLASS_NAME_RELASHIN, related_name="NAME_OF_THE_CLASS")
    

class Booking(models.Model):
    flight = models.ForeignKey(
        Flight, on_delete=models.CASCADE, related_name="bookings"
    )
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    passengers = models.PositiveIntegerField()


"""
# Create your models here.


class Profile(models.Model):
    
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to="media/",null=True ,blank=True)
    # Relations    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username}"

    
    
class Ingredient (models.Model):
    ingredient_name = models.CharField(max_length=255)
    
    #table name
    def __str__(self) :
        return self.ingredient_name
    

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    ingredient =models.ManyToManyField(Ingredient, related_name='ingredient')
    
    #table name
    def __str__(self) :
        return self.category_name


class Recipe (models.Model):
    food_name = models.CharField(max_length=255)
    recipe = models.TextField()
    image = models.ImageField( blank=True, null=True)
    
    # Relastions
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='recipe')
    ingredient = models.ManyToManyField(Ingredient,related_name='Recipe_ingredient')
    category = models.ManyToManyField(Category, related_name='category')
    
    
     #table name
    def __str__(self) :
        return f"{self.food_name} by {self.profile.user.username}"


