from django.db import models
from django.db.models import CharField
from django_mysql.models import ListCharField
import datetime
# Create your models here.

class User(models.Model):
    nome= models.CharField(max_length=400)
    email=models.CharField(max_length=400)
    username=models.CharField(max_length=400)
    password=models.CharField(max_length=200)
    identifier = models.CharField(max_length=200)
    actived = models.BooleanField(default=True)
    status=models.CharField(max_length=200)
    key=models.CharField(("Key"), max_length=100,primary_key=True)
    class Meta:
        verbose_name_plural = "users"
    
    def __str__(self):
        return self.identifier

class Seguidores(models.Model):
    name_reference=models.CharField(max_length=100)
    list_followers=ListCharField(
        base_field=CharField(max_length=10),
        size=6,
        max_length=6*11
        )
    class Meta:
        verbose_name_plural="seguidores"

class Tags(models.Model):
    name_reference=models.CharField(max_length=100)
    list_tag=ListCharField(
        base_field=CharField(max_length=10),
        size=6,
        max_length=6*11
        )

    class Meta:
        verbose_name_plural="tags"

class Posts(models.Model):
    name_reference=models.CharField(max_length=100)
    list_posts=ListCharField(
        base_field=CharField(max_length=10),
        size=6,
        max_length=6*11
    )
    
    class Meta:
        verbose_name_plural="posts"

class Feedbacks(models.Model):
    name_reference=models.CharField(max_length=100)
    list_feedbacks=ListCharField(
        base_field=CharField(max_length=10),
        size=6,
        max_length=6*11
    )
    
    class Meta:
        verbose_name_plural="posts"

class Perfis(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    seguidores = models.ManyToManyField(Seguidores)
    tags = models.ManyToManyField(Tags)
    posts = models.ManyToManyField(Posts)
    feedbacks = models.ManyToManyField(Feedbacks)
    class Meta:
        verbose_name_plural="perfis"


class Gestor(models.Model):
    identifier=models.CharField(max_length=100,primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    Perfis = models.ManyToManyField(Perfis, null=True, blank=True)
    class Meta:
        verbose_name_plural = "gestores"
