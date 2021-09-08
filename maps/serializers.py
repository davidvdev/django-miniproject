from .models import Map
from rest_framework import serializers

class MapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Map
        fields = ['id', 'rows', 'columns', 'layout']