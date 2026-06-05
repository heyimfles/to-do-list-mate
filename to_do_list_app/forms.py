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
            "deadline": forms.DateTimeInput(attrs={
                "type": "datetime-local",
            }),
        }
