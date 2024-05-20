"""
@Description: Enrollment App Forms modules
@Author: Jobet Casquejo
@Group: 
@Last Modified By: Jobet Casquejo
@Last Modifed On: 5/20/2024
Modification Log
Ver     Date        Author          Modification
1.0     5/20/2024   Jobet Casquejo  Initial Version
"""
from django import forms
from .models import Enrollment, EmergencyContact, Education, Payment


class DateInput(forms.DateInput):
    """
    A form class that changes the input type to 'date'.
    This is used to render input elements with type 'date' in templates.
    """
    input_type = "date"


class EnrollmentForms(forms.Form):
    """
    This class represents a form for enrollment data.
    It contains all necessary fields required for the enrollment process.
    """
    first_name = forms.CharField(label="First Name", max_length=255, widget=forms.TextInput(
        attrs={"class": "form-control"}))
    middle_initial = forms.CharField(
        label="Middle Initial", max_length=255, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=255, widget=forms.TextInput(
        attrs={"class": "form-control"}))
    birthdate = forms.DateField(
        label="Birth Date", widget=forms.DateInput(attrs={"class": "form-control"}))
    phone = forms.PhoneNumberField(
        label="Phone", widget=forms.PhoneNumberField(attrs={"class": "form-control"}))
