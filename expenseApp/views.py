from django.shortcuts import render, redirect
from expenseApp.forms import ExpenseForm
from expenseApp.models import Expense
from django.db.models import Sum
import datetime
import json
# Create your views here.

def index(request):
    if request.method == "POST":
        data = ExpenseForm(request.POST)
        if data.is_valid():
            data.save()
    expenses = Expense.objects.all()
    # total_expense = expenses.aaggregate(Sum('amount'))
    total_expense = expenses.aggregate(Sum('amount'))['amount__sum'] 

    '''logic for calculating monthly,yearly, weekly expense'''
    yearly = datetime.date.today() - datetime.timedelta(days=365)
    data = Expense.objects.filter(date__gt=yearly)
    yearly_sum = data.aggregate(Sum('amount'))

    monthly = datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(date__gt=monthly)
    monthly_sum = data.aggregate(Sum('amount'))

    weekly = datetime.date.today() - datetime.timedelta(days=7)
    data = Expense.objects.filter(date__gt=weekly)
    weekly_sum = data.aggregate(Sum('amount'))

    daily_sum = Expense.objects.filter().values('date').order_by('date').annotate(sum=Sum('amount'))

    category_sum = Expense.objects.filter().values('category').order_by('category').annotate(sum=Sum('amount'))

    form = ExpenseForm()
    return render(request,'expenseApp/index.html',
                  {'form':form, 
                   'expenses':expenses,
                   'total_expense':total_expense,
                   'yearly_sum':yearly_sum,
                   'monthly_sum':monthly_sum,
                   'weekly_sum':weekly_sum,
                   'daily_sum':daily_sum,
                   'category_sum':category_sum,})

def edit(request, id):
    data = Expense.objects.get(id = id)
    expense_form = ExpenseForm(instance=data)
    if request.method == "POST":
        data = Expense.objects.get(id=id)
        expense_form = ExpenseForm(request.POST, instance=data)
        if expense_form.is_valid:
            expense_form.save()
            return redirect('index')

    return render(request, 'expenseApp/edit.html',{'expense_form':expense_form})


def delete(request, id):
    data = Expense.objects.get(id=id)
    if request.method=="POST":
        data.delete()
        return redirect('index')
    return render(request,'expenseApp/delete.html',{'data':data})

    # if request.method=="POST":
    #     data = Expense.objects.get(id=id)
    #     data.delete()
    # return redirect('index') #you can delete directly in this way but you need to add form action for this delete to handle POST request in index.html
    #like in above code we handling POST request for delete in delete.html . same like we can do directly in index.html itself, which dont require confirm delete.
