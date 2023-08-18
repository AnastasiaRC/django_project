from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.datetime_safe import date
from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):

        product_list = [
            {'title_product': 'Молоко', 'description_product': 'Milk', 'category': 'Молочные продукты', 'price': 1.87,
             'date_of_creation': date.today(), 'data_last_modified': date.today()},
            {'title_product': 'Говядина', 'description_product': 'Beef', 'category': 'Мясные продукты', 'price': 5.49,
             'date_of_creation': date.today(), 'data_last_modified': date.today()},
            {'title_product': 'Помидор', 'description_product': 'Tomato', 'category': 'Овощи', 'price': 3.99,
             'date_of_creation': date.today(), 'data_last_modified': date.today()},
            {'title_product': 'Огурец', 'description_product': 'Cucumber', 'category': 'Овощи', 'price': 1.59,
             'date_of_creation': date.today(), 'data_last_modified': date.today()},
            {'title_product': 'Яблоко', 'description_product': 'Аpple', 'category': 'Фрукты', 'price': 2.49,
             'date_of_creation': date.today(), 'data_last_modified': date.today()},
            {'title_product': 'Виноград', 'description_product': 'Grape', 'category': 'Фрукты', 'price': 5.99,
             'date_of_creation': date.today(), 'data_last_modified': date.today()},
            {'title_product': 'Батон', 'description_product': 'Baton', 'category': 'Хлебобyлочные изделия',
             'price': 0.95,
             'date_of_creation': date.today(), 'data_last_modified': date.today()},
            {'title_product': 'Йогурт', 'description_product': 'Yogurt', 'category': 'Молочные продукты', 'price': 1.25,
             'date_of_creation': date.today(), 'data_last_modified': date.today()}
        ]

        product_for_create = []
        for product_item in product_list:
            product_for_create.append(Product(**product_item))
        now = timezone.now()
        x = Product.objects.filter(date_of_creation=now)
        if x:
            x.delete()
            Product.objects.bulk_create(product_for_create)
        else:
            Product.objects.bulk_create(product_for_create)
