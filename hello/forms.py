from turtle import textinput
from django import forms

from hello.models import Friend,Message

class MessageForm( forms.ModelForm ):
    class Meta:
        model = Message
        fields = ['title','content','friend']
        widget = {
            'title':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'content':forms.Textarea(attrs={'class':'form-control form-control-sm','rows':2}),
            'friend':forms.Select( attrs={'class':'form-control form-control-sm'})
        }


class FriendForm( forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name','mail','gender','age','birthday']

class FindForm( forms.Form):
    find = forms.CharField(label='Find',required=False,
        widget=forms.TextInput(attrs={'class':'form-controls'}))
    findName = forms.CharField( label='FindName', required=False,
        widget=forms.TextInput(attrs={'class':'form-controls'}))
    findMail = forms.CharField( label='FindMail' , required=False,
        widget=forms.TextInput(attrs={'class':'form-controls'}))
    order = forms.BooleanField(label='Order',required=False,
        widget=forms.CheckboxInput(attrs={'class':'form-controls'}))

class CheckForm( forms.Form ):
    str = forms.CharField(label='Name',min_length=8,
        widget=forms.TextInput(attrs={'class':'form-control'}))
    date = forms.DateField( label='Date', input_formats=['%y/%m/%d'],
        widget=forms.DateInput(attrs={'class':'form-control'}))


    
