from django.forms import ModelForm
from django.contrib.admin import widgets                                       
from django import forms
from securityrules import models 


class SecurityRulesForms(ModelForm):
    """
    Enable the security rules.
    """
    class Meta:
        model = models.SecurityRules
        fields = "__all__"
