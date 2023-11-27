from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
<<<<<<< HEAD
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иван'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'you@example.com'}))
    adress = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Россия, Москва, ул. Мира, дом 6'}))



=======
>>>>>>> 8470923e56e3144860044b5825601e497bc2c1d5
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'adress')