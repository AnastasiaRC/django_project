import json
from django.core.management import BaseCommand
from blog.models import Blog


class Command(BaseCommand):
    def handle(self, *args, **options):
        blog_for_create = []
        Blog.objects.all().delete()
        with open('data_blog.json', 'r', encoding='utf-8') as f:
            data_blog = json.load(f)
            for blog in data_blog:
                id = blog['pk']
                title = blog['fields']['title']
                slug = blog['fields']['slug']
                body = blog['fields']['body']
                image = blog['fields']['image']
                date_of_creation = blog['fields']['date_of_creation']
                is_published = blog['fields']['is_published']
                views_count = blog['fields']['views_count']
                blog_for_create.append(Blog(id, title, slug, body, image, date_of_creation, is_published, views_count))
        Blog.objects.bulk_create(blog_for_create)
