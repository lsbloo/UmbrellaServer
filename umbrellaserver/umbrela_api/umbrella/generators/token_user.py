from django.conf import settings
from django.db.models.signals import post_save
#from django.dispath import receiver
from rest_framework.authtoken.models import Token
from ..models import User

#@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

"""
Cria um token aleatorio para uma instancia user especificada;
        -> Return true se a criação for sucesso;
"""
def gerenate_token(my_instance_of_user):
        Token.objects.create(user=my_instance_of_user)
        return True
