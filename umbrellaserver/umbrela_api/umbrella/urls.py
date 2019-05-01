from django.conf.urls import url
from umbrella import views


urlpatterns = [

    url(r'^gestores/$', views.GestorList.as_view(),name='gestores_list')
]