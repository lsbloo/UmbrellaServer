from django.shortcuts import render
from rest_framework import generics,serializers,viewsets
from django.http import response,request
from django.http import HttpResponse
import django_filters
from django_filters import rest_framework as filters
from .models import Gestor
from .models import User
from .models import Seguidores
from .models import Feedbacks
from .models import Tags
from .models import Posts
from .models import Perfis
from .serializables.gestorSerializable import GestorSerializable
from .serializables.userSerializable import UserSerializable
from .serializables.seguidoresSerializable import SeguidoresSerializable
from .serializables.feedbackSerializable import FeedbackSerializable
from .serializables.tagsSerializable import TagsSerializable
from .serializables.postsSerializable import PostSerializable
from .serializables.perfisSerializable import PerfisSerializable
from .serializables.perfisSerializable import PerfisSerializableCreate
from .serializables.gestorSerializable import CreateGestorSerializable
from .serializables.userSerializable import CreateUserSerializable
from .serializables.seguidoresSerializable import SeguidoresSerializableCreate
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from django.utils.decorators import method_decorator
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from braces.views import CsrfExemptMixin
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.views import APIView

# Create your views here.

class Object(CsrfExemptMixin, APIView):
    authentication_classes = []

    def post(self, request, format=None):
        return Response({'received data': request.data})

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

class CreateGestor(viewsets.ModelViewSet):
    queryset=Gestor.objects.all()
    serializer_class= CreateGestorSerializable
    authentication_classes=[TokenAuthentication , BasicAuthentication]
    permission_classes=(IsAuthenticated,)
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



