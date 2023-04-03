"""sipnsavor URL Configuration

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
from django.urls import path, include
from accounts import views as account_views
from django.contrib.auth import views as auth_views

handler404 = 'recipes.views.handler404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
    path('register/', account_views.register, name='user-register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='user-logout'),
    path('mybar/', account_views.my_bar, name='my-bar'),
    path('mybar/add/', account_views.add_ingredients, name='add_ingredients'),
    path('mybar/delete/<int:pk>/', account_views.delete_ingredient, name='delete_ingredient'),
    path('mybar/recipes/', account_views.get_bar_recipes, name='search_bar_recipes'),
]
