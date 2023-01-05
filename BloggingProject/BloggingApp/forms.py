from dataclasses import fields
from django import forms
from BloggingApp.models import Comments
class SendEmailForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)

class CommentForm(forms.ModelForm):
     class Meta:
         model=Comments
         fields=('name','email','body')

