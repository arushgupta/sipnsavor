from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Ingredient(models.Model):
    class IngredientType(models.IntegerChoices):
        ALCOHOL = 1, _('Alcohol')
        MIXER = 2, _('Mixer')
        GARNISH = 3, _('Garnish')

    name = models.CharField(_('Name'), max_length=50)
    type = models.PositiveSmallIntegerField(_('Type'), choices=IngredientType.choices, default=IngredientType.ALCOHOL)

    class Meta:
        verbose_name = _('Ingredient')
        verbose_name_plural = _('Ingredients')
    
    def __str__(self):
        return self.name

class UserIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('User - Ingredient')
        verbose_name_plural = _('User - Ingredients')
        unique_together = ('user', 'ingredient')
    
    def __str__(self):
        return f'{self.user.username} - {self.ingredient.name}'

class Tags(models.Model):
    uid = models.CharField(_('Unique ID'), max_length=25)
    name = models.CharField(_('Name'), max_length=50)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')
    
    def __str__(self):
        return self.name

class UserRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_id = models.CharField(max_length=50)
    recipe_name = models.CharField(max_length=250)
    recipe_description = models.TextField(blank=True, null=True)
    recipe_instructions = models.TextField(blank=True, null=True)
    recipe_alcoholic = models.BooleanField()
    recipe_db_type = models.CharField(max_length=2)
    recipe_tags = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    recipe_image_url = models.CharField(max_length=250)

    class Meta:
        verbose_name = _('User - Recipe')
        verbose_name_plural = _('User - Recipes')
        unique_together = ('user', 'recipe_id', 'recipe_db_type')
    
    def __str__(self):
        return f'{self.user.username} - {self.recipe_db_type}.{self.recipe_id}'
