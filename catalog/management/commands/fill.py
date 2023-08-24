import json
from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        product_for_create = []
        category_for_create = []
        Category.objects.all().delete()
        Product.objects.all().delete()
        with open('data_category.json', 'r', encoding='utf-8') as f:
            data_category = json.load(f)
            for category in data_category:
                id = category['pk']
                title_category = category['fields']['title_category']
                description_category = category['fields']['description_category']
                category_for_create.append(Category(id, title_category, description_category))
        with open('data_product.json', 'r', encoding='utf-8') as f:
            data_products = json.load(f)
            for product in data_products:
                id = product['pk']
                title_product = product['fields']['title_product']
                description_product = product['fields']['description_product']
                price = product['fields']['price']
                category = product['fields']['category']
                image = product['fields']['image']
                date_of_creation = product['fields']['date_of_creation']
                data_last_modified = product['fields']['data_last_modified']
                product_for_create.append(
                    Product(id=id, title_product=title_product, description_product=description_product,
                            category=Category(category),
                            image=image, price=price, date_of_creation=date_of_creation,
                            data_last_modified=data_last_modified, ))
        Category.objects.bulk_create(category_for_create)
        Product.objects.bulk_create(product_for_create)
