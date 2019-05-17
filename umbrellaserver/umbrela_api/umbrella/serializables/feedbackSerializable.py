from rest_framework import serializers
from ..models import Feedbacks


"""
retorna a lista de entidades do tipo feedback
"""
class FeedbackSerializable(serializers.ModelSerializer):
    class Meta:
        model = Feedbacks
        fields = '__all__'
