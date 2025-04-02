from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):
    summary = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'summary',
            }
        )
    )

    memo = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder':'memo',
                'rows':5, 
                'cols':20,
                'style': 'resize: none;'
            }
        )
    )

    class Meta:
        model = Memo
        fields = '__all__'