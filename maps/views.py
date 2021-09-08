from .models import Map
from rest_framework import viewsets, permissions
from .serializers import MapSerializer

class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    permission_classes = [permissions.AllowAny]