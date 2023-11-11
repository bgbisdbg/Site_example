from django.contrib import admin  # Импорт админки
from products.models import (  # Импорт моделей для вывода в админки в табличной форме
    Basket, Product, ProductCategory)

admin.site.register(ProductCategory)        # регистрация модели "Категории" для вывода в админки


@admin.register(Product)                  # Декаратор для регистрации класса модели "Продуктов"
class ProductAdmin(admin.ModelAdmin):     # Класс для отображение модели продуктов в админке наследуемого от
    list_display = ('name', 'price', 'quantity', 'category') # Переменная для отображения столбцов в админке
    fields = ('image', 'name', 'description', ('price', 'quantity'), 'category') # Переменная отвечающая за отображение в админке в самом продукте по строкам (можно менять местами)
    # readonly_fields = ('description',)  # Выбранное поле будет заблокированно для изменений только для чтения
    search_fields = ('name',) # Добовляет поля для поиска в данной переменной добавлен поиск по названию товара
    ordering = ('name',)  # Переменная для фильрации в алфовитном порядке (Если -name то фильрация будет в обратном порядке)


class BasketAdmin(admin.TabularInline): # Класс корзины наследуется от TabularInline Не от админ.Модел
    model = Basket # Указываем от какой модели наследуемся
    fields = ('product', 'quantity',) # № Указываем переменные которые хотим видить в админке
    extra = 0 # Переменная которая уберает 3 пусты админских строки которые добовляются автоматически
