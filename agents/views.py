from django.shortcuts import render
from .models import Agent

# Create your views here.
def agents_list(request):
    agents = Agent.objects.filter(is_active=True)
    context = {
        'agents': agents,
    }
    return render(request, 'agents/agents.html', context)
