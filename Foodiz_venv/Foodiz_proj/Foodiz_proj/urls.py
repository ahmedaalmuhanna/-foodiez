"""Foodiz_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Foodiz_app.views import get_recipies,logout_view, create_recipe, create_category, create_ingredients, update_recipe, get_category,get_recipe, register_user, login_user
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("recipe/",get_recipies, name = "get_recipies"),
    path("create_recipe/",create_recipe, name = "create_recipe"),
    path("create_ingredient/",create_ingredients, name = "create_ingredients"),
    path("add_category/",create_category, name = "add_category"),
    path("update_recipe/<int:recipe_id>",update_recipe, name = "update_recipe"),
    path("category_list_page/",get_category, name = "get_category"),
    path("register/",register_user, name ="register_user"),
    path("login/",login_user, name ="login_user"),
    path("recipe_details/<int:recipe_id>",get_recipe, name ="recipe_details"),
    path("logout/",logout_view, name ="logout"),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)