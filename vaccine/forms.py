from django import forms
from django.forms import DateTimeInput
from .models import Vaccine , Payment
from .models import Vaccination
class VaccinetionForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields= ('Vaccine_name','First_schudle')
        widgets = {
            'First_schudle': DateTimeInput(attrs={'type': 'datetime-local'}),
        }
class EditVaccinetionForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields= ('First_schudle','Second_schdule')
        widgets = {
            'First_schudle': DateTimeInput(attrs={'type': 'datetime-local'}),
            'Second_schdule': DateTimeInput(attrs={'type': 'datetime-local'}),
        }
class VaccineForm(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ('__all__')


class PaymentForm(forms.ModelForm):
    class Meta:
        model= Payment
        fields = ('Name','Card_No','Expiry_date','Cvv')



