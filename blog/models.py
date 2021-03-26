from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.reverse_related import ManyToOneRel


class Blog_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Extending user class
    birthday = models.DateField()
    date_joined = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username


class Blog(models.Model):
    user_blog = models.ForeignKey(Blog_user, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    blog_content = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(Blog_user,related_name='+',blank=True)

    def __str__(self):
        return self.title