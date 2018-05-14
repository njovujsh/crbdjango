from django.db import models


class ValidatedAndSaved(models.Model):
    name = models.CharField(max_length=120, blank=False,null=False)
    filename = models.FileField(upload_to=".", blank=True, null=True, max_length=500)
    imagename = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-id",)
    
    def __unicode__(self):
        return self.name 
