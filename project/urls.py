from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('list/', views.project_list, name='project_list'),
    path('create/', views.create_project, name='create_project'),
]
