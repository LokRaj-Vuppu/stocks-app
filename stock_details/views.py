from django.shortcuts import render
from django.contrib import messages
from stock_details.models import Stocks


# for fetching form data, validating and saving to DB
def home(request):
    if request.method == 'POST':
        stock_name = request.POST['stock_name']
        quantity = request.POST['stock_quantity']
        stock_data = Stocks.objects.filter(stock_name=stock_name).exists()
        if not stock_data:
            Stocks.objects.get_or_create(stock_name=stock_name, quantity=quantity)
            messages.success(request,f'{stock_name} added to Watchlist')
        else:
            messages.error(request, f'{stock_name} already exists in Watchlist')
    return render(request, 'home.html')


# For fetching all records from DB
def stock_data(request):
    stock_details = Stocks.objects.all().order_by('-quantity')
    context = {
        'stock_details': stock_details,
    }
    return render(request,'stock-data.html', context)
