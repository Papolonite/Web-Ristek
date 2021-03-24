from django.db import models
from django.contrib.auth.models import User


class Blog_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Extending user class
    birthday = models.DateField()
    date_joined = models.DateField(auto_now=True)


class Blog(models.Model):
    user_blog = models.ForeignKey(Blog_user, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    blog_content = models.TextField()
    created_date = models.DateTimeField(auto_now=True)

    like = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_comment = models.ForeignKey(Blog_user, on_delete=models.CASCADE)
    on_blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_content = models.TextField()

    def __str__(self):
        return f'{self.comment_content} on {self.on_blog.title} from {self.user_comment.user.name}'
