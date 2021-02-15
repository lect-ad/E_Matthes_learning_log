"""
Sets URL patterns for learning_logs app.
"""

from django.urls import path
from . import views


app_name = 'learning_logs'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Page with all the topics created by user.
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic')
]