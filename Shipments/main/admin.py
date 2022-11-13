from django.contrib import admin
from django.contrib.auth.models import Group
from .models import BlogPost

# Register your models here.
admin.site.register(BlogPost)

# Unregister your models here.
admin.site.unregister(Group)