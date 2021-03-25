from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from blog.models import Blog_user

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            birthday = form.cleaned_data.get('birthday')
            new_blog_user = Blog_user.objects.create(user=user, birthday=birthday)
            new_blog_user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account Created for {username}")
            return redirect('login')
    else:
        form = RegisterForm()
    context = {'form':form}
    return render(request,'register.html',context)