from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    company = models.CharField(max_length=200, null=True)
    job = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    about = models.TextField(null=True)
    image = models.ImageField(default='avatar.jpg', upload_to='profile_media')
    
    def __str__(self):
        return self.staff.username 