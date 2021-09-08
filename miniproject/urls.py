from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from maps.views import MapViewSet

router = routers.DefaultRouter()
router.register(r'maps', MapViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]