from django import template

register = template.Library()

@register.filter
def get_range(value):
    return range(value)

@register.filter
def get_ingredient(recipe, counter):
    counter += 1
    ingredient = "strIngredient" + str(counter)
    return recipe[ingredient]

@register.filter
def get_measure(recipe, counter):
    counter += 1
    measure = "strMeasure" + str(counter)
    if recipe[measure] == None or "":
        return ""
    else:
        return recipe[measure]