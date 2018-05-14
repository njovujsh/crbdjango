from django.contrib import admin

from processrecords import models 

class ExcelSheetAdmin(admin.ModelAdmin):
    list_display=("id", "sheetname")
admin.site.register(models.ExcelSheets, ExcelSheetAdmin)

class ExcelSheetProcessed(admin.ModelAdmin):
    list_display=("id", "recordname", "updatedate", "processby")
admin.site.register(models.ProcessRecords, ExcelSheetProcessed)
