from django.contrib import admin
from securityrules import models 

class RegisterSecurityRules(admin.ModelAdmin):
    list_display=("id", "decision", "source_IP", "description",'date')
admin.site.register(models.SecurityRules, RegisterSecurityRules)
