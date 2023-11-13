"""
URL configuration for my_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings  # Импорт осноных настроек сюда
from django.conf.urls.static import static  # Для работы со статикой
from django.contrib import admin  # Импорт админ панели
from django.urls import (  # Импорт метода path отвечающий за формирование ссылок, чтобы подключить другие URL-шаблоны. Она используется для создания "вложенных" URL-шаблонов, чтобы разделить маршрутизацию на более модульные и управляемые части.
    include, path)
from products.views import \
    IndexView  # Импорт класоового представление из файла views для работы со странице с продуктами

urlpatterns = [
    path('admin/', admin.site.urls),  # Урл адрес в админ панель
    path("", IndexView.as_view(), name="index"),  # Урл на главную страницу
    path("products/", include('products.urls', namespace='products')),  # Урл на католог ссылка с продуктами
    path("users/", include('users.urls', namespace='users')),  # Урл на Пользовательский интерфейс
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
