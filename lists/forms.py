from django import forms
from .models import twoDo

class twoDoForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Add Todo '}))
    class Meta:
        model = twoDo
        fields = ('title',)