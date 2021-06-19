from django.urls import path
from .views import HomePageView, ConfirmSaleView, SaleList, UpdatedPriceList

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('sales/', SaleList.as_view(), name='sales-list'),
    path('<slug>/', ConfirmSaleView.as_view(), name='confirm-sale'),
    path('updated-price/<slug>/', UpdatedPriceList.as_view(), name='updated-price'),
]
