from django.urls import path

from .views import SimpleCandlestickWithPandas

urlpatterns = [

    path('dashboard', SimpleCandlestickWithPandas.as_view(),name='simple-candlestick'),

]