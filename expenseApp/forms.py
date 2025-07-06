from django import forms
from expenseApp.models import Expense

class ExpenseForm(forms.ModelForm):    
    class Meta:
        model = Expense
        fields = ['name', 'amount','category']
