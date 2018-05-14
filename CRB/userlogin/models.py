from django.db import models
from django.contrib.auth.models import User
from datasets import models as dataset_models


class InstitutionLogo(models.Model):
    LOGO_DIR = "institution_logo"
    institution_logo_url = models.ImageField(upload_to=LOGO_DIR, height_field=None, width_field=None, max_length=150, blank=True)
    institution_name = models.CharField(max_length=50, default="Swirling", blank=True)
    institution_website = models.URLField(blank=True, null=True)
    
    def __unicode__(self):
        return self.institution_name
        
    class Meta:
        ordering = ("-id",)
        
class CreditInstitutionStaff(models.Model):
    """
    Data model underlaying the database structure.
    """
    
    GENDER_CHOICE = ( ("M", "Male"),
                     ("F", "Female")
                    )
                    
    firstname = models.CharField(max_length=150, blank=False, null=False)
    lastname = models.CharField(max_length=150, blank=False, null=False)
    username = models.OneToOneField(User, blank=False, null=False, unique=True)
    phone = models.CharField(max_length=180, blank=True, null=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICE, blank=False, null=False)
    data_access_rights = models.ManyToManyField(dataset_models.Dataset, blank=True)
    can_edit = models.BooleanField(default=False)
    can_upload_file = models.BooleanField(default=False)
    can_process_data = models.BooleanField(default=False)
    
    class Meta:
        ordering = ("-id",)
        
    def __unicode__(self):
        """
        Return the unicode representation.
        """
        return self.username.username 
        
    def get_staff_abspath(self):
        """
        Return the absolute path.
        """
        return "/baseuser/details/%s" % str(slug)
