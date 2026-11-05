from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Property
from enquiries.forms import EnquiryForm
from django.conf import settings
from django.core.mail import send_mail


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
            enquiry.property = property
            enquiry.save()

            subject = f'New Property Enquiry - {property.title}'

            message = f"""
        A new enquiry has been submitted on EstateAgency.

        CLIENT DETAILS
        --------------
        Name: {enquiry.full_name}
        Email: {enquiry.email}
        Phone: {enquiry.phone or 'Not provided'}

        ENQUIRY DETAILS
        ---------------
        Type: {enquiry.enquiry_type}
        Property: {property.title}
        Property ID: {property.property_id}
        Location: {property.location}

        MESSAGE
        -------
        {enquiry.message}
        """

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.AGENCY_EMAIL],
                fail_silently=False,
            )

            messages.success(
                request,
                'Your enquiry has been submitted successfully!'
            )

            return redirect('properties:detail', slug=property.slug)

    else:
        form = EnquiryForm()

    context = {
        'property': property,
        'form': form,
    }
    return render( request, 'properties/property_detail.html', context )
