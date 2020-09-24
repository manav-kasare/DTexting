from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.register, name='register'),
    path('home/', views.index, name='index'),
    path('signin/',  LoginView.as_view(template_name='signin.html'), name="signin"),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit', views.edit_profile, name='edit_profile')
]