from django.urls import \
    path  # Импорт метода path отвечающий за формирование ссылок
from products.views import ProductsListView, basket_add, basket_remove

# Здсь проходя по ссылке product из urls в корневой папке идёт до настройка

app_name = "products"  # Название приложения которое используется в корневой папке в файле urls

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'), # Отображение основоной страницы
    path('category/<int:category_id>/', ProductsListView.as_view(), name='category'), #Обарботчик ссыкли категорий если нажемать на выбор категории будет в соответсие с id категории отображать продукты которые относятся к этой категориии
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'), # Обработчик страниц и кноппок предыдущая и следующая страница
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),  # Обработчик отвечающий за кнопку "Добавить в корзину"
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'), # Обработчик удаления из корзины

]
