from testapp.models import Employee
from django import forms
class Empform(ModelForm):
    class Meta:
        model=Employee
        fields=__all__
