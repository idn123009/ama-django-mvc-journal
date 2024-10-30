from django import forms
from django.forms import ModelForm
from .models import Entry, Mood

class EntryForm(ModelForm):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'h3 my-1 fw-light w-75 border-1 rounded py-2 text-center'}), max_length=50)
    body = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'w-100 form-control', 'style':'height:600px'}))
    mood = forms.ModelChoiceField(label="Mood", queryset=Mood.objects.all())
    
    class Meta:
        model = Entry
        fields = ['title', 'body', 'mood']