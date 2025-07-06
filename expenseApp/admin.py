from django.contrib import admin

# Register your models here.
from expenseApp.models import Expense

admin.site.register(Expense)