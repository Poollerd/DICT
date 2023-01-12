from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ComputerViewSet, UpgradecomputerViewSet, ComputerAllViewSet

router = DefaultRouter()
router.register('computers', ComputerViewSet, basename='computers')
router.register('computersall', ComputerAllViewSet, basename='computersall')
router.register('upgradecomputers', UpgradecomputerViewSet, basename='upgradecomputers')


urlpatterns = [
    path('', include(router.urls)),
]