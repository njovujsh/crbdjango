from django.contrib import admin
from datasets import models 

class DatasetModelAdmin(admin.ModelAdmin):
    list_display=("id", "dataset", "slug")
    prepopulated_fields={"slug":["dataset"],"dataset":["dataset_record"]}
admin.site.register(models.Dataset, DatasetModelAdmin)

