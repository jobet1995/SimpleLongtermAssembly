"""
@Description: Enrollment App Models modules
@Author: Jobet Casquejo
@Group: 
@Last Modified By: Jobet Casquejo
@Last Modifed On: 5/20/2024
Modification Log
Ver     Date        Author          Modification
1.0     5/20/2024   Jobet Casquejo  Initial Version
"""
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
import datetime


class BaseModel(models.Model):
    """
    This is an abstract base class that provides audit fields for child models.
    Child models will automatedly get these fields and use them to track when a 
    record is created or updated, and by whom.
    """
    created_date = models.DateField()
    updated_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    # adding an example of public method
    def is_created_recently(self):
        """
        This checks if the BaseModel record was created recently
        """
        return self.created_date >= timezone.now() - datetime.timedelta(hours=1)

    class Meta:
        abstract = True


class Users(AbstractUser):
    REGISTRAR = '1'
    TREASURER = '2'

    """
    model that includes type with options, extends Django's Abstract.
    """
    EMAIL_TO_USER_TYPE_MAP = {
        'Registrar': REGISTRAR,
        'Treasurer': TREASURER
    }
    user_type_data = ((REGISTRAR, "Registrar"), (TREASURER, "Treasurer"))
    user_type = models.CharField(
        default=1, choices=user_type_data, max_length=10)


class Enrollment(BaseModel):
    """
    Model to handle student enrollment records, includes demographic and contact information.
    """
    gender = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    enrollment_id = models.AutoField(primary_key=True, null=False)
    first_name = models.CharField(max_length=255, null=False)
    middle_initial = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=False)
    birtdate = models.DateField(null=False)
    gender = models.ManyToManyField(gender)
    country = CountryField(blank_label='(Of which country are you a citizen?)')
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)


class EmergencyContact(BaseModel):
    """
    Model to store emergency contact details for enrolling students, includes name, 
    relationship, and contact information.
    """
    languages = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
    emergency_id = models.AutoField(primary_key=True, null=False)
    e_first_name = models.CharField(max_length=255, null=False)
    e_last_name = models.CharField(max_length=255, null=False)
    e_relationship = models.CharField(max_length=255, null=False)
    e_email = models.EmailField(max_length=255)
    e_language = models.ManyToManyField(languages)
    e_language_list = models.TextField()


class Education(BaseModel):
    """
     Model to handle student education history records, includes high school information 
     and graduation date.
    """
    # fields to handle education
    s_id = models.AutoField(primary_key=True, null=False)
    high_school_id = models.AutoField(primary_key=True, null=False)
    high_school_name = models.CharField(max_length=255)
    graduation_date = models.DateField()
    s_city = models.CharField(max_length=255, null=False)
    s_state = models.CharField(max_length=255, null=False)
    s_country = CountryField(blank_label='(Country)')


class Payment(BaseModel):
    """
    Model to handle student payment information, includes payment method options.
    """
    payment_method = [
        ('Credit Card', 'Credit Card'),
        ('Mail a Checkk', 'Mail a Check'),
        ('In-person at school', 'In-person at school')
    ]

    payment_id = models.AutoField(primary_key=True, null=False)
    payment_type = models.ManyToManyField(payment_method)
