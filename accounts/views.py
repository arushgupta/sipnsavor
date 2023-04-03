from accounts import my_forms
from recipes.recipe_getter import RecipeGetter
from recipes.models import UserIngredient, Ingredient

from django.urls import reverse
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = my_forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username}, your account has been created, please login.")
            return redirect('user-login')
    else:
        form = my_forms.UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def my_bar(request):
    user_ingredients = UserIngredient.objects.filter(user=request.user).select_related('ingredient').order_by('ingredient__type', 'ingredient__name')
    all_ingredients = Ingredient.objects.all().order_by('type', 'name')
    return render(request, 'accounts/my_bar.html', {'user_ingredients': user_ingredients, 'all_ingredients': all_ingredients})

@login_required
def add_ingredients(request):
    if request.method == 'POST':
        ingredients = request.POST.getlist('ingredients')
        for ingredient_id in ingredients:
            ingredient = get_object_or_404(Ingredient, id=ingredient_id)
            user_ingredient, created = UserIngredient.objects.get_or_create(user=request.user, ingredient=ingredient)
            if created:
                messages.success(request, f"Added {ingredient.name} to your bar.")
    return redirect('my-bar')
    
@login_required
def delete_ingredient(request, pk):
    user_ingredient = get_object_or_404(UserIngredient, id=pk, user=request.user)
    if request.method == 'POST':
        user_ingredient.delete()
        messages.success(request, f"Removed {user_ingredient.ingredient.name} from your bar.")
        return redirect('my-bar')
    else:
        return render(request, 'accounts/confirm_delete.html', {'user_ingredient': user_ingredient})

@login_required
def get_bar_recipes(request):
    # Get all UserIngredient objects for the given user
    user_ingredients = UserIngredient.objects.filter(user=request.user)
    
    # Extract the names of each ingredient and join them with commas
    ingredient_names = ','.join([ui.ingredient.name for ui in user_ingredients])
    
    cocktails = RecipeGetter.bar_cocktails(ingredient_names)
    return render(request, 'recipes/recipe_list.html', {'cocktails': cocktails})
