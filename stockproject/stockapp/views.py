from django.shortcuts import render, redirect

# Create your views here.
import requests
import json
from stockapp.models import Stock
from stockapp.forms import StockForm
from django.contrib import messages

def home(request):
    stockName = ''
    if request.method == "POST":
        stockName = request.POST['stockName']
        api_key = "Tp6WD2iFJXgTfhoCiXKevXySuA3cIWHM"
        url = f"https://financialmodelingprep.com/api/v3/quote/{stockName}?apikey={api_key}"
        try:
            response = requests.get(url)
            data = response.json()
        except Exception as e:
            print(f"{e} error from url")

        return render(request, 'home.html', {'data':data})
    else:
        return render (request, 'home.html',{'StockName':'Enter Correct Name for Stock'})


def about(request):
    return render(request, 'about.html', {})


def addstock(request):
    if request.method == "POST":
        form = StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'stock added successfully')
            return redirect('/addstock')
    else:
        stockName = Stock.objects.all()
        print(stockName)
        output = []
        api_key = "Tp6WD2iFJXgTfhoCiXKevXySuA3cIWHM"

        for stock in stockName:
            url = f"https://financialmodelingprep.com/api/v3/quote/{stock}?apikey={api_key}"
            try:
                response = requests.get(url)
                data = response.json()
                # print(data)
                output.append(data[0])
            except Exception as e:
                print(e)
        return render(request,'addstock.html',{'stockName':stockName, 'output':output})
    


def delete(request, pk):
    item = Stock.objects.get(pk=pk)
    item.delete()
    messages.success(request,"Stock Deleted Successfully From Portfolio")
    return redirect ("/delete_stock")


def delete_stock(request):
    stockName = Stock.objects.all()
    return render(request, 'delete.html', {'stockName':stockName})