# Generated by Django 3.2.13 on 2022-12-06 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
                ('name_fa', models.CharField(max_length=200, null=True, verbose_name='نام')),
                ('name_en', models.CharField(max_length=200, null=True, verbose_name='نام')),
                ('name_ar', models.CharField(max_length=200, null=True, verbose_name='نام')),
                ('slug', models.SlugField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='category.category', verbose_name='دسته بندی والد')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته ها',
                'unique_together': {('slug', 'parent')},
            },
        ),
    ]