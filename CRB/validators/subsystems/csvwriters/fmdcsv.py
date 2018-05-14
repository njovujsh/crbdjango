import csv
from django.http import HttpResponse
from django.utils.encoding import smart_str
from validators.subsystems.csvwriters import processcsvs
from validators.subsystems.csvwriters import pivalidatecsv
from validators.subsystems.datasets import pcivalidate 
from validators.subsystems.datasets import scivalidate 
from validators.subsystems.datasets import eivalidate 
from validators.subsystems.datasets import iivalidate 
from validators.subsystems.datasets import gsvalidate 
from validators.subsystems.datasets import validationstatus 

class ProcessCSVFMD(processcsvs.ProcessCSV):
    def __init__(self, filename, dialect, row, headers, delimiter="|",response=None):
        super(ProcessCSVFMD, self).__init__(filename, dialect,response=response)
        
        self.delimiter = delimiter
        self.row = row 
        
        if(headers):
            self.write_headers(headers)
            
    def write_row_data(self, coldata):
        try:
            for data in coldata:
                self.writer.writerow([
                                self.get_data_id(),
                                smart_str(unicode(data.PI_Identification_Code.pi_identification_code)),
                                smart_str(unicode(data.Branch_Identification_Code.branch_code)),
                                smart_str(unicode(data.Borrowers_Client_Number.Client_Number)),
                                smart_str(unicode(data.Consumer_Classification)),
                                smart_str(unicode(data.Category_Code)),
                                smart_str(unicode(data.Sub_Category_Code)),
                                smart_str(unicode(data.Incident_Date)),
                                smart_str(unicode(data.Loss_Amount)),
                                smart_str(unicode(data.Currency_Type)),
                                smart_str(unicode(data.Incident_Details)),
                                smart_str(unicode(data.Forensic_Information_Available)),
                                
                                smart_str(unicode(data.Borrowers_Client_Number.idi.II_Registration_Certificate_Number)),
                                smart_str(unicode(data.Borrowers_Client_Number.idi.II_Tax_Identification_Number)),
                                smart_str(unicode(data.Borrowers_Client_Number.idi.II_Value_Added_Tax_Number)),
                                smart_str(unicode(data.Borrowers_Client_Number.idi.II_FCS_Number)),
                                smart_str(unicode(data.Borrowers_Client_Number.idi.II_Passport_Number)),
                                smart_str(unicode(data.Borrowers_Client_Number.idi.II_Drivers_Licence_ID_Number)),
                                smart_str(unicode(data.Borrowers_Client_Number.idi.II_Voters_PERNO)),
                                smart_str(unicode(data.Borrowers_Client_Number.idi.II_Drivers_License_Permit_Number)),
                                smart_str(unicode(data.Borrowers_Client_Number.idi.II_NSSF_Number)),
                                smart_str(unicode(data.Borrowers_Client_Number.idi.II_Country_ID)),
                                smart_str(unicode(data.Borrowers_Client_Number.idi.II_Country_Issuing_Authority)),
                                smart_str(unicode(data.Borrowers_Client_Number.idi.II_Nationality)),
                                smart_str(unicode(data.Borrowers_Client_Number.idi.II_Police_ID_Number)),
                                smart_str(unicode(data.Borrowers_Client_Number.idi.II_UPDF_Number)),
                                smart_str(unicode(data.Borrowers_Client_Number.idi.II_KACITA_License_Number)),
                                smart_str(unicode(data.Borrowers_Client_Number.idi.II_Public_Service_Pension_Number)),
                                smart_str(unicode(data.Borrowers_Client_Number.idi.II_Teacher_Registration_Number)),
                                smart_str(unicode(data.Borrowers_Client_Number.idi.II_Country_Of_Issue)),
                                
                                smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Business_Name)),
                                smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Trading_Name)),
                                smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Activity_Description)),
                                smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Industry_Sector_Code)),
                                smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Date_Registered)),
                                smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Business_Type_Code)),
                                smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Surname)),
                                smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Forename1)),
                                smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Forename2)),
                                smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Forename3)),
                                smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Gender)),
                                smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Marital_Status)),
                                smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Date_of_Birth)),
                                
                                smart_str(unicode(data.Borrowers_Client_Number.ei.EI_Employment_Type)),
                                smart_str(unicode(data.Borrowers_Client_Number.ei.EI_Primary_Occupation)),
                                smart_str(unicode(data.Borrowers_Client_Number.ei.EI_Employer_Name)),
                                smart_str(unicode(data.Borrowers_Client_Number.ei.EI_Employee_Number)),
                                smart_str(unicode(data.Borrowers_Client_Number.ei.EI_Employment_Date)),
                                smart_str(unicode(data.Borrowers_Client_Number.ei.EI_Income_Band)),
                                smart_str(unicode(data.Borrowers_Client_Number.ei.EI_Salary_Frequency)),
                                
                                smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Building_Name)),  
                                smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Floor_Number)),  
                                smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Plot_or_Street_Number)),  
                                smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_LC_or_Street_Name)),  
                                smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Parish)),  
                                smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Suburb)), 
                                smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Village)),  
                                smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_County_or_Town)), 
                                smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_District)),  
                                smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Region)),  
                                smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_PO_Box_Number)),  
                                smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Post_Office_Town)),  
                                smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Country_Code)),  
                                smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Period_At_Address)),  
                                smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Flag_of_Ownership)),  
                                #smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Primary_Number_Country_Dialling_Code)),  
                                smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Primary_Number_Telephone_Number)),  
                                #smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Other_Number_Country_Dialling_Code)),  
                                smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Other_Number_Telephone_Number)),  
                                #smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Mobile_Number_Country_Dialling_Code)),  
                                smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Mobile_Number_Telephone_Number)),  
                                #smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Facsimile_Country_Dialling_Code)),  
                                smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Facsimile_Number)), 
                                smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Email_Address)),  
                                smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Web_site)),  
                                smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Unit_Number)),  
                                smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Unit_Name)),  
                                smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Floor_Number)), 
                                smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Plot_or_Street_Number)),  
                                smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_LC_or_Street_Name)),  
                                smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Parish)),  
                                smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Suburb)),  
                                smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Village)),  
                                smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_County_or_Town)),  
                                smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_District)), 
                                smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Region)),  
                                smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_PO_Box_Number)),  
                                smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Post_Office_Town)),  
                                smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Country_Code)), 
                                smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Period_At_Address)),  
                                smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Flag_for_ownership)),  
                                #smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Primary_Number_Country_Dialling_Code)),  
                                smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Primary_Number_Telephone_Number)),  
                                #smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Other_Number_Country_Dialling_Code)),  
                                smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Other_Number_Telephone_Number)),  
                                #smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Mobile_Number_Country_Dialling_Code)),  
                                smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Mobile_Number_Telephone_Number)),  
                                #smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Facsimile_Country_Dialling_Code)),  
                                smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Facsimile_Number)),  
                                smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Email_Address)),
                                smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Web_site))
                            ])
            return self.response 
        except:
            raise 
            
class CSVFMDValidated(pivalidatecsv.CSVPIValidated):
    def __init__(self,filename, dialect, row, headers, delimiter="|",response=None):
        super(CSVFMDValidated, self).__init__(filename, dialect,delimiter, headers,response=response)
        
        self.delimiter = delimiter
        self.row = row 
   
    def write_row_data(self, coldata, val):
        try:
            
            #Validate the records
            self.validated_field = self.validate_and_return(val)
            
            self.pi_field = self.load_validated_field(self.validated_field.get("PI_Identification_Code"))
            self.cid_field = self.load_validated_field(self.validated_field.get("Branch_Identification_Code"))
            self.cn_field = self.load_validated_field(self.validated_field.get("Borrowers_Client_Number"))
            self.ccc_field = self.load_validated_field(self.validated_field.get("Consumer_Classification"))
            self.cc_field = self.load_validated_field(self.validated_field.get("Category_Code"))
            self.scc_field = self.load_validated_field(self.validated_field.get("Sub_Category_Code"))
            self.idd_field = self.load_validated_field(self.validated_field.get("Incident_Date"))
            self.la_field = self.load_validated_field(self.validated_field.get("Loss_Amount"))
            self.ct_field = self.load_validated_field(self.validated_field.get("Currency_Type"))
            self.id_field = self.load_validated_field(self.validated_field.get("Incident_Details"))
            self.fia_field = self.load_validated_field(self.validated_field.get("Forensic_Information_Available"))
            
            #PCI SCI
            #handle the pcivalidation
            self.pci_validation = pcivalidate.PCIValidate()
            self.sci_validation = scivalidate.SCIValidate()
            self.ii_validation = iivalidate.IIValidate()
            self.gs_validation = gsvalidate.GSValidate()
            self.ei_validation = eivalidate.EIValidate()
            
            self.sci_validation.begin_validation()
            self.pci_validation.begin_validation()
            self.ii_validation.begin_validation()
            self.gs_validation.begin_validation()
            self.ei_validation.begin_validation()
            
            self.validated_pci_dict = self.pci_validation.get_real_dict()
            self.validated_sci_dict = self.sci_validation.get_real_dict()
            self.validated_ii_dict = self.ii_validation.get_real_dict()
            self.validated_gs_dict = self.gs_validation.get_real_dict()
            self.validated_ei_dict = self.ei_validation.get_real_dict()
            
            self.II_Registration_Certificate_Number = self.load_validated_field(self.validated_ii_dict.get("II_Registration_Certificate_Number"))
            self.II_Tax_Identification_Number = self.load_validated_field(self.validated_ii_dict.get("II_Tax_Identification_Number"))
            self.II_Value_Added_Tax_Number = self.load_validated_field(self.validated_ii_dict.get("II_Value_Added_Tax_Number"))
            self.II_FCS_Number = self.load_validated_field(self.validated_ii_dict.get("II_FCS_Number"))
            self.II_Passport_Number = self.load_validated_field(self.validated_ii_dict.get("II_Passport_Number"))
            self.II_Drivers_Licence_ID_Number = self.load_validated_field(self.validated_ii_dict.get("II_Drivers_Licence_ID_Number"))
            self.II_Voters_PERNO = self.load_validated_field(self.validated_ii_dict.get("II_Voters_PERNO"))
            self.II_Drivers_License_Permit_Number = self.load_validated_field(self.validated_ii_dict.get("II_Drivers_License_Permit_Number"))
            self.II_NSSF_Number = self.load_validated_field(self.validated_ii_dict.get("II_NSSF_Number"))
            self.II_Country_ID = self.load_validated_field(self.validated_ii_dict.get("II_Country_ID"))
            self.II_Country_Issuing_Authority = self.load_validated_field(self.validated_ii_dict.get("II_Country_Issuing_Authority"))
            self.II_Nationality = self.load_validated_field(self.validated_ii_dict.get("II_Nationality"))
            self.II_Police_ID_Number = self.load_validated_field(self.validated_ii_dict.get("II_Police_ID_Number"))
            self.II_UPDF_Number = self.load_validated_field(self.validated_ii_dict.get("II_UPDF_Number"))
            self.II_KACITA_License_Number = self.load_validated_field(self.validated_ii_dict.get("II_KACITA_License_Number"))
            self.II_Public_Service_Pension_Number = self.load_validated_field(self.validated_ii_dict.get("II_Public_Service_Pension_Number"))
            self.II_Teacher_Registration_Number = self.load_validated_field(self.validated_ii_dict.get("II_Teacher_Registration_Number"))
            self.II_Country_Of_Issue = self.load_validated_field(self.validated_ii_dict.get("II_Country_Of_Issue"))
            
            self.GSCAFB_Business_Name = self.load_validated_field(self.validated_gs_dict.get("GSCAFB_Business_Name"))
            self.GSCAFB_Trading_Name = self.load_validated_field(self.validated_gs_dict.get("GSCAFB_Trading_Name"))
            self.GSCAFB_Activity_Description = self.load_validated_field(self.validated_gs_dict.get("GSCAFB_Activity_Description"))
            self.GSCAFB_Industry_Sector_Code = self.load_validated_field(self.validated_gs_dict.get("GSCAFB_Industry_Sector_Code"))
            self.GSCAFB_Date_Registered = self.load_validated_field(self.validated_gs_dict.get("GSCAFB_Date_Registered"))
            self.GSCAFB_Business_Type_Code = self.load_validated_field(self.validated_gs_dict.get("GSCAFB_Business_Type_Code"))
            self.GSCAFB_Surname = self.load_validated_field(self.validated_gs_dict.get("GSCAFB_Surname"))
            self.GSCAFB_Forename1 = self.load_validated_field(self.validated_gs_dict.get("GSCAFB_Forename1"))
            self.GSCAFB_Forename2 = self.load_validated_field(self.validated_gs_dict.get("GSCAFB_Forename2"))
            self.GSCAFB_Forename3 = self.load_validated_field(self.validated_gs_dict.get("GSCAFB_Forename3"))
            self.GSCAFB_Gender = self.load_validated_field(self.validated_gs_dict.get("GSCAFB_Gender"))
            self.GSCAFB_Marital_Status = self.load_validated_field(self.validated_gs_dict.get("GSCAFB_Marital_Status"))
            self.GSCAFB_Date_of_Birth = self.load_validated_field(self.validated_gs_dict.get("GSCAFB_Date_of_Birth"))
            
            self.EI_Employment_Type = self.load_validated_field(self.validated_ei_dict.get("EI_Employment_Type"))
            self.EI_Primary_Occupation = self.load_validated_field(self.validated_ei_dict.get("EI_Primary_Occupation"))
            self.EI_Employer_Name = self.load_validated_field(self.validated_ei_dict.get("EI_Employer_Name"))
            self.EI_Employee_Number = self.load_validated_field(self.validated_ei_dict.get("EI_Employee_Number"))
            self.EI_Employment_Date = self.load_validated_field(self.validated_ei_dict.get("EI_Employment_Date"))
            self.EI_Income_Band = self.load_validated_field(self.validated_ei_dict.get("EI_Income_Band"))
            self.EI_Salary_Frequency = self.load_validated_field(self.validated_ei_dict.get("EI_Salary_Frequency"))
            
            self.PCI_Building_Unit_Number =  self.load_validated_field(self.validated_pci_dict.get("PCI_Building_Unit_Number"))
            self.PCI_Building_Name =  self.load_validated_field(self.validated_pci_dict.get("PCI_Building_Name"))
            self.PCI_Floor_Number =  self.load_validated_field(self.validated_pci_dict.get("PCI_Floor_Number"))
            self.PCI_Plot_or_Street_Number =  self.load_validated_field(self.validated_pci_dict.get("PCI_Plot_or_Street_Number"))
            self.PCI_LC_or_Street_Name =  self.load_validated_field(self.validated_pci_dict.get("PCI_LC_or_Street_Name"))
            self.PCI_Parish =  self.load_validated_field(self.validated_pci_dict.get("PCI_Parish"))
            self.PCI_Suburb =  self.load_validated_field(self.validated_pci_dict.get("PCI_Suburb"))
            self.PCI_Village =  self.load_validated_field(self.validated_pci_dict.get("PCI_Village"))
            self.PCI_County_or_Town =  self.load_validated_field(self.validated_pci_dict.get("PCI_County_or_Town"))
            self.PCI_District =  self.load_validated_field(self.validated_pci_dict.get("PCI_District"))
            self.PCI_Region =  self.load_validated_field(self.validated_pci_dict.get("PCI_Region"))
            self.PCI_PO_Box_Number =  self.load_validated_field(self.validated_pci_dict.get("PCI_PO_Box_Number"))
            self.PCI_Post_Office_Town =  self.load_validated_field(self.validated_pci_dict.get("PCI_Post_Office_Town"))
            self.PCI_Country_Code =  self.load_validated_field(self.validated_pci_dict.get("PCI_Country_Code"))
            self.PCI_Period_At_Address =  self.load_validated_field(self.validated_pci_dict.get("PCI_Period_At_Address"))
            self.PCI_Flag_of_Ownership =  self.load_validated_field(self.validated_pci_dict.get("PCI_Flag_of_Ownership"))
            #self.PCI_Primary_Number_Country_Dialling_Code =  self.load_validated_field(self.validated_pci_dict.get("PCI_Primary_Number_Country_Dialling_Code"))
            self.PCI_Primary_Number_Telephone_Number =  self.load_validated_field(self.validated_pci_dict.get("PCI_Primary_Number_Telephone_Number"))
            #self.PCI_Other_Number_Country_Dialling_Code =  self.load_validated_field(self.validated_pci_dict.get("PCI_Other_Number_Country_Dialling_Code"))
            self.PCI_Other_Number_Telephone_Number = self.load_validated_field(self.validated_pci_dict.get("PCI_Other_Number_Telephone_Number"))
            #self.PCI_Mobile_Number_Country_Dialling_Code =  self.load_validated_field(self.validated_pci_dict.get("PCI_Mobile_Number_Country_Dialling_Code"))
            self.PCI_Mobile_Number_Telephone_Number =  self.load_validated_field(self.validated_pci_dict.get("PCI_Mobile_Number_Telephone_Number"))
            #self.PCI_Facsimile_Country_Dialling_Code =  self.load_validated_field(self.validated_pci_dict.get("PCI_Facsimile_Country_Dialling_Code"))
            self.PCI_Facsimile_Number =  self.load_validated_field(self.validated_pci_dict.get("PCI_Facsimile_Number"))
            self.PCI_Email_Address =  self.load_validated_field(self.validated_pci_dict.get("PCI_Email_Address"))
            self.PCI_Web_site =  self.load_validated_field(self.validated_pci_dict.get("PCI_Web_site"))
            
            #self.PCI_Web_site =  self.load_validated_field(self.validated_pci_dict.get("PCI_Web_site"))
            
            self.SCI_Unit_Number =  self.load_validated_field(self.validated_sci_dict.get("SCI_Unit_Number"))
            self.SCI_Unit_Name =  self.load_validated_field(self.validated_sci_dict.get("SCI_Unit_Name"))
            self.SCI_Floor_Number =  self.load_validated_field(self.validated_sci_dict.get("SCI_Floor_Number"))
            self.SCI_Plot_or_Street_Number =  self.load_validated_field(self.validated_sci_dict.get("SCI_Plot_or_Street_Number"))
            self.SCI_LC_or_Street_Name =  self.load_validated_field(self.validated_sci_dict.get("SCI_LC_or_Street_Name"))
            self.SCI_Parish =  self.load_validated_field(self.validated_sci_dict.get("SCI_Parish"))
            self.SCI_Suburb =  self.load_validated_field(self.validated_sci_dict.get("SCI_Suburb"))
            self.SCI_Village =  self.load_validated_field(self.validated_sci_dict.get("SCI_Village"))
            self.SCI_County_or_Town =  self.load_validated_field(self.validated_sci_dict.get("SCI_County_or_Town"))
            self.SCI_District =  self.load_validated_field(self.validated_sci_dict.get("SCI_District"))
            self.SCI_Region =  self.load_validated_field(self.validated_sci_dict.get("SCI_Region"))
            self.SCI_PO_Box_Number =  self.load_validated_field(self.validated_sci_dict.get("SCI_PO_Box_Number"))
            self.SCI_Post_Office_Town =  self.load_validated_field(self.validated_sci_dict.get("SCI_Post_Office_Town"))
            self.SCI_Country_Code =  self.load_validated_field(self.validated_sci_dict.get("SCI_Country_Code"))
            self.SCI_Period_At_Address =  self.load_validated_field(self.validated_sci_dict.get("SCI_Period_At_Address"))
            self.SCI_Flag_of_Ownership =  self.load_validated_field(self.validated_sci_dict.get("SCI_Flag_for_ownership"))
            #self.SCI_Primary_Number_Country_Dialling_Code =  self.load_validated_field(self.validated_sci_dict.get("SCI_Primary_Number_Country_Dialling_Code"))
            self.SCI_Primary_Number_Telephone_Number =  self.load_validated_field(self.validated_sci_dict.get("SCI_Primary_Number_Telephone_Number"))
            #self.SCI_Other_Number_Country_Dialling_Code =  self.load_validated_field(self.validated_sci_dict.get("SCI_Other_Number_Country_Dialling_Code"))
            self.SCI_Other_Number_Telephone_Number = self.load_validated_field(self.validated_sci_dict.get("SCI_Other_Number_Telephone_Number"))
            #self.SCI_Mobile_Number_Country_Dialling_Code =  self.load_validated_field(self.validated_sci_dict.get("SCI_Mobile_Number_Country_Dialling_Code"))
            self.SCI_Mobile_Number_Telephone_Number =  self.load_validated_field(self.validated_sci_dict.get("SCI_Mobile_Number_Telephone_Number"))
            #self.SCI_Facsimile_Country_Dialling_Code =  self.load_validated_field(self.validated_sci_dict.get("SCI_Facsimile_Country_Dialling_Code"))
            self.SCI_Facsimile_Number =  self.load_validated_field(self.validated_sci_dict.get("SCI_Facsimile_Number"))
            self.SCI_Email_Address =  self.load_validated_field(self.validated_sci_dict.get("SCI_Email_Address"))
            self.SCI_Web_site =  self.load_validated_field(self.validated_sci_dict.get("SCI_Web_site"))
            
            for data in coldata:
                self.writer.writerow([
                                self.get_data_id(),
                                self.value_in(smart_str(unicode(data.PI_Identification_Code.pi_identification_code)), self.pi_field),
                                self.value_in(smart_str(unicode(data.Branch_Identification_Code.branch_code)),self.cid_field),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.Client_Number)),self.cn_field),
                                self.value_in(smart_str(unicode(data.Consumer_Classification)),self.ccc_field),
                                self.value_in(smart_str(unicode(data.Category_Code)),self.cc_field),
                                self.value_in(smart_str(unicode(data.Sub_Category_Code)),self.scc_field),
                                self.value_in(smart_str(unicode(data.Incident_Date)),self.idd_field),
                                self.value_in(smart_str(unicode(data.Loss_Amount)),self.la_field),
                                self.value_in(smart_str(unicode(data.Currency_Type)),self.ct_field),
                                self.value_in(smart_str(unicode(data.Incident_Details)),self.id_field),
                                self.value_in(smart_str(unicode(data.Forensic_Information_Available)),self.fia_field),
                                
                                #II
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.idi.II_Registration_Certificate_Number)),self.II_Registration_Certificate_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.idi.II_Tax_Identification_Number)),self.II_Tax_Identification_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.idi.II_Value_Added_Tax_Number)),self.II_Value_Added_Tax_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.idi.II_FCS_Number)),self.II_FCS_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.idi.II_Passport_Number)),self.II_Passport_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.idi.II_Drivers_Licence_ID_Number)),self.II_Drivers_Licence_ID_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.idi.II_Voters_PERNO)),self.II_Voters_PERNO),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.idi.II_Drivers_License_Permit_Number)),self.II_Drivers_License_Permit_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.idi.II_NSSF_Number)),self.II_NSSF_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.idi.II_Country_ID)),self.II_Country_ID),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.idi.II_Country_Issuing_Authority)),self.II_Country_Issuing_Authority),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.idi.II_Nationality)),self.II_Nationality),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.idi.II_Police_ID_Number)),self.II_Police_ID_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.idi.II_UPDF_Number)),self.II_UPDF_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.idi.II_KACITA_License_Number)),self.II_KACITA_License_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.idi.II_Public_Service_Pension_Number)),self.II_Public_Service_Pension_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.idi.II_Teacher_Registration_Number)),self.II_Teacher_Registration_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.idi.II_Country_Of_Issue)),self.II_Country_Of_Issue),
                                
                                #GS
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Business_Name)),self.GSCAFB_Business_Name),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Trading_Name)),self.GSCAFB_Trading_Name),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Activity_Description)),self.GSCAFB_Activity_Description),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Industry_Sector_Code)),self.GSCAFB_Industry_Sector_Code),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Date_Registered)),self.GSCAFB_Date_Registered),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Business_Type_Code)),self.GSCAFB_Business_Type_Code),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Surname)),self.GSCAFB_Surname),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Forename1)),self.GSCAFB_Forename1),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Forename2)),self.GSCAFB_Forename2),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Forename3)),self.GSCAFB_Forename3),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Gender)),self.GSCAFB_Gender),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Marital_Status)),self.GSCAFB_Marital_Status),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.gscafb.GSCAFB_Date_of_Birth)),self.GSCAFB_Date_of_Birth),
                                
                                #EI
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.ei.EI_Employment_Type)),self.EI_Employment_Type),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.ei.EI_Primary_Occupation)),self.EI_Primary_Occupation),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.ei.EI_Employer_Name)),self.EI_Employer_Name),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.ei.EI_Employee_Number)),self.EI_Employee_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.ei.EI_Employment_Date)),self.EI_Employment_Date),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.ei.EI_Income_Band)),self.EI_Income_Band),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.ei.EI_Salary_Frequency)),self.EI_Salary_Frequency),
                                #PCIINFOR
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Building_Unit_Number)), self.PCI_Building_Unit_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Building_Name)), self.PCI_Building_Name),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Floor_Number)), self.PCI_Floor_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Plot_or_Street_Number)), self.PCI_Plot_or_Street_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_LC_or_Street_Name)), self.PCI_LC_or_Street_Name),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Parish)), self.PCI_Parish),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Suburb)), self.PCI_Suburb),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Village)), self.PCI_Village),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_County_or_Town)), self.PCI_County_or_Town),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_District)), self.PCI_District),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Region)), self.PCI_Region),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_PO_Box_Number)), self.PCI_PO_Box_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Post_Office_Town)), self.PCI_Post_Office_Town),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Country_Code)), self.PCI_Country_Code),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Period_At_Address)), self.PCI_Period_At_Address),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Flag_of_Ownership)), self.PCI_Flag_of_Ownership),
                                #self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Primary_Number_Country_Dialling_Code)), self.PCI_Primary_Number_Country_Dialling_Code),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Primary_Number_Telephone_Number)), self.PCI_Primary_Number_Telephone_Number),
                                #self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Other_Number_Country_Dialling_Code)), self.PCI_Other_Number_Country_Dialling_Code),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Other_Number_Telephone_Number)), self.PCI_Other_Number_Telephone_Number),
                                #self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Mobile_Number_Country_Dialling_Code)), self.PCI_Mobile_Number_Country_Dialling_Code),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Mobile_Number_Telephone_Number)), self.PCI_Mobile_Number_Telephone_Number),
                                #self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Facsimile_Country_Dialling_Code)), self.PCI_Facsimile_Country_Dialling_Code),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Facsimile_Number)), self.PCI_Facsimile_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Email_Address)), self.PCI_Email_Address),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.pci.PCI_Web_site)), self.PCI_Web_site),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Unit_Number)), self.SCI_Unit_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Unit_Name)), self.SCI_Unit_Name),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Floor_Number)), self.SCI_Floor_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Plot_or_Street_Number)), self.SCI_Plot_or_Street_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_LC_or_Street_Name)), self.SCI_LC_or_Street_Name),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Parish)), self.SCI_Parish),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Suburb)), self.SCI_Suburb),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Village)), self.SCI_Village),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_County_or_Town)), self.SCI_County_or_Town),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_District)), self.SCI_District),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Region)), self.SCI_Region),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_PO_Box_Number)), self.SCI_PO_Box_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Post_Office_Town)), self.SCI_Post_Office_Town),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Country_Code)), self.SCI_Country_Code),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Period_At_Address)), self.SCI_Period_At_Address),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Flag_for_ownership)), self.SCI_Flag_of_Ownership),
                                #self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Primary_Number_Country_Dialling_Code)), self.SCI_Primary_Number_Country_Dialling_Code),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Primary_Number_Telephone_Number)), self.SCI_Primary_Number_Telephone_Number),
                                #self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Other_Number_Country_Dialling_Code)), self.SCI_Other_Number_Country_Dialling_Code),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Other_Number_Telephone_Number)), self.SCI_Other_Number_Telephone_Number),
                                #self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Mobile_Number_Country_Dialling_Code)), self.SCI_Mobile_Number_Country_Dialling_Code),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Mobile_Number_Telephone_Number)), self.SCI_Mobile_Number_Telephone_Number),
                                #self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Facsimile_Country_Dialling_Code)), self.SCI_Facsimile_Country_Dialling_Code),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Facsimile_Number)), self.SCI_Facsimile_Number),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Email_Address)), self.SCI_Email_Address),
                                self.value_in(smart_str(unicode(data.Borrowers_Client_Number.sci.SCI_Web_site)), self.SCI_Web_site)
                        ])
            return self.response 
        except Exception as e:
            pass 
