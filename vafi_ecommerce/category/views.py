from django.shortcuts import render
from .models import Category
# Create your views here.
def show_categories(request):
    categories = Category.objects.all()
    context = {
    "categories": categories,
    }
    return render(request, "categories.html", context)
