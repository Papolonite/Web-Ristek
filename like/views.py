from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from blog.models import Blog, Blog_user
from django.urls import reverse



# Create your views here.
def add_like(request,id):
    if request.user.is_authenticated:
        blog_user = Blog_user.objects.get(user = request.user)
        blog = Blog.objects.get(id=id)
        if not blog_user in blog.like.all():
            blog.like.add(blog_user)
            return HttpResponseRedirect(reverse('blog_detail',kwargs={'id':id}))
        else:
            messages.error(request, 'Link does not available')
            return redirect('home')

    else:
        messages.error(request, 'Link does not available')
        return redirect('home')

def remove_like(request,id):
    if request.user.is_authenticated:
        blog_user = Blog_user.objects.get(user = request.user)
        blog = Blog.objects.get(id=id)
        if blog_user in blog.like.all():
            blog.like.remove(blog_user)
            return HttpResponseRedirect(reverse('blog_detail',kwargs={'id':id}))
        else:
            messages.error(request, 'Link does not available')
            return redirect('home')

    else:
        messages.error(request, 'Link does not available')
        return redirect('home')

def like_check(request, id):
    blog_user = Blog_user.objects.get(user = request.user)
    blog = Blog.objects.get(id=id)
    if blog_user in blog.like.all():
        return True
    else:
        return False