

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RecipeForm, RegisterForm, LoginForm, IngredientForm, CategoryForm
from .models import  Recipe, Category
# from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser







############### USER ###############
#Logout
def logout_view(request):
    logout(request)
    return redirect("login_user")

#Signin
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

    return render(request, 'login_page.html', context)


# Signup
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
def get_recipies(request):
    recipes =  Recipe.objects.all()
    context = {"recipes" : recipes}
    return render(request, "home_page.html", context)

# details View
def get_recipe(request, recipe_id):

    recipe = Recipe.objects.get(id=recipe_id)

    context= {
        'recipe':{
            'food_name' :recipe.food_name ,
            'profile'   : recipe.profile ,
            'image'     : recipe.image,
            'recipe'    :recipe.recipe ,
            'ingredient': recipe.ingredient,
            'category'  : recipe.category,                       
        }
    }
    return render(request, "recipe_details.html",context)


# list of cato
def get_category(request):
    category =  Category.objects.all()
    context = {"category" : category}
    return render(request, "category_list_page.html", context)


#Creat Category
def create_category(request):
    form = CategoryForm()
    if request.method =="POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form. save(commit=False)
            category.save()
            return redirect('add_category')
    context = {
        "form" : form
    }
    return render(request, 'add_category.html', context)

# Creat Ingredients
def create_ingredients(request):
    form =IngredientForm()

    if request.method == "POST":
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit= False)
            ingredient.save()
            return redirect('create_ingredients')
        
    context = {
        "form" : form
    }
    
    return render(request,'add_ingredient.html', context)


# Create Recipe:   
def create_recipe(request):
    
    form =RecipeForm()
    form2 = IngredientForm()
    form3 = CategoryForm()
    
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit= False)
            print(dir())
            recipe.profile = request.user.profile   
            recipe.save()
            return redirect('get_recipies')
        
    context = {
        "form" : form,
        "form2" : form2,
        "form3" : form3
    }
    
    return render(request,'create_recipe.html', context)


# Update Recipe
def update_recipe(request, recipe_id ):
    
        
    recipe = Recipe.objects.get(id = recipe_id)
    form = RecipeForm(instance= recipe)

    if request.method == "POST":
        form =RecipeForm(request.POST, request.FILES,instance= recipe)
        if form.is_valid():
            form.save()
            return redirect("get_recipies")
    context = {
        "form" : form,
        "recipe" : recipe
    }
    
    
    return render(request, "Update_recipe.html", context)