from django.contrib import admin
from branchcode.models import RequiredHeader, BranchCode, PIIdentificationCode, BranchNames

class RecordHeadersModelAdmin(admin.ModelAdmin):
    list_display=("id", "header", 'submission_date', "branch_name", "branch_code",
                    'version_number'
                )
    #prepopulated_fields={"slug":["header", "creation_date", "pi_identification_code", "institution_name"]} 
admin.site.register(RequiredHeader, RecordHeadersModelAdmin)

class BranchCodeModelAdmin(admin.ModelAdmin):
    list_display=("id", "Branch_Code")
admin.site.register(BranchCode, BranchCodeModelAdmin)

class BranchNamesModelAdmin(admin.ModelAdmin):
    list_display=("id", "Branch_Code", "Branch_name")
admin.site.register(BranchNames, BranchNamesModelAdmin)

class PIIdentificationCodeModelAdmin(admin.ModelAdmin):
    list_display=("id", "pi_identification_code", "insitution_Name", "date")
admin.site.register(PIIdentificationCode, PIIdentificationCodeModelAdmin)
