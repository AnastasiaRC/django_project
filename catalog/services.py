from django.core.cache import cache
from catalog.models import Category
from django.conf import settings


def get_categories():
    category_list = Category.objects.all()

    if settings.CACHE_ENABLED:
        categories = cache.get('categories')
        if categories is None:
            categories = category_list
            cache.set('categories', categories)
        return categories

    return category_list
