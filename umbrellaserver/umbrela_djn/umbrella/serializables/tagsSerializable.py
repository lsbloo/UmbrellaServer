from rest_framework import serializers
from ..models import Tags

class TagsSerializable(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'
