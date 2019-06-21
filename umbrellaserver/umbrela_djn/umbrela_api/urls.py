
"""umbrela_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from umbrella_application import views

urlpatterns = [
    path('admin/', admin.site.urls),
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
    url(r'umbrella/api/v1/mgmnt/tags/g' , views.TagsList.as_view(),name='tags_list'),

    url(r'api-token-auth/' , views.CustomAuthToken.as_view(), name="user_token_list"),
    
    url(r'umbrella/api/v1/toolkit/follow/tags/$' , views.ToolkitActivateFollowersByTag.as_view(
        {'post' : 'create'}
    ),name="toolkit_follow_by_tag") ,

    url(r'umbrella/api/v1/toolkit/follow/g/$', views.GetAtualMyFollowersProfile.as_view(
        {'post' : 'create'}
    ), name="toolkit_get_my_followers"),

    url(r'umbrella/api/v1/toolkit/follow/friends/$' , views.FollowFriendsOfMySession.as_view(
        {'post' : 'create'}
    ), name='follow_friend_my_followers')

]
