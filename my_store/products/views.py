from common.views import TitleMixin
from django.contrib.auth.decorators import \
    login_required  # Импорт декаратора на профиль пользьвателей
from django.shortcuts import \
    HttpResponseRedirect  # Импорт класса который возвращает HTTP запрос
from django.views.generic.base import \
    TemplateView  # Импорт класса котороый отвечает за отображение главной стринцы
from django.views.generic.list import \
    ListView  # Импорт класса который отвечает за посписочный вывод иноформации
from products.models import Basket, Product, ProductCategory  # Импорт моделей

# функции = контролеры = вьюхи


class IndexView(TitleMixin, TemplateView):           # Создание класса
    template_name = "products/index.html"   # назанчение переменной
    title = 'Store'


class ProductsListView(TitleMixin, ListView):   #Создаёт общую переменную object_list
    model = Product                 # Указываем модель которую будем использовать
    template_name = "products/products.html"
    paginate_by = 3                 # Создаёт переменную page_obj
    title = "Store - Каталог"
    def get_queryset(self):   # возвращение queryseta - это список объектов которые имеются в БД
        queryset = super(ProductsListView, self).get_queryset() # формирование queryseta
        category_id =self.kwargs.get('category_id') # Создание переменной для id категории
        return queryset.filter(category_id=category_id) if category_id else queryset # возврат id категория

    def get_context_data(self, *, object_list=None, **kwargs):
        # Получаем контекст данных с помощью метода get_context_data из родительского класса.
        context = super(ProductsListView, self).get_context_data()
        # Получаем все объекты модели ProductCategory и сохраняем их в контексте данных.
        context['categories'] = ProductCategory.objects.all()
        # Возвращаем обновленный контекст данных.
        return context


# Логика добовления продуктов в корзину
@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
