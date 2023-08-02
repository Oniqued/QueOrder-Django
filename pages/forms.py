from django import forms
from pages.models import Review
from pages.models import Contact


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['subject', 'content']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'tel_num', 'mail', 'content']
