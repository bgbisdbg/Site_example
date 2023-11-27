from django.contrib import admin

<<<<<<< HEAD
from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status')
    fields = ('id', 'created',
              ('first_name', 'last_name'),
              ('email', 'adress'),
              'basket_history', 'status', 'initiator'
              )
    readonly_fields = ('id', 'created')
=======
# Register your models here.
>>>>>>> 8470923e56e3144860044b5825601e497bc2c1d5
