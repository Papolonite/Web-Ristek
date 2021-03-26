from django.shortcuts import render
from .models import Comment
from .forms import CommentForm

# Create your views here.
def get_comment_data():
    return Comment.objects.all()

def create_comment_form(request):
    return CommentForm(request.POST or None)

def save_comment(user,blog,comment):
    new_comment = Comment.objects.create(
            user_comment = user,
            on_blog = blog,
            comment = comment,
        )
    new_comment.save()
