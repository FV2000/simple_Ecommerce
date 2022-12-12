from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name="نام",max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self',verbose_name="دسته بندی والد", blank=True, null=True, related_name='children', on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "دسته بندی"
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "دسته ها"

    def get_categories(self):
        if self.parent is None:
            return self.name
        else:
            return self.parent.get_categories() + ' -> ' + self.name


    def __str__(self):
        return self.get_categories()