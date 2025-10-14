from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),  
    path('dashboard/', include('dashboard.urls')),  
    path('project/', include('project.urls')),
    path('tasks/', include('tasks.urls')),
    path('todo/', include('todo.urls')),
    path('team/', include('team.urls')),
]