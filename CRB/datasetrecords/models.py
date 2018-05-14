from django.db import models
from validators.subsystems import picode
import datetime
from fraudcategory import models as fraud_model
from fraudcategory.appendix import apendx15
from fraudcategory.subcategory import stakeholdertype
from fraudcategory.subcategory import stakeholdercategory
from fraudcategory.subcategory import applicationclassification
from fraudcategory.subcategory import creditappstatus
from fraudcategory.subcategory import consentflag
from fraudcategory.subcategory import creditapprejectionreason
from fraudcategory.subcategory import creditaccountclosure
from fraudcategory.subcategory import restructured
from fraudcategory.subcategory import riskclassification
from fraudcategory.subcategory import creditaccountstatus
from fraudcategory.subcategory import creditindicator
from fraudcategory.subcategory import paymentfrequency
from fraudcategory.subcategory import monitizationtype
from fraudcategory.subcategory import enf074code
from fraudcategory.subcategory import interesttype
from fraudcategory.subcategory import openbalanceindicator
from fraudcategory.subcategory import branchtype
from fraudcategory.subcategory import chequebounceresons
from fraudcategory.subcategory import currencyisocode
from fraudcategory.subcategory import chequeaccounttype
from fraudcategory.subcategory import chequeclassic
from fraudcategory.subcategory import gaurantortype
from fraudcategory.subcategory import gauranteetype
from fraudcategory.subcategory import collateralclassification
from fraudcategory.subcategory import forensicinfo
from fraudcategory.subcategory import pitype
from fraudcategory.subcategory import ugandanregions
from fraudcategory.subcategory import propertyowner
from fraudcategory.subcategory import countryisocode
from fraudcategory.subcategory import eitypes
from fraudcategory.subcategory import salarayband
from fraudcategory.subcategory import salaryfrequency
from fraudcategory.subcategory import maritalstatus
from fraudcategory.subcategory import businesscode
from fraudcategory.subcategory import gender
from fraudcategory.subcategory import industrycode
from fraudcategory.subcategory import countrydialing
from branchcode import models as branchmodel
from util import handleregions as utilregions
from CRB import settings
import datetime
import django.utils

DATE_FORMAT = "%Y-%m-%d"  
DATE = datetime.datetime.today()
FORMATTED = DATE.strftime(DATE_FORMAT)

APPENDIX12 = apendx15.Appendix15()
#choices = countrydialing.get_class_code(),

IMPORTED_FILE = False 
'''
class BorrowersStakeDetails(models.Model):
    firstname = models.CharField(max_length=220, blank=True, null=True)
    lastname = models.CharField(max_length=220, blank=True, null=True)
    othernames = models.CharField(max_length=220, blank=True, null=True)

    def __str__(self):
        return "%s %s" % (str(self.firstname), str(self.lastname))
'''       
class BorrowerHistory(models.Model):
    borrower_status = models.IntegerField(blank=True, default=0)
    amount = models.CharField(max_length=250, blank=True, null=True)
    account_reference = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % str(self.borrower_status)

class BorrowingTimes(models.Model):
    borrower_time = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return "%s" % self.borrower_time
        
class PCI(models.Model):
    PCI_Building_Unit_Number= models.CharField(max_length=250, default="",  blank=True, null=False)
    PCI_Building_Name= models.CharField(max_length=250, default="",  blank=True, null=False)
    PCI_Floor_Number= models.CharField(max_length=250, default="",  blank=True, null=False)
    PCI_Plot_or_Street_Number= models.CharField(max_length=250, default="",  blank=True, null=False)
    PCI_LC_or_Street_Name= models.CharField(max_length=250, default="",  blank=True, null=False)
    PCI_Region= models.CharField(max_length=250,  choices=ugandanregions.get_class_region(), default="", blank=True, null=False)
    PCI_District= models.CharField(max_length=250, blank=True, default="", choices=utilregions.all_districts(), null=False)
    PCI_County_or_Town= models.CharField(max_length=250, blank=True, default="", choices=utilregions.all_subcounties(), null=False)
    PCI_Parish= models.CharField(max_length=250, blank=True,default="", choices=utilregions.all_parishes(), null=False)
    PCI_Suburb= models.CharField(max_length=250, default="", blank=True, null=False)
    PCI_Village= models.CharField(max_length=250,  blank=True, default="", null=False)
    PCI_PO_Box_Number= models.CharField(max_length=250, default="",  blank=True, null=False)
    PCI_Post_Office_Town= models.CharField(max_length=250, default="",  blank=True, null=False)
    PCI_Country_Code= models.CharField(max_length=250, choices = countryisocode.get_class_isocode(), default="", blank=True, null=False)
    #PCI_Country_Code= models.CharField(max_length=250, choices = countryisocode.get_class_isocode(), default=countryisocode.get_class_isocode()[0][0],  blank=False, null=False)
    PCI_Period_At_Address= models.CharField(max_length=250, blank=True, default="", null=False)
    PCI_Flag_of_Ownership= models.CharField(max_length=250,  choices=propertyowner.get_class_owner(), default="", blank=True, null=False)
    #PCI_Primary_Number_Country_Dialling_Code= models.CharField(max_length=250, choices=countrydialing.get_class_code(),default="256", blank=False, null=False)
    PCI_Primary_Number_Telephone_Number= models.CharField(max_length=10,  blank=True,default="", null=False)
    #PCI_Other_Number_Country_Dialling_Code= models.CharField(max_length=250,  choices = countrydialing.get_class_code(), default="256",blank=False, null=False)
    PCI_Other_Number_Telephone_Number= models.CharField(max_length=10,  blank=True, default="", null=False)
    #PCI_Mobile_Number_Country_Dialling_Code= models.CharField(max_length=250, choices = countrydialing.get_class_code(), default="256", blank=False, null=False)
    PCI_Mobile_Number_Telephone_Number= models.CharField(max_length=10, default="",  blank=True, null=False)
    #PCI_Facsimile_Country_Dialling_Code= models.CharField(max_length=250,  choices = countrydialing.get_class_code(),default="256", blank=False, null=False)
    PCI_Facsimile_Number= models.CharField(max_length=250, default="",  blank=True, null=False)
    PCI_Email_Address= models.EmailField(max_length=250, default="", blank=True, null=False)
    PCI_Web_site= models.CharField(max_length=250, default="", blank=True, null=False)

    def __str__(self):
        return "%s" % self.PCI_Building_Unit_Number

    def save(self, *args, **kwargs):
        if(self.PCI_Region == None):
            self.PCI_Region = ""
            super(PCI, self).save(*args, **kwargs)
        else:
            super(PCI, self).save(*args, **kwargs)

        if(self.PCI_Country_Code == None):
            self.PCI_Country_Code = ""
            super(PCI, self).save(*args, **kwargs)
        else:
            super(PCI, self).save(*args, **kwargs)#

        if(self.PCI_Flag_of_Ownership == None):
            self.PCI_Flag_of_Ownership = ""
            super(PCI, self).save(*args,  **kwargs)
        else:
            super(PCI, self).save(*args, **kwargs)

class SCI(models.Model):
    SCI_Unit_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    SCI_Unit_Name= models.CharField(max_length=250, default="", blank=True, null=False)
    SCI_Floor_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    SCI_Plot_or_Street_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    SCI_LC_or_Street_Name= models.CharField(max_length=250, default="", blank=True, null=False)
    SCI_Region= models.CharField(max_length=250, choices=ugandanregions.get_class_region(),default="", blank=True, null=False)
    SCI_District= models.CharField(max_length=250, blank=True, default="",choices=utilregions.all_districts(), null=False)
    SCI_County_or_Town= models.CharField(max_length=250, blank=True, default="", choices=utilregions.all_subcounties(),null=False)
    SCI_Parish= models.CharField(max_length=250, blank=True, default="", choices=utilregions.all_parishes(), null=False)
    SCI_Suburb= models.CharField(max_length=250, default="", blank=True, null=False)
    SCI_Village= models.CharField(max_length=250, default="", blank=True, null=False)
    SCI_PO_Box_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    SCI_Post_Office_Town= models.CharField(max_length=250, default="", blank=True, null=False)
    SCI_Country_Code= models.CharField(max_length=250, blank=True, choices=countryisocode.get_class_isocode(), default="", null=False)
    SCI_Period_At_Address= models.CharField(max_length=250, default="", blank=True, null=True)
    SCI_Flag_for_ownership= models.CharField(max_length=250, choices=propertyowner.get_class_owner(), default="",blank=True, null=False)
    #SCI_Primary_Number_Country_Dialling_Code= models.CharField(max_length=250, choices = countrydialing.get_class_code(), default="256", blank=False, null=False)
    SCI_Primary_Number_Telephone_Number= models.CharField(max_length=10, default="", blank=True, null=False)
    #SCI_Other_Number_Country_Dialling_Code= models.CharField(max_length=250, default="256",choices = countrydialing.get_class_code(), blank=False, null=False)
    SCI_Other_Number_Telephone_Number= models.CharField(max_length=10, default="", blank=True, null=False)
    #SCI_Mobile_Number_Country_Dialling_Code= models.CharField(max_length=250, default="256", choices = countrydialing.get_class_code(), blank=False, null=False)
    SCI_Mobile_Number_Telephone_Number= models.CharField(max_length=10, default="", blank=True, null=False)
    #SCI_Facsimile_Country_Dialling_Code= models.CharField(max_length=250, default="256",choices = countrydialing.get_class_code(), blank=False, null=False)
    SCI_Facsimile_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    SCI_Email_Address= models.CharField(max_length=250, default="", blank=True, null=False)
    SCI_Web_site= models.CharField(max_length=250, default="", blank=True, null=False)

    def __str__(self):
        return "%s" % self.SCI_Unit_Number

    def save(self, *args, **kwargs):
        if(self.SCI_Region == None):
            self.SCI_Region = ""
            super(SCI, self).save(*args, **kwargs)
        else:
            super(SCI, self).save(*args, **kwargs)

        if(self.SCI_Country_Code == None):
            self.SCI_Country_Code = ""
            super(SCI, self).save(*args, **kwargs)
        else:
            super(SCI, self).save(*args, **kwargs)

        if(self.SCI_Flag_for_ownership == None):
            self.SCI_Flag_for_ownership = ""
            super(SCI, self).save(*args,  **kwargs)
        else:
            super(SCI, self).save(*args, **kwargs)


class EMPLOYMENT_INFORMATION(models.Model):
    EI_Employment_Type= models.CharField(max_length=250, choices = eitypes.get_employement(), default="",  blank=True, null=False) #NULL
    EI_Primary_Occupation= models.CharField(max_length=250, default="", blank=True, null=True)
    EI_Employer_Name= models.CharField(max_length=250, default="", blank=True, null=True)
    EI_Employee_Number= models.CharField(max_length=250, default="", blank=True, null=True)
    EI_Employment_Date= models.CharField(max_length=250, default="", blank=True, null=True)
    EI_Income_Band= models.CharField(max_length=250,choices=salarayband.get_salary(),default="", blank=True, null=False) #NULL
    EI_Salary_Frequency= models.CharField(max_length=250, choices =salaryfrequency.get_class_freq(), default="", blank=True, null=False) #NULL

    def __str__(self):
        return "%s" % str(self.id)

class IDENTIFICATION_INFORMATION(models.Model):
    II_Registration_Certificate_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    II_Tax_Identification_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    II_Value_Added_Tax_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    II_FCS_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    II_Passport_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    II_Drivers_Licence_ID_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    II_Voters_PERNO= models.CharField(max_length=250, default="", blank=True, null=False)
    II_Drivers_License_Permit_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    II_NSSF_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    II_Country_ID= models.CharField(max_length=250, default="", blank=True, null=False)
    II_Police_ID_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    II_UPDF_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    II_KACITA_License_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    II_Public_Service_Pension_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    II_Teacher_Registration_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    II_Country_Issuing_Authority= models.CharField(max_length=250, choices = countryisocode.get_class_isocode(), default="", blank=True, null=False)
    II_Nationality= models.CharField(max_length=250, choices=countryisocode.get_class_isocode(), default="", blank=True, null=False)
    II_Country_Of_Issue= models.CharField(max_length=250, choices=countryisocode.get_class_isocode(), default="", blank=True, null=False)

    def __str__(self):
        return "%s" % str(self.id)

class GSCAFB_INFORMATION(models.Model):
    GSCAFB_Business_Name= models.CharField(max_length=250, default="", blank=True, null=False)
    GSCAFB_Trading_Name= models.CharField(max_length=250, default="", blank=True, null=False)
    GSCAFB_Activity_Description= models.TextField(max_length=280, default="", blank=True, null=False)
    GSCAFB_Industry_Sector_Code= models.CharField(max_length=250, default="", blank=True, null=False) #choices = industrycode.get_industrycode()
    GSCAFB_Date_Registered= models.CharField(max_length=250, default="", blank=True, null=False)
    GSCAFB_Business_Type_Code= models.CharField(max_length=250, choices =businesscode.get_bcodes(), default="", blank=True, null=False) #NULL
    GSCAFB_Surname= models.CharField(max_length=250, default="", blank=True, null=False)
    GSCAFB_Forename1= models.CharField(max_length=250, default="", blank=True, null=False)
    GSCAFB_Forename2= models.CharField(max_length=250, default="", blank=True, null=False)
    GSCAFB_Forename3= models.CharField(max_length=250, default="", blank=True, null=False)
    GSCAFB_Gender= models.CharField(max_length=250, choices=gender.get_gender(), default="", blank=True, null=False) #NULL
    GSCAFB_Marital_Status= models.CharField(max_length=250, choices=maritalstatus.get_status(), default="", blank=True, null=False) #NULL
    GSCAFB_Date_of_Birth= models.CharField(max_length=250, default="", blank=True, null=False)

    def __str__(self):
        return "%s" % str(self.id)

class ClientInformation(models.Model):
    surname = models.CharField(max_length=250, blank=True, null=True)
    firstname = models.CharField(max_length=250, blank=True, null=True)
    business_name = models.CharField(max_length=250, blank=True, null=True)
    
    def __str__(self):
        if(self.business_name):
            return "%s" % str(self.business_name)
        else:
            return "%s  %s" % (str(self.surname), str(self.firstname))
        '''
        if(self.surname):
            return "%s" % str(self.surname)
        else:
            if(self.business_name):
                return "%s" % self.business_name
            else:
                return str(self.id)
        '''
            
#----Creating models corresponding to the database---#
class PARTICIPATING_INSTITUTION(models.Model):
    #dateset_ref = models.ForeignKey(DataSetRecords)
    PI_Identification_Code = models.ForeignKey(branchmodel.PIIdentificationCode, blank=True, null=True, unique=False)
    Institution_Type = models.CharField(max_length=80, choices=pitype.get_ittype(), default="", blank=True, null=False)
    Institution_Name = models.CharField(max_length=80, default="", blank=True, null=False)
    License_Issuing_Date = models.CharField(max_length=100, blank=True, null=False, default="")
    pci = models.OneToOneField(PCI, null=True, blank=True, unique=False)
    date = models.DateField(auto_now=True)
    #sci = models.OneToOneField(SCI, null=True, blank=True, unique=False)
    validated = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        #if(self.PI_Identification_Code ):
        #    super(PARTICIPATING_INSTITUTION, self).save(*args, **kwargs)
        #else:
        #self.searched_pi = self.search_picode(settings.PI_IDENTIFICATION)
        #self.PI_Identification_Code = self.searched_pi
        super(PARTICIPATING_INSTITUTION, self).save(*args, **kwargs)
        
    class Meta:
        ordering = ("-id", )
        
    def __str__(self):
        """
        Return the object representation.
        """
        if(self.PI_Identification_Code.pi_identification_code):
            return "%s %s %s" % (self.Institution_Name, self.Institution_Type, self.PI_Identification_Code.pi_identification_code)
        else:
            return "%s %s %s" % (self.Institution_Name, self.Institution_Type)

    def validate_pi_code(self, rules):
        self.PI = picode.PICode(self, PI)

    def search_picode(self, CODE):
        try:
            return branchmodel.RequiredHeader.objects.get(pi_identification_code=CODE)
        except:
            raise
                
    def get_pi_name(self):
        """
        return the participating instituion name.
        """
        return self.Institution_Name

    def get_full_name(self):
        return "PARTICIPATING_INSTITUTION".replace("_", " ", len(self.PI_Identification_Code.pi_identification_code))

    def get_update_path(self):
        return "/newupdate/dataupdatingsystem/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_process_path(self):
        return "/processing/data/existing/"

    def get_view_path(self):
        return "/view/dataview/request/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_delete_path(self):
        return "/purgerecords/deleting/%s/True/" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_new_path(self):
        return "/process/sys/data/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

#-------Creating datdabase structure for the branch---------------(IB)-#
class INSTITUTION_BRANCH(models.Model):
    PI_Identification_Code = models.ForeignKey(branchmodel.PIIdentificationCode, blank=False, null=True, unique=False)
    Branch_Identification_Code = models.ForeignKey(branchmodel.RequiredHeader, blank=True, null=True)
    Branch_Name = models.CharField(max_length=250,blank=False, null=False)
    Branch_Type = models.CharField(max_length=250, choices=branchtype.get_branchtype(), default="", blank=False, null=False)
    Date_Opened = models.CharField(max_length=100, blank=True, null=True)
    pci = models.OneToOneField(PCI,blank=True, null=True, unique=False)
    date = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ("-id", )
        
    def save(self, *args, **kwargs):
        """
        Override the save method allowing us to perform additional
        settings.
        """
        try:
            super(INSTITUTION_BRANCH, self).save(*args, **kwargs)
        except Exception as e:
            raise 
        
    def get_allsettings(self):
        return branchmodel.DefaultHeaders.objects.all()

    def search_picode(self, CODE):
        try:
            return branchmodel.RequiredHeader.objects.get(pi_identification_code=CODE)
        except:
            raise
            
    def filter_by_id(self, headers):
        if(headers):
            return headers.get(pi_identification_code=settings.PI_IDENTIFICATION)
        else:
            return None 
            
    def __str__(self):
        """
        Return the object representation.
        """
        return self.PI_Identification_Code.pi_identification_code

    def get_pi_name(self):
        """
        return the participating instituion name.
        """
        return self.Branch_Name

    def get_pi_type(self):
        """
        return the instition type.
        """
        return self.Branch_Type

    def get_abbreviation_name(self):
        """
        return the abbreviation name of the model dataset
        """
        return "%s" % "IB"

    def get_dataset_name(self):
        """
        """
        pass
        #return "%s" % self.dateset_ref.navigation_title

    def get_full_name(self):
        return "INSTITUTION_BRANCH".replace("_", " ", len(self.PI_Identification_Code.pi_identification_code))

    def get_update_path(self):
        return "/newupdate/dataupdatingsystem/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_process_path(self):
        return "/processing/data/existing/"

    def get_view_path(self):
        return "/view/dataview/request/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_delete_path(self):
        return "/purgerecords/deleting/%s/True/" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_new_path(self):
        return "/process/sys/data/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

#-----(CAP)------#[('closed','closed'),('open','open')]
class CREDIT_APPLICATION(models.Model):
    client_details = models.ForeignKey(ClientInformation, blank=True, null=True,unique=False)
    PI_Identification_Code = models.ForeignKey(branchmodel.PIIdentificationCode, blank=False, null=False, unique=False)
    Branch_Identification_Code= models.ForeignKey(branchmodel.RequiredHeader, blank=True, null=False)
    Client_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    Credit_Application_Status= models.CharField(max_length=250, choices=creditappstatus.get_class_status(), default=creditappstatus.get_class_status()[2], blank=True, null=False)
    Client_Consent_flag= models.CharField(max_length=250, choices=consentflag.get_consents(), default="", blank=True, null=False)
    Credit_Application_Reference= models.CharField(max_length=250, default="", blank=True, null=False)
    Applicant_Classification= models.CharField(max_length=250, choices=applicationclassification.get_app_class(), default="", blank=True, null=False)
    Credit_Application_Date= models.CharField(max_length=250, default="", blank=True, null=False)
    Amount= models.CharField(max_length=250, default="", blank=True, null=False)
    Currency= models.CharField(max_length=250, choices=currencyisocode.get_currency(), default="", blank=True, null=False)
    Credit_Account_or_Loan_Product_Type= models.CharField(max_length=250, choices=APPENDIX12.get_values_tuple(), default="", blank=True, null=False)
    Last_Status_Change_Date= models.DateField(auto_now=True)
    #Last_Status_Change_Date= models.CharField(max_length=120, default=FORMATTED, blank=True, null=False)
    Credit_Application_Duration= models.CharField(max_length=250, default="", blank=True, null=False)
    Rejection_Reason= models.CharField(max_length=250, choices=creditapprejectionreason.get_reject_reason(), default="", blank=True, null=False)
    gscafb = models.OneToOneField(GSCAFB_INFORMATION, blank=True, null=True, unique=False)
    idi = models.OneToOneField(IDENTIFICATION_INFORMATION, blank=True, null=True, unique=False)
    ei = models.OneToOneField(EMPLOYMENT_INFORMATION, blank=True, null=True, unique=False)
    pci = models.OneToOneField(PCI,blank=True, null=True, unique=False)
    sci = models.OneToOneField(SCI,blank=True, null=True, unique=False)
    history = models.ManyToManyField(BorrowerHistory, blank=False)
    howmanytimes = models.OneToOneField(BorrowingTimes, blank=True, null=True)
    date = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ("-id", )
        
    def save(self, *args, **kwargs):
        """
        Override the save method allowing us to perform additional
        settings.
        """
        try:
            if(self.PI_Identification_Code):
                self.dsettings = self.get_allsettings()
                self.filtereds = self.search_picode(settings.PI_IDENTIFICATION)
                
                if(self.Branch_Identification_Code):
                    self.Credit_Application_Date = self.cleanse_date(self.Credit_Application_Date)
                    self.Last_Status_Change_Date = self.cleanse_date(self.Credit_Application_Date)
                else:
                    self.Branch_Identification_Code = self.settings.BRANCH_IDENTIFICATION_CODE
                    self.Credit_Application_Date = self.cleanse_date(self.Credit_Application_Date)
                    self.Last_Status_Change_Date = self.cleanse_date(self.Credit_Application_Date)

                if(self.PI_Identification_Code):
                    super(CREDIT_APPLICATION, self).save(*args, **kwargs)
                else:
                    self.PI_Identification_Code = self.filtereds
                    super(CREDIT_APPLICATION, self).save(*args, **kwargs)
                
            else:
                self.PI = self.search_picode(settings.PI_IDENTIFICATION)
                if(self.PI):
                    self.PI_Identification_Code = self.PI
                    
                if(not self.Branch_Identification_Code):
                    self.Branch_Identification_Code = settings.BRANCH_IDENTIFICATION_CODE
                super(CREDIT_APPLICATION, self).save(*args, **kwargs)

            self.Amount = self.clean_amounts(self.Amount)
            super(CREDIT_APPLICATION, self).save(*args, **kwargs)
        except Exception as e:
            raise 

    def cleanse_date(self, date):
        try:
            if(date):
                return date.replace("-", "", len(str(date))).strip().lstrip().rstrip().replace("/", "", len(str(date)))
            else:
                return  date
        except:
            raise

    def clean_amounts(self, amount):
        """
        Attempt to clean the commas in amounts.
        """
        try:
            if(amount):
                if("," in amount):
                    return float(amount.replace(",", "", len(amount)))
                else:
                    return amount
            else:
                return amount 
        except:
            raise
            
    def get_allsettings(self):
        return branchmodel.RequiredHeader.objects.all()

    def search_picode(self, CODE):
        try:
            return branchmodel.PIIdentificationCode.objects.get(pi_identification_code=CODE)
        except:
            raise
            
    def filter_by_id(self, headers):
        if(headers):
            return headers.get(id=1)
        else:
            return None 
            
    def __str__(self):
        """
        Return the object representation.
        """
        return "%s" % self.Client_Number #self.PI_Identification_Code.pi_identification_code

    def get_pi_code(self):
        """
        return the instition type.
        """
        return self.Branch_Identification_Code

    def get_abbreviation_name(self):
        """
        return the abbreviation name of the model dataset
        """
        return "%s" % "CAP"

    def get_dataset_name(self):
        """
        """
        pass
        #return "%s" % self.dateset_ref.navigation_title

    def get_full_name(self):
        return "CREDIT_APPLICATION".replace("_", "", len(self.PI_Identification_Code.pi_identification_code))

    def get_update_path(self):
        return "/newupdate/dataupdatingsystem/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_process_path(self):
        return "/processing/data/existing/"

    def get_view_path(self):
        return "/view/dataview/request/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_delete_path(self):
        return "/purgerecords/deleting/%s/True/" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_new_path(self):
        return "/process/sys/data/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))


#(CBA)
class CREDITBORROWERACCOUNT(models.Model):
    PI_Identification_Code = models.ForeignKey(branchmodel.PIIdentificationCode, blank=True, null=True, unique=False)
    Branch_Identification_Code = models.ForeignKey(branchmodel.RequiredHeader, blank=True, null=True)
    Borrowers_Client_Number = models.ForeignKey(CREDIT_APPLICATION, blank=True, null=True, unique=False)
    Borrower_Classification = models.CharField(max_length=250, choices=applicationclassification.get_app_class(), default="", blank=True, null=False)
    Credit_Account_Reference = models.CharField(max_length=250, default="", blank=True, null=False)
    Credit_Account_Date = models.CharField(max_length=250, default="", blank=True, null=False)
    Credit_Amount = models.CharField(max_length=250, default="", blank=True, null=False)
    Facility_Amount_Granted = models.CharField(max_length=250, default="", blank=True, null=False)
    Credit_Account_Type = models.CharField(max_length=250, choices=APPENDIX12.get_values_tuple(), default="", blank=True, null=False)
    Group_Identification_Joint_Account_Number = models.CharField(max_length=250, default="", blank=True, null=False)
    Transaction_Date = models.CharField(max_length=250, default="", blank=True, null=False)
    Currency = models.CharField(max_length=250, choices=currencyisocode.get_currency(), default="", blank=True, null=False)
    Opening_Balance_Indicator= models.CharField(max_length=250, choices=openbalanceindicator.get_class_status(), default="", blank=True, null=False)
    Maturity_Date= models.CharField(max_length=250, default="", blank=True, null=False)
    Type_of_Interest= models.CharField(max_length=250, choices=interesttype.get_class_status(), default="", blank=True, null=False)
    Interest_Calculation_Method= models.CharField(max_length=250, choices=enf074code.get_class_status(), default="", blank=True, null=False)
    Annual_Interest_Rate_at_Disbursement= models.CharField(max_length=250, default="", blank=True, null=False)
    Annual_Interest_Rate_at_Reporting= models.CharField(max_length=250, default="", blank=True, null=False)
    Date_of_First_Payment= models.CharField(max_length=250, default="", blank=True, null=False)
    Credit_Amortization_Type= models.CharField(max_length=250, choices=monitizationtype.get_status(), default="", blank=True, null=False)
    Credit_Payment_Frequency= models.CharField(max_length=250, choices=paymentfrequency.get_class_freq(), default="", blank=True, null=False)
    Number_of_Payments= models.CharField(max_length=250, default="", blank=True, null=False)
    Monthly_Instalment_Amount= models.CharField(max_length=250, blank=True, null=False)
    Current_Balance_Amount= models.CharField(max_length=250, default="", blank=True, null=False)
    Current_Balance_Indicator= models.CharField(max_length=250, choices=creditindicator.get_class_indicator(), default="", blank=True, null=False)
    Last_Payment_Date= models.CharField(max_length=250, default="", blank=True, null=False)
    Last_Payment_Amount= models.CharField(max_length=250, default="", blank=True, null=False)
    Credit_Account_Status= models.CharField(max_length=250, choices=creditaccountstatus.get_status(), default="", blank=True, null=False)
    Last_Status_Change_Date= models.CharField(max_length=250, default="", blank=True, null=False)
    Credit_Account_Risk_Classification= models.CharField(max_length=250, choices=riskclassification.get_risk(), default="", blank=True, null=False)
    Credit_Account_Arrears_Date= models.CharField(max_length=250, default="", blank=True, null=False)
    Number_of_Days_in_Arrears= models.CharField(max_length=250, default="", blank=True, null=False)
    Balance_Overdue= models.CharField(max_length=250, default="", blank=True, null=False)
    Flag_for_Restructured_Credit= models.CharField(max_length=250, choices=restructured.get_restructure(), default="", blank=True, null=False)
    Old_Branch_Code= models.CharField(max_length=250, default="", blank=True, null=False)
    Old_Account_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    Old_Client_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    Balance_Overdue_Indicator= models.CharField(max_length=250, default="", blank=True, null=False)
    Credit_Account_Closure_Date= models.CharField(max_length=250, default="", blank=True, null=False)
    Credit_Account_Closure_Reason= models.CharField(max_length=250, choices=creditaccountclosure.get_closure(), default="", blank=True, null=False)
    Specific_Provision_Amount= models.CharField(max_length=250, default="", blank=True, null=True)
    Client_Consent_Flag= models.CharField(max_length=250, choices=consentflag.get_consents(), default="", blank=True, null=False)
    Client_Advice_Notice_Flag= models.CharField(max_length=250, choices=consentflag.get_consents(), default="", blank=True, null=False)
    Term= models.CharField(max_length=250, default="", blank=True, null=True)
    Loan_Purpose= models.CharField(max_length=250, default="", blank=True, null=True)
    date = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ("-id", )
        
    def save(self, *args, **kwargs):
        """
        Override the save method allowing us to perform additional
        settings.
        """
        try:
            if( not self.PI_Identification_Code ):
                self.searched_pi = self.search_picode(settings.PI_IDENTIFICATION)
                self.PI_Identification_Code = self.searched_pi

            if( not self.Branch_Identification_Code):
                self.Branch_Identification_Code = settings.BRANCH_IDENTIFICATION_CODE
                
            self.Credit_Account_Date =self.cleanse_date(self.Credit_Account_Date)
            self.Transaction_Date = self.cleanse_date(self.Transaction_Date)
            self.Maturity_Date = self.cleanse_date(self.Maturity_Date)
            self.Date_of_First_Payment = self.cleanse_date(self.Date_of_First_Payment)
            self.Last_Payment_Date = self.cleanse_date(self.Last_Payment_Date)
            self.Last_Status_Change_Date = self.cleanse_date(self.Last_Status_Change_Date)
            self.Credit_Account_Closure_Date = self.cleanse_date(self.Credit_Account_Closure_Date)

            #Cleanse amounts  =
            self.Credit_Amount = self.clean_amounts(self.Credit_Amount)
            self.Facility_Amount_Granted = self.clean_amounts(self.Facility_Amount_Granted)
            self.Current_Balance_Amount = self.clean_amounts(self.Current_Balance_Amount)
            self.Monthly_Instalment_Amount = self.clean_amounts(self.Monthly_Instalment_Amount)
            self.Last_Payment_Amount = self.clean_amounts(self.Last_Payment_Amount)
            self.Specific_Provision_Amount = self.clean_amounts(self.Specific_Provision_Amount)
            super(CREDITBORROWERACCOUNT, self).save(*args, **kwargs)
            
        except Exception as e:
            raise 
        
    def get_allsettings(self):
        return branchmodel.DefaultHeaders.objects.all()

    def search_picode(self, CODE):
        try:
            return branchmodel.RequiredHeader.objects.get(pi_identification_code=CODE)
        except:
            raise
            
    def filter_by_id(self, headers):
        if(headers):
            return headers.get(id=1)
        else:
            return None 
            
    def __str__(self):
        if(self.Borrowers_Client_Number.Client_Number):
            return "%s  &  %s" % (self.Credit_Account_Reference, self.Borrowers_Client_Number.Client_Number)
        else:
            return "%s" % self.Credit_Account_Reference
       
    def get_all(self):
        if(self.Borrowers_Client_Number.Client_Number):
            return "%s  &  %s" % (self.Credit_Account_Reference, self.Borrowers_Client_Number.Client_Number)
        else:
            return "%s" % self.Credit_Account_Reference
            
    def cleanse_date(self, date):
        try:
            if(date):
                return str(date).replace("-", "", len(str(date))).strip().lstrip().rstrip().replace("/", "", len(str(date))).replace(".", "", len(str(date)))
            else:
                return  date
        except:
            raise

    def cleanse_uploaded_data(self, value):
        try:
            if("." in value):
                return int(float(value))
            else:
                return value
        except ValueError as error:
            return value
            
    def get_abbreviation_name(self):
        return "%s" % "CBA"

    def get_dataset_name(self):
        """
        """
        #return "%s" % self.dateset_ref.navigation_title
        pass

    def get_full_name(self):
        return "CREDITBORROWERACCOUNT"

    def get_update_path(self):
        return "/newupdate/dataupdatingsystem/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_process_path(self):
        return "/processing/data/existing/"

    def get_view_path(self):
        return "/view/dataview/request/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_delete_path(self):
        return "/purgerecords/deleting/%s/True/" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_new_path(self):
        return "/process/sys/data/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def clean_amounts(self, amount):
        """
        Attempt to clean the commas in amounts.
        """
        try:
            if(amount):
                if("," in str(amount)):
                    return float(amount.replace(",", "", len(str(amount))))
                else:
                    return amount
            else:
                return amount 
        except:
            raise
            
#(BC)
class BOUNCEDCHEQUES(models.Model):
    PI_Identification_Code = models.ForeignKey(branchmodel.PIIdentificationCode, blank=True, null=True, unique=False)
    Branch_Identification_Code= models.ForeignKey(branchmodel.RequiredHeader, blank=True, null=True)
    Borrowers_Client_Number = models.ForeignKey(CREDIT_APPLICATION, blank=True, null=True, unique=False)
    PI_Client_Classification= models.CharField(max_length=250, choices=applicationclassification.get_app_class(), default="", blank=True, null=False)
    Cheque_Account_Reference_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    Cheque_Account_Opened_Date= models.CharField(max_length=250, default="", blank=True, null=False)
    Cheque_Account_Classification= models.CharField(max_length=250, choices=chequeclassic.get_cheque(), default="", blank=True, null=False)
    Cheque_Account_Type= models.CharField(max_length=250, choices=chequeaccounttype.get_cheque(), default="", blank=True, null=False)
    Cheque_Number= models.CharField(max_length=250, default="", blank=True, null=False)
    Cheque_Amount= models.CharField(max_length=250, default="", blank=True, null=False)
    Cheque_Currency= models.CharField(max_length=250, choices=currencyisocode.get_currency(), default="", blank=True, null=False)
    Beneficiary_Name_Or_Payee= models.CharField(max_length=250, default="", blank=True, null=True)
    Cheque_Bounce_Date= models.CharField(max_length=250, default="", blank=True, null=True)
    Cheque_Account_Bounce_Reason= models.CharField(max_length=250, choices=chequebounceresons.get_all(), default="", blank=True, null=False)
    date = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ("-id", )
        
    def save(self, *args, **kwargs):
        """
        Override the save method allowing us to perform additional
        settings.
        """
        try:
            if( not self.PI_Identification_Code ):
                self.searched_pi = self.search_picode(settings.PI_IDENTIFICATION)
                self.PI_Identification_Code = self.searched_pi

            if( not self.Branch_Identification_Code):
                self.Branch_Identification_Code = settings.BRANCH_IDENTIFICATION_CODE

            super(BOUNCEDCHEQUES, self).save(*args, **kwargs)
            
            if(self.Cheque_Account_Opened_Date):
                self.Cheque_Account_Opened_Date = self.cleanse_date(self.Cheque_Account_Opened_Date)
                super(BOUNCEDCHEQUES, self).save(*args, **kwargs)

            if(self.Cheque_Bounce_Date):
                self.Cheque_Bounce_Date = self.cleanse_date(self.Cheque_Bounce_Date)
                super(BOUNCEDCHEQUES, self).save(*args, **kwargs)

            self.Cheque_Amount = self.clean_amounts(self.Cheque_Amount)
            super(BOUNCEDCHEQUES, self).save(*args, **kwargs)
        except Exception as e:
            raise 

    def search_picode(self, CODE):
        try:
            return branchmodel.RequiredHeader.objects.get(pi_identification_code=CODE)
        except:
            raise

    def clean_amounts(self, amount):
        """
        Attempt to clean the commas in amounts.
        """
        try:
            if(amount):
                if("," in str(amount)):
                    return float(amount.replace(",", "", len(str(amount))))
                else:
                    return
            else:
                return amount 
        except:
            raise
            
    def cleanse_date(self, date):
        if(date):
            return str(date).strip().lstrip().rstrip().replace("-", "", 25).replace("/", "", 50)
        else:
            return date
            
    def get_allsettings(self):
        return branchmodel.DefaultHeaders.objects.all()
        
    def filter_by_id(self, headers):
        if(headers):
            return headers.get(id=1)
        else:
            return None 

    def get_branchcode(self):
        return branchmodel.RequiredHeader.objects.all()

    def filter_by_id_branchcode(self, queried_model):
        d = []
        for ids in queried_model:
            d.append(ids.id)

        return queried_model.get(id=min(d))
        
    def __str__(self):
        return self.PI_Identification_Code.pi_identification_code

    def get_abbreviation_name(self):
        return "%s" % "BC"
        
    def get_full_name(self):
        return "BOUNCEDCHEQUES".replace("_", " ", len(self.PI_Identification_Code.pi_identification_code))

    def get_update_path(self):
        return "/newupdate/dataupdatingsystem/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_process_path(self):
        return "/processing/data/existing/"

    def get_view_path(self):
        return "/view/dataview/request/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_delete_path(self):
        return "/purgerecords/deleting/%s/True/" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_new_path(self):
        return "/process/sys/data/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    class Meta:
        ordering = ("-id", )

#(PIS)
class PARTICIPATINGINSTITUTIONSTAKEHOLDER(models.Model):
    PI_Identification_Code = models.ForeignKey(branchmodel.PIIdentificationCode, blank=True, null=True, unique=False)
    participating_institution = models.ForeignKey(PARTICIPATING_INSTITUTION, blank=True, null=True, unique=False)
    Stakeholder_Type= models.CharField(max_length=250, choices=stakeholdertype.get_stakeholders(), default="", blank=True, null=False)
    Stakeholder_Category= models.CharField(max_length=250, choices=stakeholdercategory.get_category(), default="", blank=True, null=False)
    Shareholder_Percentage= models.CharField(max_length=250, choices=stakeholdercategory.get_percentage(), default="", blank=True, null=False)
    gscafb = models.OneToOneField(GSCAFB_INFORMATION, blank=True, null=True, unique=False)
    idi = models.OneToOneField(IDENTIFICATION_INFORMATION, blank=True, null=True, unique=False)
    ei = models.OneToOneField(EMPLOYMENT_INFORMATION, blank=True, null=True, unique=False)
    pci = models.OneToOneField(PCI,blank=True, null=True, unique=False)
    sci = models.OneToOneField(SCI,blank=True, null=True, unique=False)
    date = models.DateField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if( not self.PI_Identification_Code ):
            self.searched_pi = self.search_picode(settings.PI_IDENTIFICATION)
            self.PI_Identification_Code = self.searched_pi
        super(PARTICIPATINGINSTITUTIONSTAKEHOLDER, self).save(*args, **kwargs)
            
    class Meta:
        ordering = ("-id", )
        
    def __str__(self):
        if(self.participating_institution.Institution_Name):
            return "%s [ %s ]  %s " % (self.participating_institution.Institution_Name, self.participating_institution.Institution_Type, self.PI_Identification_Code.pi_identification_code)
        else:
            return "%s %s " % (self.participating_institution.Institution_Type, self.PI_Identification_Code.pi_identification_code)
        #return self.PI_Identification_Code.pi_identification_code

    def get_abbreviation_name(self):
        return "%s" % "PIS"

    def search_picode(self, CODE):
        try:
            return branchmodel.RequiredHeader.objects.get(pi_identification_code=CODE)
        except:
            raise
            
    def get_dataset_name(self):
        """
        """
        pass
        #return "%s" % self.dateset_ref.navigation_title

    def get_full_name(self):
        return "PARTICIPATINGINSTITUTIONSTAKEHOLDER".replace("_", " ", len(self.PI_Identification_Code.pi_identification_code))

    def get_update_path(self):
        return "/newupdate/dataupdatingsystem/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_process_path(self):
        return "/processing/data/existing/"

    def get_view_path(self):
        return "/view/dataview/request/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_delete_path(self):
        return "/purgerecords/deleting/%s/True/" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_new_path(self):
        return "/process/sys/data/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

class BORROWERSTAKEHOLDER(models.Model): #(BS)
    PI_Identification_Code = models.ForeignKey(branchmodel.PIIdentificationCode, blank=True, null=True, unique=False)
    Branch_Identification_Code= models.ForeignKey(branchmodel.RequiredHeader, blank=True, null=True)
    Borrowers_Client_Number= models.ForeignKey(CREDIT_APPLICATION, blank=False, null=False)
    Stakeholder_Type= models.CharField(max_length=250, choices=stakeholdertype.get_stakeholders(), default="", blank=True)
    Stakeholder_Category= models.CharField(max_length=250, choices=stakeholdercategory.get_category(), default="", blank=True)
    Shareholder_Percentage= models.CharField(max_length=250, choices=stakeholdercategory.get_percentage(), default="", blank=True)
    gscafb = models.OneToOneField(GSCAFB_INFORMATION, blank=True, null=True, unique=False)
    idi = models.OneToOneField(IDENTIFICATION_INFORMATION, blank=True, null=True, unique=False)
    ei = models.OneToOneField(EMPLOYMENT_INFORMATION, blank=True, null=True, unique=False)
    pci = models.OneToOneField(PCI,blank=True, null=True, unique=False)
    sci = models.OneToOneField(SCI,blank=True, null=True, unique=False)
    date = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ("-id", )
        
    def save(self, *args, **kwargs):
        """
        Override the save method allowing us to perform additional
        settings.
        """
        super(BORROWERSTAKEHOLDER, self).save(*args, **kwargs)
        try:
            if( not self.PI_Identification_Code ):
                self.searched_pi = self.search_picode(settings.PI_IDENTIFICATION)
                self.PI_Identification_Code = self.searched_pi

            if( not self.Branch_Identification_Code):
                self.Branch_Identification_Code = settings.BRANCH_IDENTIFICATION_CODE
            super(BORROWERSTAKEHOLDER, self).save(*args, **kwargs)
            
        except Exception as e:
            raise 

    def search_picode(self, CODE):
        try:
            return branchmodel.RequiredHeader.objects.get(pi_identification_code=CODE)
        except:
            raise
            
    def get_allsettings(self):
        return branchmodel.DefaultHeaders.objects.all()
        
    def filter_by_id(self, headers):
        if(headers):
            return headers.get(id=1)
        else:
            return None 
            
    def __str__(self):
        return self.PI_Identification_Code.pi_identification_code

    def get_abbreviation_name(self):
        return "%s" % "BS"

    def get_full_name(self):
        return "BORROWERSTAKEHOLDER"

    def get_update_path(self):
        return "/newupdate/dataupdatingsystem/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_process_path(self):
        return "/processing/data/existing/"

    def get_view_path(self):
        return "/view/dataview/request/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_delete_path(self):
        return "/purgerecords/deleting/%s/True/" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_new_path(self):
        return "/process/sys/data/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

#(CMC)
class COLLATERAL_MATERIAL_COLLATERAL(models.Model):
    #dateset_ref = models.ForeignKey(DataSetRecords)
    PI_Identification_Code = models.ForeignKey(branchmodel.PIIdentificationCode, blank=True, null=True, unique=False)
    Branch_Identification_Code= models.ForeignKey(branchmodel.RequiredHeader, blank=True, null=True)
    Borrowers_Client_Number= models.ForeignKey(CREDIT_APPLICATION, blank=False, null=False, unique=False)
    #Borrower_Account_Reference= models.CharField(max_length=250, default="", blank=True, null=True) #utilregions.get_cba_referencenumber()
    Borrower_Account_Reference= models.ForeignKey(CREDITBORROWERACCOUNT, blank=True) #utilregions.get_cba_referencenumber()
    Borrower_Classification= models.CharField(max_length=250, choices=stakeholdertype.get_stakeholders(), default="", blank=True)
    Collateral_Type_Identification= models.CharField(max_length=250, choices=collateralclassification.get_collateral(), default="", blank=True)
    Collateral_Reference_Number= models.CharField(max_length=250, default="", blank=True)
    Collateral_Description= models.TextField(max_length=100, default="", blank=True)
    Collateral_Currency= models.CharField(max_length=250, choices=currencyisocode.get_currency(), default="", blank=True)
    Collateral_Open_Market_Value = models.CharField(max_length=250, default="", blank=True)
    Collateral_Forced_Sale_Value= models.CharField(max_length=250, default="", blank=True)
    Collateral_Valuation_Expiry_Date = models.CharField(max_length=250, default="", blank=True)
    Instrument_of_Claim= models.CharField(max_length=250, default="", blank=True)
    Valuation_Date= models.CharField(max_length=250, default="", blank=True)
    date = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ("-id", )
        
    def save(self, *args, **kwargs):
        """
        Override the save method allowing us to perform additional
        settings.
        """
        super(COLLATERAL_MATERIAL_COLLATERAL, self).save(*args, **kwargs)
        try:
            if( not self.PI_Identification_Code ):
                self.searched_pi = self.search_picode(settings.PI_IDENTIFICATION)
                self.PI_Identification_Code = self.searched_pi

            if( not self.Branch_Identification_Code):
                self.Branch_Identification_Code = settings.BRANCH_IDENTIFICATION_CODE
            super(COLLATERAL_MATERIAL_COLLATERAL, self).save(*args, **kwargs)
            
        except Exception as e:
            raise 

    def search_picode(self, CODE):
        try:
            return branchmodel.RequiredHeader.objects.get(pi_identification_code=CODE)
        except:
            raise
            
    def get_allsettings(self):
        return branchmodel.DefaultHeaders.objects.all()
        
    def filter_by_id(self, headers):
        if(headers):
            return headers.get(id=1)
        else:
            return None 
            
    def __str__(self):
        return self.PI_Identification_Code.pi_identification_code

    def get_abbreviation_name(self):
        return "%s" % "CMC"

    def get_dataset_name(self):
        """
        """
        #return "%s" % self.dateset_ref.navigation_title
        pass

    def get_full_name(self):
        return "COLLATERAL_MATERIAL_COLLATERAL".replace("_", " ", len(self.PI_Identification_Code.pi_identification_code))

    def get_update_path(self):
        return "/newupdate/dataupdatingsystem/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_process_path(self):
        return "/processing/data/existing/"

    def get_view_path(self):
        return "/view/dataview/request/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_delete_path(self):
        return "/purgerecords/deleting/%s/True/" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_new_path(self):
        return "/process/sys/data/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

#(CCG)
class COLLATERAL_CREDIT_GUARANTOR(models.Model):
    #dateset_ref = models.ForeignKey(DataSetRecords)
    PI_Identification_Code = models.ForeignKey(branchmodel.PIIdentificationCode, blank=True, null=True, unique=False)
    Branch_Identification_Code= models.ForeignKey(branchmodel.RequiredHeader, blank=True, null=True)
    Borrowers_Client_Number= models.ForeignKey(CREDIT_APPLICATION, blank=False, null=False, unique=False)
    Borrower_Account_Reference= models.ForeignKey(CREDITBORROWERACCOUNT, blank=True, unique=False)
    Guarantor_Classification= models.CharField(max_length=250, choices=stakeholdertype.get_stakeholders(), default="", blank=True, null=False)
    Guarantee_Type= models.CharField(max_length=250, choices=gauranteetype.get_guaranteetype(), default="", blank=True, null=False)
    Guarantor_Type= models.CharField(max_length=250, choices=gaurantortype.get_guarantortype(), default="", blank=True, null=False)
    #borrower_stake = models.ForeignKey(CREDITBORROWERACCOUNT, blank=True, null=True, unique=False)
    gscafb = models.OneToOneField(GSCAFB_INFORMATION, blank=True, null=True, unique=False)
    idi = models.OneToOneField(IDENTIFICATION_INFORMATION, blank=True, null=True, unique=False)
    ei = models.OneToOneField(EMPLOYMENT_INFORMATION, blank=True, null=True, unique=False)
    pci = models.OneToOneField(PCI,blank=True, null=True, unique=False)
    sci = models.OneToOneField(SCI,blank=True, null=True, unique=False)
    date = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ("-id", )
        
    def save(self, *args, **kwargs):
        """
        Override the save method allowing us to perform additional
        settings.
        """
        super(COLLATERAL_CREDIT_GUARANTOR, self).save(*args, **kwargs)
        try:
            if( not self.PI_Identification_Code ):
                self.searched_pi = self.search_picode(settings.PI_IDENTIFICATION)
                self.PI_Identification_Code = self.searched_pi

            if( not self.Branch_Identification_Code):
                self.Branch_Identification_Code = settings.BRANCH_IDENTIFICATION_CODE
            super(COLLATERAL_CREDIT_GUARANTOR, self).save(*args, **kwargs)
            
        except Exception as e:
            raise 

    def search_picode(self, CODE):
        try:
            return branchmodel.RequiredHeader.objects.get(pi_identification_code=CODE)
        except:
            raise
            
    def get_allsettings(self):
        return branchmodel.DefaultHeaders.objects.all()
        
    def filter_by_id(self, headers):
        if(headers):
            return headers.get(id=1)
        else:
            return None 
            
    def __str__(self):
        return self.PI_Identification_Code.pi_identification_code

    def get_abbreviation_name(self):
        return "%s" % "CCG"

    def get_dataset_name(self):
        """
        """
        pass
        #return "%s" % self.dateset_ref.navigation_title

    def get_full_name(self):
        return "COLLATERAL_CREDIT_GUARANTOR".replace("_", " ", len(self.PI_Identification_Code.pi_identification_code))

    def get_update_path(self):
        return "/newupdate/dataupdatingsystem/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_process_path(self):
        return "/processing/data/existing/"

    def get_view_path(self):
        return "/view/dataview/request/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_delete_path(self):
        return "/purgerecords/deleting/%s/True/" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_new_path(self):
        return "/process/sys/data/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

#(FRA)
class FINANCIAL_MALPRACTICE_DATA(models.Model):
    #dateset_ref = models.ForeignKey(DataSetRecords)
    PI_Identification_Code = models.ForeignKey(branchmodel.PIIdentificationCode, blank=True, null=True, unique=False)
    Branch_Identification_Code= models.ForeignKey(branchmodel.RequiredHeader, blank=True, null=True)
    Borrowers_Client_Number =  models.ForeignKey(CREDIT_APPLICATION, blank=True, null=True)
    Consumer_Classification= models.CharField(max_length=250, choices=stakeholdertype.get_stakeholders(), default="", blank=True, null=False)
    Category_Code= models.CharField(max_length=250, choices=fraud_model.FRAUD_CHOICES, blank=False, null=False)
    Sub_Category_Code= models.CharField(max_length=250, choices=fraud_model.FRAUD_CHOICES, blank=False, null=False)
    Incident_Date= models.CharField(max_length=250, default="", blank=True, null=False)
    Loss_Amount= models.CharField(max_length=250, default="", blank=True, null=False)
    Currency_Type= models.CharField(max_length=250, choices=currencyisocode.get_currency(), default="", blank=True, null=False)
    Incident_Details= models.TextField(max_length=1000, default="", blank=True, null=False)
    Forensic_Information_Available= models.CharField(max_length=250, choices=forensicinfo.get_forensic(), default="", blank=True, null=False)
    date = models.DateField(auto_now=True)
    
    def save(self, *args, **kwargs):
        """
        Override the save method allowing us to perform additional
        settings.
        """
        super(FINANCIAL_MALPRACTICE_DATA, self).save(*args, **kwargs)
        try:
            if( not self.PI_Identification_Code ):
                self.searched_pi = self.search_picode(settings.PI_IDENTIFICATION)
                self.PI_Identification_Code = self.searched_pi

            if( not self.Branch_Identification_Code):
                self.Branch_Identification_Code = settings.BRANCH_IDENTIFICATION_CODE
            super(FINANCIAL_MALPRACTICE_DATA, self).save(*args, **kwargs)
        except Exception as e:
            raise 

    def search_picode(self, CODE):
        try:
            return branchmodel.RequiredHeader.objects.get(pi_identification_code=CODE)
        except:
            raise
            
    def get_allsettings(self):
        return branchmodel.DefaultHeaders.objects.all()
        
    def filter_by_id(self, headers):
        if(headers):
            return headers.get(id=1)
        else:
            return None 
            
    def __str__(self):
        return self.PI_Identification_Code.pi_identification_code

    def get_abbreviation_name(self):
        return "%s" % "CMC"

    def get_full_name(self):
        return "FINANCIAL_MALPRACTICE_DATA".replace("_", " ", len(self.PI_Identification_Code.pi_identification_code))

    def get_update_path(self):
        return "/newupdate/dataupdatingsystem/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_process_path(self):
        return "/processing/data/existing/"

    def get_view_path(self):
        return "/view/dataview/request/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_delete_path(self):
        return "/purgerecords/deleting/%s/True/" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    def get_new_path(self):
        return "/process/sys/data/%s" % (self.get_full_name().lower().replace("_", " ", len(self.get_full_name())))

    class Meta:
        ordering = ("-id", )
