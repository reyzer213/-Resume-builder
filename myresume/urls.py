from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='reg/login.html'), name='login'),  
    path('register/', views.register, name='register'),  
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('api/poll/', PollSerializer.as_view(), name='polls-list-api'),
]
