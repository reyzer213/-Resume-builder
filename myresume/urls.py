from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    register,
    profile,
    edit_profile,
    resume_list,
    ResumeDetailView,
    ResumeCreateView,
    ResumeUpdateView,
    ResumeDeleteView,
)

urlpatterns = [
    
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('login/', LoginView.as_view(template_name='reg/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    
    path('resumes/', resume_list, name='resume_list'),  
    path('resumes/<int:pk>/', ResumeDetailView.as_view(), name='resume_detail'),  
    path('resumes/create/', ResumeCreateView.as_view(), name='resume_create'),  
    path('resumes/<int:pk>/edit/', ResumeUpdateView.as_view(), name='resume_update'),  
    path('resumes/<int:pk>/delete/', ResumeDeleteView.as_view(), name='resume_delete'),  
]