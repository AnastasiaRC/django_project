from catalog.models import Product
from django.views.generic import TemplateView, ListView


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'
