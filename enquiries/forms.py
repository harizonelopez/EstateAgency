from django import forms
from .models import Enquiry
import dns.resolver
from django.core.exceptions import ValidationError

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry

        fields = [
            'full_name',
            'email',
            'phone',
            'enquiry_type',
            'message',
        ]

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Full Name',
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email Address',
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Phone Number',
            }),

            'enquiry_type': forms.Select(attrs={
                'class': 'form-select',
            }),

            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Write your enquiry here...',
            }),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        domain = email.rsplit('@', 1)[1]

        domain_has_route = False

        for record_type in ('MX', 'A', 'AAAA'):
            try:
                dns.resolver.resolve(domain, record_type, lifetime=5)
                domain_has_route = True
                break

            except dns.resolver.NoAnswer:
                continue

            except dns.resolver.NXDOMAIN:
                raise ValidationError(
                    'This email domain does not exist.'
                )

            except (
                dns.resolver.NoNameservers,
                dns.resolver.LifetimeTimeout
            ):
                raise ValidationError(
                    'We could not verify this email domain. Please try again.'
                )

        if not domain_has_route:
            raise ValidationError(
                'This email domain cannot receive emails.'
            )

        return email