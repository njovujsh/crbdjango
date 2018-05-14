from django.forms import ModelForm
from fileprocessor.models import *
from django.contrib.admin import widgets                                       
from django import forms
from django.forms.models import inlineformset_factory

class FileForms(ModelForm):
    class Meta:
        exclude=("uploaded_by", "content_type", "file_size", "slug")
        model = FileUploader
