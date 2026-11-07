from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .forms import EnquiryForm

def contact(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save(commit=False)
            enquiry.property = None
            enquiry.save()

            subject = f'New General Enquiry - {enquiry.full_name}'
            message = f"""
                A new enquiry has been submitted through the contact section.

                CLIENT DETAILS
                --------------
                Name: {enquiry.full_name}
                Email: {enquiry.email}
                Phone: {enquiry.phone or 'Not provided'}

                ENQUIRY TYPE
                ---------------
                Type: {enquiry.enquiry_type}

                MESSAGE
                -------
                {enquiry.message}
            """

            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.AGENCY_EMAIL],
                fail_silently=False,
            )

            send_mail(
                subject='We received your enquiry - PropertyPlus',
                message=f"""
                    Hello {enquiry.full_name},

                    Thank you for contacting PropertyPlus EstateAgency.

                    We have successfully received your enquiry. Our team will get back to you.

                    Thank you for choosing PropertyPlus.

                    PropertyPlus EstateAgency Help Desk Team.
                """,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[enquiry.email],
                fail_silently=True,
            )

            messages.success(request, 'Your message has been sent successfully. Thank you for contacting us!')
            return redirect('enquiries:contact')
    else:
        form = EnquiryForm()

    return render(request, 'enquiries/contact.html', {'form': form})
