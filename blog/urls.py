from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home_view
#url for app
urlpatterns = [
    path('', home_view, name='home'),
]