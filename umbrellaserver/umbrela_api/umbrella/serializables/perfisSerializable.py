from rest_framework import serializers
from ..models import Perfis

class PerfisSerializable(serializers.ModelSerializer):
    class Meta:
        model = Perfis
        fields = '__all__'
