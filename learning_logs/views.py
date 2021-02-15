from django.shortcuts import render

from .models import Topic

# Create your views here.

def index(request):
    """Home page of learning_logs app."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Shows all the topics created by user."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)