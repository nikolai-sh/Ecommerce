from django.urls import path
from .views import HomePageView, ItemDetailView, SaleList

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('sales/', SaleList.as_view(), name='sales-list'),
    path('<slug>/', ItemDetailView.as_view(), name='item-detail'),
]
