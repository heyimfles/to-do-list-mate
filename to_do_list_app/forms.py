from django import forms

from to_do_list_app.models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "content",
            "deadline",
            "tags",
        ]

        widgets = {
            "content": forms.TextInput(attrs={
                "class": "form-control",
            }),
            "deadline": forms.DateTimeInput(attrs={
                "class": "form-control",
                "type": "datetime-local",
            }),
            "tags": forms.SelectMultiple(attrs={
                "class": "form-control",
            }),
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = [
            "name",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
            }),
        }