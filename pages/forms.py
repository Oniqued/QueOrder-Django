from django import forms
from pages.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['subject', 'user_name', 'content']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
