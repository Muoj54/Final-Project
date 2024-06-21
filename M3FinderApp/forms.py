from django import forms

class DestinationSubmissionForm(forms.Form):
    name = forms.CharField(label='Destination Name', max_length=100)
    latitude = forms.DecimalField(label='Latitude', max_digits=9, decimal_places=6)
    longitude = forms.DecimalField(label='Longitude', max_digits=9, decimal_places=6)