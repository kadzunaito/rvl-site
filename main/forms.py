from django import forms

from .models import FeedbackMessage


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackMessage
        fields = ("name", "email", "subject", "message")
        widgets = {
            "name": forms.TextInput(attrs={"class": "input"}),
            "email": forms.EmailInput(attrs={"class": "input"}),
            "subject": forms.TextInput(attrs={"class": "input"}),
            "message": forms.Textarea(attrs={"class": "textarea", "rows": 4}),
        }
