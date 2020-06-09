from django import forms
from .models import NotesDB

class NotesDBForm(forms.ModelForm):
    notes = forms.CharField(widget=forms.Textarea(attrs={"rows":10, "cols":80}))
    todo = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":40}))
    class Meta:
        model = NotesDB
        fields= "__all__"
