from .models import *
from django import forms


class BookRoomForm(forms.ModelForm):
    class Meta:
        model = BookRoom
        fields = {
            "full_name",
            "phone_number",
            "arrive_date",
            "departure_date",
            "time",
        }
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.NumberInput(attrs={"class": "form-control"}),
            "arrive_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "departure_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "time": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
        }
