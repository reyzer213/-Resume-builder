from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()



class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Резюме")
    title_resume = models.CharField(max_length=100, help_text="Резюме на тему...")
    desire_pos = models.CharField(max_length=100, help_text="На якій посаді бажаєте бути?")
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Яку я хочу зарплату")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title_resume} - {self.desire_pos}"
    
class InfoUser(models.Model):
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE, related_name="info_about_user")
    full_bio = models.CharField(max_length=50, help_text="ПІБ")
    phone = models.CharField(max_length=13, blank=True, help_text="Номер телефону")
    email = models.EmailField("Електронна почта")
    adress = models.CharField(max_length=100, help_text="Ваше місто")
    hb_date = models.DateField(blank=True, null=True, help_text="Дата народження")

    def __str__(self):
        return f"{self.full_bio} - {self.adress}"

#class MainResume(models.Model):
#    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="chapters")

    # досвід роботи

#    job_title = models.CharField(max_length=100, blank=True, help_text="Назва посади")
#    company_name = models.CharField(max_length=100, blank=True, help_text="Назва компанії")
#    start_date = models.DateField(blank=True, null=True)
#    end_date = models.DateField(blank=True, null=True, help_text="нічого не писати")
#    responsibilities = models.TextField(blank=True, help_text="Основні обов'язки")
 
    # освіта/навички

#    university_name = models.CharField(max_length=50, blank=True, help_text="Назва місця навчання")
#    start_time = models.DateTimeField()

class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="experiences")
    job_title = models.CharField(max_length=100, help_text="Назва посади")
    company_name = models.CharField(max_length=100, help_text="Назва компанії")
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Залиште порожнім, якщо ще працюєте")
    responsibilities = models.TextField(help_text="Основні обов'язки", blank=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

class Study(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="eductions")
    institution_name = models.CharField(max_length=100, help_text="Назва навчального закладу")
    qualification_lvl = models.CharField(max_length=100, help_text="Кваліфікація або спеціальність")
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Дата закінчення навчального закладу")

    def __str__(self):
        return f"{self.qualification_lvl} at {self.institution_name}"


class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="skills")
    skill_name = models.TextField(max_length=200, help_text="Опис ваших навичок")


    def __str__(self):
        return self.skill_name

class AddInfo(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="add_info")
    hobbies = models.TextField(blank=True, help_text="Інтереси та хобі")
    personal_qualities = models.TextField(blank=True, help_text="Особисті якості")
    achievements = models.TextField(blank=True, help_text="Досягнення")

    def __str__(self):
        return f"Додаткова інформація для {self.resume.title_resume}"