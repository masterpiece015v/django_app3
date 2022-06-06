from django import forms

class FindForm( forms.Form):
    find = forms.CharField(label='Find',required=False,
    widget=forms.TextInput(attrs={'class':'form-controls'}))
