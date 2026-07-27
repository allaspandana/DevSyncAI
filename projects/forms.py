from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project

        fields = [
            'name',
            'description',
            'team',
            'manager',
            'status',
            'priority',
            'start_date',
            'end_date'
        ]

        widgets = {

            'start_date': forms.DateInput(attrs={
                'type': 'date'
            }),

            'end_date': forms.DateInput(attrs={
                'type': 'date'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()

        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')

        if start and end:
            if end < start:
                raise forms.ValidationError(
                    "End date cannot be before start date."
                )

        return cleaned_data