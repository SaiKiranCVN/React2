from rest_framework import serializers
from .models import *


class AddressSerial(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'


class CurrSerial(serializers.ModelSerializer):
    class Meta:
        model = Currencies
        fields = '__all__'

class InvenSerial(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

class BankSerial(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class ItemSerial(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class PriceSerial(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'



class TradeSerial(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = '__all__'

