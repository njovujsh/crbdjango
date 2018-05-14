from django.forms import ModelForm
from datasetrecords.models import *
#from django.contrib.admin import widgets                                       
from django import forms
from django.forms import widgets 
from django.forms.models import inlineformset_factory
#from datasetrecords.models import RequiredHeader
from util import models as umodels 
from branchcode import models as model 

#Creating forms class for the PARTICIPATING_INSTITUTION
class PI_Forms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PI_Forms, self).__init__(*args, **kwargs)
        self.fields['Institution_Name'].widget.attrs['placeholder'] = self.fields['Institution_Name'].label
        self.fields['License_Issuing_Date'].widget.attrs['placeholder'] = "yy-mm-dd" #self.fields['Institution_Name'].label
        #self.fields['PI_Identification_Code'].widget.attrs['class'] = "chosen-select chosen-select-width" #self.fields['Institution_Name'].label
        #self.fields['Institution_Type'].widget.attrs['class'] = "chosen-select chosen-select-width" #self.fields['Institution_Name'].label

    class Meta:
        #Does not have other information privided here fcag id, ei
        exclude=["pci", "sci", "validated"] #, "PI_Identification_Code"]
        model = PARTICIPATING_INSTITUTION
        
class ClientInformation_Forms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientInformation_Forms, self).__init__(*args, **kwargs)
        self.fields['surname'].widget.attrs['placeholder'] = self.fields['surname'].label
        self.fields['firstname'].widget.attrs['placeholder'] = self.fields['firstname'].label
        self.fields['business_name'].widget.attrs['placeholder'] = self.fields['business_name'].label

    class Meta:
        #Does not have other information privided here fcag id, ei
        #exclude=["pci", "sci", "validated"]
        model = ClientInformation
        fields = "__all__"
  
class IB_Forms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(IB_Forms, self).__init__(*args,  **kwargs)
        self.fields['Date_Opened'].widget.attrs['placeholder'] = "yy-mm-dd"
        self.fields['Date_Opened'].widget.attrs['class'] = "form-control date-picker"
        #self.fields['Branch_Identification_Code'].widget.attrs['placeholder'] = self.fields['Branch_Identification_Code'].label
        self.fields['Branch_Name'].widget.attrs['placeholder'] = self.fields['Branch_Name'].label
        self.fields['Branch_Type'].widget.attrs['placeholder'] = self.fields['Branch_Type'].label

        # Add class attributes
        #self.fields['Branch_Type'].widget.attrs['class'] = 'chosen-select chosen-select-width'
        #self.fields['PI_Identification_Code'].widget.attrs['class'] = 'chosen-select chosen-select-width'
        
    class Meta:
        #Does not container sci, fcag, id, ei
        exclude=["pci", ] #"Branch_Identification_Code", "Branch_Name", "PI_Identification_Code"]
        model  = INSTITUTION_BRANCH

class CBA_Forms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CBA_Forms, self).__init__(*args,  **kwargs)
        self.fields['Credit_Account_Date'].widget.attrs['placeholder'] = "yy-mm-dd"
        self.fields['Transaction_Date'].widget.attrs['placeholder'] = "yy-mm-dd"
        self.fields['Maturity_Date'].widget.attrs['placeholder'] = "yy-mm-dd"
        self.fields['Date_of_First_Payment'].widget.attrs['placeholder'] = "yy-mm-dd"
        self.fields['Last_Payment_Date'].widget.attrs['placeholder'] = "yy-mm-dd"
        self.fields['Last_Status_Change_Date'].widget.attrs['placeholder'] = "yy-mm-dd"
        self.fields['Credit_Account_Arrears_Date'].widget.attrs['placeholder'] = "yy-mm-dd"
        #self.fields['Branch_Identification_Code'].widget.attrs['placeholder'] = self.fields['Branch_Identification_Code'].label
        self.fields['Borrowers_Client_Number'].widget.attrs['placeholder'] = self.fields['Borrowers_Client_Number'].label
        self.fields['Credit_Account_Reference'].widget.attrs['placeholder'] = self.fields['Credit_Account_Reference'].label
        self.fields['Credit_Amount'].widget.attrs['placeholder'] = self.fields['Credit_Amount'].label
        self.fields['Facility_Amount_Granted'].widget.attrs['placeholder'] = self.fields['Facility_Amount_Granted'].label
        self.fields['Group_Identification_Joint_Account_Number'].widget.attrs['placeholder'] = self.fields['Group_Identification_Joint_Account_Number'].label
        self.fields['Credit_Account_Closure_Date'].widget.attrs['placeholder'] = "yy-mm-dd" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Old_Client_Number'].widget.attrs['placeholder'] = self.fields['Old_Client_Number'].label
        self.fields['Old_Account_Number'].widget.attrs['placeholder'] = self.fields['Old_Account_Number'].label
        self.fields['Old_Branch_Code'].widget.attrs['placeholder'] = self.fields['Old_Branch_Code'].label
        self.fields['Balance_Overdue'].widget.attrs['placeholder'] = "0.0"
        self.fields['Number_of_Days_in_Arrears'].widget.attrs['placeholder'] = "506"
        self.fields['Annual_Interest_Rate_at_Reporting'].widget.attrs['placeholder'] = "4.0"

        # Add class attributes to them.
        self.fields['Borrowers_Client_Number'].widget.attrs['class'] = "chosen-select chosen-select-width" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Currency'].widget.attrs['class'] = "chosen-select chosen-select-width" #self.fields['Credit_Account_Closure_Date'].label
    
    class Meta:
        #Has all
        exclude=["pci", "sci","gscafb", "idi", "ei"]
        model = CREDITBORROWERACCOUNT

class CAP_Forms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CAP_Forms, self).__init__(*args, **kwargs)
        self.fields['Credit_Application_Reference'].widget.attrs['placeholder'] = "System Auto Generated Only If Left Blank!..." #self.fields['Institution_Name'].label
        #self.fields['Last_Status_Change_Date'].widget.attrs['placeholder'] = "yy-mm-dd" #self.fields['Institution_Name'].label
        self.fields['Credit_Application_Date'].widget.attrs['placeholder'] = "yy-mm-dd" #self.fields['Institution_Name'].label
       
        #self.fields['PI_Identification_Code'].widget.attrs['class'] = "chosen-select chosen-select-width" #self.fields['Institution_Name'].label
        #self.fields['Applicant_Classification'].widget.attrs['class'] = "chosen-select chosen-select-width" #self.fields['Institution_Name'].label
        #self.fields['Credit_Account_or_Loan_Product_Type'].widget.attrs['class'] = "chosen-select chosen-select-width" #self.fields['Institution_Name'].label
        #self.fields['Credit_Application_Status'].widget.attrs['class'] = "chosen-select chosen-select-width" #self.fields['Institution_Name'].label
        #self.fields['Rejection_Reason'].widget.attrs['class'] = "chosen-select chosen-select-width" #self.fields['Institution_Name'].label
        #self.fields['Client_Consent_flag'].widget.attrs['class'] = "chosen-select chosen-select-width" #self.fields['Institution_Name'].label
        self.fields['Currency'].widget.attrs['class'] = "chosen-select chosen-select-width" #self.fields['Institution_Name'].label
        self.fields['Amount'].widget.attrs['placeholder'] = "0.0"  
        self.fields['Credit_Application_Duration'].widget.attrs['placeholder'] = "In Numbers 93"  
        
    class Meta:
        #Has all
        exclude=["pci", "sci","gscafb", "idi", "ei", "client_details", "history", "howmanytimes"]
        model = CREDIT_APPLICATION
        
class BC_Forms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BC_Forms, self).__init__(*args, **kwargs)
        self.fields['Cheque_Account_Opened_Date'].widget.attrs['placeholder'] = "yy-mm-dd"
        self.fields['Cheque_Bounce_Date'].widget.attrs['placeholder'] = "yy-mm-dd"
        #self.fields['PI_Identification_Code'].widget.attrs['class'] = "chosen-select chosen-select-width"
        #self.fields['PI_Client_Classification'].widget.attrs['class'] = "chosen-select chosen-select-width"
        #self.fields['Cheque_Account_Classification'].widget.attrs['class'] = "chosen-select chosen-select-width"
        #self.fields['Cheque_Account_Type'].widget.attrs['class'] = "chosen-select chosen-select-width"
        self.fields['Cheque_Currency'].widget.attrs['class'] = "chosen-select chosen-select-width"
        #self.fields['Cheque_Account_Bounce_Reason'].widget.attrs['class'] = "chosen-select chosen-select-width"
        self.fields['Cheque_Amount'].widget.attrs['placeholder'] = "0.0"  
        self.fields['Cheque_Account_Reference_Number'].widget.attrs['placeholder'] = "12321BC1231SAS"  
        self.fields['Cheque_Account_Opened_Date'].widget.attrs['placeholder'] = "yy-mm-dd"  
        self.fields['Cheque_Number'].widget.attrs['placeholder'] = "Number 1309"  
        self.fields['Beneficiary_Name_Or_Payee'].widget.attrs['placeholder'] = self.fields["Beneficiary_Name_Or_Payee"].label 

        
    class Meta:
        #Has all
        exclude=["pci", "sci","gscafb", "idi", "ei"]
        model = BOUNCEDCHEQUES
        
class PIS_Forms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PIS_Forms, self).__init__(*args, **kwargs)
        #self.fields['Shareholder_Percentage'].widget.attrs['class'] = "chosen-select chosen-select-width"
        #self.fields['Stakeholder_Category'].widget.attrs['class'] = "chosen-select chosen-select-width"
        #self.fields['Stakeholder_Type'].widget.attrs['class'] = "chosen-select chosen-select-width"
        #self.fields['PI_Identification_Code'].widget.attrs['class'] = "chosen-select chosen-select-width"
        
    class Meta:
        exclude=["pci", "sci","gscafb", "idi", "ei"]
        model = PARTICIPATINGINSTITUTIONSTAKEHOLDER

class BS_Forms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BS_Forms, self).__init__(*args, **kwargs)
        #self.fields['PI_Identification_Code'].widget.attrs['class'] = "chosen-select chosen-select-width"
        self.fields['Borrowers_Client_Number'].widget.attrs['class'] = "chosen-select chosen-select-width"
        self.fields['Borrowers_Client_Number'].widget.attrs['id'] = "Borrowers_Client_NumberBS"
        #self.fields['Stakeholder_Type'].widget.attrs['class'] = "chosen-select chosen-select-width"
        #self.fields['Stakeholder_Category'].widget.attrs['class'] = "chosen-select chosen-select-width"
        #self.fields['Shareholder_Percentage'].widget.attrs['class'] = "chosen-select chosen-select-width"
        #self.fields['borrower_stake_details'].widget.attrs['class'] = "chosen-select chosen-select-width"
        
    class Meta:
        #Has all
        exclude=["pci", "sci","gscafb", "idi", "ei", "borrower_stake", "borrower_stake_details"]
        model = BORROWERSTAKEHOLDER
        
class CMC_Forms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CMC_Forms, self).__init__(*args, **kwargs)
        self.fields['Valuation_Date'].widget.attrs['placeholder'] = "yy-mm-dd"
        self.fields['Collateral_Valuation_Expiry_Date'].widget.attrs['placeholder'] = "yy-mm-dd"
        self.fields['Collateral_Reference_Number'].widget.attrs['placeholder'] = self.fields["Collateral_Reference_Number"].label
        self.fields['Collateral_Open_Market_Value'].widget.attrs['placeholder'] = "11000.0"
        self.fields['Collateral_Forced_Sale_Value'].widget.attrs['placeholder'] = "11000.0"
        self.fields['Instrument_of_Claim'].widget.attrs['placeholder'] = self.fields["Instrument_of_Claim"].label 

        self.fields['Collateral_Currency'].widget.attrs['class'] = "chosen-select chosen-select-width"
        #self.fields['Collateral_Type_Identification'].widget.attrs['class'] = "chosen-select chosen-select-width"
        #self.fields['Borrower_Classification'].widget.attrs['class'] = "chosen-select chosen-select-width"
        self.fields['Borrowers_Client_Number'].widget.attrs['class'] = "chosen-select chosen-select-width"
        self.fields['Borrowers_Client_Number'].widget.attrs['id'] = "Borrowers_Client_NumberCMC"
        #self.fields['PI_Identification_Code'].widget.attrs['class'] = "chosen-select chosen-select-width"
        
    class Meta:
        #Has all 
        exclude=["pci", "sci","gscafb", "idi", "ei", "borrower_stake"]
        model = COLLATERAL_MATERIAL_COLLATERAL
        
class CCG_Forms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CCG_Forms, self).__init__(*args, **kwargs)
        #self.fields['Guarantor_Type'].widget.attrs['class'] = "chosen-select chosen-select-width"
        #self.fields['Guarantee_Type'].widget.attrs['class'] = "chosen-select chosen-select-width"
        #self.fields['Guarantor_Classification'].widget.attrs['class'] = "chosen-select chosen-select-width"
        self.fields['Borrowers_Client_Number'].widget.attrs['class'] = "chosen-select chosen-select-width"
        self.fields['Borrowers_Client_Number'].widget.attrs['id'] = "Borrowers_Client_NumberSelect"
        #self.fields['PI_Identification_Code'].widget.attrs['class'] = "chosen-select chosen-select-width"
        
    class Meta:
        exclude=["pci", "sci","gscafb", "idi", "ei", "borrower_stake"] #Has all
        model = COLLATERAL_CREDIT_GUARANTOR
        
class FRA_Forms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FRA_Forms, self).__init__(*args, **kwargs)
        self.fields['Incident_Date'].widget.attrs['placeholder'] = "yy-mm-dd"
        self.fields['Loss_Amount'].widget.attrs['placeholder'] = "0.0"

        #self.fields['Forensic_Information_Available'].widget.attrs['class'] = "chosen-select chosen-select-width"
        self.fields['Currency_Type'].widget.attrs['class'] = "chosen-select chosen-select-width"
        #self.fields['Sub_Category_Code'].widget.attrs['class'] = "chosen-select chosen-select-width"
        #self.fields['Category_Code'].widget.attrs['class'] = "chosen-select chosen-select-width"
        #self.fields['Consumer_Classification'].widget.attrs['class'] = "chosen-select chosen-select-width"
        self.fields['Borrowers_Client_Number'].widget.attrs['class'] = "chosen-select chosen-select-width"
        self.fields['Borrowers_Client_Number'].widget.attrs['id'] = "Borrowers_Client_NumberFRA"
        #self.fields['PI_Identification_Code'].widget.attrs['class'] = "chosen-select chosen-select-width"
        
    class Meta:
        exclude=["pci", "sci","gscafb", "idi", "ei",] #Has all
        model = FINANCIAL_MALPRACTICE_DATA

class PCIForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PCIForms, self).__init__(*args, **kwargs)
        self.fields['PCI_Period_At_Address'].widget.attrs["placeholder"] = "In Months"
        self.fields['PCI_Email_Address'].widget.attrs["placeholder"] = "username@email.com"
        self.fields['PCI_Web_site'].widget.attrs["placeholder"] = "www.domain.com"

        for field in self.fields:
            self.fields[field].widget.attrs["placeholder"] = self.fields[field].label
            
    class Meta:
        model = PCI
        fields = "__all__"
        
class SCIForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SCIForms, self).__init__(*args, **kwargs) 
        self.fields['SCI_Period_At_Address'].widget.attrs["placeholder"]="In Months"
        self.fields['SCI_Email_Address'].widget.attrs["placeholder"] = "username@email.com"
        self.fields['SCI_Web_site'].widget.attrs["placeholder"] = "www.domain.com"

        
        for field in self.fields:
            self.fields[field].widget.attrs["placeholder"] = self.fields[field].label
            
    class Meta:
        model = SCI
        fields = "__all__"
        
class EIForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EIForms, self).__init__(*args, **kwargs)
        #id_EIForms-EI_Employment_Date
        self.fields["EI_Employment_Date"].widget.attrs["placeholder"]="yy-mm-dd"

        
        for field in self.fields:
            self.fields[field].widget.attrs["placeholder"] = self.fields[field].label
            
    class Meta:
        model = EMPLOYMENT_INFORMATION
        fields = "__all__"
        
class IDForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(IDForms, self).__init__(*args, **kwargs)
        #self.fields["II_Registration_Certificate_Number"].widget.attrs["class"]="HideMe"
        self.fields["II_Country_Of_Issue"].widget.attrs["class"]="chosen-select chosen-select-width"
        self.fields["II_Country_Issuing_Authority"].widget.attrs["class"]="chosen-select chosen-select-width"
        self.fields["II_Nationality"].widget.attrs["class"]="chosen-select chosen-select-width"


        for field in self.fields:
            self.fields[field].widget.attrs["placeholder"] = self.fields[field].label
            
    class Meta:
        model = IDENTIFICATION_INFORMATION
        fields = "__all__"
        
class GSCAFBForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(GSCAFBForms, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["placeholder"] = self.fields[field].label
            
        self.fields["GSCAFB_Date_Registered"].widget.attrs["placeholder"]="yy-mm-dd"
        self.fields["GSCAFB_Date_of_Birth"].widget.attrs["placeholder"]="yy-mm-dd"

        #self.fields['GSCAFB_Marital_Status'].widget.attrs['class'] = "chosen-select chosen-select-width"
        #self.fields['GSCAFB_Gender'].widget.attrs['class'] = "chosen-select chosen-select-width"
        #self.fields['GSCAFB_Business_Type_Code'].widget.attrs['class'] = "chosen-select"
        
        self.fields['GSCAFB_Business_Name'].widget.attrs['class'] = "HideMe"
        self.fields['GSCAFB_Trading_Name'].widget.attrs['class'] = "HideMe"
        self.fields['GSCAFB_Activity_Description'].widget.attrs['class'] = "HideMe"
        self.fields['GSCAFB_Industry_Sector_Code'].widget.attrs['class'] = "HideMe"
        self.fields['GSCAFB_Date_Registered'].widget.attrs['class'] = "HideMe"
        self.fields['GSCAFB_Business_Type_Code'].widget.attrs['class'] = "HideMe"
        
    class Meta:
        model = GSCAFB_INFORMATION
        fields = "__all__"
        
def get_cba_referencenumber():
    """
    Returns only reference number of cba.
    """
    cba_ref_list = []
    allrec = CREDITBORROWERACCOUNT.objects.all()
    if( not len(allrec)):
        cba_ref_list.append(("", ""))
        return cba_ref_list
    else:
        for a in allrec:
            cba_ref_list.append((a.Credit_Account_Reference, a.Credit_Account_Reference))
        return tuple(cba_ref_list)
