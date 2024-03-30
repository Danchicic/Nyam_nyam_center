from django.shortcuts import render

from .models import Dish, Process_Description, Categories
from ingredients.models import Ingredient


# Create your views here.
def simple_view(request):
    dishes = Dish.objects.all()
    categories = Categories.objects.all()
    context = {"dishes": dishes, "categories": categories}
    return render(request, template_name='dishes/index.html', context=context)


def recipe_view(request, dish_address):
    dish = Dish.objects.select_related().get(address=dish_address)
    recipe = Process_Description.objects.select_related().filter(dish_id=dish.id)

    steps = {}
    c = 0
    steps['time']: int = 0
    steps['ingredient']: list[dict] = []
    steps['final_cost']: float = 0
    names = set()
    steps['cooking_process']: list[str] = []

    # creating context dict
    for step in recipe:
        if step.process_description is not None:
            # create new description row
            c += 1
            steps['cooking_process'].append(step.process_description)
            steps['time'] += int(step.time.split(' ')[0])
        # work with the outer model to count cost
        ##
        ingredient_properties = Ingredient.objects.get(name=step.ingredient)
        if ingredient_properties.price_per_unit[-1] == '$':
            # dollar units cost
            mn = float(ingredient_properties.price_per_unit[:-1])
            cost_unit = '$'
        else:
            # cents units cost
            mn = float(ingredient_properties.price_per_unit.split()[0])
            cost_unit = 'cents'

        cost = round(step.quantity * mn, 2)
        ##
        if cost_unit == 'cents':
            steps['final_cost'] += cost / 100
        else:
            steps['final_cost'] += cost
        # check double names
        if step.ingredient in names:
            for ing in steps['ingredient']:
                if ing['name'] == step.ingredient:
                    ing['quantity'] += step.quantity
                    ing['cost'] += cost
                    break
        else:
            names.add(step.ingredient)
            steps['ingredient'].append({"name": step.ingredient, "quantity": step.quantity, "unit": step.unit,
                                        "cost": cost, "cost_unit": cost_unit})
    return render(request, template_name='dishes/recipe.html', context={"dish": dish, "recipe": steps})
