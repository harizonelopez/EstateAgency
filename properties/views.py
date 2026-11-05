from django.shortcuts import render, get_object_or_404
from .models import Property


def property_list(request):
    properties = Property.objects.filter(
        is_available=True
    )

    context = {
        'properties': properties,
    }

    return render(request,'properties/property_list.html', context)

def property_detail(request, slug):
    property = get_object_or_404(
        Property.objects.prefetch_related('images'), 
        slug=slug,
        is_available=True
    )

    context = {
        'property': property,
    }

    return render(request, 'properties/property_detail.html', context)
