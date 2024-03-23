from django import forms
from .models import Bookings,Event

class Dateinput(forms.DateInput):
    input_type='date'

class Bookingform(forms.ModelForm):
    class Meta:
        model=Bookings
        fields='__all__'
        
        widgets={
            'booking_date':Dateinput()
        }
        
        labels={
            'cus_name':'name',
            'cus_ph':'phone',
            'name':'event name',
            
            
        }
        