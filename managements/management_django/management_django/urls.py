
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/dict/', include('djoser.urls')),
    path('api/dict/', include('djoser.urls.authtoken')),

    path('api/dict/', include('network.urls')),

    path('api/dict/', include('computer.urls')),

    path('api/dict/', include('personals.urls')),
    path('api/dict/', include('team.urls')),

]
