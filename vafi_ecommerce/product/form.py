from product.models import Product
from django.forms import ModelForm

class addProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('id','user_id',)