# Generated by Django 3.2.13 on 2022-12-06 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='نام')),
                ('name_fa', models.CharField(max_length=100, null=True, verbose_name='نام')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='نام')),
                ('name_ar', models.CharField(max_length=100, null=True, verbose_name='نام')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('description_fa', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('description_ar', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('image_url', models.FileField(blank=True, max_length=200, null=True, upload_to='gallery/', verbose_name='پروفایل')),
                ('real_price', models.IntegerField(default=0, verbose_name='قیمت اصلی')),
                ('real_price_fa', models.IntegerField(default=0, null=True, verbose_name='قیمت اصلی')),
                ('real_price_en', models.IntegerField(default=0, null=True, verbose_name='قیمت اصلی')),
                ('real_price_ar', models.IntegerField(default=0, null=True, verbose_name='قیمت اصلی')),
                ('discount_price', models.IntegerField(default=0, verbose_name='قیمت با تخفیف')),
                ('discount_price_fa', models.IntegerField(default=0, null=True, verbose_name='قیمت با تخفیف')),
                ('discount_price_en', models.IntegerField(default=0, null=True, verbose_name='قیمت با تخفیف')),
                ('discount_price_ar', models.IntegerField(default=0, null=True, verbose_name='قیمت با تخفیف')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='category.category', verbose_name='دسته')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
    ]
