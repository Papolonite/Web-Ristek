from django.urls import path
from django.contrib.auth import views as auth_views
from .views import add_like, remove_like

urlpatterns = [
    path('like/<int:id>', add_like, name='like'),
    path('unlike/<int:id>', remove_like, name='unlike' )
]