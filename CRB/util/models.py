from django.db import models

class Regions(models.Model):
    name = models.CharField(max_length=255)
    #class Meta:
    #    db_table = 'util_regions'
        
    def __str__(self):
        return self.name 

class Districts(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    region = models.ForeignKey(Regions, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)

    #class Meta:
    #    db_table = 'util_districts'
        
    def __str__(self):
        return self.name
        
class Subcounties(models.Model):
    district  = models.ForeignKey(Districts, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)

    #class Meta:
    #    db_table = 'util_subcounties'

    def __str__(self):
        return self.name
        
class Parishes(models.Model):
    subcounty = models.ForeignKey(Subcounties, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    votecode = models.CharField(max_length=255, blank=True, null=True)
    coordinate = models.CharField(max_length=255, blank=True, null=True)

    #class Meta:
    #    db_table = 'util_parishes'
  
    def __str__(self):
        return self.name
