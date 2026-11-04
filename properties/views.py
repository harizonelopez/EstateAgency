from django.shortcuts import render
from .models import Property


def property_list(request):
    properties = Property.objects.filter(
        is_available=True
    )

    context = {
        'properties': properties,
    }

    return render(
        request,
        'properties/property_list.html',
        context
    )
