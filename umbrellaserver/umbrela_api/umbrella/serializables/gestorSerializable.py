from rest_framework import serializers
from ..models import Gestor

class GestorSerializable(serializers.ModelSerializer):
    class Meta:
        model = Gestor
        fields = '__all__'
