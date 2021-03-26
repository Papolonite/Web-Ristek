from django.urls import path
from django.contrib.auth import views as auth_views
from .views import delete_comment, update_comment

urlpatterns = [
    path('delete_comment/<int:id>', delete_comment, name='delete_comment'),
    path('update_comment/<int:id>', update_comment, name='update_comment'),
]