from modeltranslation.translator import translator, TranslationOptions
from .models import Product

class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'real_price', 'discount_price')

translator.register(Product, ProductTranslationOptions)