from rest_framework import serializers
from ..models import Seguidores
import time
import datetime

class SeguidoresSerializable(serializers.ModelSerializer):
    class Meta:
        model = Seguidores
        fields = '__all__'
        extra_kwargs = {'list_followers' : {'required' : False } , 'name_reference' : {'required' : False}}
        

class SeguidoresSerializableCreate(serializers.ModelSerializer):
    #od = serializers.ModelSerializer(many=True, read_only=False)
    def create(self,validate_data):
        seguidores = Seguidores.objects.create(
            name_reference=validate_data['name_reference'],
            list_followers=validate_data['list_followers'],
            status_follor=validate_data['status_follor']
        )
        seguidores.save()
        return seguidores
    def get_mytimestamp(self, obj):
        return time.mktime(datetime.datetime.now().timetuple())    

    class Meta:
        model = Seguidores
        fields = ['name_reference' , 'list_followers' , 'status_follor']
        