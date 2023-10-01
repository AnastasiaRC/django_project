from django.urls import path
from django.views.decorators.cache import cache_page
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsTemplateView, ProductCreateView, ProductDetailView, \
    ProductUpdateView, ProductDeleteView, AccessErrorView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('view/<int:pk>/',cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('error/', AccessErrorView.as_view(), name='error'),
]
