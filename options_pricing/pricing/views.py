# views.py
from rest_framework import viewsets
from .models import OptionType, Asset, Option, ProfitLoss
from .serializers import OptionTypeSerializer, AssetSerializer, OptionSerializer, ProfitLossSerializer

class OptionTypeViewSet(viewsets.ModelViewSet):
    queryset = OptionType.objects.all()
    serializer_class = OptionTypeSerializer

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class ProfitLossViewSet(viewsets.ModelViewSet):
    queryset = ProfitLoss.objects.all()
    serializer_class = ProfitLossSerializer
