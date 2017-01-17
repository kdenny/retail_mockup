from django.conf.urls import url, include
from django.views import generic

from mockup import views



urlpatterns = [
    url(r'^view1/$', views.view1, name='view1'),
    url(r'^view2/$', views.view2, name='view2'),
    url(r'^view3/$', views.view3, name='view3'),
    url(r'^view4/$', views.view4, name='view4'),
    url(r'^view5/$', views.view5, name='view5'),
    url(r'^view6/$', views.view6, name='view6'),
    url(r'^view7/$', views.view7, name='view7'),
    url(r'^view8/$', views.view8, name='view8'),
    url(r'^view9/$', views.view9, name='view9'),
    # url(r'^logout/$', views.user_logout, name='logout'),
    # url(r'^api/$', views.api_examples, name='api')
]