from django.db import models

FRAUD_CHOICES = (
            ("1", "FALSE IDENTITY"),
            ("2", "FALSE EMPLOYER DETAILS"),
            ("3", "ILLEGAL SALE"),
            ("4", "OTHERS"),
            ("5", "EVADING LIABILITY"),
            ("6", "AID, ABET OR CONSPIRE"),
            ("8", "INSURANCE CLAIMED FRAUD"),
            ("9", "DEFAULTING FIRST PAYMENT"),
            ("10", "PERSONA UNKNOWN FRAUD"),
            ("11", "SUSPECT FRAUD-DECLINED"),
            ("12", "VICTIM"),
)
            
