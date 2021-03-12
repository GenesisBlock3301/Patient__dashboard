from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from PatitentDash import settings

urlpatterns = [
    path('', views.PatientFormView.as_view(), name='form'),
    path('dashboard/', views.DashboardView.as_view(), name="dashboard"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
]
