from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)

RANK = (
    ('Admin', 'Admin'),
    ('Employee', 'Employee'),
    ('Client', 'Client')
)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  related_name='profile')
    uid = models.UUIDField(default=uuid4, editable=False)
    image = models.ImageField(blank=True, null=True, upload_to='profile_pics')
    address = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(blank=True, null=True, max_length=15)
    gender = models.CharField(default="Others", blank=True, null=True, max_length=6, help_text="Gender", choices=GENDER)
    dob = models.DateField(blank=True, null=True,help_text='Date of Birth')
    reg_date = models.DateTimeField(auto_now_add=True, auto_now= False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)
    rank = models.CharField(default='Client', max_length=15, help_text="Rank", choices=RANK)
    active = models.BooleanField(default=False)

    class Meta: 
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        ordering = ["-reg_date", 'user']

    def get_name(self):
        if self.user.first_name and self.user.last_name:
            return str(self.user.first_name) + " " + str(self.user.last_name) 
        else:
            return str(self.user.username)

    def user_status(self):
        if self.rank == "Admin":
            return "Admin"
        elif self.rank == "Employee":
            return "Employee"
        elif self.rank == "Client":
            return "Client"
        else:
            return "User Status Not Defined"

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return str(self.user.first_name) + " " + str(self.user.last_name) 
        else:
            return str(self.user.username)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class EmployeeProfile(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE,  related_name='employee_profile')
    uid = models.UUIDField(default=uuid4, editable=True)
    about = models.TextField(blank=True, null=True)
    reg_date = models.DateTimeField(auto_now_add=True, auto_now= False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)
    active = models.BooleanField(default=False)
  
    def __str__(self):
    	return str(self.profile)

    class Meta: 
        verbose_name = 'Employee Profile'
        verbose_name_plural = 'Employees Profiles'
        ordering = ["-reg_date", 'profile']


class ClientProfile(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE,  related_name='client_profile')
    uid = models.UUIDField(default=uuid4, editable=True)
    reg_date = models.DateTimeField(auto_now_add=True, auto_now= False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)
    active = models.BooleanField(default=True)
    
    class Meta: 
        verbose_name = 'Client Profile'
        verbose_name_plural = 'Clients Profiles'
        ordering = ["-reg_date", 'profile']

    def __str__(self):
    	return str(self.profile)

@receiver(post_save, sender=UserProfile)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ClientProfile.objects.create(profile=instance)

@receiver(post_save, sender=UserProfile)
def save_user_profile(sender, instance, **kwargs):
    instance.client_profile.save()

    