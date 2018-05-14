from django.db import models
import datetime 
from datasetrecords import models as datasetrecords_models 

class Dataset(models.Model):
    
    #we want to extract class from our module using dir
    model_classes = dir(datasetrecords_models)
    model_class_list = [ ]
    for classes in model_classes:
        if "__" in classes:
            pass 
        elif classes == "models":
            pass 
        elif classes == "PCI":
            pass 
        elif classes == "SCI":
            pass 
        else:
            model_class_list.append(classes)
            
    DATA_SET_CLASSES = [ ]
    for data_record in model_class_list:
        DATA_SET_CLASSES.append((data_record, data_record))
      
    #convert the list into a tuple becase that is what is needed  
    DATA_SET_CLASSES = tuple(DATA_SET_CLASSES)
    dataset_record = models.CharField(max_length=250, blank=False, null=False, choices=DATA_SET_CLASSES)
    dataset = models.CharField(max_length=250, blank=False, null=False)
    slug = models.SlugField(unique=True)
    
    def __unicode__(self):
        """
        Return the unicode representation.
        """
        return u"%s" % self.dataset 
    
    class Meta:
        ordering = ("-id",)
        
    def get_update_path(self):
        return "/newupdate/dataupdatingsystem/%s" % self.slug

    def get_process_path(self):
        return "/processing/data/existing/" #% self.slug

    def get_view_path(self):
        return "/view/dataview/request/%s" % self.slug

    def get_delete_path(self):
        return "/purgerecords/deleting/%s/True/" % self.slug

    def get_new_path(self):
        return "/app/process/datasetrecord/%s" % self.slug
     
