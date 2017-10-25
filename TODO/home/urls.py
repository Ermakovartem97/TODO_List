from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^aktive/(?P<task_id>\d+)/$', views.aktive),
    url(r'^dell/(?P<task_id>\d+)/$', views.dell),

]