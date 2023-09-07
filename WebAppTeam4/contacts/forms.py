
from django.forms import ModelForm, CharField, TextInput, EmailField, EmailInput, DateField, DateInput, SelectDateWidget
from datetime import date

from .models import Contact


class ContactForm(ModelForm):
    date_range = 70    
    this_year = date.today().year
    
    first_name = CharField(max_length=100, widget=TextInput(
        attrs={'class': "form-control"}))
    last_name = CharField(max_length=100, widget=TextInput(
        attrs={'class': "form-control"}))
    email = EmailField(max_length=100, required=True,
                       widget=EmailInput(attrs={'class': "form-control"}))
    phone = CharField(max_length=100, widget=TextInput(
        attrs={'class': "form-control"}))
    # birth_date = DateField(required=True, widget=DateInput(
    #     attrs={'class': "form-control"}))
    birth_date = DateField(required=True, widget=SelectDateWidget(years=range(this_year - date_range, this_year+1)))
    comment = CharField(max_length=255, widget=TextInput(attrs={'class': "form-control"}))

########################################################################################
#    comment = CharField(max_length=100, widget=TextInput(attrs={'class': "form-control"}))
# it was commented becasue html does not correspond to this form that is why it does not work if not commented

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'phone', 'birth_date')
