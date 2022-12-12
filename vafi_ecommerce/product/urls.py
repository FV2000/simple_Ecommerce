from django.urls import path
from .views import product_list
app_name = 'product'
urlpatterns = [
    path('productlist/<int:id>/', product_list, name = "product_list"),
]