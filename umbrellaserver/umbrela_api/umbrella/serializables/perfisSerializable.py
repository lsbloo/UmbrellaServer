from rest_framework import serializers
from ..models import Perfis
from ..models import Seguidores
from ..models import Tags
from ..models import Feedbacks
from ..models import Posts

"""
Retorna todos os perfils criados; param get;
"""
class PerfisSerializable(serializers.ModelSerializer):
    class Meta:
        model = Perfis
        fields = ['username','password','seguidores','tags','posts','feedbacks']
        extra_kwargs = {'seguidores' : {'required' : False } , 'tags' : {'required' : False} ,'posts' : {'required' : False} , 'feedbacks' : {'required' : False}}


""" param POST;
Cria uma entidade Perfil que tem como atributos obrigatorios nome e password
as demais entidades relacionadas ao perfil são criadas com valores default
    "username": "mer",
        "password": "6236",
        "seguidores": [
            17
        ],
        "tags": [
            17
        ],
        "posts": [
            16
        ],
        "feedbacks": [
            16
        ]
    }
    Onde o objeto seguidores por exemplo tem como referencia o id daquele objeto iniciado com
    valores default, o mesmo vale para os demais.
"""
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


    