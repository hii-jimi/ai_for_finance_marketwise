from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_with_ai, name='chat_with_ai'),
    path('register/', views.register_user, name='register_user'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('login-otp/', views.login_otp, name='login_otp'),      # New login OTP endpoint
    path('verify-login-otp/', views.verify_login_otp, name='verify_login_otp'), # New login OTP verification endpoint
]