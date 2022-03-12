from pyexpat import model
from re import A
from tkinter import HIDDEN
from django import forms
from .models import post


class postform(forms.ModelForm):
    class Meta:
        model = post
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id' : 'name', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
