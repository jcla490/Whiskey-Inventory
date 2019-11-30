from django.shortcuts import render
from .models import Spirit

def index(request):
    spirits = Spirit.objects.all()
    
    context = {
        "spirits": spirits
    }

    return render(request, 'whiskey_list/index.html', context)

# Maybe I'll add a detail view later, who can say?