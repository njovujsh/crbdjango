from django.db import models
from CRB import settings 

class SuccessFullFailedGraph(models.Model):
    GRAPH_LOCATION="analysisgraphics"
    graph_image = models.ImageField(upload_to=settings.IMAGE_UPLOAD_PATH, height_field=None, width_field=None, blank=True, null=True, max_length=500)
    record_type = models.CharField(max_length=150, blank=True, null=True)
    imagename = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        if(self.record_type):
            return unicode(self.record_type)
        else:
            return unicode(self.id)
            
