from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, EmailValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


# Профіль 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null= True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null= True)

    def __str__(self):
        return f"{self.user.username}'s Профіль"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()



class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="resumes")
    title = models.CharField(max_length=100, help_text="Резюме на тему...")
    desire_pos = models.CharField(max_length=100, help_text="На яку посаду ви претендуєте?", null= True)
    salary = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        blank=True, 
        null=True, 
        help_text="Очікувана заробітна плата"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=50, help_text="Ваше ім'я")
    last_name = models.CharField(max_length=50, help_text="Ваше прізвище")
    photo = models.ImageField(upload_to='resume_photos/', blank=True, help_text="Ваше фото")
    phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Введіть правильний номер телефону.")],
        help_text="Контактний номер телефону", 
    )
    email = models.EmailField(
        help_text="Електронна пошта",
        null= True, 
        blank= True
    )
    experience = models.TextField(blank=True, help_text="Ваш професійний досвід", null= True)
    education = models.TextField(blank=True, help_text="Інформація про освіту", null= True)
    additional_info = models.TextField(blank=True, help_text="Додаткова інформація", null= True)

    def __str__(self):
        return f"{self.title} ({self.user.username})"


# Досвід роботи
class WorkExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="work_experiences")
    job_title = models.CharField(max_length=100, help_text="Посада")
    company_name = models.CharField(max_length=100, help_text="Компанія")
    start_date = models.DateField(help_text="Дата початку")
    end_date = models.DateField(blank=True, null=True, help_text="Дата завершення")
    responsibilities = models.TextField(blank=True, help_text="Обов'язки або досягнення")

    def __str__(self):
        return f"{self.job_title} ({self.company_name})"


# Освіта
class Study(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="educations")
    institution_name = models.CharField(max_length=100, help_text="Навчальний заклад")
    qualification_lvl = models.CharField(max_length=100, help_text="Кваліфікація/спеціальність")
    start_date = models.DateField(help_text="Дата початку навчання")
    end_date = models.DateField(blank=True, null=True, help_text="Дата завершення навчання")

    def __str__(self):
        return f"{self.qualification_lvl} ({self.institution_name})"


# Навички
class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="skills")
    skill_name = models.CharField(max_length=100, help_text="Назва навички")

    def __str__(self):
        return self.skill_name


# Додаткова інформація
class AddInfo(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="AddInfo")
    hobbies = models.TextField(blank=True, help_text="Інтереси та хобі")
    personal_qualities = models.TextField(blank=True, help_text="Особисті якості")
    achievements = models.TextField(blank=True, help_text="Досягнення")

    def __str__(self):
        return f"Додаткова інформація для резюме {self.resume.title}"
