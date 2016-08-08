from django import forms
from django.forms import Textarea
from .models import Comment

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message', 'author', 'jjal']
        widgets = {
            'message': Textarea(attrs={'cols': 40, 'rows': 2}),
        }


class CommentForm(forms.Form):
    message = forms.CharField()
    author = forms.CharField()
    jjal = forms.ImageField()