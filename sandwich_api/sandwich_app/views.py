# Create your views here.
from django.shortcuts import render
from django.views import View

ingredients = {
    'Meats':['Turkey', 'Veggie Burger', 'Ham'],
    'Cheeses': ['Provolone', 'Pepper Jack', 'Fondue'],
    'Toppings': ['Onions', 'Cream Cheese', 'Relish']
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
        return render(
            request = request,
            template_name = 'ingredients_list.html',
            context= {
                'ingredients': ingredients[ingredient_type],
                'ingredient_type': ingredient_type,
            }
        )