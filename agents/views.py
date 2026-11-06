from django.shortcuts import render, get_object_or_404
from .models import Agent


def agents_list(request):
    agents = Agent.objects.filter(is_active=True)
    context = {
        'agents': agents,
    }
    return render(request, 'agents/agents.html', context)


def agent_detail(request, pk):
    agent = get_object_or_404(
        Agent.objects.prefetch_related('services'),
        pk=pk,
        is_active=True
    )
    services = agent.services.filter(is_active=True)
    context = {
        'agent': agent,
        'services': services,
    }
    return render(request, 'agents/agent_detail.html', context)