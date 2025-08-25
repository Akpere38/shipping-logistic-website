from django import forms

class TrackingForm(forms.Form):
    tracking_id = forms.CharField(max_length=20, label='Tracking ID')