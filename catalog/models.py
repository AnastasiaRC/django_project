from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    title_product = models.CharField(max_length=100, verbose_name='наименование продукта')
    description_product = models.TextField(verbose_name='описание продукта')
    image = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=100, verbose_name='категория')
    price = models.FloatField(verbose_name='цена')
    date_of_creation = models.DateField(verbose_name='дата создания')
    data_last_modified = models.DateField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.title_product} {self.price} {self.category} {self.date_of_creation} {self.data_last_modified}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('title_product',)


class Category(models.Model):
    title_category = models.CharField(max_length=100, verbose_name='наименование категории')
    description_category = models.TextField(verbose_name='описание категории')

    def __str__(self):
        return f'{self.title_category} {self.description_category}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('title_category',)

