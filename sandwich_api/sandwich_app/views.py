# Create your views here.
from django.shortcuts import render
from django.views import View
from django.http import Http404
import random



ingredients = {
    'meats':['Turkey', 'Veggie Burger', 'Ham'],
    'cheeses': ['Provolone', 'Pepper Jack', 'Fondue'],
    'toppings': ['Onions', 'Cream Cheese', 'Relish']
}
class SandwichappView(View):
    def get(self, request):
        return render(
            request = request,
            template_name = 'sandwichapp.html',
            context = {'ingredients': ingredients.keys()}
        )

class IngredientsListView(View):
    def get(self, request, ingredient_type):
        if ingredient_type not in ingredients:
            raise Http404(f'No such ingredient: {ingredient_type}')
        return render(
            request = request,
            template_name = 'ingredients_list.html',
            context= {
                'ingredients': ingredients[ingredient_type],
                'ingredient_type': ingredient_type,
            }
        )

class SandwichGeneratorView(View):
    def get(self, request):
        selected_meat = random.choice(ingredients['meats'])
        selected_cheese = random.choice(ingredients['cheeses'])
        selected_toppings = random.choice(ingredients['toppings'])
        sandwich = f'{selected_meat} & {selected_cheese} with {selected_toppings}'
        return render(
            request, 'sandwich_generator.html', 
            context = {'sandwich' : sandwich}
            )

class SandwichMenuView(View):
    def get(self, request):
        return render(
            request = request,
            template_name = 'sandwichmenu.html',
            context = {'ingredients': ingredients.keys()}
        )
        