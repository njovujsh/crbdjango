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
        self.fields['PI_Identification_Code'].widget.attrs['disabled'] = "disabled" #self.fields['Institution_Name'].label
        self.fields['Institution_Type'].widget.attrs['disabled'] = "disabled" #self.fields['Institution_Name'].label

    class Meta:
        #Does not have other information privided here fcag id, ei
        exclude=["pci", "sci", "validated"]
        model = PARTICIPATING_INSTITUTION
        
class ClientInformation_Forms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientInformation_Forms, self).__init__(*args, **kwargs)
        self.fields['surname'].widget.attrs['placeholder'] = self.fields['surname'].label
        self.fields['firstname'].widget.attrs['placeholder'] = self.fields['firstname'].label
        self.fields['business_name'].widget.attrs['placeholder'] = self.fields['business_name'].label

        # Disable
        self.fields['surname'].widget.attrs['disabled'] = "disabled"
        self.fields['firstname'].widget.attrs['disabled'] = "disabled"
        self.fields['business_name'].widget.attrs['disabled'] = "disabled"

    class Meta:
        #Does not have other information privided here fcag id, ei
        #exclude=["pci", "sci", "validated"]
        model = ClientInformation
        fields = "__all__"
  
class IB_Forms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(IB_Forms, self).__init__(*args,  **kwargs)
        self.fields['Date_Opened'].widget.attrs['placeholder'] = "yy-mm-dd"
        #self.fields['Branch_Identification_Code'].widget.attrs['placeholder'] = self.fields['Branch_Identification_Code'].label
        #self.fields['Branch_Name'].widget.attrs['placeholder'] = self.fields['Branch_Name'].label
        self.fields['Branch_Type'].widget.attrs['placeholder'] = self.fields['Branch_Type'].label

        # Add class attributes
        self.fields['Branch_Type'].widget.attrs['disabled'] = 'disabled'
        self.fields['PI_Identification_Code'].widget.attrs['disabled'] = 'disabled'
        
    class Meta:
        #Does not container sci, fcag, id, ei
        exclude=["pci", "Branch_Identification_Code", "Branch_Name"]
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

        
        # Add class attributes to them.
        self.fields['PI_Identification_Code'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Branch_Identification_Code'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Borrowers_Client_Number'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Borrower_Classification'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Credit_Account_Type'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Currency'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Opening_Balance_Indicator'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Type_of_Interest'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Interest_Calculation_Method'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Credit_Amortization_Type'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Credit_Payment_Frequency'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Current_Balance_Indicator'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Credit_Account_Status'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Credit_Account_Risk_Classification'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Flag_for_Restructured_Credit'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Credit_Account_Closure_Reason'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Client_Consent_Flag'].widget.attrs['disabled'] = " disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Client_Advice_Notice_Flag'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Loan_Purpose'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Term'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Specific_Provision_Amount'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Balance_Overdue_Indicator'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Balance_Overdue'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Number_of_Days_in_Arrears'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Credit_Account_Arrears_Date'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Last_Status_Change_Date'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Last_Payment_Date'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Current_Balance_Amount'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Monthly_Instalment_Amount'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Number_of_Payments'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Date_of_First_Payment'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Annual_Interest_Rate_at_Disbursement'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Annual_Interest_Rate_at_Reporting'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Maturity_Date'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Facility_Amount_Granted'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Credit_Amount'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Credit_Account_Date'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        self.fields['Credit_Account_Reference'].widget.attrs['disabled'] = "disabled" #self.fields['Credit_Account_Closure_Date'].label
        
    class Meta:
        #Has all
        exclude=["pci", "sci","gscafb", "idi", "ei"]
        model = CREDITBORROWERACCOUNT

class CAP_Forms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CAP_Forms, self).__init__(*args, **kwargs)
        self.fields['Credit_Application_Reference'].widget.attrs['placeholder'] = "Leave black, It's Auto generated by System" 
        self.fields['Credit_Application_Reference'].widget.attrs['disabled'] = "disabled" #self.fields['Institution_Name'].label
        self.fields['PI_Identification_Code'].widget.attrs['disabled'] = "disabled" #self.fields['Institution_Name'].label
        self.fields['Branch_Identification_Code'].widget.attrs['disabled'] = "disabled" #self.fields['Institution_Name'].label
        self.fields['Client_Number'].widget.attrs['disabled'] = "disabled" #self.fields['Institution_Name'].label
        self.fields['Applicant_Classification'].widget.attrs['disabled'] = "disabled" #self.fields['Institution_Name'].label
        self.fields['Credit_Application_Date'].widget.attrs['disabled'] = "disabled" #self.fields['Institution_Name'].label
        self.fields['Amount'].widget.attrs['disabled'] = "disabled" #self.fields['Institution_Name'].label
        self.fields['Currency'].widget.attrs['disabled'] = "disabled" #self.fields['Institution_Name'].label
        self.fields['Credit_Account_or_Loan_Product_Type'].widget.attrs['disabled'] = "disabled" #self.fields['Institution_Name'].label
        self.fields['Credit_Application_Status'].widget.attrs['disabled'] = "disabled" #self.fields['Institution_Name'].label
        #self.fields['Last_Status_Change_Date'].widget.attrs['disabled'] = "disabled" #self.fields['Institution_Name'].label
        self.fields['Credit_Application_Duration'].widget.attrs['disabled'] = "disabled" #self.fields['Institution_Name'].label
        self.fields['Rejection_Reason'].widget.attrs['disabled'] = "disabled" #self.fields['Institution_Name'].label
        self.fields['Client_Consent_flag'].widget.attrs['disabled'] = "disabled" #self.fields['Institution_Name'].label

    class Meta:
        #Has all
        exclude=["pci", "sci","gscafb", "idi", "ei",  "client_details","history", "howmanytimes"]
        model = CREDIT_APPLICATION
        
class BC_Forms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BC_Forms, self).__init__(*args, **kwargs)

        self.fields['Cheque_Account_Opened_Date'].widget.attrs['disabled'] = "disabled"
        self.fields['Cheque_Bounce_Date'].widget.attrs['disabled'] = "disabled"
        self.fields['PI_Identification_Code'].widget.attrs['disabled'] = "disabled"
        self.fields['PI_Client_Classification'].widget.attrs['disabled'] = "disabled"
        self.fields['Cheque_Account_Classification'].widget.attrs['disabled'] = "disabled"
        self.fields['Cheque_Account_Type'].widget.attrs['disabled'] = "disabled"
        self.fields['Cheque_Currency'].widget.attrs['disabled'] = "disabled"
        self.fields['Cheque_Account_Bounce_Reason'].widget.attrs['disabled'] = "disabled"
        self.fields['Beneficiary_Name_Or_Payee'].widget.attrs['disabled'] = "disabled"
        self.fields['Cheque_Amount'].widget.attrs['disabled'] = "disabled"
        self.fields['Cheque_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['Cheque_Account_Reference_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['Borrowers_Client_Number'].widget.attrs['disabled'] = "disabled"
        
    class Meta:
        #Has all
        exclude=["pci", "sci","gscafb", "idi", "ei"]
        model = BOUNCEDCHEQUES
        
class PIS_Forms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PIS_Forms, self).__init__(*args, **kwargs)
        self.fields['Shareholder_Percentage'].widget.attrs['disabled'] = "disabled"
        self.fields['Stakeholder_Category'].widget.attrs['disabled'] = "disabled"
        self.fields['Stakeholder_Type'].widget.attrs['disabled'] = "disabled"
        self.fields['PI_Identification_Code'].widget.attrs['disabled'] = "disabled"
        
    class Meta:
        exclude=["pci", "sci","gscafb", "idi", "ei"]
        model = PARTICIPATINGINSTITUTIONSTAKEHOLDER

class BS_Forms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BS_Forms, self).__init__(*args, **kwargs)
        self.fields['Shareholder_Percentage'].widget.attrs['disabled'] = "disabled"
        self.fields['Stakeholder_Category'].widget.attrs['disabled'] = "disabled"
        self.fields['Stakeholder_Type'].widget.attrs['disabled'] = "disabled"
        self.fields['Borrowers_Client_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['Branch_Identification_Code'].widget.attrs['disabled'] = "disabled"
        self.fields['PI_Identification_Code'].widget.attrs['disabled'] = "disabled"
        
    class Meta:
        #Has all
        exclude=["pci", "sci","gscafb", "idi", "ei", "borrower_stake"]
        model = BORROWERSTAKEHOLDER
        
class CMC_Forms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CMC_Forms, self).__init__(*args, **kwargs)
        self.fields['PI_Identification_Code'].widget.attrs['disabled'] = "disabled"
        self.fields['Branch_Identification_Code'].widget.attrs['disabled'] = "disabled"
        self.fields['Borrowers_Client_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['Borrower_Account_Reference'].widget.attrs['disabled'] = "disabled"
        self.fields['Borrower_Classification'].widget.attrs['disabled'] = "disabled"
        self.fields['Collateral_Type_Identification'].widget.attrs['disabled'] = "disabled"
        self.fields['Collateral_Reference_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['Collateral_Description'].widget.attrs['disabled'] = "disabled"
        self.fields['Collateral_Currency'].widget.attrs['disabled'] = "disabled"
        self.fields['Collateral_Open_Market_Value'].widget.attrs['disabled'] = "disabled"
        self.fields['Collateral_Forced_Sale_Value'].widget.attrs['disabled'] = "disabled"
        self.fields['Collateral_Valuation_Expiry_Date'].widget.attrs['disabled'] = "disabled"
        self.fields['Instrument_of_Claim'].widget.attrs['disabled'] = "disabled"
        self.fields['Valuation_Date'].widget.attrs['disabled'] = "disabled"
        
    class Meta:
        #Has all 
        exclude=["pci", "sci","gscafb", "idi", "ei", "borrower_stake"]
        model = COLLATERAL_MATERIAL_COLLATERAL
        
class CCG_Forms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CCG_Forms, self).__init__(*args, **kwargs)        
        self.fields['Guarantor_Type'].widget.attrs['disabled'] = "disabled"
        self.fields['Guarantee_Type'].widget.attrs['disabled'] = "disabled"
        self.fields['Guarantor_Classification'].widget.attrs['disabled'] = "disabled"
        self.fields['Borrowers_Client_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['PI_Identification_Code'].widget.attrs['disabled'] = "disabled"
        self.fields['Borrower_Account_Reference'].widget.attrs['disabled'] = "disabled"
        
    class Meta:
        exclude=["pci", "sci","gscafb", "idi", "ei", "borrower_stake", "Branch_Identification_Code"] #Has all
        model = COLLATERAL_CREDIT_GUARANTOR
        
class FRA_Forms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FRA_Forms, self).__init__(*args, **kwargs)
        
        self.fields['Forensic_Information_Available'].widget.attrs['disabled'] = "disabled"
        self.fields['Incident_Details'].widget.attrs['disabled'] = "disabled"
        self.fields['Currency_Type'].widget.attrs['disabled'] = "disabled"
        self.fields['Loss_Amount'].widget.attrs['disabled'] = "disabled"
        self.fields['Incident_Date'].widget.attrs['disabled'] = "disabled"
        self.fields['Sub_Category_Code'].widget.attrs['disabled'] = "disabled"
        self.fields['Category_Code'].widget.attrs['disabled'] = "disabled"
        self.fields['Consumer_Classification'].widget.attrs['disabled'] = "disabled"
        self.fields['Borrowers_Client_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['Branch_Identification_Code'].widget.attrs['disabled'] = "disabled"
        self.fields['PI_Identification_Code'].widget.attrs['disabled'] = "disabled"
        
    class Meta:
        exclude=["pci", "sci","gscafb", "idi", "ei"] #Has all
        model = FINANCIAL_MALPRACTICE_DATA

class PCIForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PCIForms, self).__init__(*args, **kwargs)
        #self.fields['PCI_District'] = forms.CharField(required=False, widget=forms.Select())
        #self.fields['PCI_County_or_Town'] = forms.CharField(required=False, widget=forms.Select())
        #self.fields['PCI_Parish'] = forms.CharField(required=False, widget=forms.Select())
        
        #self.fields['PCI_District'] = forms.CharField(required=False, widget=forms.Select(choices=umodels.Districts.objects.all().values_list("name", "name")))
        #self.fields['PCI_County_or_Town'] = forms.CharField(required=False, widget=forms.Select(choices=umodels.Subcounties.objects.all().values_list("name", "name")))
        #self.fields['PCI_County_or_Town'] = forms.CharField(required=False, widget=forms.Select())
        #self.fields['PCI_Parish'] = forms.CharField(required=False, widget=forms.Select())
        #self.fields['PCI_Parish'] = forms.CharField(required=False, widget=forms.Select(choices=umodels.Parishes.objects.all().values_list("name", "name")))
        
        self.fields['PCI_Period_At_Address'].widget.attrs["plachoder"] = "In Months"


        #disable forms
        self.fields['PCI_Building_Unit_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['PCI_Building_Name'].widget.attrs['disabled'] = "disabled"
        self.fields['PCI_Floor_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['PCI_Plot_or_Street_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['PCI_LC_or_Street_Name'].widget.attrs['disabled'] = "disabled"
        self.fields['PCI_Region'].widget.attrs['disabled'] = "disabled"
        self.fields['PCI_District'].widget.attrs['disabled'] = "disabled"
        self.fields['PCI_County_or_Town'].widget.attrs['disabled'] = "disabled"
        self.fields['PCI_Parish'].widget.attrs['disabled'] = "disabled"
        self.fields['PCI_Suburb'].widget.attrs['disabled'] = "disabled"
        self.fields['PCI_Village'].widget.attrs['disabled'] = "disabled"
        self.fields['PCI_PO_Box_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['PCI_Post_Office_Town'].widget.attrs['disabled'] = "disabled"
        self.fields['PCI_Country_Code'].widget.attrs['disabled'] = "disabled"
        self.fields['PCI_Period_At_Address'].widget.attrs['disabled'] = "disabled"
        self.fields['PCI_Flag_of_Ownership'].widget.attrs['disabled'] = "disabled"
        self.fields['PCI_Primary_Number_Telephone_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['PCI_Other_Number_Telephone_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['PCI_Mobile_Number_Telephone_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['PCI_Facsimile_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['PCI_Email_Address'].widget.attrs['disabled'] = "disabled"
        self.fields['PCI_Web_site'].widget.attrs['disabled'] = "disabled"
    class Meta:
        model = PCI
        fields = "__all__"
        
class SCIForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SCIForms, self).__init__(*args, **kwargs)
        #self.fields['SCI_District'] = forms.CharField(required=False, widget=forms.Select())
        #self.fields['SCI_County_or_Town'] = forms.CharField(required=False, widget=forms.Select())
        #self.fields['SCI_Parish'] = forms.CharField(required=False, widget=forms.Select())
        self.fields['SCI_Period_At_Address'].widget.attrs["plachoder"]="In Months"

        #self.fields['SCI_District'] = forms.CharField(required=False, widget=forms.Select(choices=umodels.Districts.objects.all().values_list("name", "name")))
        #self.fields['SCI_District'] = forms.CharField(required=False, widget=forms.Select())
        #self.fields['SCI_County_or_Town'] = forms.CharField(required=False, widget=forms.Select(choices=umodels.Subcounties.objects.all().values_list("name", "name")))
        #self.fields['SCI_County_or_Town'] = forms.CharField(required=False, widget=forms.Select())
        #self.fields['SCI_Parish'] = forms.CharField(required=False, widget=forms.Select(choices=umodels.Parishes.objects.all().values_list("name", "name")))

        #disable forms
        self.fields['SCI_Unit_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['SCI_Unit_Name'].widget.attrs['disabled'] = "disabled"
        self.fields['SCI_Floor_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['SCI_Plot_or_Street_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['SCI_LC_or_Street_Name'].widget.attrs['disabled'] = "disabled"
        self.fields['SCI_Region'].widget.attrs['disabled'] = "disabled"
        self.fields['SCI_District'].widget.attrs['disabled'] = "disabled"
        self.fields['SCI_County_or_Town'].widget.attrs['disabled'] = "disabled"
        self.fields['SCI_Parish'].widget.attrs['disabled'] = "disabled"
        self.fields['SCI_Suburb'].widget.attrs['disabled'] = "disabled"
        self.fields['SCI_Village'].widget.attrs['disabled'] = "disabled"
        self.fields['SCI_PO_Box_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['SCI_Post_Office_Town'].widget.attrs['disabled'] = "disabled"
        self.fields['SCI_Country_Code'].widget.attrs['disabled'] = "disabled"
        self.fields['SCI_Period_At_Address'].widget.attrs['disabled'] = "disabled"
        self.fields['SCI_Flag_for_ownership'].widget.attrs['disabled'] = "disabled"
        self.fields['SCI_Primary_Number_Telephone_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['SCI_Other_Number_Telephone_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['SCI_Mobile_Number_Telephone_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['SCI_Facsimile_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['SCI_Email_Address'].widget.attrs['disabled'] = "disabled"
        self.fields['SCI_Web_site'].widget.attrs['disabled'] = "disabled"
    class Meta:
        model = SCI
        fields = "__all__"
        
class EIForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EIForms, self).__init__(*args, **kwargs)
        #id_EIForms-EI_Employment_Date
        self.fields["EI_Employment_Date"].widget.attrs["placeholder"]="yy-mm-dd"

        #Disable.
        self.fields['EI_Employment_Type'].widget.attrs['disabled'] = "disabled"
        self.fields['EI_Primary_Occupation'].widget.attrs['disabled'] = "disabled"
        self.fields['EI_Employer_Name'].widget.attrs['disabled'] = "disabled"
        self.fields['EI_Employee_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['EI_Employment_Date'].widget.attrs['disabled'] = "disabled"
        self.fields['EI_Income_Band'].widget.attrs['disabled'] = "disabled"
        self.fields['EI_Salary_Frequency'].widget.attrs['disabled'] = "disabled"
    class Meta:
        model = EMPLOYMENT_INFORMATION
        fields = "__all__"
        
class IDForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(IDForms, self).__init__(*args, **kwargs)

        #Disable.
        self.fields['II_Registration_Certificate_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['II_Tax_Identification_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['II_Value_Added_Tax_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['II_FCS_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['II_Passport_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['II_Drivers_Licence_ID_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['II_Voters_PERNO'].widget.attrs['disabled'] = "disabled"
        self.fields['II_Drivers_License_Permit_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['II_NSSF_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['II_Country_ID'].widget.attrs['disabled'] = "disabled"
        self.fields['II_Country_Issuing_Authority'].widget.attrs['disabled'] = "disabled"
        self.fields['II_Nationality'].widget.attrs['disabled'] = "disabled"
        self.fields['II_Police_ID_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['II_UPDF_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['II_KACITA_License_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['II_Public_Service_Pension_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['II_Teacher_Registration_Number'].widget.attrs['disabled'] = "disabled"
        self.fields['II_Country_Of_Issue'].widget.attrs['disabled'] = "disabled"
        
    class Meta:
        model = IDENTIFICATION_INFORMATION
        fields = "__all__"
        
class GSCAFBForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super(GSCAFBForms, self).__init__(*args, **kwargs)
        #Disable
        self.fields['GSCAFB_Business_Name'].widget.attrs['disabled'] = "disabled"
        self.fields['GSCAFB_Trading_Name'].widget.attrs['disabled'] = "disabled"
        self.fields['GSCAFB_Activity_Description'].widget.attrs['disabled'] = "disabled"
        self.fields['GSCAFB_Industry_Sector_Code'].widget.attrs['disabled'] = "disabled"
        self.fields['GSCAFB_Date_Registered'].widget.attrs['disabled'] = "disabled"
        self.fields['GSCAFB_Business_Type_Code'].widget.attrs['disabled'] = "disabled"
        self.fields['GSCAFB_Surname'].widget.attrs['disabled'] = "disabled"
        self.fields['GSCAFB_Forename1'].widget.attrs['disabled'] = "disabled"
        self.fields['GSCAFB_Forename2'].widget.attrs['disabled'] = "disabled"
        self.fields['GSCAFB_Forename3'].widget.attrs['disabled'] = "disabled"
        self.fields['GSCAFB_Gender'].widget.attrs['disabled'] = "disabled"
        self.fields['GSCAFB_Marital_Status'].widget.attrs['disabled'] = "disabled"
        self.fields['GSCAFB_Date_of_Birth'].widget.attrs['disabled'] = "disabled"
        
    class Meta:
        model = GSCAFB_INFORMATION
        fields = "__all__"

"""
<form >
<input type="text" placeholder="Enter your email address ..." id="email" name="emailAddress"   />
<button class="btn validate" type="submit" disabled >Join</button>
</form>
 
<script>
 jQuery(document).ready(function($) {
      //  var testEmail = /^[A-Z0-9._%+-]+@([A-Z0-9-]+\.)+[A-Z]{2,4}$/i;
      <!-- another regex filter you can use -->
      var testEmail =    /^[ ]*([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]{2,})[ ]*$/i;
      jQuery('input#email').bind('input propertychange', function() {
        if (testEmail.test(jQuery(this).val()))
        {
           jQuery(this).css({ 'border':'1px solid green'});
           jQuery('button.validate').prop("disabled",false);
         } else
         {
           jQuery(this).css({ 'border':'1px solid red'});
           jQuery('button.validate').prop("disabled",true);
         }
       });
});
</script>
"""
