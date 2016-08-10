from django import forms
from django.forms import Textarea
from .models import Comment

'''
class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message', 'author', 'jjal']
        widgets = {
            'message': Textarea(attrs={'cols': 40, 'rows': 2}),
        }
'''

class CommentForm(forms.Form):
    message = forms.CharField()
    author = forms.CharField()
    jjal = forms.ImageField()


# 폼으로 모델폼 역할 하도록 만들기
class CommentModelForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    author = forms.CharField()

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)

        if self.instance:
            self.fields['message'].initial = self.instance.message
            self.fields['author'].initial = self.instance.author
        else:
            self.instance = Comment()

    def save(self, commit=True):
        self.instance.message = self.cleaned_data['message']
        self.instance.author = self.cleaned_data['atuthor']
        if commit:
            self.instance.save()
        return self.instance




