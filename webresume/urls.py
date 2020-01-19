from django.contrib import admin
from django.urls import path
from django.urls import include
from webresume import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('subjects/<int:pk>', views.GenreListView.as_view(), name='genres'),
]