
# from cProfile import Profile
# from multiprocessing import context
from django.shortcuts import render
# from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from .models import  Recipe
# from .serializer import TripListSerializer,DetailSerializer,UpdateSerializer,UserRegisterserializer,CreateSerializer,ProfileDetailSerializer,ProfileUpdateSerializer
# from rest_framework.permissions import IsAuthenticated,IsAdminUser
# from rest_framework import serializers
# from .permissions import IsUser



# Create your views here.
# list Views
def get_recipies(request):
    recipes =  Recipe.objects.all()
    context = {"recipes" : recipes}
    return render(request, "home_page.html", context)

#register view   creating a profile with user
# class RegisterUserView(CreateAPIView): 
#     serializer_class = UserRegisterserializer
  
