from django import forms
from stockapp.models import Stock

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'