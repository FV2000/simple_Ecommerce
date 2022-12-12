from django.db import models

# Create your models here.

class Comment(models.Model):
    user_id = models.ForeignKey("user.User" , on_delete=models.PROTECT,verbose_name='کاربر')
    product_id = models.ForeignKey("product.Product" , on_delete=models.PROTECT,verbose_name='محصول')
    message = models.TextField(null=True, verbose_name="نظر شما")

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'



    def __str__(self):
        return self.product_id.name.__str__()