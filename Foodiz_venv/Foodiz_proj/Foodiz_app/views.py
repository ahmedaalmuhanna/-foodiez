
# from cProfile import Profile
# from multiprocessing import context
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RecipeForm, RegisterForm
# from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from .models import  Recipe, Ingredient, Category




# Create your views here.

############### USER ###############
def register_user(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            
            login(request,user)
    



############### Recipies ###############
# list Views
def get_recipies(request):
    recipes =  Recipe.objects.all()
    context = {"recipes" : recipes}
    return render(request, "home_page.html", context)


# # list of cato
def get_category(request):
    category =  Category.objects.all()
    test = Category.objects.get(id =8)
    # print(test.ingredient.is_value)
    context = {"category" : category}
    return render(request, "category_list_page.html", context)


# ???????#
# Create Recipe:    ## not working
def create_recipe(request):
    
    form =RecipeForm()
    
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit= False)
            recipe.profile = request.user
    
            
            recipe.save()
            return redirect('get_recipies')
        
    context = {
        "form" : form
    }
    
    return render(request,'create_recipe.html', context)


# Update Recipe
def update_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id = recipe_id)
    form = RecipeForm(request.POST, request.FILES)
    if request.method == "POST":
        form =RecipeForm(request.POST, instance= recipe)
        if form.is_valid():
            form.save()
            return redirect("get_recipies")
    context = {
        "form" : form,
        "recipe" : recipe
    }
    
    return render(request, "Update_recipe.html", context)