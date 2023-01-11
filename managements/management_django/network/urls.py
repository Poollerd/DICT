from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import NetworkViewSet, NetworkAllViewSet

router = DefaultRouter()
router.register('networks', NetworkViewSet, basename='networks')
router.register('networksall', NetworkAllViewSet, basename='networksall')

urlpatterns = [
    path('', include(router.urls)),
]