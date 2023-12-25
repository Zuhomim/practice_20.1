from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, contacts, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='catalog'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/products/', ProductListView.as_view(), name='list_product'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='view_product')
]
