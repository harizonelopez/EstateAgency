from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Property
from enquiries.forms import EnquiryForm


def property_list(request):
    properties = Property.objects.filter(
        is_available=True
    )
    context = {
        'properties': properties,
    }
    return render( request, 'properties/property_list.html', context )


def property_detail(request, slug):
    property = get_object_or_404(
        Property.objects.prefetch_related('images'),
        slug=slug,
        is_available=True
    )
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save(commit=False)

            # Associate the enquiry with this property
            enquiry.property = property
            enquiry.save()
            messages.success(
                request,
                'Your enquiry has been submitted successfully!'
            )
            return redirect( 'properties:detail', slug=property.slug )

    else:
        form = EnquiryForm()

    context = {
        'property': property,
        'form': form,
    }

    return render( request, 'properties/property_detail.html', context )
