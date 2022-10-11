from django.contrib import admin
from django.urls import path
from . import views

app_name='either'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    # path('<int:pk>/detail', views.detail, name='detail'),
]