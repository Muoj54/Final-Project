from django import forms

class DestinationSubmissionForm(forms.Form):
    name = forms.CharField(label='Destination Name', max_length=100, required=False)
    latitude = forms.DecimalField(label='Latitude', max_digits=9, decimal_places=6, required=False)
    longitude = forms.DecimalField(label='Longitude', max_digits=9, decimal_places=6, required=False)
    additional_info = forms.CharField(label='Additional Information', max_length=200, required=False)
    message = forms.CharField(label='Suggestions/Recommendations', max_length=200, required=False)