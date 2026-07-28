from django import forms
from .models import Task
from datetime import date


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task

        fields = [
            'sprint',
            'assigned_to',
            'title',
            'description',
            'status',
            'priority',
            'due_date',
            'estimated_hours'
        ]

        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']

        if not title.strip():
            raise forms.ValidationError("Title cannot be empty.")

        return title

    def clean_due_date(self):
        due = self.cleaned_data['due_date']

        if due < date.today():
            raise forms.ValidationError(
                "Due date cannot be before today."
            )

        return due

    def clean_estimated_hours(self):
        hours = self.cleaned_data['estimated_hours']

        if hours <= 0:
            raise forms.ValidationError(
                "Estimated hours must be greater than zero."
            )

        return hours

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'