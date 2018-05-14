from django.contrib import admin
from creditreports import models 


class RegisterPI(admin.ModelAdmin):
    list_display=("id", "validation_date", "total_records", "successful_records", "failed_records",
                    "number_of_fields_passed", "number_of_fields_failed",
                    "record_type", "pi_name"
                    ) 
admin.site.register(models.PIValidationReport, RegisterPI)

class RegisterPIS(admin.ModelAdmin):
    list_display=("id", "validation_date", "total_records", "successful_records", "failed_records",
                    "number_of_fields_passed", "number_of_fields_failed",
                    "record_type", "pi_name"
                    ) 
admin.site.register(models.PISValidationReport, RegisterPIS)

class RegisterBC(admin.ModelAdmin):
    list_display=("id", "validation_date", "total_records", "successful_records", "failed_records",
                    "number_of_fields_passed", "number_of_fields_failed",
                    "record_type", "pi_name"
                    ) 
admin.site.register(models.BCValidationReport, RegisterBC)

class RegisterBS(admin.ModelAdmin):
    list_display=("id", "validation_date", "total_records", "successful_records", "failed_records",
                    "number_of_fields_passed", "number_of_fields_failed",
                    "record_type", "pi_name"
                    ) 
admin.site.register(models.BSValidationReport, RegisterBS)

class RegisterCAP(admin.ModelAdmin):
    list_display=("id", "validation_date", "total_records", "successful_records", "failed_records",
                    "number_of_fields_passed", "number_of_fields_failed",
                    "record_type", "pi_name"
                    ) 
admin.site.register(models.CAPValidationReport, RegisterCAP)

class RegisterCBA(admin.ModelAdmin):
    list_display=("id", "validation_date", "total_records", "successful_records", "failed_records",
                    "number_of_fields_passed", "number_of_fields_failed",
                    "record_type", "pi_name"
                    ) 
admin.site.register(models.CBAValidationReport, RegisterCBA)


class RegisterFRA(admin.ModelAdmin):
    list_display=("id", "validation_date", "total_records", "successful_records", "failed_records",
                    "number_of_fields_passed", "number_of_fields_failed",
                    "record_type", "pi_name"
                    ) 
admin.site.register(models.FRAValidationReport, RegisterFRA)

class RegisterCMC(admin.ModelAdmin):
    list_display=("id", "validation_date", "total_records", "successful_records", "failed_records",
                    "number_of_fields_passed", "number_of_fields_failed",
                    "record_type", "pi_name"
                    ) 
admin.site.register(models.CMCValidationReport, RegisterCMC)

class RegisterCCG(admin.ModelAdmin):
    list_display=("id", "validation_date", "total_records", "successful_records", "failed_records",
                    "number_of_fields_passed", "number_of_fields_failed",
                    "record_type", "pi_name"
                    ) 
admin.site.register(models.CCGValidationReport, RegisterCCG)

class RegisterIB(admin.ModelAdmin):
    list_display=("id", "validation_date", "total_records", "successful_records", "failed_records",
                    "number_of_fields_passed", "number_of_fields_failed",
                    "record_type", "pi_name"
                    ) 
admin.site.register(models.IBValidationReport, RegisterIB)


