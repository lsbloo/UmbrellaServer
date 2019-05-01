from django.shortcuts import render
from rest_framework import generics
from .models import Gestor
from .gestorSerializable import GestorSerializable
# Create your views here.



class GestorList(generics.ListCreateAPIView):
    queryset=Gestor.objects.all()
    serializer_class = GestorSerializable