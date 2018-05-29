from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$',views.index_new,name='index'),
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
]
