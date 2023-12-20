from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import catalog, contacts, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', catalog, name='catalog'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/products/', product, name='product')
]