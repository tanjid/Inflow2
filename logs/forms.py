from django import forms

class LogSearch(forms.Form):
    invoive_number = forms.CharField(required=True)