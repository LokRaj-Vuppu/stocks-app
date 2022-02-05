from django.urls import path
from .views import home, stock_data

urlpatterns = [
    path('home/', home , name='home'),
    path('stock-data/', stock_data ,name='stock-data')
]
