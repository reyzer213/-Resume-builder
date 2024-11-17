from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from .models import Resume
from .forms import CustomUserCreationForm, ProfileForm, ResumeForm
from rest_framework.generics import *
from .serializers import *



def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'reg/reg.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'reg/profile.html')


#аватарка профілю

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'reg/edit_profile.html', {'form': form})


class PollListAPI(ListCreateAPIView):
    queryset = myresume.objects.all()
    serializer_class = PollSerializer