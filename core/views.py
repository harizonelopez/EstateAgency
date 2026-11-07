from django.shortcuts import render, get_object_or_404
from properties.models import Property
from agents.models import Agent
from .models import Service

def home(request):
    featured_properties = Property.objects.filter(
        is_featured=True,
        is_available=True
    )[:3]

    agents = Agent.objects.filter(
        is_active=True
    )[:3]

    services = Service.objects.filter(
        is_active=True
    )[:3]

    context = {
        'featured_properties': featured_properties,
        'agents': agents,
        'services': services,
    }
    return render(request, 'core/index.html', context)

def services(request):
    services = Service.objects.filter(is_active=True).order_by('display_order')

    context = {
        'services': services,
    }
    return render(request, 'core/services.html', context)

def service_detail(request, slug):
    service = get_object_or_404(Service,slug=slug,is_active=True)

    other_services = Service.objects.filter(is_active=True).exclude(id=service.id)

    context = {
        'service': service,
        'other_services': other_services,
    }
    return render(request, 'core/service_detail.html', context)

def about(request):
    return render(request, 'core/about.html')