from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # api endpoints for file watcher
    path('created/', views.created),
    path('deleted/', views.deleted),
    path('modified/', views.modified),
    path('moved/', views.moved),
]