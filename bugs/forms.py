from django import forms
from .models import Bug


class BugForm(forms.ModelForm):

    class Meta:

        model = Bug

        fields = [
            "task",
            "assigned_to",
            "title",
            "description",
            "severity",
            "priority",
            "status",
            "resolved_date",
        ]


        widgets = {

            "title": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Enter bug title"
                }
            ),


            "description": forms.Textarea(
                attrs={
                    "class":"form-control",
                    "rows":4,
                    "placeholder":"Describe the bug"
                }
            ),


            "severity": forms.Select(
                attrs={
                    "class":"form-select"
                }
            ),


            "priority": forms.Select(
                attrs={
                    "class":"form-select"
                }
            ),


            "status": forms.Select(
                attrs={
                    "class":"form-select"
                }
            ),


            "task": forms.Select(
                attrs={
                    "class":"form-select"
                }
            ),


            "assigned_to": forms.Select(
                attrs={
                    "class":"form-select"
                }
            ),


            "resolved_date": forms.DateInput(
                attrs={
                    "class":"form-control",
                    "type":"date"
                }
            ),
        }