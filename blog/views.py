from django.shortcuts import redirect, render
from blog.models import Blog, Blog_user
from .forms import PostCreation
from django.contrib import messages
from comment.views import create_comment_form, get_comment_data, save_comment

def home_view(request):
    blog_data = Blog.objects.all()
    blog_context = []

    # Loop to get all data
    for i in blog_data:
        blog_context.append({
            'id' : i.id,
            'title' : i.title,
            'content' : i.blog_content,
            'posted_by' : i.user_blog.user.username,
            'posted_time' : i.created_date,
            'like_count' : len(i.like.all()),
            'comment_count' : 0
        })

    # Updating comment_count
    comment_data = get_comment_data()
    for i in comment_data:
        for j in blog_context:
            if i.on_blog.title == j['title']:
                j['comment_count'] += 1
                break

    context = {
        'blog' : blog_context
    }

    return render(request,'home.html',context)

def your_post_view(request):
    if request.user.is_authenticated():
        blog_data = Blog.objects.all()
        blog_context = []

        # Loop to get all data
        for i in blog_data:
            if i.user_blog.user == request.user:
                blog_context.append({
                    'id' : i.id,
                    'title' : i.title,
                    'content' : i.blog_content,
                    'posted_by' : i.user_blog.user.username,
                    'posted_time' : i.created_date,
                    'like_count' : len(i.like.all()),
                    'comment_count' : 0
                })

        # Updating comment_count
        comment_data = get_comment_data()
        for i in comment_data:
            for j in blog_context:
                if i.on_blog.title == j['title']:
                    j['comment_count'] += 1
                    break

        context = {
            'blog' : blog_context
        }

        return render(request,'home.html',context)

    else:
        return redirect('login')


def blog_detail(request,id):
    blog_data_detail = Blog.objects.get(id=id)
    context = dict() #init context

    # Creating comment form if user logged in
    if request.user.is_authenticated:

        #Checking Owenership
        if request.user == blog_data_detail.user_blog.user:
            context['id'] = blog_data_detail.id

        #Creating Comment Form
        comment_form = create_comment_form(request)
        context['comment_form'] = comment_form

        # Saving the comment
        if (comment_form.is_valid() and request.method == 'POST'):
            comment_data = comment_form.cleaned_data.get('comment')
            save_comment(Blog_user.objects.get(user=request.user), blog_data_detail, comment_data)

    context['title'] = blog_data_detail.title
    context['content'] = blog_data_detail.blog_content
    context['posted_by'] = blog_data_detail.user_blog.user.username
    context['posted_time'] = blog_data_detail.created_date
    context['like_count'] = len(blog_data_detail.like.all())
    context['comment'] = []

    comment_data = get_comment_data()
    for i in comment_data:
        if i.on_blog.title == context['title']:
            context['comment'].append(i)

    return render(request, 'blog_detail.html', context)

def create_post(request):
    context = dict()
    if request.user.is_authenticated:
        blog_form = PostCreation(request.POST or None)
        context['blog_form'] = blog_form

        if blog_form.is_valid() and request.method == 'POST':
            title = blog_form.cleaned_data.get('title')
            content = blog_form.cleaned_data.get('blog_content')
            new_blog = Blog.objects.create(
                user_blog = Blog_user.objects.get(user=request.user),
                title = title,
                blog_content = content
            )
            new_blog.save()
            messages.success(request, f'Blog {title} Successfully Created')
            return redirect('home')


    return render(request, 'create_post.html', context)

def delete_post(request,id):
    blog = Blog.objects.get(id=id)
    if (request.user == blog.user_blog.user):
        messages.success(request, f"{blog.title} succesfully deleted")
        blog.delete()
        return redirect('home')
    else:
        messages.error(request,f"Link cannot be found")
        return redirect('home')

def update_post(request,id):
    context = {}
    blog_now = Blog.objects.get(id=id)
    if request.user == blog_now.user_blog.user:
        blog_form = PostCreation(request.POST or None, instance = blog_now)
        context['blog_form'] = blog_form

        if blog_form.is_valid():
            blog_form.save()
            messages.success(request,f'Blog {blog_now.title} has been updated')
            return redirect('home')

        return render(request,'create_post.html', context)

    else:
        messages.error(request,f'Link does not exist')
        return redirect('home')



