from django import forms
from .models import Bug

class BugForm(forms.ModelForm):

    class Meta:
        model = Bug

        fields = [
            'task',
            'assigned_to',
            'title',
            'description',
            'severity',
            'priority',
            'status',
            'resolved_date'
        ]

        widgets = {
            'resolved_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get("title")
        task = cleaned_data.get("task")
        status = cleaned_data.get("status")
        resolved_date = cleaned_data.get("resolved_date")

        if not title:
            self.add_error("title", "Title cannot be empty.")

        if not task:
            self.add_error("task", "Task is required.")

        if status in ["Resolved", "Closed"] and not resolved_date:
            self.add_error(
                "resolved_date",
                "Resolved date is required."
            )

        return cleaned_data