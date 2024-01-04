from django.shortcuts import render
from rest_framework import generics, views, status
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


class ShopFilter(views.APIView):
    def get(self, request):
        street = request.query_params.get('street', '')
        city = request.query_params.get('city', '')
        open = request.query_params.get('open', None)

        queryset = Shop.objects.all()

        if street:
            queryset = Shop.objects.filter(street=street)
        if city:
            queryset = Shop.objects.filter(city=city)
        if open:
            queryset = Shop.objects.filter(open=open)
        serializer = ShopSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ShopListView(generics.ListAPIView):
    queryset = Shop.objects.all().select_related("city", "street", "street__city")
    serializer_class = ShopSerializer
