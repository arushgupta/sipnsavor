from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

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
