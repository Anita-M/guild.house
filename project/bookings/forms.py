# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .models import Booking
from datetime import date, timedelta
from django import forms
from tinymce.widgets import TinyMCE


class BookingAdminForm(forms.ModelForm):

    class Meta(object):
        fields = ['name', 'site', 'reserved_date', 'reserved_time']
        model = Booking
        widgets = {'notes': TinyMCE()}


class BookingForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta(object):
        fields = ['name', 'reserved_time', 'reserved_date', 'party_size', 'email',
                  'phone', 'booking_method', 'status', 'notes']
        model = Booking
        widgets = {'notes': forms.Textarea(attrs={'rows':4, 'cols':22})}

        def __init__(self, *args, **kwargs):
            super(BookingForm, self).__init__(*args, **kwargs)
            self.fields['phone'].required = True
            self.fields['email'].required = True

    def clean(self, *args, **kwargs):
        cleaned_data = super(BookingForm, self).clean(*args, **kwargs)
        if not cleaned_data.get('email') and not cleaned_data.get('phone'):
            raise forms.ValidationError('Either a phone or an email address must be provided (or both).')
        return super(BookingForm, self).clean(*args, **kwargs)