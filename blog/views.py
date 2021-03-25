from django.shortcuts import render
from blog.models import Blog,Blog_user,Comment

# Create your views here.
def home_view(request):
    blog_data = Blog.objects.all()
    blog_context = []
    for i in blog_data:
        blog_context.append({
            'title' : i.title ,
            'content' : i.blog_content,
            'posted_by' : i.user_blog.user.username,
            'posted_time' : i.created_date,
            'like_count' : len(i.like.all()),
            'comment_count' : 0
        })

    # Updating comment_count
    comment_data = Comment.objects.all()
    for i in comment_data:
        for j in blog_context:
            if i.on_blog.title == j['title']:
                j['comment_count'] += 1
                break

    context = {
        'blog' : blog_context
    }

    return render(request,'home.html',context)
