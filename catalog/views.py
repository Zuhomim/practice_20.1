from django.shortcuts import render
from django.views.generic import DetailView, ListView

from catalog.models import Category, Product


class CategoryListView(ListView):
    model = Category


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'contacts/contact_list.html')

# FBV
# def catalog(request):
#     context = {
#         'object_list': Category.objects.all(),
#         'title': "TestStore",
#     }
#     return render(request, 'catalog/category_list.html', context)

# def product_info(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         "object_item": product_item,
#         "title": f'Product {product_item.name}',
#     }
#     print(context["object_item"], product_item.name)
#     return render(request, 'product/product_detail.html', context)

# def product(request, pk):
#     category_item = Category.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(category_id=pk),
#         'title': f'Products from {category_item.name}',
#     }
#     return render(request, 'product/product_list.html', context)
