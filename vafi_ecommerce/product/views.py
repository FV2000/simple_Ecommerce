from django.shortcuts import render
from category.models import Category
from .models import Product
from user.models import User
from .form import addProductForm
from itertools import chain

def product_list(request,id):
    category = Category.objects.filter(pk=id)
    cats = category.first().children.all()
    #print(list(chain(category, cats)))
    products = Product.objects.filter(category_id__in = category | cats)
    context = {
        "category": category,
        'products': products,
    }
    return render(request, "product_list.html", context)

def addProduct(request,id):
    if request.method == 'POST':
        user = User.objects.get(id = id)
        #if user.onuse + 1 > user.limit:
            #return HttpResponse('You cannot add product over limitation!')

        productform = addProductForm(request, request.FILES)
        if productform.is_valid():
            obj = productform.save(commit=False)
            user = User.objects.get(id = id)
            obj.user_id_id = id
            user.onuse = user.onuse + 1
            user.save()
            obj.save()

