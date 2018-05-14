from django.db import models

class FileUploader(models.Model):
    #UPLOAD_DIR="/home/wangolo/Public/BOI/banking/datasetsystem/datamedia/filesuploaded"
    file_name = models.CharField(max_length=100)
    uploaded_name = models.FileField(upload_to=".")
    uploaded_by = models.CharField(max_length=100, blank=False)
    content_type = models.CharField(max_length=100, blank=True, null=True)
    file_size = models.CharField(max_length=150, blank=True, null=True)
    #slug = models.SlugField(blank=True, null=True, unique=True)
    
    
    def __unicode__(self):
       return u"%s" % str(self.file_name)

    def get_file_size(self):
       try:
           print os.path.getsize(self.file_name)
           return 12 #os.path.getsize(self.fname)
       except os.error as error:
           raise

    def filepath(self):
       return "/system/asserts/%s" % self.file_name
    
    class Meta:
        ordering = ("-id",)


