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
    # Page with all the entries for certain topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page with a form for creating new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page with a form for creating new entry for some topic.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]