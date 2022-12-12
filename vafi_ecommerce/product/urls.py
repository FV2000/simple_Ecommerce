from django.urls import path
from .views import product_list,show_user_products,addProduct, deletePro
app_name = 'product'
urlpatterns = [
    path('productlist/<int:id>/', product_list, name = "product_list"),
    path('userproduct/<int:id>/', show_user_products, name = "user_product"),
    path('addproduct/<int:id>/', addProduct, name = "addproduct"),
    path('deleteproduct/<int:id>/', deletePro, name = "deleteproduct"),
]