from category.models import Category
from .models import Product
from user.models import User
from .form import addProductForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
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

def show_user_products(request,id):
    user = User.objects.get(pk=id)
    products = Product.objects.filter(user_id = user)
    productform = addProductForm()
    context = {
        "user": user,
        'products': products,
        "productform": productform,
    }
    return render(request, "user_products.html", context)
def addProduct(request,id):
    if request.method == 'POST':
        user = User.objects.get(id = id)
        if user.onuse + 1 > user.limit:
            return HttpResponse('You cannot add product over limitation!')

        productform = addProductForm(request.POST, request.FILES)
        if productform.is_valid():
            obj = productform.save(commit=False)
            user = User.objects.get(id = id)
            obj.user_id_id = id
            user.onuse = user.onuse + 1
            user.save()
            obj.save()
    return redirect("product:user_product", id=id)


def deletePro(request, id):
    if request.POST.get('delete'):
        Product.objects.filter(id=request.POST.get('delete')).delete()
        user = User.objects.get(id = id)
        user.onuse -= 1
        user.save()
        return redirect("product:user_product", id=id)
