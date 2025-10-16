from django.urls import path
from . import views

app_name = 'team'

urlpatterns = [
    path('', views.team, name='team'),
    path('create/', views.create_team_member, name='create_team_member'),
    path('update/<int:pk>/', views.update_team_member, name='update_team_member'),
    path('delete/<int:pk>/', views.delete_team_member, name='delete_team_member'),
]