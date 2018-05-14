from django.forms import ModelForm
from django.contrib.admin import widgets                                       
from django import forms
from legacysystems import models 


class LegacySystemsForms(ModelForm):
    """
    """
    class Meta:
        model = models.LegacyTracker
        fields = "__all__"
        
class ReplicationDatabaseForms(ModelForm):
    """
    """
    class Meta:
        model = models.ReplicationDatabase
        fields = "__all__"
