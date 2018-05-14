from django.contrib import admin
from util import models

class RegionsModelAdmin(admin.ModelAdmin):
    list_display=("id", "name")
admin.site.register(models.Regions, RegionsModelAdmin)

class DistrictsModelAdmin(admin.ModelAdmin):
    list_display=("id", "name", "code")
admin.site.register(models.Districts, DistrictsModelAdmin)

class SubcountiesModelAdmin(admin.ModelAdmin):
    list_display=("id", "name")
admin.site.register(models.Subcounties, SubcountiesModelAdmin)

class ParishesModelAdmin(admin.ModelAdmin):
    list_display=("id", "name", "name", "votecode", "coordinate")
admin.site.register(models.Parishes, ParishesModelAdmin)
