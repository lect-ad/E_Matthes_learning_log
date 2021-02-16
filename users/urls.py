"""
Sets URL patterns for users app.
"""

from django.urls import path, include

from . import views


app_name = 'users'
urlpatterns = [
    # Django default authentication pages.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', views.register, name='register')
]