from rest_framework import serializers
from ..models import Gestor
from django.http import request
from ..models import Userx
from ..models import Perfis
"""
retorna as entidades do tipo gestor;
"""
class GestorSerializable(serializers.ModelSerializer):
    class Meta:
        model = Gestor
        fields = '__all__'



class CreateGestorSerializable(serializers.ModelSerializer):

    perfis = serializers.SlugRelatedField(
        allow_null=True, 
        many=True, 
        queryset=Gestor.objects.all(),
        slug_field="name_reference"
        
        )
    # FALTA IMPLEMENTAR ISSO AQ
    def create(self,validate_data):
        
        user_auth = Userx.objects.get(identifier='fdp')
        manager = Gestor.objects.create(
                identifier=validate_data['identifier']
            )
        
        manager.user=user_auth
        manager.Perfis.add(Perfis.objects.get(id=2))
        manager.save()
        return manager
    
    class Meta:
        model = Gestor
        fields = ['identifier', 'perfis']



