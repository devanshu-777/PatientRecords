"""patientrecords URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf.urls import handler404

def user_login_redirect(request):
    # Redirect users to Google OAuth login
    return redirect("/accounts/google/login/")

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin login works with Django's default login page
    path('accounts/', include("allauth.urls")),  # Allauth URLs for OAuth login
    path('', include("users.urls")),  # User-defined views
    path('login/', user_login_redirect, name="login"),  # Custom login route for users
]

handler404 = 'users.views.custom_404_view'