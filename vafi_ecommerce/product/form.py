from product.models import Product
from django.forms import ModelForm

class addProductForm(ModelForm):
    class Meta:
        model = mProduct
        fields = '__all__'
        exclude = ('user_id',)