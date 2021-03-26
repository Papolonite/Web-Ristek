from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home_view, blog_detail, your_post_view, create_post, delete_post, update_post

urlpatterns = [
    path('', home_view, name='home'),
    path('your_post',your_post_view, name="your_post" ),
    path('blog/<int:id>', blog_detail, name='blog_detail'),
    path('new_blog', create_post, name='create_post'),
    path('delete_post/<int:id>', delete_post, name='delete_post'),
    path('update_post/<int:id>', update_post, name='update_post' )
]