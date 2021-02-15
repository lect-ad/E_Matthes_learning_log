"""
Sets URL patterns for users app.
"""

from django.urls import path, include


app_name = 'users'
urlpatterns = [
    # Django default log-in page.
    path('', include('django.contrib.auth.urls')),
]