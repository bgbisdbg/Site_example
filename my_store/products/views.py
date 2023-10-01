from django.shortcuts import render
from products.models import ProductCategory, Product
# Create your views here.
# функции = контролеры = вьюхи

def index(request):
    context = {
        "title": "Test Title",
    }
    return render(request, "products/index.html", context)  # render принимает два обязательных параметра
    # request и ссылка на html файл


def products(request):
    context = {
        "title": "Store - Каталог",
        "products": Product.objects.all(),
        "categories": ProductCategory.objects.all(),
    }

    return render(request, "products/products.html", context)

