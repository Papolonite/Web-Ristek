from django.shortcuts import render,redirect
from .models import Comment
from .forms import CommentForm
from django.contrib import messages

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

def delete_comment(request,id):
    comment_now = Comment.objects.get(id=id)
    if (request.user == comment_now.user_comment.user):
        messages.success(request, f"Comment succesfully deleted")
        comment_now.delete()
        return redirect('home')
    else:
        messages.error(request,f"Link cannot be found")
        return redirect('home')

def update_comment(request,id):
    context = {}
    comment_now = Comment.objects.get(id=id)
    if request.user == comment_now.user_comment.user:
        comment_form = CommentForm(request.POST or None, instance = comment_now)
        context['comment_form'] = comment_form

        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, f'Comment has been updated')
            return redirect('home')

        return render(request,'edit_comment.html', context)

    else:
        messages.error(request,f'Link does not exist')
        return redirect('home')