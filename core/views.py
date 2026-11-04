from django.shortcuts import render
from properties.models import Property
from agents.models import Agent

def home(request):
    featured_properties = Property.objects.filter(
        is_featured=True,
        is_available=True
    ) [:3]

    agents = Agent.objects.filter(
        is_active=True
    ) [:3]

    context = {
        'featured_properties': featured_properties,
        'agents': agents,
    }

    return render(request, 'core/index.html', context)