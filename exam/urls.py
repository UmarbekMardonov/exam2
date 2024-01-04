from django.urls import path
from .views import CityView, CityDetailView, ShopCreate, ShopFilter, ShopListView

urlpatterns = [
    path('city/', CityView.as_view(), name='city-list'),
    path('city/<int:pk>/', CityDetailView.as_view(), name='city-detail'),
    path('shop/create/', ShopCreate.as_view(), name='shop-create'),
    path('shop/filter/', ShopFilter.as_view(), name='shop-filter'),
    path('shop/list/', ShopListView.as_view(), name='shop-list'),
]
