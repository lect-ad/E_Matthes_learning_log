from django.shortcuts import render

# Create your views here.

def index(request):
    """Home page of learning_logs app."""
    return render(request, 'learning_logs/index.html')