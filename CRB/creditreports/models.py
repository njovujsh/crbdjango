from django.db import models

class PIValidationReport(models.Model):
    total_records = models.CharField(max_length=300, blank=True, null=True)
    successful_records = models.CharField(max_length=300, blank=True, null=True)
    failed_records = models.CharField(max_length=300, blank=True, null=True)
    number_of_fields_passed = models.CharField(max_length=350, blank=True, null=True)
    number_of_fields_failed = models.CharField(max_length=350, blank=True, null=True)
    new_monthly_records = models.CharField(max_length=300, blank=True, null=True)
    record_type = models.CharField(max_length=100, blank=True, null=True)
    validation_date = models.DateTimeField(auto_now_add=True)
    pi_name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        ordering = ("-id", )
        
    def __unicode__(self):
        """
        Return a use full object
        representation.
        """
        return "/validations/pi/%s" % str(self.id)
        
class PISValidationReport(models.Model):
    total_records = models.CharField(max_length=300, blank=True, null=True)
    successful_records = models.CharField(max_length=300, blank=True, null=True)
    failed_records = models.CharField(max_length=300, blank=True, null=True)
    number_of_fields_passed = models.CharField(max_length=350, blank=True, null=True)
    number_of_fields_failed = models.CharField(max_length=350, blank=True, null=True)
    new_monthly_records = models.CharField(max_length=300, blank=True, null=True)
    record_type = models.CharField(max_length=100, blank=True, null=True)
    validation_date = models.DateTimeField(auto_now_add=True)
    pi_name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        ordering = ("-id", )
        
    def __unicode__(self):
        """
        Return a use full object
        representation.
        """
        return "/validations/pi/%s" % str(self.id)
        
class BCValidationReport(models.Model):
    total_records = models.CharField(max_length=300, blank=True, null=True)
    successful_records = models.CharField(max_length=300, blank=True, null=True)
    failed_records = models.CharField(max_length=300, blank=True, null=True)
    number_of_fields_passed = models.CharField(max_length=350, blank=True, null=True)
    number_of_fields_failed = models.CharField(max_length=350, blank=True, null=True)
    new_monthly_records = models.CharField(max_length=300, blank=True, null=True)
    record_type = models.CharField(max_length=100, blank=True, null=True)
    validation_date = models.DateTimeField(auto_now_add=True)
    pi_name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        ordering = ("-id", )
        
    def __unicode__(self):
        """
        Return a use full object
        representation.
        """
        return "/validations/pi/%s" % str(self.id)
        
class BSValidationReport(models.Model):
    total_records = models.CharField(max_length=300, blank=True, null=True)
    successful_records = models.CharField(max_length=300, blank=True, null=True)
    failed_records = models.CharField(max_length=300, blank=True, null=True)
    number_of_fields_passed = models.CharField(max_length=350, blank=True, null=True)
    number_of_fields_failed = models.CharField(max_length=350, blank=True, null=True)
    new_monthly_records = models.CharField(max_length=300, blank=True, null=True)
    record_type = models.CharField(max_length=100, blank=True, null=True)
    validation_date = models.DateTimeField(auto_now_add=True)
    pi_name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        ordering = ("-id", )
        
    def __unicode__(self):
        """
        Return a use full object
        representation.
        """
        return "/validations/pi/%s" % str(self.id)
        
class CAPValidationReport(models.Model):
    total_records = models.CharField(max_length=300, blank=True, null=True)
    successful_records = models.CharField(max_length=300, blank=True, null=True)
    failed_records = models.CharField(max_length=300, blank=True, null=True)
    number_of_fields_passed = models.CharField(max_length=350, blank=True, null=True)
    number_of_fields_failed = models.CharField(max_length=350, blank=True, null=True)
    new_monthly_records = models.CharField(max_length=300, blank=True, null=True)
    record_type = models.CharField(max_length=100, blank=True, null=True)
    validation_date = models.DateTimeField(auto_now_add=True)
    pi_name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        ordering = ("-id", )
        
    def __unicode__(self):
        """
        Return a use full object
        representation.
        """
        return "/validations/pi/%s" % str(self.id)
        
class CBAValidationReport(models.Model):
    total_records = models.CharField(max_length=300, blank=True, null=True)
    successful_records = models.CharField(max_length=300, blank=True, null=True)
    failed_records = models.CharField(max_length=300, blank=True, null=True)
    number_of_fields_passed = models.CharField(max_length=350, blank=True, null=True)
    number_of_fields_failed = models.CharField(max_length=350, blank=True, null=True)
    new_monthly_records = models.CharField(max_length=300, blank=True, null=True)
    record_type = models.CharField(max_length=100, blank=True, null=True)
    validation_date = models.DateTimeField(auto_now_add=True)
    pi_name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        ordering = ("-id", )
        
    def __unicode__(self):
        """
        Return a use full object
        representation.
        """
        return "/validations/pi/%s" % str(self.id)
        
class FRAValidationReport(models.Model):
    total_records = models.CharField(max_length=300, blank=True, null=True)
    successful_records = models.CharField(max_length=300, blank=True, null=True)
    failed_records = models.CharField(max_length=300, blank=True, null=True)
    number_of_fields_passed = models.CharField(max_length=350, blank=True, null=True)
    number_of_fields_failed = models.CharField(max_length=350, blank=True, null=True)
    new_monthly_records = models.CharField(max_length=300, blank=True, null=True)
    record_type = models.CharField(max_length=100, blank=True, null=True)
    validation_date = models.DateTimeField(auto_now_add=True)
    pi_name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        ordering = ("-id", )
        
    def __unicode__(self):
        """
        Return a use full object
        representation.
        """
        return "/validations/pi/%s" % str(self.id)
        
class CMCValidationReport(models.Model):
    total_records = models.CharField(max_length=300, blank=True, null=True)
    successful_records = models.CharField(max_length=300, blank=True, null=True)
    failed_records = models.CharField(max_length=300, blank=True, null=True)
    number_of_fields_passed = models.CharField(max_length=350, blank=True, null=True)
    number_of_fields_failed = models.CharField(max_length=350, blank=True, null=True)
    new_monthly_records = models.CharField(max_length=300, blank=True, null=True)
    record_type = models.CharField(max_length=100, blank=True, null=True)
    validation_date = models.DateTimeField(auto_now_add=True)
    pi_name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        ordering = ("-id", )
        
    def __unicode__(self):
        """
        Return a use full object
        representation.
        """
        return "/validations/pi/%s" % str(self.id)
        
class CCGValidationReport(models.Model):
    total_records = models.CharField(max_length=300, blank=True, null=True)
    successful_records = models.CharField(max_length=300, blank=True, null=True)
    failed_records = models.CharField(max_length=300, blank=True, null=True)
    number_of_fields_passed = models.CharField(max_length=350, blank=True, null=True)
    number_of_fields_failed = models.CharField(max_length=350, blank=True, null=True)
    new_monthly_records = models.CharField(max_length=300, blank=True, null=True)
    record_type = models.CharField(max_length=100, blank=True, null=True)
    validation_date = models.DateTimeField(auto_now_add=True)
    pi_name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        ordering = ("-id", )
        
    def __unicode__(self):
        """
        Return a use full object
        representation.
        """
        return "/validations/pi/%s" % str(self.id)
        
class IBValidationReport(models.Model):
    total_records = models.CharField(max_length=300, blank=True, null=True)
    successful_records = models.CharField(max_length=300, blank=True, null=True)
    failed_records = models.CharField(max_length=300, blank=True, null=True)
    number_of_fields_passed = models.CharField(max_length=350, blank=True, null=True)
    number_of_fields_failed = models.CharField(max_length=350, blank=True, null=True)
    new_monthly_records = models.CharField(max_length=300, blank=True, null=True)
    record_type = models.CharField(max_length=100, blank=True, null=True)
    validation_date = models.DateTimeField(auto_now_add=True)
    pi_name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        ordering = ("-id", )
        
    def __unicode__(self):
        """
        Return a use full object
        representation.
        """
        return "/validations/pi/%s" % str(self.id)
