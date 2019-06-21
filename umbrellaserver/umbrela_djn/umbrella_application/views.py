from django.shortcuts import render
from rest_framework import generics,viewsets
from django.http import request
from django_filters import rest_framework as filters

from .serializable.handlerSerializable import *

from rest_framework.authentication import SessionAuthentication,TokenAuthentication,BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.response import Response
#from braces.views import CsrfExemptMixin

#from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.views import APIView

# Create your views here.


class GetAtualMyFollowersProfile(viewsets.ModelViewSet):
    serializer_class=ToolkitGetMyFollowersSerializabler
    queryset= Gestor.objects.all()
    authentication_classes=[TokenAuthentication,BasicAuthentication]
    permission_classes=(IsAuthenticated,)
    filter_fields=['id_perfil_select','identifier']

class ToolkitActivateFollowersByTag(viewsets.ModelViewSet):
    serializer_class=ToolkitFollowersByTagSerializer
    authentication_classes=[TokenAuthentication,BasicAuthentication]
    permission_classes=(IsAuthenticated,)
    filter_fields=['id_perfil_select','identifier']


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

class GestorListFilter(filters.FilterSet):
    date_gte = filters.DateFilter(name="date",lookup_expr='gte')
    class Meta:
        model = Gestor
        fields = "__all__"

class GestorList(generics.ListCreateAPIView):
    queryset=Gestor.objects.all()
    serializer_class = GestorSerializable
    authentication_classes=[TokenAuthentication, BasicAuthentication, ]
    permission_classes=(IsAuthenticated, )
    #filter_backends = (filters.DjangoFilterBackend)
    filter_fields = '__all__'

class UsersList(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class= UserSerializable
    authentication_classes=[TokenAuthentication, BasicAuthentication, ]
    permission_classes=(IsAuthenticated, )
    #filter_backends = (filters.DjangoFilterBackend)
    filter_fields = '__all__'

class SeguidoresList(generics.ListCreateAPIView):
    queryset=Seguidores.objects.all()
    serializer_class=SeguidoresSerializable
    authentication_classes=[TokenAuthentication, BasicAuthentication, CsrfExemptSessionAuthentication ]
    permission_classes=(IsAuthenticated, )
    filter_fields='__all__'


class SeguidoresViewSet(viewsets.ModelViewSet):
    queryset=Seguidores.objects.all()
    serializer_class=SeguidoresSerializableCreate
    authentication_classes=[TokenAuthentication,BasicAuthentication,]
    permission_classes=(IsAuthenticated, )


    
class FeedbacksList(generics.ListCreateAPIView):
    queryset=Feedbacks.objects.all()
    serializer_class=FeedbackSerializable
    authentication_classes=[TokenAuthentication, BasicAuthentication, ]
    permission_classes=(IsAuthenticated, )
    filter_fields='__all__'

class TagsList(generics.ListCreateAPIView):
    queryset=Tags.objects.all()
    serializer_class=TagsSerializable
    authentication_classes=[TokenAuthentication, BasicAuthentication, ]
    permission_classes=(IsAuthenticated, )
    filter_fields='__all__'

class PostList(generics.ListCreateAPIView):
    queryset=Posts.objects.all()
    serializer_class=PostSerializable
    authentication_classes=[TokenAuthentication, BasicAuthentication, ]
    permission_classes=(IsAuthenticated, )
    filter_fields = '__all__'

class PerfisList(generics.ListCreateAPIView):
    queryset=Perfis.objects.all()
    serializer_class=PerfisSerializable
    authentication_classes=[TokenAuthentication, BasicAuthentication, ]
    permission_classes=(IsAuthenticated, )
    filter_fields='__all__'

class CreateProfiles(viewsets.ModelViewSet):
    queryset=Perfis.objects.all()
    serializer_class=PerfisSerializableCreate
    authentication_classes=[TokenAuthentication,BasicAuthentication]
    permission_classes=(IsAuthenticated,)
    filter_fields='__all__'


class CreateUser(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=CreateUserSerializable
    permission_classes=(AllowAny,)
    filter_fields='__all__'
    

class CustomAuthToken(ObtainAuthToken):
    serializer_class = UserSerializable
    def post(self,request,*args,**kwargs):
        serializer = serializer_class(data=request.data,context={'request' : request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token,created = Token.objects.get_or_create(user=user)
        return Response(
            {
                'token' : token.key,
                'user_id' : user.pk,
                'email' : user.email
            }
        )



