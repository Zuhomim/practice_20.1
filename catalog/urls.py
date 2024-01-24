from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, contacts, ProductListView, ProductDetailView, ProductCreateView, \
    ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='catalog'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/products/', ProductListView.as_view(), name='list_product'),
    path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='view_product'),
    path('<int:pk>/product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
]
