from django.forms import ModelForm
from datasets.models import *
from django.contrib.admin import widgets                                       
from django import forms
from django.forms.models import inlineformset_factory
from processrecords import models

class ExcelLegacyForms(ModelForm):
    class Meta:
        model = models.TemporaryExcelUploader
        fields = "__all__"
