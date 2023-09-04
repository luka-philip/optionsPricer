# serializers.py
from rest_framework import serializers
from .models import OptionType, Asset, Option, ProfitLoss

class OptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionType
        fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class ProfitLossSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfitLoss
        fields = '__all__'
