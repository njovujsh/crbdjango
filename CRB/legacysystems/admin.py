from django.contrib import admin
from legacysystems import models 

class RegisterLegacySystems(admin.ModelAdmin):
    list_display=("id", "database_engine", "database_hostname", "database_port", "database_username")
admin.site.register(models.LegacyTracker, RegisterLegacySystems) 

class RegisterReplicationSystems(admin.ModelAdmin):
    list_display=("id", "destination_engine", "destination_hostname", "destination_port", "destination_username")
admin.site.register(models.ReplicationDatabase, RegisterReplicationSystems) 
