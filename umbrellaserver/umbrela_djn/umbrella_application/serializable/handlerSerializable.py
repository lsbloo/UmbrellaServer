from rest_framework import serializers
from ..models import Perfis
from ..models import Seguidores
from ..models import Tags
from ..models import User
from ..models import Userx
from ..models import Gestor
from ..models import Feedbacks
from ..models import Posts
import threading
from datetime import *
from umbrella_application.generators.token_user import gerenate_token
from ..toolkit.umbrella_bot import UmbrellaBot
from ..manipulatorTh.manipulator import Manipulator
"""
Retorna todos os perfils criados; param get;
"""
manipulador = Manipulator()
class PerfisSerializable(serializers.ModelSerializer):
    class Meta:
        model = Perfis
        fields= '__all__'

class PerfisSerializableCreate(serializers.HyperlinkedModelSerializer):
     
    class Meta:
        model = Perfis
        fields = ('username','password','identifier')
    
    def create(self,validate_data):
        profiles = Perfis.objects.create(
            username=validate_data['username'],
            password=validate_data['password'],
            amount=500
        )
        g = Gestor.objects.get(identifier=validate_data['identifier'])
        profiles.seguidores.add(Seguidores.objects.create())
        profiles.tags.add(Tags.objects.create())
        profiles.posts.add(Posts.objects.create())
        profiles.feedbacks.add(Feedbacks.objects.create())
        profiles.save()
        result = Perfis.objects.get(id=profiles.id)
        g.Perfis.add(result)
        return profiles
    


"""
retorna a lista de entidades do tipo feedback
"""
class FeedbackSerializable(serializers.ModelSerializer):
    class Meta:
        model = Feedbacks
        fields = '__all__'

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


class PostSerializable(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'


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


"""
retorna as referencias dos usuarios criados;
"""
class UserSerializable(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk' , read_only=True )
    class Meta:
        model = Userx
        fields = ['id']


"""
Define a criação de um usuário(user model), com um token associado para o mesmo (authentication);
    ->
"""
class CreateUserSerializable(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ['email', 'password','username']
        extra_kwargs = {'username': {'required': False}, 'password' : {'required': False} }

    def create(self, validated_data):
        #User Model
        name= validated_data.get('username')
        email = validated_data.get('email')
        passx = validated_data.get('password')
        user = User.objects.create(username=name,email=email)
        user.set_password(passx)
        gerenate_token(user)
        user.save()
        ###############################################################
        #User Associate;
        identifier = validated_data['username']
        actived = True
        userx = Userx.objects.create(identifier=identifier,actived=actived)
        userx.user = user
        userx.save()
        #################################################################
        # Manager Associate
        manager = Gestor.objects.create(user=userx, identifier=identifier)
        manager.save()

        return user


class TagsSerializable(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


############### TOOLKIT ################################################




list_dt=[]
class ToolkitFollowersByTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gestor
        fields = ['id_perfil_select','identifier']
    
    def create(self,validate_data):
        perfil = Perfis.objects.get(id=validate_data.get('id_perfil_select'))
        gestor = Gestor.objects.get(identifier=validate_data.get('identifier'))
        identificador = validate_data.get('identifier')
        a = UmbrellaBot(perfil.username,perfil.password,perfil.amount,5,identificador)
        manipulador.add_identifier(identificador)
        manipulador.add_thread(a,identificador)
        p = perfil.tags.all()
        list_dt.append(a)
        list_dt.append(p)
        tag = []
        for x in p:
            tag = x.list_tag
        a.sessions_following_by_list_tags(tag)
        return gestor
        
    

class ToolkitGetMyFollowersSerializabler(serializers.ModelSerializer):
    class Meta:
        model = Gestor
        fields = ['id_perfil_select' , 'identifier']

    
    def create(self,validate_data):
        
        perfil = Perfis.objects.get(id=validate_data.get('id_perfil_select'))
        gestor = Gestor.objects.get(identifier=validate_data.get('identifier'))
        identificador = validate_data.get('identifier')
        a = UmbrellaBot(perfil.username,perfil.password,perfil.amount,5,identificador)
        manipulador.add_identifier(identificador)
        manipulador.add_thread(a,identificador)
        result =  a.get_my_followers_of_my_sessions(perfil.username)
        seguidores = Seguidores.objects.get(id=perfil.id)
        if len(result) >= 1:
            if len(seguidores.list_followers)  >= 1:
                for i in seguidores.list_followers:
                    if search_linear(result,i):
                        pass
                    else:
                        seguidores.list_followers.append(i)
                seguidores.save()
            seguidores.list_followers=result
            seguidores.save()
        else:
            print("dont have followers")

        
        return Gestor


def search_linear(result,followers):
    for i in result:
        if i == followers:
            return True
        return False
