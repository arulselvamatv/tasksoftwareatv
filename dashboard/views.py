from django.shortcuts import render
from django.utils import timezone

def index(request):
    current_time = timezone.now()
    context = {
        'current_time': current_time.strftime('%I:%M %p IST, %B %d, %Y')
    }
    return render(request, 'dashboard.html', context)
