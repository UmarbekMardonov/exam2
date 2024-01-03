from rest_framework import serializers
from .models import City, Street, Shop


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class CityDetail(serializers.ModelSerializer):
    # city = City.objects.all()

    class Meta:
        model = Street
        fields = ('id', 'title',)


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"
