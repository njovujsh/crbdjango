from django.contrib import admin

from validators import models 

class RegisterValidated(admin.ModelAdmin):
    list_display=("id", "name", "filename", "date")
admin.site.register(models.ValidatedAndSaved, RegisterValidated)
