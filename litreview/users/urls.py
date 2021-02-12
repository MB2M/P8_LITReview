from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls.conf import include

from . import views


app_name = 'users'
urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            redirect_field_name='reviews/feed.html',
            template_name='users/login.html'
            ),
        name='login'
    ),
    path('register/', views.user_register, name='register'),
    path('', include('django.contrib.auth.urls')),
]
