from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.Homepage.as_view()),
    path('login', auth_views.LoginView.as_view())
] 