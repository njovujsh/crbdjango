#  capcsv.py
#  
#  Copyright 2015 Wangolo Joel <wangolo@developer>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import csv
from django.http import HttpResponse
from django.utils.encoding import smart_str
from validators.subsystems.csvwriters import processcsvs
from validators.subsystems.csvwriters import pivalidatecsv
from validators.subsystems.datasets import validationstatus 
from validators.subsystems.datasets import pcivalidate 
from validators.subsystems.datasets import scivalidate
from validators.subsystems.datasets import gsvalidate
from validators.subsystems.datasets import eivalidate
from validators.subsystems.datasets import iivalidate

class ProcessCSVCAP(processcsvs.ProcessCSV):
    def __init__(self, filename, dialect, row, headers, delimiter="|",response=None):
        super(ProcessCSVCAP, self).__init__(filename, dialect,response=response)
        
        self.delimiter = delimiter
        self.row = row 
        
        if(headers):
            self.write_headers(headers)
            
    def write_row_data(self, coldata):
        try:
            for data in coldata:
                #print "SCI_District ", data.SCI_District
                self.writer.writerow([
                                self.get_data_id(),
                                smart_str(unicode(data.PI_Identification_Code.pi_identification_code)),
                                smart_str(unicode(data.Branch_Identification_Code.branch_code)),
                                smart_str(unicode(data.Client_Number)),
                                smart_str(unicode(data.Credit_Application_Reference.replace("-", "", 80).replace(":", "",82))),
                                smart_str(unicode(data.Applicant_Classification)),
                                smart_str(unicode(data.Credit_Application_Date)),
                                smart_str(unicode(data.Amount)),
                                smart_str(unicode(data.Currency)),
                                smart_str(unicode(data.Credit_Account_or_Loan_Product_Type)),
                                smart_str(unicode(data.Credit_Application_Status)),
                                smart_str(unicode(data.Last_Status_Change_Date)),
                                smart_str(unicode(data.Credit_Application_Duration)),
                                smart_str(unicode(data.Rejection_Reason)),
                                smart_str(unicode(data.Client_Consent_flag)),
                                smart_str(unicode(data.idi.II_Registration_Certificate_Number)),
                                smart_str(unicode(data.idi.II_Tax_Identification_Number)), 
                                smart_str(unicode(data.idi.II_Value_Added_Tax_Number)), 
                                smart_str(unicode(data.idi.II_FCS_Number)), 
                                smart_str(unicode(data.idi.II_Passport_Number)), 
                                smart_str(unicode(data.idi.II_Drivers_Licence_ID_Number)), 
                                smart_str(unicode(data.idi.II_Voters_PERNO)),
                                smart_str(unicode(data.idi.II_Drivers_License_Permit_Number)), 
                                smart_str(unicode(data.idi.II_NSSF_Number)),
                                smart_str(unicode(data.idi.II_Country_ID)), 
                                smart_str(unicode(data.idi.II_Country_Issuing_Authority)), 
                                smart_str(unicode(data.idi.II_Nationality)), 
                                smart_str(unicode(data.idi.II_Police_ID_Number)),
                                smart_str(unicode(data.idi.II_UPDF_Number)), 
                                smart_str(unicode(data.idi.II_KACITA_License_Number)), 
                                smart_str(unicode(data.idi.II_Public_Service_Pension_Number)), 
                                smart_str(unicode(data.idi.II_Teacher_Registration_Number)), 
                                smart_str(unicode(data.idi.II_Country_Of_Issue)),
                                smart_str(unicode(data.gscafb.GSCAFB_Business_Name)), 
                                smart_str(unicode(data.gscafb.GSCAFB_Trading_Name)),
                                smart_str(unicode(data.gscafb.GSCAFB_Activity_Description)), 
                                smart_str(unicode(data.gscafb.GSCAFB_Industry_Sector_Code)), 
                                smart_str(unicode(data.gscafb.GSCAFB_Date_Registered)), 
                                smart_str(unicode(data.gscafb.GSCAFB_Business_Type_Code)), 
                                smart_str(unicode(data.gscafb.GSCAFB_Surname)), 
                                smart_str(unicode(data.gscafb.GSCAFB_Forename1)), 
                                smart_str(unicode(data.gscafb.GSCAFB_Forename2)), 
                                smart_str(unicode(data.gscafb.GSCAFB_Forename3)), 
                                smart_str(unicode(data.gscafb.GSCAFB_Gender)), 
                                smart_str(unicode(data.gscafb.GSCAFB_Marital_Status)), 
                                smart_str(unicode(data.gscafb.GSCAFB_Date_of_Birth)),
                                smart_str(unicode(data.ei.EI_Employment_Type)), 
                                smart_str(unicode(data.ei.EI_Primary_Occupation)),
                                smart_str(unicode(data.ei.EI_Employer_Name)),
                                smart_str(unicode(data.ei.EI_Employee_Number)),
                                smart_str(unicode(data.ei.EI_Employment_Date)), 
                                smart_str(unicode(data.ei.EI_Income_Band)),
                                smart_str(unicode(data.ei.EI_Salary_Frequency)),
                                smart_str(unicode(data.pci.PCI_Building_Unit_Number)),
                                smart_str(unicode(data.pci.PCI_Building_Name)),  
                                smart_str(unicode(data.pci.PCI_Floor_Number)),  
                                smart_str(unicode(data.pci.PCI_Plot_or_Street_Number)),  
                                smart_str(unicode(data.pci.PCI_LC_or_Street_Name)),  
                                smart_str(unicode(data.pci.PCI_Region)),
                                smart_str(unicode(data.pci.PCI_District)),
                                smart_str(unicode(data.pci.PCI_County_or_Town)),
                                smart_str(unicode(data.pci.PCI_Parish)),  
                                smart_str(unicode(data.pci.PCI_Suburb)), 
                                smart_str(unicode(data.pci.PCI_Village)),
                                smart_str(unicode(data.pci.PCI_PO_Box_Number)),  
                                smart_str(unicode(data.pci.PCI_Post_Office_Town)),  
                                smart_str(unicode(data.pci.PCI_Country_Code)),  
                                smart_str(unicode(data.pci.PCI_Period_At_Address)),  
                                smart_str(unicode(data.pci.PCI_Flag_of_Ownership)),  
                                smart_str(unicode(data.pci.PCI_Primary_Number_Telephone_Number)),  
                                smart_str(unicode(data.pci.PCI_Other_Number_Telephone_Number)),  
                                smart_str(unicode(data.pci.PCI_Mobile_Number_Telephone_Number)),  
                                smart_str(unicode(data.pci.PCI_Facsimile_Number)), 
                                smart_str(unicode(data.pci.PCI_Email_Address)),  
                                smart_str(unicode(data.pci.PCI_Web_site)),  
                                smart_str(unicode(data.sci.SCI_Unit_Number)),  
                                smart_str(unicode(data.sci.SCI_Unit_Name)),  
                                smart_str(unicode(data.sci.SCI_Floor_Number)), 
                                smart_str(unicode(data.sci.SCI_Plot_or_Street_Number)),  
                                smart_str(unicode(data.sci.SCI_LC_or_Street_Name)),  
                                smart_str(unicode(data.sci.SCI_Region)),
                                smart_str(unicode(data.sci.SCI_District)),
                                smart_str(unicode(data.sci.SCI_County_or_Town)),
                                smart_str(unicode(data.sci.SCI_Parish)),  
                                smart_str(unicode(data.sci.SCI_Suburb)),  
                                smart_str(unicode(data.sci.SCI_Village)),
                                smart_str(unicode(data.sci.SCI_PO_Box_Number)),  
                                smart_str(unicode(data.sci.SCI_Post_Office_Town)),  
                                smart_str(unicode(data.sci.SCI_Country_Code)), 
                                smart_str(unicode(data.sci.SCI_Period_At_Address)),  
                                smart_str(unicode(data.sci.SCI_Flag_for_ownership)),  
                                smart_str(unicode(data.sci.SCI_Primary_Number_Telephone_Number)),  
                                smart_str(unicode(data.sci.SCI_Other_Number_Telephone_Number)),  
                                smart_str(unicode(data.sci.SCI_Mobile_Number_Telephone_Number)),  
                                smart_str(unicode(data.sci.SCI_Facsimile_Number)),  
                                smart_str(unicode(data.sci.SCI_Email_Address)),
                                smart_str(unicode(data.sci.SCI_Web_site)),
                            ])
            return self.response 
        except:
            raise 
            
class CSVCAPValidated(pivalidatecsv.CSVPIValidated):
    def __init__(self,filename, dialect, row, headers, delimiter="|",response=None):
        super(CSVCAPValidated, self).__init__(filename, dialect, delimiter, headers,response=response)
        
        self.delimiter = delimiter
        self.row = row 
        
    def write_row_data(self, coldata, val):
        try:
            
            self.validated_field = self.validate_and_return(val)
            
            self.pi_field = self.load_validated_field(self.validated_field.get("PI_Identification_Code"))
            self.bic_field = self.load_validated_field(self.validated_field.get("Branch_Identification_Code"))
            self.cn_field = self.load_validated_field(self.validated_field.get("Client_Number"))
            self.car_field = self.load_validated_field(self.validated_field.get("Credit_Application_Reference"))
            self.clean_field = []
            for field in self.car_field:
                if(field):
                    self.clean_field.append(str(field).replace("-", "", 80).replace(":", "", 90))
                else:
                    self.clean_field.append(field)
                        
            self.ac_field = self.load_validated_field(self.validated_field.get("Applicant_Classification"))
            self.cad_field = self.load_validated_field(self.validated_field.get("Credit_Application_Date"))
            self.amount_field = self.load_validated_field(self.validated_field.get("Amount"))
            self.currency_field = self.load_validated_field(self.validated_field.get("Currency"))
            self.loan_field = self.load_validated_field(self.validated_field.get("Credit_Account_or_Loan_Product_Type"))
            self.cas_field = self.load_validated_field(self.validated_field.get("Credit_Application_Status"))
            self.lastdate_field = self.load_validated_field(self.validated_field.get("Last_Status_Change_Date"))
            self.duration_field = self.load_validated_field(self.validated_field.get("Credit_Application_Duration"))
            self.rejection_field = self.load_validated_field(self.validated_field.get("Rejection_Reason"))
            self.consent_field = self.load_validated_field(self.validated_field.get("Client_Consent_flag"))
            #print "DATE ", self.lastdate_field
            
            #handle the pcivalidation
            self.pci_validation = pcivalidate.PCIValidate()
            self.sci_validation = scivalidate.SCIValidate()
            
            self.sci_validation.begin_validation()
            self.pci_validation.begin_validation()
            self.validated_pci_dict = self.pci_validation.get_real_dict()
            self.validated_sci_dict = self.sci_validation.get_real_dict()
            
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
            
            #Validate GS, II, EI
            self.gs_validate = gsvalidate.GSValidate()
            self.ii_validate = iivalidate.IIValidate()
            self.ei_validate = eivalidate.EIValidate()
            
            #Call there validation functions
            self.gs_validate.begin_validation()
            self.ii_validate.begin_validation()
            self.ei_validate.begin_validation()
            
            #Get the validated records
            self.gs_validated = self.gs_validate.get_real_dict()
            self.ii_validated = self.ii_validate.get_real_dict()
            self.ei_validated = self.ei_validate.get_real_dict()
            
            #Get the records of GS
            self.EI_Employment_Type = self.load_validated_field(self.ei_validated.get("EI_Employment_Type"))
            self.EI_Primary_Occupation = self.load_validated_field(self.ei_validated.get("EI_Primary_Occupation"))
            self.EI_Employer_Name = self.load_validated_field(self.ei_validated.get("EI_Employer_Name"))
            self.EI_Employee_Number = self.load_validated_field(self.ei_validated.get("EI_Employee_Number"))
            self.EI_Employment_Date = self.load_validated_field(self.ei_validated.get("EI_Employment_Date"))
            self.EI_Income_Band = self.load_validated_field(self.ei_validated.get("EI_Income_Band"))
            self.EI_Salary_Frequency = self.load_validated_field(self.ei_validated.get("EI_Salary_Frequency"))
            
            #Get the records of II
            self.II_Registration_Certificate_Number = self.load_validated_field(self.ii_validated.get("II_Registration_Certificate_Number"))
            self.II_Tax_Identification_Number = self.load_validated_field(self.ii_validated.get("II_Tax_Identification_Number"))
            self.II_Value_Added_Tax_Number = self.load_validated_field(self.ii_validated.get("II_Value_Added_Tax_Number"))
            self.II_FCS_Number = self.load_validated_field(self.ii_validated.get("II_FCS_Number"))
            self.II_Passport_Number = self.load_validated_field(self.ii_validated.get("II_Passport_Number"))
            self.II_Drivers_Licence_ID_Number = self.load_validated_field(self.ii_validated.get("II_Drivers_Licence_ID_Number"))
            self.II_Voters_PERNO = self.load_validated_field(self.ii_validated.get("II_Voters_PERNO"))
            self.II_Drivers_License_Permit_Number = self.load_validated_field(self.ii_validated.get("II_Drivers_License_Permit_Number"))
            self.II_NSSF_Number = self.load_validated_field(self.ii_validated.get("II_NSSF_Number"))
            self.II_Country_ID = self.load_validated_field(self.ii_validated.get("II_Country_ID"))
            self.II_Country_Issuing_Authority = self.load_validated_field(self.ii_validated.get("II_Country_Issuing_Authority"))
            self.II_Nationality = self.load_validated_field(self.ii_validated.get("II_Nationality"))
            self.II_Police_ID_Number = self.load_validated_field(self.ii_validated.get("II_Police_ID_Number"))
            self.II_UPDF_Number = self.load_validated_field(self.ii_validated.get("II_UPDF_Number"))
            self.II_KACITA_License_Number = self.load_validated_field(self.ii_validated.get("II_KACITA_License_Number"))
            self.II_Public_Service_Pension_Number = self.load_validated_field(self.ii_validated.get("II_Public_Service_Pension_Number"))
            self.II_Teacher_Registration_Number = self.load_validated_field(self.ii_validated.get("II_Teacher_Registration_Number"))
            self.II_Country_Of_Issue = self.load_validated_field(self.ii_validated.get("II_Country_Of_Issue"))
            
            #Get the Records of GS
            self.GSCAFB_Business_Name = self.load_validated_field(self.gs_validated.get("GSCAFB_Business_Name"))
            self.GSCAFB_Trading_Name = self.load_validated_field(self.gs_validated.get("GSCAFB_Trading_Name"))
            self.GSCAFB_Activity_Description = self.load_validated_field(self.gs_validated.get("GSCAFB_Activity_Description"))
            self.GSCAFB_Industry_Sector_Code = self.load_validated_field(self.gs_validated.get("GSCAFB_Industry_Sector_Code"))
            self.GSCAFB_Date_Registered = self.load_validated_field(self.gs_validated.get("GSCAFB_Date_Registered"))
            self.GSCAFB_Business_Type_Code = self.load_validated_field(self.gs_validated.get("GSCAFB_Business_Type_Code"))
            self.GSCAFB_Surname = self.load_validated_field(self.gs_validated.get("GSCAFB_Surname"))
            self.GSCAFB_Forename1 = self.load_validated_field(self.gs_validated.get("GSCAFB_Forename1"))
            self.GSCAFB_Forename2 = self.load_validated_field(self.gs_validated.get("GSCAFB_Forename2"))
            self.GSCAFB_Forename3 = self.load_validated_field(self.gs_validated.get("GSCAFB_Forename3"))
            self.GSCAFB_Gender = self.load_validated_field(self.gs_validated.get("GSCAFB_Gender"))
            self.GSCAFB_Marital_Status = self.load_validated_field(self.gs_validated.get("GSCAFB_Marital_Status"))
            self.GSCAFB_Date_of_Birth = self.load_validated_field(self.gs_validated.get("GSCAFB_Date_of_Birth"))
            
            for data in coldata:                
                self.writer.writerow([
                            self.get_data_id(),
                            self.value_in(smart_str(unicode(data.PI_Identification_Code.pi_identification_code)), self.pi_field),
                            self.value_in(smart_str(unicode(data.Branch_Identification_Code.branch_code)), self.bic_field),
                            self.value_in(smart_str(unicode(data.Client_Number)), self.cn_field),
                            self.value_in(smart_str(unicode(data.Credit_Application_Reference.replace("-", "",90).replace(":", "",95))), self.clean_field),
                            self.value_in(smart_str(unicode(data.Applicant_Classification)), self.ac_field),
                            self.value_in(smart_str(unicode(data.Credit_Application_Date)), self.cad_field),
                            self.value_in(smart_str(unicode(data.Amount)), self.amount_field),
                            self.value_in(smart_str(unicode(data.Currency)), self.currency_field),
                            self.value_in(smart_str(unicode(data.Credit_Account_or_Loan_Product_Type)), self.loan_field),
                            self.value_in(smart_str(unicode(data.Credit_Application_Status)), self.cas_field),
                            self.value_in(smart_str(unicode(str(data.Last_Status_Change_Date).replace("-", "", 50))), self.lastdate_field),
                            self.value_in(smart_str(unicode(data.Credit_Application_Duration)), self.duration_field),
                            self.value_in(smart_str(unicode(data.Rejection_Reason)), self.rejection_field),
                            self.value_in(smart_str(unicode(data.Client_Consent_flag)), self.consent_field),
                            
                            #II
                            self.value_in(smart_str(unicode(data.idi.II_Registration_Certificate_Number)), self.II_Registration_Certificate_Number),
                            self.value_in(smart_str(unicode(data.idi.II_Tax_Identification_Number)), self.II_Tax_Identification_Number),
                            self.value_in(smart_str(unicode(data.idi.II_Value_Added_Tax_Number)), self.II_Value_Added_Tax_Number),
                            self.value_in(smart_str(unicode(data.idi.II_FCS_Number)), self.II_FCS_Number),
                            self.value_in(smart_str(unicode(data.idi.II_Passport_Number)), self.II_Passport_Number),
                            self.value_in(smart_str(unicode(data.idi.II_Drivers_Licence_ID_Number)), self.II_Drivers_Licence_ID_Number),
                            self.value_in(smart_str(unicode(data.idi.II_Voters_PERNO)), self.II_Voters_PERNO),
                            self.value_in(smart_str(unicode(data.idi.II_Drivers_License_Permit_Number)), self.II_Drivers_License_Permit_Number),
                            self.value_in(smart_str(unicode(data.idi.II_NSSF_Number)), self.II_NSSF_Number),
                            self.value_in(smart_str(unicode(data.idi.II_Country_ID)), self.II_Country_ID),
                            self.value_in(smart_str(unicode(data.idi.II_Country_Issuing_Authority)), self.II_Country_Issuing_Authority),
                            self.value_in(smart_str(unicode(data.idi.II_Nationality)), self.II_Nationality),
                            self.value_in(smart_str(unicode(data.idi.II_Police_ID_Number)), self.II_Police_ID_Number),
                            self.value_in(smart_str(unicode(data.idi.II_UPDF_Number)), self.II_UPDF_Number),
                            self.value_in(smart_str(unicode(data.idi.II_KACITA_License_Number)), self.II_KACITA_License_Number),
                            self.value_in(smart_str(unicode(data.idi.II_Public_Service_Pension_Number)), self.II_Public_Service_Pension_Number),
                            self.value_in(smart_str(unicode(data.idi.II_Teacher_Registration_Number)), self.II_Teacher_Registration_Number),
                            self.value_in(smart_str(unicode(data.idi.II_Country_Of_Issue)), self.II_Country_Of_Issue),
                            
                            #GS
                            self.value_in(smart_str(unicode(data.gscafb.GSCAFB_Business_Name)), self.GSCAFB_Business_Name),
                            self.value_in(smart_str(unicode(data.gscafb.GSCAFB_Trading_Name)), self.GSCAFB_Trading_Name),
                            self.value_in(smart_str(unicode(data.gscafb.GSCAFB_Activity_Description)), self.GSCAFB_Activity_Description),
                            self.value_in(smart_str(unicode(data.gscafb.GSCAFB_Industry_Sector_Code)), self.GSCAFB_Industry_Sector_Code),
                            self.value_in(smart_str(unicode(data.gscafb.GSCAFB_Date_Registered)), self.GSCAFB_Date_Registered),
                            self.value_in(smart_str(unicode(data.gscafb.GSCAFB_Business_Type_Code)), self.GSCAFB_Business_Type_Code),
                            self.value_in(smart_str(unicode(data.gscafb.GSCAFB_Surname)), self.GSCAFB_Surname),
                            self.value_in(smart_str(unicode(data.gscafb.GSCAFB_Forename1)), self.GSCAFB_Forename1),
                            self.value_in(smart_str(unicode(data.gscafb.GSCAFB_Forename2)), self.GSCAFB_Forename2),
                            self.value_in(smart_str(unicode(data.gscafb.GSCAFB_Forename3)), self.GSCAFB_Forename3),
                            self.value_in(smart_str(unicode(data.gscafb.GSCAFB_Gender)), self.GSCAFB_Gender),
                            self.value_in(smart_str(unicode(data.gscafb.GSCAFB_Marital_Status)), self.GSCAFB_Marital_Status),
                            #self.value_in(smart_str(unicode(str(data.gscafb.GSCAFB_Date_of_Birth).replace("-", "", 50))), self.GSCAFB_Date_of_Birth),
                            self.value_in(smart_str(unicode(data.gscafb.GSCAFB_Date_of_Birth)), self.GSCAFB_Date_of_Birth),
                            
                            #IE
                            self.value_in(smart_str(unicode(data.ei.EI_Employment_Type)), self.EI_Employment_Type),
                            self.value_in(smart_str(unicode(data.ei.EI_Primary_Occupation)), self.EI_Primary_Occupation),
                            self.value_in(smart_str(unicode(data.ei.EI_Employer_Name)), self.EI_Employer_Name),
                            self.value_in(smart_str(unicode(data.ei.EI_Employee_Number)), self.EI_Employee_Number),
                            self.value_in(smart_str(unicode(data.ei.EI_Employment_Date)), self.EI_Employment_Date),
                            self.value_in(smart_str(unicode(data.ei.EI_Income_Band)), self.EI_Income_Band),
                            self.value_in(smart_str(unicode(data.ei.EI_Salary_Frequency)), self.EI_Salary_Frequency),
     
                            self.value_in(smart_str(unicode(data.pci.PCI_Building_Unit_Number)), self.PCI_Building_Unit_Number),
                            self.value_in(smart_str(unicode(data.pci.PCI_Building_Name)), self.PCI_Building_Name),
                            self.value_in(smart_str(unicode(data.pci.PCI_Floor_Number)), self.PCI_Floor_Number),
                            self.value_in(smart_str(unicode(data.pci.PCI_Plot_or_Street_Number)), self.PCI_Plot_or_Street_Number),
                            self.value_in(smart_str(unicode(data.pci.PCI_LC_or_Street_Name)), self.PCI_LC_or_Street_Name),
                            self.value_in(smart_str(unicode(data.pci.PCI_Region)), self.PCI_Region),
                            self.value_in(smart_str(unicode(data.pci.PCI_District)), self.PCI_District),
                            self.value_in(smart_str(unicode(data.pci.PCI_County_or_Town)), self.PCI_County_or_Town),
                            self.value_in(smart_str(unicode(data.pci.PCI_Parish)), self.PCI_Parish),
                            self.value_in(smart_str(unicode(data.pci.PCI_Suburb)), self.PCI_Suburb),
                            self.value_in(smart_str(unicode(data.pci.PCI_Village)), self.PCI_Village),
                            self.value_in(smart_str(unicode(data.pci.PCI_PO_Box_Number)), self.PCI_PO_Box_Number),
                            self.value_in(smart_str(unicode(data.pci.PCI_Post_Office_Town)), self.PCI_Post_Office_Town),
                            self.value_in(smart_str(unicode(data.pci.PCI_Country_Code)), self.PCI_Country_Code),
                            self.value_in(smart_str(unicode(data.pci.PCI_Period_At_Address)), self.PCI_Period_At_Address),
                            self.value_in(smart_str(unicode(data.pci.PCI_Flag_of_Ownership)), self.PCI_Flag_of_Ownership),
                            #self.value_in(smart_str(unicode(data.pci.PCI_Primary_Number_Country_Dialling_Code)), self.PCI_Primary_Number_Country_Dialling_Code),
                            self.value_in(smart_str(unicode(data.pci.PCI_Primary_Number_Telephone_Number)), self.PCI_Primary_Number_Telephone_Number),
                            #self.value_in(smart_str(unicode(data.pci.PCI_Other_Number_Country_Dialling_Code)), self.PCI_Other_Number_Country_Dialling_Code),
                            self.value_in(smart_str(unicode(data.pci.PCI_Other_Number_Telephone_Number)), self.PCI_Other_Number_Telephone_Number),
                            #self.value_in(smart_str(unicode(data.pci.PCI_Mobile_Number_Country_Dialling_Code)), self.PCI_Mobile_Number_Country_Dialling_Code),
                            self.value_in(smart_str(unicode(data.pci.PCI_Mobile_Number_Telephone_Number)), self.PCI_Mobile_Number_Telephone_Number),
                            #self.value_in(smart_str(unicode(data.pci.PCI_Facsimile_Country_Dialling_Code)), self.PCI_Facsimile_Country_Dialling_Code),
                            self.value_in(smart_str(unicode(data.pci.PCI_Facsimile_Number)), self.PCI_Facsimile_Number),
                            self.value_in(smart_str(unicode(data.pci.PCI_Email_Address)), self.PCI_Email_Address),
                            self.value_in(smart_str(unicode(data.pci.PCI_Web_site)), self.PCI_Web_site),
                            self.value_in(smart_str(unicode(data.sci.SCI_Unit_Number)), self.SCI_Unit_Number),
                            self.value_in(smart_str(unicode(data.sci.SCI_Unit_Name)), self.SCI_Unit_Name),
                            self.value_in(smart_str(unicode(data.sci.SCI_Floor_Number)), self.SCI_Floor_Number),
                            self.value_in(smart_str(unicode(data.sci.SCI_Plot_or_Street_Number)), self.SCI_Plot_or_Street_Number),
                            self.value_in(smart_str(unicode(data.sci.SCI_LC_or_Street_Name)), self.SCI_LC_or_Street_Name),
                            self.value_in(smart_str(unicode(data.sci.SCI_Region)), self.SCI_Region),
                            self.value_in(smart_str(unicode(data.sci.SCI_District)), self.SCI_District),
                            self.value_in(smart_str(unicode(data.sci.SCI_County_or_Town)), self.SCI_County_or_Town),
                            self.value_in(smart_str(unicode(data.sci.SCI_Parish)), self.SCI_Parish),
                            self.value_in(smart_str(unicode(data.sci.SCI_Suburb)), self.SCI_Suburb),
                            self.value_in(smart_str(unicode(data.sci.SCI_Village)), self.SCI_Village),
                            self.value_in(smart_str(unicode(data.sci.SCI_PO_Box_Number)), self.SCI_PO_Box_Number),
                            self.value_in(smart_str(unicode(data.sci.SCI_Post_Office_Town)), self.SCI_Post_Office_Town),
                            self.value_in(smart_str(unicode(data.sci.SCI_Country_Code)), self.SCI_Country_Code),
                            self.value_in(smart_str(unicode(data.sci.SCI_Period_At_Address)), self.SCI_Period_At_Address),
                            self.value_in(smart_str(unicode(data.sci.SCI_Flag_for_ownership)), self.SCI_Flag_of_Ownership),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Primary_Number_Country_Dialling_Code)), self.SCI_Primary_Number_Country_Dialling_Code),
                            self.value_in(smart_str(unicode(data.sci.SCI_Primary_Number_Telephone_Number)), self.SCI_Primary_Number_Telephone_Number),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Other_Number_Country_Dialling_Code)), self.SCI_Other_Number_Country_Dialling_Code),
                            self.value_in(smart_str(unicode(data.sci.SCI_Other_Number_Telephone_Number)), self.SCI_Other_Number_Telephone_Number),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Mobile_Number_Country_Dialling_Code)), self.SCI_Mobile_Number_Country_Dialling_Code),
                            self.value_in(smart_str(unicode(data.sci.SCI_Mobile_Number_Telephone_Number)), self.SCI_Mobile_Number_Telephone_Number),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Facsimile_Country_Dialling_Code)), self.SCI_Facsimile_Country_Dialling_Code),
                            self.value_in(smart_str(unicode(data.sci.SCI_Facsimile_Number)), self.SCI_Facsimile_Number),
                            self.value_in(smart_str(unicode(data.sci.SCI_Email_Address)), self.SCI_Email_Address),
                            self.value_in(smart_str(unicode(data.sci.SCI_Web_site)), self.SCI_Web_site),
                            
                        ])
            return self.response 
        except:
            raise 
