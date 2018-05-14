from django.forms import ModelForm
from userlogin.models import *
from django.contrib.admin import widgets                                       
from django import forms
from django.forms.models import inlineformset_factory

from django.contrib.auth.models import User

class UserForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForms, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = "Please enter a Unique username" #self.fields['firstname'].label
        self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label
        self.fields['password'].widget.attrs['placeholder'] = "Password Strength is not enforced."
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        fields=("username","email", "password")
        model = User
        #fields = "__all__"
        
class UserLoginForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForms, self).__init__(*args,  **kwargs)
        self.fields['firstname'].widget.attrs['placeholder'] = self.fields['firstname'].label
        self.fields['lastname'].widget.attrs['placeholder'] = self.fields['lastname'].label
        self.fields['phone'].widget.attrs['placeholder'] =  '+2567111111111 or 07111111111'
        
    class Meta:
        fields = ("firstname", "lastname","phone", "gender",
                 "data_access_rights", "can_edit", "can_upload_file",
                 "can_process_data"
                 )
        model = CreditInstitutionStaff
