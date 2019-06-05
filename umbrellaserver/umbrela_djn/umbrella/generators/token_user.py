from rest_framework.authtoken.models import Token
"""
Cria um token aleatorio para uma instancia user especificada;
        -> Return true se a criação for sucesso;
"""
def gerenate_token(my_instance_of_user):
        Token.objects.create(user=my_instance_of_user)
        return True