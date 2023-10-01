from django.forms import inlineformset_factory
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from catalog.services import get_categories


class AccessErrorView(TemplateView):
    template_name = 'catalog/error.html'


class AccessСheckMixinView(View):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('catalog:error')
        return super().dispatch(request, *args, **kwargs)


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()
        context_data['category_list'] = get_categories()
        return context_data


class ProductCreateView(AccessСheckMixinView, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        if form.is_valid():
            product = form.save()
            product.author = self.request.user
            product.save()
        return super().form_valid(form)


class ProductUpdateView(AccessСheckMixinView, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        active_versions = Version.objects.filter(product=self.object, is_active=True)
        if active_versions.count() > 1:
            form.add_error(None, 'Невозможно выбрать несколько версий')
            return self.form_invalid(form)
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(AccessСheckMixinView, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'
