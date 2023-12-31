# Generated by Django 4.2.4 on 2023-08-18 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_category', models.CharField(max_length=100, verbose_name='наименование категории')),
                ('description_category', models.TextField(verbose_name='описание категории')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ('title_category',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_product', models.CharField(max_length=100, verbose_name='наименование продукта')),
                ('description_product', models.TextField(verbose_name='описание продукта')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='изображение')),
                ('category', models.CharField(max_length=100, verbose_name='категория')),
                ('price', models.FloatField(verbose_name='цена')),
                ('date_of_creation', models.DateField(verbose_name='дата создания')),
                ('data_last_modified', models.DateField(verbose_name='дата последнего изменения')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'ordering': ('title_product',),
            },
        ),
    ]
