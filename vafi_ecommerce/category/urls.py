from django.urls import path
from .views import show_categories
app_name = 'category'
urlpatterns = [
    path('categorylist/', show_categories, name = "category_list"),
]