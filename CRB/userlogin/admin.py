from django.contrib import admin
from userlogin import models 


class StaffAdmin(admin.ModelAdmin):
    list_display=("firstname", "lastname", "gender", "phone",
                )
    #prepopulated_fields={"slug":["firstname", "lastname", "username"]}
admin.site.register(models.CreditInstitutionStaff, StaffAdmin)

