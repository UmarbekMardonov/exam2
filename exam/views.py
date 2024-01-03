from django.shortcuts import render
from rest_framework import generics, views
from .models import City, Street, Shop
from .serialsizers import CitySerializer, CityDetail, ShopSerializer
from rest_framework.response import Response


class CityView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetailView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetail


class ShopCreate(generics.CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
