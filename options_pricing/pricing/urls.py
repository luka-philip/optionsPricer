# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OptionTypeViewSet, AssetViewSet, OptionViewSet, ProfitLossViewSet

router = DefaultRouter()
router.register(r'option-types', OptionTypeViewSet)
router.register(r'assets', AssetViewSet)
router.register(r'options', OptionViewSet)
router.register(r'profit-loss', ProfitLossViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
