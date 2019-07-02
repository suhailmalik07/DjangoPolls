from django import forms

class CreatePost(forms.Form):
    question = forms.CharField(label = 'Question: ', max_length=120)
    