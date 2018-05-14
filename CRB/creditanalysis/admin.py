from django.contrib import admin
from creditanalysis import models as creditmodels

class RegisterCreditAnalysis(admin.ModelAdmin):
    list_display=("id", "graph_image", "record_type","imagename", "date") 
admin.site.register(creditmodels.SuccessFullFailedGraph, RegisterCreditAnalysis)
