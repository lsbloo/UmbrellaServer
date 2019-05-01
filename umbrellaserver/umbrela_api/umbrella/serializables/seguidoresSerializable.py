from rest_framework import serializers
from ..models import Seguidores

class SeguidoresSerializable(serializers.ModelSerializer):
    class Meta:
        model = Seguidores
        fields = '__all__'
