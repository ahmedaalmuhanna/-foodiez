
# from cProfile import Profile
# from multiprocessing import context
from multiprocessing import context # what is this import for, where are you using this
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RecipeForm, RegisterForm, LoginForm
# from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from .models import  Recipe, Ingredient, Category


"""
Remove Unused imports
Why is context being imported from multiprocessing and why is there a commented import statement from rest_framework
KEEP YOUR CODE CLEAN!
"""

# Create your views here.

############### USER ###############

def login_user(request):
    form = LoginForm()
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            authenticate_user = authenticate(username = username, password = password )
            login(request, authenticate_user)
            return redirect('get_recipies')
    context = {
        "form" : form,
        # "user" : authenticate_user
    }
    # remove used import in the context
    return render(request, 'login_page.html', context)


def register_user(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            
            login(request,user)
            return redirect('get_recipies')
    context ={
        "form" : form
    }
    return render(request,'register_page.html',  context)
    



############### Recipies ###############
# list Views
def get_recipies(request): # function spelling issue
    recipes =  Recipe.objects.all()
    context = {"recipes" : recipes}
    return render(request, "home_page.html", context)


# # list of cato
def get_category(request):
    category =  Category.objects.all()
    test = Category.objects.get(id =8) # remove unused queries
    # print(test.ingredient.is_value)
    context = {"category" : category}
    return render(request, "category_list_page.html", context)
    # remove print statements and unused comments

# ???????#
# Create Recipe:    ## not working
def create_recipe(request):
    
    form =RecipeForm()
    
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit= False)
            recipe.profile = request.user # Recipe model is expecting a Profile instance, not a User instance, hence, why this is not working
            recipe.save()
            return redirect('get_recipies')
        
    context = {
        "form" : form
    }
    
    return render(request,'create_recipe.html', context)


# Update Recipe

# dont forget to check for permissions in this case
def update_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id = recipe_id)
    print("recipe: ",recipe) # remove print statement
    form = RecipeForm(instance= recipe)
    if request.method == "POST":
        form =RecipeForm(request.POST, request.FILES,instance= recipe)
        if form.is_valid():
            form.save()
            return redirect("get_recipies")
    context = {
        "form" : form,
        "recipe" : recipe # since we are passing the recipe instance into the form, do we need the recipe instance in the context?
    }
    
    return render(request, "Update_recipe.html", context) # template names should be lowercase