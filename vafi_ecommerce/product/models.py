from django.db import models

# Create your models here.

class Product(models.Model):
    user_id = models.ForeignKey("user.User" , on_delete=models.CASCADE,verbose_name="کاربر")
    category_id = models.ForeignKey("category.Category" , on_delete=models.PROTECT,verbose_name='دسته')
    name = models.CharField(max_length=100 , null=True,verbose_name='نام')
    description = models.TextField( null=True,verbose_name='توضیحات',blank=True)
    image_url = models.FileField(max_length=200, null=True,blank=True, verbose_name="پروفایل",upload_to='gallery/')
    real_price = models.IntegerField(default=0,verbose_name='قیمت اصلی')
    discount_price = models.IntegerField(default=0,verbose_name='قیمت با تخفیف')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name.__str__()

