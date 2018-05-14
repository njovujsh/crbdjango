from django.forms import ModelForm
from django.contrib.admin import widgets                                       
from django import forms
from django.forms.models import inlineformset_factory
from branchcode import models 
from django.contrib.admin import widgets    

class PIIdentificationCodeForm(ModelForm):
    class Meta:
        exclude=("date",)
        model = models.PIIdentificationCode
        #fields = "__all__"
        
class BranchCodeForms(ModelForm):
    class Meta:
        model = models.BranchCode
        fields = "__all__"
        
#class DefaultHeadersForms(ModelForm):
#    def __init__(self, *args,  **kwargs):
#        super(DefaultHeadersForms, self).__init__(*args, **kwargs)
#        self.fields['default_headers'].widget.attrs['class'] = "Developers."
        
#    class Meta:
#        model = models.DefaultHeaders
#        fields = '__all__'

class EmailForm(forms.Form):
    endpoint_address  = forms.EmailField(label='Endpoint email', required = True)
    source_address = forms.EmailField(label="Source Email", required=True)
    upload_one = forms.Field(label='Upload One', widget = forms.FileInput,    required = True)
    upload_two = forms.Field(label='Upload Two', widget = forms.FileInput, required = False )
    upload_three = forms.Field(label='Upload Three', widget = forms.FileInput, required = False)
    upload_four = forms.Field(label='Upload  Four', widget = forms.FileInput, required = False)
    upload_five = forms.Field(label='Upload  Five', widget = forms.FileInput, required = False)
    description = forms.CharField(label='Few words', required =False )

class SFTPForm(forms.Form):
    hostname = forms.CharField(label="SFTP Server", required=True)
    port = forms.CharField(label="SFTP Port", required=True)
    username = forms.CharField(label="SFTP Username", required=True)
    password = forms.CharField(label="SFTP Password", required=True,widget=forms.PasswordInput)
    upload_one = forms.Field(label='Local file 1', widget=forms.FileInput, required = True)
    upload_two = forms.Field(label='Local file 2', widget=forms.FileInput, required = True)
    upload_three = forms.Field(label='Local file 3', widget=forms.FileInput, required = True)
    upload_four = forms.Field(label='Local file 4', widget=forms.FileInput, required = True)
    upload_five = forms.Field(label='Local file 5', widget=forms.FileInput, required = True)
  
class DatasetRecordForms(ModelForm):
    def __init__(self, *args,  **kwargs):
        super(DatasetRecordForms, self).__init__(*args, **kwargs)
        self.fields['pi_identification_code'].widget.attrs['placeholder'] = "Unique PI CODE" #self.fields['pi_identification_code'].label
        #self.fields['institution_name'].widget.attrs['placeholder'] = self.fields['institution_name'].label
        self.fields['submission_date'].widget.attrs['placeholder'] = "yy-mm-dd" #self.fields['institution_name'].label
        self.fields['version_number'].widget.attrs['placeholder'] = "Enter version number EG V 1" #self.fields['institution_name'].label
        #self.fields['creation_date'].widget.attrs['placeholder'] = "yy-mm-dd" #self.fields['institution_name'].label
        
    class Meta:
        exclude=("header","creation_date")
        model = models.RequiredHeader
        #fields = "__all__"
        
class RequiredHeaderForm(ModelForm):
    def __init__(self, *args,  **kwargs):
        super(RequiredHeaderForm, self).__init__(*args, **kwargs)
        self.fields['pi_identification_code'].widget.attrs['placeholder'] = "Unique PI CODE" #self.fields['pi_identification_code'].label
        #self.fields['institution_name'].widget.attrs['placeholder'] = self.fields['institution_name'].label
        #self.fields['submission_date'].widget.attrs['placeholder'] = "yy-mm-dd" #self.fields['institution_name'].label
        #self.fields['version_number'].widget.attrs['placeholder'] = "Enter version number EG V 1" #self.fields['institution_name'].label
        #self.fields['creation_date'].widget.attrs['placeholder'] = "yy-mm-dd" #self.fields['institution_name'].label
        
    class Meta:
        exclude=("header","creation_date", "submission_date", "version_number")
        model = models.RequiredHeader
        #fields = "__all__"  
