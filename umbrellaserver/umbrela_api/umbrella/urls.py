from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from umbrella import views 
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt

#router_followers = routers.DefaultRouter()
#router_followers.register(r'followers/create/', views.SeguidoresViewSet)


urlpatterns = [

    url(r'^gestores/$', views.GestorList.as_view(),name='gestores_list'),
    url(r'^users/$', views.UsersList.as_view(),name="users_list"),
    url(r'^followers/$', views.SeguidoresList.as_view(),name="followers_list"),
    url(r'^perfis/$',views.PerfisList.as_view(),name="perfis_list"),
    url(r'^feedback/$',views.FeedbacksList.as_view(),name="feedback_list"),
    url(r'^posts/$',views.PostList.as_view(),name="posts_list"),
    url(r'^perfis/$',views.PerfisList.as_view(),name="perfis_list"),
    url(r'followers/create/', views.SeguidoresViewSet.as_view(
        {'get': 'list',
        'post': 'create'}
    ) , name="create_followers"),
    
    url(r'api-token-auth/' , views.CustomAuthToken.as_view(), name="user_token_list")

]