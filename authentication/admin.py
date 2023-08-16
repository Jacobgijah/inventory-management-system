from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('staff', 'company', 'job', 'address', 'phone', 'image')
    list_filter = ['job']

admin.site.register(Profile, ProfileAdmin)