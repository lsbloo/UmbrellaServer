from django.conf import settings
from django.db.models.signals import post_save
from django.dispath import receiver
from rest_framework.authtoken.models import Token
from ..models import User

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


def gerenate_token():
    for user in User.objects.all():
        Token.objects.get_or_create(user=user)
