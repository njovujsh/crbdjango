from django.db import models


class SecurityRules(models.Model):
    DEFINED_RULES = (
                    ("log", "Log Request"),
                    ("accept", "Accept Request"),
                    ("deny", "Deny Request"),
                    ("redirect", "Redirect Request to captive Portal"),
                    ("blockall", "* Block any Request, (not recommended)"),
                    )
                    
    decision = models.CharField(max_length=250, choices=DEFINED_RULES, blank=False, null=False)
    source_IP = models.CharField(max_length=250, blank=False, null=False)
    description = models.CharField(max_length=150, blank=True, null=True)
    #is_blocked = models.BooleanField(default=False)
    date  = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        """
        Return the unicode representation.
        """
        return u"%s" % str(self.decision)
        
    class Meta:
        ordering = ("-id",)
