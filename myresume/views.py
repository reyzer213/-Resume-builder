from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Resume
from .forms import CustomUserCreationForm, ProfileForm, ResumeForm


class ResumeListView(LoginRequiredMixin, ListView):  # лише авторизовані користувачі можуть переглядати резюме
    model = Resume
    template_name = 'resume/resume_list.html'
    context_object_name = 'resumes'

    def get_queryset(self):
        # Повертає тільки резюме, створені поточним користувачем
        return Resume.objects.filter(user=self.request.user)


class ResumeDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):  # перевірка доступу до деталей
    model = Resume
    template_name = 'resume/resume_detail.html'

    def test_func(self):
        # Тільки власник резюме може переглядати його деталі
        resume = self.get_object()
        return self.request.user == resume.user


class ResumeCreateView(LoginRequiredMixin, CreateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'resume/resume_create.html'
    success_url = reverse_lazy('resume_list')

    def form_valid(self, form):
        # Робить резюме власністю поточного користувача
        form.instance.user = self.request.user
        return super().form_valid(form)


class ResumeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'resume/resume_update.html'
    success_url = reverse_lazy('resume_list')

    def test_func(self):
        # Тільки власник резюме може його редагувати
        resume = self.get_object()
        return self.request.user == resume.user


class ResumeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Resume
    template_name = 'resume/resume_confirm_delete.html'
    success_url = reverse_lazy('resume_list')

    def test_func(self):
        # Тільки власник резюме може його видалити
        resume = self.get_object()
        return self.request.user == resume.user


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('resume_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'reg/reg.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'reg/profile.html')


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

@login_required
def resume_list(request):
    resumes = Resume.objects.filter(user=request.user)
    return render(request, 'resume/resume_list.html', {'resumes': resumes})