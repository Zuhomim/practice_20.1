from django.shortcuts import render

from catalog.models import Category, Product


def catalog(request):
    context = {
        'object_list': Category.objects.all(),
        'title': "TestStore",
    }
    return render(request, 'catalog/catalog.html', context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'contacts/contacts.html')


def product(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Products from {category_item.name}',
    }
    return render(request, 'product/product.html', context)
