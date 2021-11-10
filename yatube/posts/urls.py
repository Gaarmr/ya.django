from . import views
from django.urls import path
from django.urls.resolvers import URLPattern


urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='groups')
]