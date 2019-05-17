from rest_framework import serializers
from ..models import Userx
from ..models import User
from ..models import Gestor
from umbrella.generators.token_user import gerenate_token

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
    


