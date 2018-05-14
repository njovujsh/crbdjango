from django.contrib import admin
from fileprocessor import models 

#---REGISTER FILES---#
class RegisterFileAdmin(admin.ModelAdmin):
    list_display=("id", "file_name", "uploaded_name", "uploaded_by", "content_type", "file_size")
    #prepopulated_fields={"slug":["file_name", "uploaded_by"]}
admin.site.register(models.FileUploader, RegisterFileAdmin)

