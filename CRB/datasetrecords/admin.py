from django.contrib import admin
from datasetrecords.models import PARTICIPATING_INSTITUTION, INSTITUTION_BRANCH
from datasetrecords.models import BOUNCEDCHEQUES, CREDITBORROWERACCOUNT
from datasetrecords.models import CREDIT_APPLICATION, BORROWERSTAKEHOLDER
from datasetrecords.models import COLLATERAL_MATERIAL_COLLATERAL, COLLATERAL_CREDIT_GUARANTOR
from datasetrecords.models import FINANCIAL_MALPRACTICE_DATA, PARTICIPATINGINSTITUTIONSTAKEHOLDER
from datasetrecords.models import PCI, SCI, BorrowerHistory

#This methods will be called when any of our data needs to be
#exported as the formated selected
def export_as_comma_separated_values(modeladmin, request, queryset):
    """
    Function exports the given data as CSV
    The data to be exported as csv will be passed to this function
    through queryset.
    """
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = "attachment; filename=exportedcsv.csv"
    writer = csv.writer(response, csv.excel)
    writer.writerow([
            smart_str(u"ID"),
            smart_str(u"Title"),
            smart_str(u"Description"),
            ])
    for obj in queryset:
        writer.writerow([
                    smart_str(obj.id),
                    smart_str(obj.username),
                    smart_str(obj.login),
                    ])
    return response 
export_as_comma_separated_values.short_description = u"Export as CSV"

def export_as_binary_excel(modeladmin, request, queryset):
    print "Exporting as ", request 
    
def export_as_office_open_xml(modeladmin, request, queryset):
    print "Exporting as openoffice", request 

class PARTICIPATING_INSTITUTION_Admin(admin.ModelAdmin):
    data_hierarch = "PI_Identification_Code" 
    #print PARTICIPATING_INSTITUTION.PI_Identification_Code
    list_display=("PI_Identification_Code", 
    "Institution_Type",
    "Institution_Name",
    "License_Issuing_Date",
)
#---Registering PARTICIPATING_INSTITUTION with the admin interface----#
admin.site.register(PARTICIPATING_INSTITUTION, PARTICIPATING_INSTITUTION_Admin)


class INSTITUTION_BRANCH_Admin(admin.ModelAdmin):
    pass 
#----INSTITUTION_BRANCH with the admin interface----#
admin.site.register(INSTITUTION_BRANCH, INSTITUTION_BRANCH_Admin)

class CREDITBORROWERACCOUNT_Admin(admin.ModelAdmin):
    pass 
admin.site.register(CREDITBORROWERACCOUNT, CREDITBORROWERACCOUNT_Admin)


class CREDIT_APPLICATION_Admin(admin.ModelAdmin):
    pass 
admin.site.register(CREDIT_APPLICATION, CREDIT_APPLICATION_Admin)

class BOUNCEDCHEQUES_Admin(admin.ModelAdmin):
    pass 
admin.site.register(BOUNCEDCHEQUES, BOUNCEDCHEQUES_Admin)

class BORROWERSTAKEHOLDER_Admin(admin.ModelAdmin):
    pass 
admin.site.register(BORROWERSTAKEHOLDER, BORROWERSTAKEHOLDER_Admin)


class COLLATERAL_MATERIAL_COLLATERAL_Admin(admin.ModelAdmin):
    pass 
admin.site.register(COLLATERAL_MATERIAL_COLLATERAL, COLLATERAL_MATERIAL_COLLATERAL_Admin)

class COLLATERAL_CREDIT_GUARANTOR_Admin(admin.ModelAdmin):
    pass 
admin.site.register(COLLATERAL_CREDIT_GUARANTOR, COLLATERAL_CREDIT_GUARANTOR_Admin)


class FINANCIAL_MALPRACTICE_DATA_Admin(admin.ModelAdmin):
    pass 
admin.site.register(FINANCIAL_MALPRACTICE_DATA, FINANCIAL_MALPRACTICE_DATA_Admin)

class PARTICIPATINGINSTITUTIONSTAKEHOLDER_Admin(admin.ModelAdmin):
    pass 
admin.site.register(PARTICIPATINGINSTITUTIONSTAKEHOLDER, PARTICIPATINGINSTITUTIONSTAKEHOLDER_Admin)

class PCIAdmin(admin.ModelAdmin):
    data_hierarch = "id"
    list_display=("id", "PCI_Building_Unit_Number", "PCI_Building_Name")
admin.site.register(PCI, PCIAdmin)

class SCIAdmin(admin.ModelAdmin):
    data_hierarch="id"
    list_display=("id", "SCI_Unit_Number", "SCI_Unit_Name")
admin.site.register(SCI, SCIAdmin)

class BorrowerHistoryAdmin(admin.ModelAdmin):
    data_hierarch="id"
    list_display=("id", "borrower_status", "amount", "account_reference", "date")
admin.site.register(BorrowerHistory, BorrowerHistoryAdmin)
