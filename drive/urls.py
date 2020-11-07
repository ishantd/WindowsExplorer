from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # api endpoints for file watcher
    path('created/', views.created),
]