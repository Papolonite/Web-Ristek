from django.db import models
from blog.models import Blog_user, Blog

class Comment(models.Model):
    user_comment = models.ForeignKey(Blog_user, on_delete=models.CASCADE)
    on_blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.comment} on {self.on_blog.title} from {self.user_comment.user.username}'
