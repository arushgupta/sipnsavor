from django.http import Http404
from django.db import IntegrityError
from recipes.recipe_getter import RecipeGetter
from django.shortcuts import render, redirect
from recipes.models import Tags, Ingredient
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from recipes.models import UserRecipe

def home(request):
    if request.method == 'GET':
        query = request.GET.get('cocktail')
        if query:
            cocktail = RecipeGetter.simple_search_cocktails(query)
            return render(request, 'recipes/recipe.html', {'recipe': cocktail, 'type': 'dd'})

    trending_recipes = RecipeGetter.trending()
    
    popular_recipes = RecipeGetter.popular()[:10]

    new_recipes = RecipeGetter.new()

    context = {
        'trending': trending_recipes,
        'popular': popular_recipes,
        'new': new_recipes
    }
    return render(request, 'recipes/home.html', context)

def recipe_detail(request, *args, **kwargs):
    db = kwargs.get("type")
    drink_id = kwargs.get("drink_id")
    recipe_detail = RecipeGetter.detail(db, drink_id)
    
    if db not in {'cd', 'dd'} or recipe_detail == "None":
        raise Http404("Page not found")
    
    context = {
        'type': db,
        'recipe': recipe_detail
    }
    return render(request, 'recipes/recipe.html', context)

def about(request):
    return render(request, 'recipes/about.html')

@login_required
def recipe_saver(request):
    if request.method == 'POST':
        
        db_type = request.POST.get('db_type')
        recipe_id = request.POST.get('recipe_id')
        cocktail_name = request.POST.get('cocktail_name')
        alcoholic = True if request.POST.get('alcoholic') == "0" else False

        try:
            if db_type == 'dd':
                description = request.POST.get('description')
                tags = request.POST.getlist('tags')
                user_recipe = UserRecipe.objects.create(
                    user=request.user,
                    recipe_id=recipe_id,
                    recipe_name=cocktail_name,
                    recipe_description=description,
                    recipe_alcoholic=alcoholic,
                    recipe_db_type=db_type,
                    recipe_tags=tags,
                )
            else:
                instructions = request.POST.get('instructions')
                image_url = request.POST.get('image_url')
                user_recipe = UserRecipe.objects.create(
                    user=request.user,
                    recipe_id=recipe_id,
                    recipe_name=cocktail_name,
                    recipe_instructions=instructions,
                    recipe_alcoholic=alcoholic,
                    recipe_db_type=db_type,
                    recipe_image_url=image_url
                )
            messages.success(request, _('This cocktail has been added to your collection!'))
        
        except IntegrityError:
            messages.warning(request, _('This cocktail is already in your collection.'))

        return redirect('recipe-detail', type=db_type, drink_id=recipe_id)
    return render(request, 'recipes/collection.html')

def handler404(request, exception):
    return render(request, 'recipes/404.html', status=404)

def advanced_search(request):
    if request.method == 'GET':
        if 'ingredients' in request.GET:
            ingredients = ",".join(request.GET.getlist('ingredients'))
            cocktails = RecipeGetter.bar_cocktails(ingredients)
            return render(request, 'recipes/recipe_list.html', {'cocktails': cocktails})
        elif 'tags' in request.GET:
            tags = ",".join(request.GET.getlist('tags'))
            cocktails = RecipeGetter.tag_search(tags)
            return render(request, 'recipes/recipe_list.html', {'cocktails': cocktails})

    tags = Tags.objects.all()
    ingredients = Ingredient.objects.all()

    return render(request, 'recipes/advanced_search.html', {'ingredients': ingredients, 'tags': tags})