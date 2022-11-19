from django.shortcuts import render
from django.views import View

# Create your views here.
class Sandwich_app_View(View):
    def get(self, request):
        return render(
            request=request,
            template_name= 'sandwich_app.html'
        )
