from django.db import models


class LegacyTracker(models.Model):
    DEFINED_DB = (
                    ("mysql", "MYSQL Database Engine"),
                    ("postgres", "Postgre Database Engine"),
                    ("sqlite3", "Sqlite3 Database Engine(Requires developer integration)"),
                    )
    database_engine = models.CharField(max_length=250, choices=DEFINED_DB, blank=False, null=False)
    database_hostname = models.CharField(max_length=250,blank=False, null=False)
    database_port = models.CharField(max_length=250,blank=False, null=False)
    database_username = models.CharField(max_length=250,blank=False, null=False)
    database_password = models.CharField(max_length=250,blank=False, null=False)
    
    def __unicode__(self):
        return u"%s" % str(self.database_engine)
        
class ReplicationDatabase(models.Model):
    DEFINED_engines = (
                    ("mysql", "MYSQL Database Engine"),
                    ("postgres", "Postgre Database Engine"),
                    )
    destination_engine = models.CharField(max_length=250, choices=DEFINED_engines, blank=False, null=False)
    destination_hostname = models.CharField(max_length=250,blank=False, null=False)
    destination_port = models.CharField(max_length=250,blank=False, null=False)
    destination_username = models.CharField(max_length=250,blank=False, null=False)
    destination_password = models.CharField(max_length=250,blank=False, null=False)
    
    def __unicode__(self):
        return u"%s" % str(self.destination_engine)
