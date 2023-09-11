from django.shortcuts import render

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
        "products": [
            {
                "image" : "/static/vendor/img/products/Adidas-hoodie.png",
                "name" : "Худи черного цвета с монограммами adidas Originals",
                "prise" : 6090,
                "description" : "Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни",
            },
            {
                "image" : "/static/vendor/img/products/Blue-jacket-The-North-Face.png",
                "name" : "Синяя куртка The North Face",
                "prise" : 23725,
                "description" : "Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.",
            },
            {
                "image" : "/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png",
                "name" : "Коричневый спортивный oversized-топ ASOS DESIGN",
                "prise" : 3390,
                "description" : "Материал с плюшевой текстурой. Удобный и мягкий",
            }
        ]
    }
    return render(request, "products/products.html", context)