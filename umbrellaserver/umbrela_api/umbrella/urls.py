from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from umbrella import views 
from umbrella import viewslogin
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt

#router_followers = routers.DefaultRouter()
#router_followers.register(r'followers/create/', views.SeguidoresViewSet)


urlpatterns = [
    #url(r'umbrella/api/v1'),
    url(r'umbrella/api/v1/mgmnt/manager/g/$', views.GestorList.as_view(),name='gestores_list'),
    url(r'umbrella/api/v1/mgmnt/users/g/$', views.UsersList.as_view(),name="users_list"),
    url(r'umbrella/api/v1/mgmnt/followers/g/$', views.SeguidoresList.as_view(),name="followers_list"),
    url(r'umbrella/api/v1/mgmnt/profiles/g/$',views.PerfisList.as_view(),name="perfis_list"),
    url(r'umbrella/api/v1/mgmnt/feedback/g/$',views.FeedbacksList.as_view(),name="feedback_list"),
    url(r'umbrella/api/v1/mgmnt/posts/g/$',views.PostList.as_view(),name="posts_list"),
    url(r'umbrella/api/v1/mgmnt/followers/cg/', views.SeguidoresViewSet.as_view(
        {'get': 'list',
        'post': 'create'}
    ) , name="create_followers"),
    url(r'umbrella/api/v1/mgmnt/profiles/c/$', views.CreateProfiles.as_view(
        {'post': 'create'}

    ) , name="profile_create"),

    url(r'umbrella/api/v1/mgmnt/users/c/$', views.CreateUser.as_view(
        {'post': 'create'}
    ), name="users_create"),

    url(r'api-token-auth/' , views.CustomAuthToken.as_view(), name="user_token_list")

]