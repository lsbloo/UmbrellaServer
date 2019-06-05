from rest_framework import serializers
from ..models import *
from umbrella.generators.token_user import gerenate_token

"""
Retorna todos os perfils criados; param get;
"""
class PerfisSerializable(serializers.ModelSerializer):
    class Meta:
        model = Perfis
        fields = ['username','password','seguidores','tags','posts','feedbacks']
        extra_kwargs = {'seguidores' : {'required' : False } , 'tags' : {'required' : False} ,'posts' : {'required' : False} , 'feedbacks' : {'required' : False}}


class PerfisSerializableCreate(serializers.ModelSerializer):
    seguidores = serializers.SlugRelatedField(
        allow_null=True, 
        many=True, 
        queryset=Perfis.objects.all(),
        slug_field="name_reference"
        )

    tags = serializers.SlugRelatedField(
        allow_null=True, 
        many=True,
        queryset=Perfis.objects.all(),
        slug_field="name_reference"
    )

    posts = serializers.SlugRelatedField(
        allow_null=True, 
        many=True, 
        queryset=Perfis.objects.all(),
        slug_field="name_reference"
        
        )

    feedbacks = serializers.SlugRelatedField(
        allow_null=True, 
        many=True,
        queryset=Perfis.objects.all(),
        slug_field="name_reference"
        
        )
    
    def create(self,validate_data):
        profiles = Perfis.objects.create(
            username=validate_data['username'],
            password=validate_data['password'],
        )
        profiles.seguidores.add(Seguidores.objects.create())
        profiles.tags.add(Tags.objects.create())
        profiles.posts.add(Posts.objects.create())
        profiles.feedbacks.add(Feedbacks.objects.create())
        profiles.save()
        return profiles
    
    def validate_response(self,validate_data):
        param_validate=[]
        empty=[]

        if validate_data['seguidores'] == empty:
            seguidores=None
            param_validate.append(seguidores)
        else:
            seguidores=validate_data=['seguidores']
            param_validate.append(seguidores)
            

        if validate_data['tags'] == empty:
            tags=None
            param_validate.append(tags)
        else:
            tags=validate_data['tags']
            param_validate.append(tags)
            
        if validate_data['posts'] == empty:
            posts=None
            param_validate.append(posts)
        else:
            posts=validate_data['posts']
            param_validate.append(posts)
            
        if validate_data['feedbacks'] == empty:
            feedbacks=None
            param_validate.append(feedbacks)
        else:
            feedbacks=validate_data['feedbacks']
            param_validate.append(feedbacks)
            
        return param_validate
    class Meta:
        model = Perfis
        fields = ['username','password','seguidores','tags','posts','feedbacks']
        extra_kwargs = {'seguidores' : {'required' : False } , 'tags' : {'required' : False} ,'posts' : {'required' : False} , 'feedbacks' : {'required' : False}}



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
class CreateUserSerializable(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password','username']

    def create(self, validated_data):
        #User Model
        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
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
