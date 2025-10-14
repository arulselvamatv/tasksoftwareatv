from django.urls import path
from . import views


app_name = 'authentication' 

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('logout/', views.logout_view, name='logout'),
    path('profile_settings/', views.profile_settings, name='profile_settings'),
]