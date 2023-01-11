from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ComputerViewSet, UpgradecomputerViewSet

router = DefaultRouter()
router.register('computers', ComputerViewSet, basename='computers')
router.register('upgradecomputers', UpgradecomputerViewSet, basename='upgradecomputers')


urlpatterns = [
    path('', include(router.urls)),
]