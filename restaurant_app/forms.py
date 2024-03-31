from . models import RestaurantTable
from django import forms

#create your forms here

class TableForm(forms.Form):
    person_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone_number = forms.IntegerField()
    # date_to_come = forms.DateField()
    # time_to_come = forms.DateTimeField()
    number_of_people = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea())
