class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data()
        context['title'] = self.title
        return context

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     # Получаем контекст данных с помощью метода get_context_data из родительского класса.
    #     context = super(ProductsListView, self).get_context_data()
    #     # Задаем значение ключа 'title' в контексте данных. Это будет использоваться для отображения заголовка в шаблоне.
    #     context['title'] = "Store - Каталог"
    #     # Получаем все объекты модели ProductCategory и сохраняем их в контексте данных.
    #     context['categories'] = ProductCategory.objects.all()
    #     # Возвращаем обновленный контекст данных.
    #     return context
