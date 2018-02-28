# from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.post_list, name='post_list'),
    path(r'<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_detail, name='post_detail'),
]
