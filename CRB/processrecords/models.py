from django.db import models
from fileprocessor import models as filemodel

class TemporaryExcelUploader(models.Model):
    excel = models.FileField(upload_to="legacyuploads", null=True, blank=True, max_length=500)

    class Meta:
        ordering = ("-id", )
        
    def __str__(self):
        return self.id
        
class ExcelSheets(models.Model):
    excelname = models.OneToOneField(filemodel.FileUploader, null=True, blank=True)
    sheetname = models.FileField(upload_to=".", blank=True, null=True, max_length=250)
    dateuploaded = models.DateTimeField(auto_now_add=True)

    
    def __unicode__(self):
        """
        return the unicode representation.
        """
        return u"%s" % str(self.sheetname)
        
    class Meta:
        ordering = ("-id", )
        
    def get_sheet_path(self):
        return "/file/sheetname/%s" % str(self.sheetname.replace("_", " ", len(self.sheetname)).replace(" ", "", len(self.sheetname)))


class ProcessRecords(models.Model):
    recordname = models.CharField(max_length=200, null=True, blank=True)
    filepath = models.FileField(upload_to=".", blank=True, null=True, max_length=250)
    updatedate = models.DateTimeField(auto_now_add=True)
    processby = models.CharField(max_length=160, blank=True, null=True)

    class Meta:
        ordering = ("-id", )
        
    def __unicode__(self):
        return "%s" % self.filepath
 
