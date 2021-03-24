from django.contrib import admin
from .models import Blog_user, Blog, Comment

# Register your models here.
admin.site.register(Blog_user)
admin.site.register(Blog)
admin.site.register(Comment)