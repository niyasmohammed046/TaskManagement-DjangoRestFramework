from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_registration, name='user-register'),
    path('login/', views.user_login, name='user-login'),
    path('password-reset/', views.password_reset, name='password-reset'),
    # Other authentication-related endpoints
]