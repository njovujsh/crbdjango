#  models.py
#  
#  Copyright 2015 wangolo joel <wangolo@wangolo-3020>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from django.db import models
import datetime

class PIIdentificationCode(models.Model):
    pi_identification_code = models.CharField(max_length=120, blank=False, unique=True)
    insitution_Name = models.CharField(max_length=120, blank=False)
    date = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return "%s" % self.pi_identification_code

class BranchNames(models.Model):
    Branch_Code = models.CharField(max_length=30, blank=True)
    Branch_name = models.CharField(max_length=30, blank=True)
    
    def __unicode__(self):
        #print "HERE ", self.default_headers.version_number
        return "%s %s " % (self.Branch_name, self.Branch_Code)
        #return unicode(self.Branch_Code)

    def save(self, *args, **kwargs):
        if(str(self.Branch_Code).strip().lstrip().rstrip()):
            self.intify = int(float(self.Branch_Code))
            self.Branch_Code = str(self.intify)
            super(BranchNames, self).save(*args, **kwargs)
        else:
            super(BranchNames, self).save(*args,  **kwargs)

class RequiredHeader(models.Model):
    DATE_FORMAT = "%Y-%m-%d" #FORMAT = "%Y-%m-%d-%H-%M", FORMAT = "%Y-%m-%d-%H-%M-%S", %Y-%m-%d-%H-%M-%S-%w-%f
    DATE = datetime.datetime.today()
    FORMATTED = DATE.strftime(DATE_FORMAT)
    header = models.CharField(max_length=100, default="H", blank=False)
    pi_identification_code = models.ForeignKey(PIIdentificationCode, blank=False)
    #branch_name = models.CharField(max_length=100, default="", blank=True)
    branch_name = models.ForeignKey(BranchNames, blank=True)
    branch_code = models.CharField(max_length=100, default="", blank=True, unique=True)
    submission_date = models.CharField(max_length=100, default="", blank=False)
    version_number = models.CharField(max_length=100, default="", blank=True)
    creation_date = models.CharField(max_length=100, default=FORMATTED, blank=False)

    def __str__(self):
        return "%s %s " % (self.branch_name, self.pi_identification_code.pi_identification_code)

    def get_code(self):
        return  "%s" % self.pi_identification_code

    def get_version(self):
        return "%s" % self.version_number
 
      
class BranchCode(models.Model):
    Branch_Code = models.CharField(max_length=30, blank=False, null=False)
    
    def __unicode__(self):
        return self.Branch_Code
         

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
