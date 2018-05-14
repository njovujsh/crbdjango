import csv
from django.http import HttpResponse
from django.utils.encoding import smart_str 

class ProcessCSV(object):
    """
    Object which will be used to process csv fileformat.
    """
    def __init__(self, filename, dialect, delimiter="|"):
    
        self.response = HttpResponse(content_type="text/csv")
        self.filename = filename 
        self.delimiter = delimiter
        self.dialect = dialect
        #create a csv  object 
        self.response['Content-Disposition'] = "attachment; filename=%s" % str(self.filename)
        
        self.writer = csv.writer(self.response, quotechar='"', quoting=csv.QUOTE_ALL, delimiter='|', dialect=csv.excel)
        
    def write_headers(self, headers):
        """
        Write the needed header files that describe.
        """
        if(headers):
            self.writer.writerow(headers)
            
    def write_row_header(self, rows):
        
        self.writer.writerow(rows)
           
    def write_row_data(self, data, rows):
        for d in data:
            #for r in rows:
            print rows 
            self.writer.writerow([smart_str(unicode(d.id))
                                 ])
        return self.response 

   
    
class ProcessCSVCMC(ProcessCSV):
    def __init__(self, filename, dialect, row, headers, delimiter="|"):
        super(ProcessCSVCMC, self).__init__(filename, dialect)
        
        self.delimiter= delimiter
        self.row = row
        
        if(headers):
            self.write_headers(headers)
            
    #def write_row_header(self, rows):
    #    """
    #    Override the method.
    #    """
        if(self.row):
            self.writer.writerow(self.row)
        
    def write_row_data(self, rowdata):
        """
        Override the method of writing rows
        because this one has long rows.
        """
        try:
            for data in rowdata:
                self.writer.writerow([
                                    smart_str(unicode(data.id)),
                                    smart_str(unicode(data.PI_Identification_Code)),
                                    smart_str(unicode(data.Branch_Identification_Code)),
                                    smart_str(unicode(data.Borrowers_Client_Number)),
                                    smart_str(unicode(data.Borrower_Account_Reference)),
                                    smart_str(unicode(data.Borrower_Classification)),
                                    smart_str(unicode(data.Collateral_Type_Identification)),
                                    smart_str(unicode(data.Collateral_Reference_Number)),
                                    smart_str(unicode(data.Collateral_Description)),
                                    smart_str(unicode(data.Collateral_Currency)),
                                    smart_str(unicode(data.Collateral_Open_Market_Value)),
                                    smart_str(unicode(data.Collateral_Forced_Sale_Value)),
                                    smart_str(unicode(data.Collateral_Valuation_Expiry_Date)),
                                    smart_str(unicode(data.Instrument_of_Claim)),
                                    smart_str(unicode(data.Valuation_Date)),
                                    ])
            return self.response 
        except:
            raise 
            
                                    

class ProcessCSVPI(ProcessCSV):
    def __init__(self, filename, dialect, row, headers, delimiter="|"):
        super(ProcessCSVPI, self).__init__(filename, dialect)
        
        self.delimiter = delimiter
        self.row = row
        
        if(headers):
            self.write_headers(headers)
            
            
        if(self.row):
            self.writer.writerow(self.row)
        else:
            return None 
            
    def write_row_data(self, coldata):
        try:
            for data in coldata:
                self.writer.writerow([
                            smart_str(unicode(data.id)),
                            smart_str(unicode(data.PI_Identification_Code)), 
                            smart_str(unicode(data.Institution_Type)), 
                            smart_str(unicode(data.Institution_Name)), 
                            smart_str(unicode(data.License_Issuing_Date)),
                            smart_str(unicode(data.pci.PCI_Building_Unit_Number)), 
                            smart_str(unicode(data.pci.PCI_Building_Name)),  
                            smart_str(unicode(data.pci.PCI_Floor_Number)),  
                            smart_str(unicode(data.pci.PCI_Plot_or_Street_Number)), 
                            smart_str(unicode(data.pci.PCI_LC_or_Street_Name)), 
                            smart_str(unicode(data.pci.PCI_Parish)), 
                            smart_str(unicode(data.pci.PCI_Suburb)), 
                            smart_str(unicode(data.pci.PCI_Village)), 
                            smart_str(unicode(data.pci.PCI_County_or_Town)), 
                            smart_str(unicode(data.pci.PCI_District)), 
                            smart_str(unicode(data.pci.PCI_Region)), 
                            smart_str(unicode(data.pci.PCI_PO_Box_Number)), 
                            smart_str(unicode(data.pci.PCI_Post_Office_Town)), 
                            smart_str(unicode(data.pci.PCI_Country_Code)), 
                            smart_str(unicode(data.pci.PCI_Period_At_Address)), 
                            smart_str(unicode(data.pci.PCI_Flag_of_Ownership)), 
                            smart_str(unicode(data.pci.PCI_Primary_Number_Country_Dialling_Code)), 
                            smart_str(unicode(data.pci.PCI_Primary_Number_Telephone_Number)), 
                            smart_str(unicode(data.pci.PCI_Other_Number_Country_Dialling_Code)), 
                            smart_str(unicode(data.pci.PCI_Other_Number_Telephone_Number)), 
                            smart_str(unicode(data.pci.PCI_Mobile_Number_Country_Dialling_Code)), 
                            smart_str(unicode(data.pci.PCI_Mobile_Number_Telephone_Number)), 
                            smart_str(unicode(data.pci.PCI_Facsimile_Country_Dialling_Code)), 
                            smart_str(unicode(data.pci.PCI_Facsimile_Number)),
                            smart_str(unicode(data.pci.PCI_Email_Address )),
                            smart_str(unicode(data.pci.PCI_Web_site)),
                        ])
            return self.response 
        except:
            raise 
                                
       
class ProcessCSVIB(ProcessCSV):
    def __init__(self, filename, dialect, row, headers, delimiter="|"):
        super(ProcessCSVIB, self).__init__(filename, dialect)
        
        self.delimiter = delimiter
        self.row = row 
        
        if(headers):
            self.write_headers(headers)
            
    #def write_row_header(self, rows):
        if(self.row):
            self.writer.writerow(self.row)
        else:
            return None 
            
    def write_row_data(self, coldata):
        try:
            for data in coldata:
                self.writer.writerow([
                                smart_str(unicode(data.id)),
                                smart_str(unicode(data.PI_Identification_Code )),
                                smart_str(unicode(data.Branch_Identification_Code )),
                                smart_str(unicode(data.Branch_Name )),
                                smart_str(unicode(data.Branch_Type )),
                                smart_str(unicode(data.Date_Opened)),
                                smart_str(unicode(data.pci.PCI_Building_Unit_Number)),
                                smart_str(unicode(data.pci.PCI_Building_Name )),
                                smart_str(unicode(data.pci.PCI_Floor_Number )),
                                smart_str(unicode(data.pci.PCI_Plot_or_Street_Number )),
                                smart_str(unicode(data.pci.PCI_LC_or_Street_Name)),
                                smart_str(unicode(data.pci.PCI_Parish )),
                                smart_str(unicode(data.pci.PCI_Suburb )),
                                smart_str(unicode(data.pci.PCI_Village )),
                                smart_str(unicode(data.pci.PCI_County_or_Town )),
                                smart_str(unicode(data.pci.PCI_District )),
                                smart_str(unicode(data.pci.PCI_Region )),
                                smart_str(unicode(data.pci.PCI_PO_Box_Number )),
                                smart_str(unicode(data.pci.PCI_Post_Office_Town )),
                                smart_str(unicode(data.pci.PCI_Country_Code )),
                                smart_str(unicode(data.pci.PCI_Period_At_Address )),
                                smart_str(unicode(data.pci.PCI_Flag_of_Ownership )),
                                smart_str(unicode(data.pci.PCI_Primary_Number_Country_Dialling_Code )),
                                smart_str(unicode(data.pci.PCI_Primary_Number_Telephone_Number )),
                                smart_str(unicode(data.pci.PCI_Other_Number_Country_Dialling_Code )),
                                smart_str(unicode(data.pci.PCI_Other_Number_Telephone_Number )),
                                smart_str(unicode(data.pci.PCI_Mobile_Number_Country_Dialling_Code )),
                                smart_str(unicode(data.pci.PCI_Mobile_Number_Telephone_Number )),
                                smart_str(unicode(data.pci.PCI_Facsimile_Country_Dialling_Code )),
                                smart_str(unicode(data.pci.PCI_Facsimile_Number)),
                                smart_str(unicode(data.pci.PCI_Email_Address)),
                                smart_str(unicode(data.pci.PCI_Web_site)),
                        ])
            return self.response 
        except:
            raise 
            
                                
class ProcessCSVCBA(ProcessCSV):
    def __init__(self, filename, dialect,row, headers, delimiter="|"):
        super(ProcessCSVCBA, self).__init__(filename, dialect)
        
        self.delimiter = delimiter
        self.row = row 
        
        if(headers):
            self.write_headers(headers)
            
        if(self.row):
            self.writer.writerow(self.row)
        else:
            return None 
            
    def write_row_data(self, coldata):
        try:
            for data in coldata:
                self.writer.writerow([
                                smart_str(unicode(data.id)),
                                smart_str(unicode(data.PI_Identification_Code )),
                                smart_str(unicode(data.Branch_Identification_Code)),
                                smart_str(unicode(data.Borrowers_Client_Number)),
                                smart_str(unicode(data.Borrower_Classification)),
                                smart_str(unicode(data.Credit_Account_Reference)),
                                smart_str(unicode(data.Credit_Account_Date)),
                                smart_str(unicode(data.Credit_Amount)),
                                smart_str(unicode(data.Facility_Amount_Granted)),
                                smart_str(unicode(data.Credit_Account_Type)),
                                smart_str(unicode(data.Group_Identification_Joint_Account_Number)),
                                smart_str(unicode(data.Transaction_Date)),
                                smart_str(unicode(data.Currency)),
                                smart_str(unicode(data.Opening_Balance_Indicator)),
                                smart_str(unicode(data.Maturity_Date)),
                                smart_str(unicode(data.Type_of_Interest)),
                                smart_str(unicode(data.Interest_Calculation_Method)),
                                smart_str(unicode(data.Annual_Interest_Rate_at_Disbursement)),
                                smart_str(unicode(data.Annual_Interest_Rate_at_Reporting)),
                                smart_str(unicode(data.Date_of_First_Payment)),
                                smart_str(unicode(data.Credit_Amortization_Type)),
                                smart_str(unicode(data.Credit_Payment_Frequency)),
                                smart_str(unicode(data.Number_of_Payments)),
                                smart_str(unicode(data.Monthly_Instalment_Amount)),
                                smart_str(unicode(data.Current_Balance_Amount)),
                                smart_str(unicode(data.Current_Balance_Indicator)),
                                smart_str(unicode(data.Last_Payment_Date)),
                                smart_str(unicode(data.Last_Payment_Amount)),
                                smart_str(unicode(data.Credit_Account_Status)),
                                smart_str(unicode(data.Last_Status_Change_Date)),
                                smart_str(unicode(data.Credit_Account_Risk_Classification)),
                                smart_str(unicode(data.Credit_Account_Arrears_Date)),
                                smart_str(unicode(data.Number_of_Days_in_Arrears)),
                                smart_str(unicode(data.Balance_Overdue)),
                                smart_str(unicode(data.Flag_for_Restructured_Credit)),
                                smart_str(unicode(data.Old_Branch_Code)),
                                smart_str(unicode(data.Old_Account_Number)),
                                smart_str(unicode(data.Old_Client_Number)),
                                smart_str(unicode(data.Balance_Overdue_Indicator)),
                                smart_str(unicode(data.Credit_Account_Closure_Date)),
                                smart_str(unicode(data.Credit_Account_Closure_Reason)),
                                smart_str(unicode(data.Specific_Provision_Amount)),
                                smart_str(unicode(data.Client_Consent_Flag)),
                                smart_str(unicode(data.Client_Advice_Notice_Flag)),
                                smart_str(unicode(data.Term)),
                                smart_str(unicode(data.Loan_Purpose)),
                                smart_str(unicode(data.II_Registration_Certificate_Number)),
                                smart_str(unicode(data.II_Tax_Identification_Number)),
                                smart_str(unicode(data.II_Value_Added_Tax_Number)),
                                smart_str(unicode(data.II_FCS_Number)),
                                smart_str(unicode(data.II_Passport_Number)),
                                smart_str(unicode(data.II_Drivers_Licence_ID_Number)),
                                smart_str(unicode(data.II_Voters_PERNO)),
                                smart_str(unicode(data.II_Drivers_License_Permit_Number)),
                                smart_str(unicode(data.II_NSSF_Number)),
                                smart_str(unicode(data.II_Country_ID)),
                                smart_str(unicode(data.II_Country_Issuing_Authority)),
                                smart_str(unicode(data.II_Nationality)),
                                smart_str(unicode(data.II_Police_ID_Number)),
                                smart_str(unicode(data.II_UPDF_Number)),
                                smart_str(unicode(data.II_KACITA_License_Number)),
                                smart_str(unicode(data.II_Public_Service_Pension_Number)),
                                smart_str(unicode(data.II_Teacher_Registration_Number)),
                                smart_str(unicode(data.II_Country_Of_Issue)),
                                smart_str(unicode(data.GSCAFB_Business_Name)),
                                smart_str(unicode(data.GSCAFB_Trading_Name)),
                                smart_str(unicode(data.GSCAFB_Activity_Description)),
                                smart_str(unicode(data.GSCAFB_Industry_Sector_Code)),
                                smart_str(unicode(data.GSCAFB_Date_Registered)),
                                smart_str(unicode(data.GSCAFB_Business_Type_Code)),
                                smart_str(unicode(data.GSCAFB_Surname)),
                                smart_str(unicode(data.GSCAFB_Forename1)),
                                smart_str(unicode(data.GSCAFB_Forename2)),
                                smart_str(unicode(data.GSCAFB_Forename3)),
                                smart_str(unicode(data.GSCAFB_Gender)),
                                smart_str(unicode(data.GSCAFB_Marital_Status)),
                                smart_str(unicode(data.GSCAFB_Date_of_Birth)),
                                smart_str(unicode(data.EI_Employment_Type)),
                                smart_str(unicode(data.EI_Primary_Occupation)),
                                smart_str(unicode(data.EI_Employer_Name)),
                                smart_str(unicode(data.EI_Employee_Number)),
                                smart_str(unicode(data.EI_Employment_Date)),
                                smart_str(unicode(data.EI_Income_Band)),
                                smart_str(unicode(data.EI_Salary_Frequency)),
                                smart_str(unicode(data.pci.PCI_Building_Unit_Number)),
                                smart_str(unicode(data.pci.PCI_Building_Name)),
                                smart_str(unicode(data.pci.PCI_Floor_Number)),
                                smart_str(unicode(data.pci.PCI_Plot_or_Street_Number)),
                                smart_str(unicode(data.pci.PCI_LC_or_Street_Name)),
                                smart_str(unicode(data.pci.PCI_Parish)),
                                smart_str(unicode(data.pci.PCI_Suburb)),
                                smart_str(unicode(data.pci.PCI_Village)),
                                smart_str(unicode(data.pci.PCI_County_or_Town)),
                                smart_str(unicode(data.pci.PCI_District)),
                                smart_str(unicode(data.pci.PCI_Region)),
                                smart_str(unicode(data.pci.PCI_PO_Box_Number)),
                                smart_str(unicode(data.pci.PCI_Post_Office_Town)),
                                smart_str(unicode(data.pci.PCI_Country_Code)),
                                smart_str(unicode(data.pci.PCI_Period_At_Address)),
                                smart_str(unicode(data.pci.PCI_Flag_of_Ownership)),
                                smart_str(unicode(data.pci.PCI_Primary_Number_Country_Dialing_code)),
                                smart_str(unicode(data.pci.PCI_Primary_Number_Telephone_Number)),
                                smart_str(unicode(data.pci.PCI_Other_Number_Country_Dialling_Code)),
                                smart_str(unicode(data.pci.PCI_Other_Number_Telephone_Number)),
                                smart_str(unicode(data.pci.PCI_Mobile_Number_Country_Dialling_Code)),
                                smart_str(unicode(data.pci.PCI_Mobile_Number_Telephone_Number)),
                                smart_str(unicode(data.pci.PCI_Facsimile_Country_Dialling_Code)),
                                smart_str(unicode(data.pci.PCI_Facsimile_Number)),
                                smart_str(unicode(data.pci.PCI_Email_Address)),
                                smart_str(unicode(data.pci.PCI_Web_site)),
                                smart_str(unicode(data.sci.SCI_Unit_Number)),
                                smart_str(unicode(data.sci.SCI_Unit_Name)),
                                smart_str(unicode(data.sci.SCI_Floor_Number)),
                                smart_str(unicode(data.sci.SCI_Plot_or_Street_Number)),
                                smart_str(unicode(data.sci.SCI_LC_or_Street_Name)),
                                smart_str(unicode(data.sci.SCI_Parish)),
                                smart_str(unicode(data.sci.SCI_Suburb)),
                                smart_str(unicode(data.sci.SCI_Village)),
                                smart_str(unicode(data.sci.SCI_County_or_Town)),
                                smart_str(unicode(data.sci.SCI_District)),
                                smart_str(unicode(data.sci.SCI_Region)),
                                smart_str(unicode(data.sci.SCI_PO_Box_Number)),
                                smart_str(unicode(data.sci.SCI_Post_Office_Town)),
                                smart_str(unicode(data.sci.SCI_Country_Code)),
                                smart_str(unicode(data.sci.SCI_Period_At_Address)),
                                smart_str(unicode(data.sci.SCI_Flag_for_ownership)),
                                smart_str(unicode(data.sci.SCI_Primary_Number_Country_Dialling_Code)),
                                smart_str(unicode(data.sci.SCI_Primary_Number_Telephone_Number)),
                                smart_str(unicode(data.sci.SCI_Other_Number_Country_Dialling_Code)),
                                smart_str(unicode(data.sci.SCI_Other_Number_Telephone_Number)),
                                smart_str(unicode(data.sci.SCI_Mobile_Number_Country_Dialling_Code)),
                                smart_str(unicode(data.sci.SCI_Mobile_Number_Telephone_Number)),
                                smart_str(unicode(data.sci.SCI_Facsimile_Country_Dialling_Code)),
                                smart_str(unicode(data.sci.SCI_Facsimile_Number)),
                                smart_str(unicode(data.sci.SCI_Email_Address)),
                                smart_str(unicode(data.sci.SCI_Web_site)),
                            ])
            return self.response 
        except:
            raise 
                            

class ProcessCSVCP(ProcessCSV):
    def __init__(self, filename, dialect, row, headers, delimiter="|"):
        super(ProcessCSVCP, self).__init__(filename, dialect)
        
        self.delimiter = delimiter
        self.row = row 
        
        if(headers):
            self.write_headers(headers)
        
        if(self.row):
            self.writer.writerow(self.row)
        else:
            return None 
            
    def write_row_data(self, coldata):
        try:
            for data in coldata:
                self.writer.writerow([
                    smart_str(unicode(data.id)),
                    smart_str(unicode(data.PI_Identification_Code)),
                    smart_str(unicode(data.Branch_Identification_Code)),
                    smart_str(unicode(data.Client_Number)),
                    smart_str(unicode(data.Credit_Application_Reference)),
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
                    smart_str(unicode(data.II_Registration_Certificate_Number)),
                    smart_str(unicode(data.II_Tax_Identification_Number)),
                    smart_str(unicode(data.II_Value_Added_Tax_Number)),
                    smart_str(unicode(data.II_FCS_Number)),
                    smart_str(unicode(data.II_Passport_Number)),
                    smart_str(unicode(data.II_Drivers_Licence_ID_Number)),
                    smart_str(unicode(data.II_Voters_PERNO)),
                    smart_str(unicode(data.II_Drivers_License_Permit_Number)),
                    smart_str(unicode(data.II_NSSF_Number)),
                    smart_str(unicode(data.II_Country_ID)),
                    smart_str(unicode(data.II_Country_Issuing_Authority)),
                    smart_str(unicode(data.II_Nationality)),
                    smart_str(unicode(data.II_Police_ID_Number)),
                    smart_str(unicode(data.II_UPDF_Number)),
                    smart_str(unicode(data.II_KACITA_License_Number)),
                    smart_str(unicode(data.II_Public_Service_Pension_Number)),
                    smart_str(unicode(data.II_Teacher_Registration_Number)),
                    smart_str(unicode(data.II_Country_Of_Issue)),
                    smart_str(unicode(data.GSCAFB_Business_Name)),
                    smart_str(unicode(data.GSCAFB_Trading_Name)),
                    smart_str(unicode(data.GSCAFB_Activity_Description)),
                    smart_str(unicode(data.GSCAFB_Industry_Sector_Code)),
                    smart_str(unicode(data.GSCAFB_Date_Registered)),
                    smart_str(unicode(data.GSCAFB_Business_Type_Code)),
                    smart_str(unicode(data.GSCAFB_Surname)),
                    smart_str(unicode(data.GSCAFB_Forename1)),
                    smart_str(unicode(data.GSCAFB_Forename2)),
                    smart_str(unicode(data.GSCAFB_Forename3)),
                    smart_str(unicode(data.GSCAFB_Gender)),
                    smart_str(unicode(data.GSCAFB_Marital_Status)),
                    smart_str(unicode(data.GSCAFB_Date_of_Birth)),
                    smart_str(unicode(data.EI_Employment_Type)),
                    smart_str(unicode(data.EI_Primary_Occupation)),
                    smart_str(unicode(data.EI_Employer_Name)),
                    smart_str(unicode(data.EI_Employee_Number)),
                    smart_str(unicode(data.EI_Employment_Date)),
                    smart_str(unicode(data.EI_Income_Band)),
                    smart_str(unicode(data.EI_Salary_Frequency)),
                    smart_str(unicode(data.pci.PCI_Building_Unit_Number)),
                    smart_str(unicode(data.pci.PCI_Building_Name)),
                    smart_str(unicode(data.pci.PCI_Floor_Number)),
                    smart_str(unicode(data.pci.PCI_Plot_or_Street_Number)),
                    smart_str(unicode(data.pci.PCI_LC_or_Street_Name)),
                    smart_str(unicode(data.pci.PCI_Parish)),
                    smart_str(unicode(data.pci.PCI_Suburb)),
                    smart_str(unicode(data.pci.PCI_Village)),
                    smart_str(unicode(data.pci.PCI_County_or_Town)),
                    smart_str(unicode(data.pci.PCI_District)),
                    smart_str(unicode(data.pci.PCI_Region)),
                    smart_str(unicode(data.pci.PCI_PO_Box_Number)),
                    smart_str(unicode(data.pci.PCI_Post_Office_Town)),
                    smart_str(unicode(data.pci.PCI_Country_Code)),
                    smart_str(unicode(data.pci.PCI_Period_At_Address)),
                    smart_str(unicode(data.pci.PCI_Flag_of_Ownership)),
                    smart_str(unicode(data.pci.PCI_Primary_Number_Country_Dialling_Code)),
                    smart_str(unicode(data.pci.PCI_Primary_Number_Telephone_Number)),
                    smart_str(unicode(data.pci.PCI_Other_Number_Country_Dialling_Code)),
                    smart_str(unicode(data.pci.PCI_Other_Number_Telephone_Number)),
                    smart_str(unicode(data.pci.PCI_Mobile_Number_Country_Dialling_Code)),
                    smart_str(unicode(data.pci.PCI_Mobile_Number_Telephone_Number)),
                    smart_str(unicode(data.pci.PCI_Facsimile_Country_Dialling_Code)),
                    smart_str(unicode(data.pci.PCI_Facsimile_Number)),
                    smart_str(unicode(data.pci.PCI_Email_Address)),
                    smart_str(unicode(data.pci.PCI_Web_site)),
                    smart_str(unicode(data.sci.SCI_Unit_Number)),
                    smart_str(unicode(data.sci.SCI_Unit_Name)),
                    smart_str(unicode(data.sci.SCI_Floor_Number)),
                    smart_str(unicode(data.sci.SCI_Plot_or_Street_Number)),
                    smart_str(unicode(data.sci.SCI_LC_or_Street_Name)),
                    smart_str(unicode(data.sci.SCI_Parish)),
                    smart_str(unicode(data.sci.SCI_Suburb)),
                    smart_str(unicode(data.sci.SCI_Village)),
                    smart_str(unicode(data.sci.SCI_County_or_Town)),
                    smart_str(unicode(data.sci.SCI_District)),
                    smart_str(unicode(data.sci.SCI_Region)),
                    smart_str(unicode(data.sci.SCI_PO_Box_Number)),
                    smart_str(unicode(data.sci.SCI_Post_Office_Town)),
                    smart_str(unicode(data.sci.SCI_Country_Code)),
                    smart_str(unicode(data.sci.SCI_Period_At_Address)),
                    smart_str(unicode(data.sci.SCI_Flag_for_ownership)),
                    smart_str(unicode(data.sci.SCI_Primary_Number_Country_Dialling_Code)),
                    smart_str(unicode(data.sci.SCI_Primary_Number_Telephone_Number)),
                    smart_str(unicode(data.sci.SCI_Other_Number_Country_Dialling_Code)),
                    smart_str(unicode(data.sci.SCI_Other_Number_Telephone_Number)),
                    smart_str(unicode(data.sci.SCI_Mobile_Number_Country_Dialling_Code)),
                    smart_str(unicode(data.sci.SCI_Mobile_Number_Telephone_Number)),
                    smart_str(unicode(data.sci.SCI_Facsimile_Country_Dialling_Code)),
                    smart_str(unicode(data.sci.SCI_Facsimile_Number)),
                    smart_str(unicode(data.sci.SCI_Email_Address)),
                    smart_str(unicode(data.sci.SCI_Web_site)),
                ])
            return self.response 
        except:
            raise 

class ProcessCSVBC(ProcessCSV):
    def __init__(self, filename, dialect, row, headers, delimiter="|"):
        super(ProcessCSVBC, self).__init__(filename, dialect)
        
        self.delimiter = delimiter
        self.row = row 
        self.headers = headers 
        if(self.headers):
            self.write_headers(self.headers)
    #def write_row_header(self, rows):
        if(self.row):
            self.writer.writerow(self.row)
        else:
            return None 
            
    def write_row_data(self, coldata):
        try:
            for data in coldata:
                        self.writer.writerow([
                            smart_str(unicode(data.id)),
                            smart_str(unicode(data.PI_Identification_Code)),
                            smart_str(unicode(data.Branch_Identification_Code)),
                            smart_str(unicode(data.Client_Number)),
                            smart_str(unicode(data.PI_Client_Classification)),
                            smart_str(unicode(data.Cheque_Account_Reference_Number)),
                            smart_str(unicode(data.Cheque_Account_Opened_Date)),
                            smart_str(unicode(data.Cheque_Account_Classification)),
                            smart_str(unicode(data.Cheque_Account_Type)),
                            smart_str(unicode(data.Cheque_Number)),
                            smart_str(unicode(data.Cheque_Amount)),
                            smart_str(unicode(data.Cheque_Currency)),
                            smart_str(unicode(data.Beneficiary_Name_Or_Payee)),
                            smart_str(unicode(data.Cheque_Bounce_Date)),
                            smart_str(unicode(data.Cheque_Account_Bounce_Reason)),
                            smart_str(unicode(data.II_Registration_Certificate_Number)),
                            smart_str(unicode(data.II_Tax_Identification_Number)),
                            smart_str(unicode(data.II_Value_Added_Tax_Number)),
                            smart_str(unicode(data.II_FCS_Number)),
                            smart_str(unicode(data.II_Passport_Number)),
                            smart_str(unicode(data.II_Drivers_Licence_ID_Number)),
                            smart_str(unicode(data.II_Voters_PERNO)),
                            smart_str(unicode(data.II_Drivers_License_Permit_Number)),
                            smart_str(unicode(data.II_NSSF_Number)),
                            smart_str(unicode(data.II_Country_ID)),
                            smart_str(unicode(data.II_Country_Issuing_Authority)),
                            smart_str(unicode(data.II_Nationality)),
                            smart_str(unicode(data.II_Police_ID_Number)),
                            smart_str(unicode(data.II_UPDF_Number)),
                            smart_str(unicode(data.II_KACITA_License_Number)),
                            smart_str(unicode(data.II_Public_Service_Pension_Number)),
                            smart_str(unicode(data.II_Teacher_Registration_Number)),
                            smart_str(unicode(data.II_Country_Of_Issue)),
                            smart_str(unicode(data.GSCAFB_Business_Name)),
                            smart_str(unicode(data.GSCAFB_Trading_Name)),
                            smart_str(unicode(data.GSCAFB_Activity_Description)),
                            smart_str(unicode(data.GSCAFB_Industry_Sector_Code)),
                            smart_str(unicode(data.GSCAFB_Date_Registered)),
                            smart_str(unicode(data.GSCAFB_Business_Type_Code)),
                            smart_str(unicode(data.GSCAFB_Surname)),
                            smart_str(unicode(data.GSCAFB_Forename1)),
                            smart_str(unicode(data.GSCAFB_Forename2)),
                            smart_str(unicode(data.GSCAFB_Forename3)),
                            smart_str(unicode(data.GSCAFB_Gender)),
                            smart_str(unicode(data.GSCAFB_Marital_Status)),
                            smart_str(unicode(data.GSCAFB_Date_of_Birth)),
                            smart_str(unicode(data.EI_Employment_Type)),
                            smart_str(unicode(data.EI_Primary_Occupation)),
                            smart_str(unicode(data.EI_Employer_Name)),
                            smart_str(unicode(data.EI_Employee_Number)),
                            smart_str(unicode(data.EI_Employment_Date)),
                            smart_str(unicode(data.EI_Income_Band)),
                            smart_str(unicode(data.EI_Salary_Frequency)),
                            smart_str(unicode(data.pci.PCI_Building_Unit_Number)),
                            smart_str(unicode(data.pci.PCI_Building_Name)),
                            smart_str(unicode(data.pci.PCI_Floor_Number)),
                            smart_str(unicode(data.pci.PCI_Plot_or_Street_Number)),
                            smart_str(unicode(data.pci.PCI_LC_or_Street_Name)),
                            smart_str(unicode(data.pci.PCI_Parish)),
                            smart_str(unicode(data.pci.PCI_Suburb)),
                            smart_str(unicode(data.pci.PCI_Village)),
                            smart_str(unicode(data.pci.PCI_County_or_Town)),
                            smart_str(unicode(data.pci.PCI_District)),
                            smart_str(unicode(data.pci.PCI_Region)),
                            smart_str(unicode(data.pci.PCI_PO_Box_Number)),
                            smart_str(unicode(data.pci.PCI_Post_Office_Town)),
                            smart_str(unicode(data.pci.PCI_Country_Code)),
                            smart_str(unicode(data.pci.PCI_Period_At_Address)),
                            smart_str(unicode(data.pci.PCI_Flag_of_Ownership)),
                            smart_str(unicode(data.pci.PCI_Primary_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.pci.PCI_Primary_Number_Telephone_Number)),
                            smart_str(unicode(data.pci.PCI_Other_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.pci.PCI_Other_Number_Telephone_Number)),
                            smart_str(unicode(data.pci.PCI_Mobile_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.pci.PCI_Mobile_Number_Telephone_Number)),
                            smart_str(unicode(data.pci.PCI_Facsimile_Country_Dialling_Code)),
                            smart_str(unicode(data.pci.PCI_Facsimile_Number)),
                            smart_str(unicode(data.pci.PCI_Email_Address)),
                            smart_str(unicode(data.pci.PCI_Web_site)),
                            smart_str(unicode(data.sci.SCI_Unit_Number)),
                            smart_str(unicode(data.sci.SCI_Unit_Name)),
                            smart_str(unicode(data.sci.SCI_Floor_Number)),
                            smart_str(unicode(data.sci.SCI_Plot_or_Street_Number)),
                            smart_str(unicode(data.sci.SCI_LC_or_Street_Name)),
                            smart_str(unicode(data.sci.SCI_Parish)),
                            smart_str(unicode(data.sci.SCI_Suburb)),
                            smart_str(unicode(data.sci.SCI_Village)),
                            smart_str(unicode(data.sci.SCI_County_or_Town)),
                            smart_str(unicode(data.sci.SCI_District)),
                            smart_str(unicode(data.sci.SCI_Region)),
                            smart_str(unicode(data.sci.SCI_PO_Box_Number)),
                            smart_str(unicode(data.sci.SCI_Post_Office_Town)),
                            smart_str(unicode(data.sci.SCI_Country_Code)),
                            smart_str(unicode(data.sci.SCI_Period_At_Address)),
                            smart_str(unicode(data.sci.SCI_Flag_for_ownership)),
                            smart_str(unicode(data.sci.SCI_Primary_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.sci.SCI_Primary_Number_Telephone_Number)),
                            smart_str(unicode(data.sci.SCI_Other_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.sci.SCI_Other_Number_Telephone_Number)),
                            smart_str(unicode(data.sci.SCI_Mobile_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.sci.SCI_Mobile_Number_Telephone_Number)),
                            smart_str(unicode(data.sci.SCI_Facsimile_Country_Dialling_Code)),
                            smart_str(unicode(data.sci.SCI_Facsimile_Number)),
                            smart_str(unicode(data.sci.SCI_Email_Address)),
                            smart_str(unicode(data.sci.SCI_Web_site)),
                        ])
            return self.response 
        except:
            raise 
            
class ProcessCSVPIS(ProcessCSV):
    def __init__(self, filename, dialect, row, headers, delimiter="|"):
        super(ProcessCSVPIS, self).__init__(filename, dialect)
        
        self.delimiter = delimiter
        self.row = row 
        
        self.headers = headers 
        if(self.headers):
            self.write_headers(self.headers)
            
        if(self.row):
            self.writer.writerow(self.row)
            
    def write_row_data(self, coldata):
        try:
            for data in coldata:
                self.writer.writerow([
                            smart_str(unicode(data.id)),
                            smart_str(unicode(data.PI_Identification_Code)),
                            smart_str(unicode(data.Stakeholder_Type)),
                            smart_str(unicode(data.Stakeholder_Category)),
                            smart_str(unicode(data.Shareholder_Percentage)),
                            smart_str(unicode(data.II_Registration_Certificate_Number)),
                            smart_str(unicode(data.II_Tax_Identification_Number)),
                            smart_str(unicode(data.II_Value_Added_Tax_Number)),
                            smart_str(unicode(data.II_FCS_Number)),
                            smart_str(unicode(data.II_Passport_Number)),
                            smart_str(unicode(data.II_Drivers_Licence_ID_Number)),
                            smart_str(unicode(data.II_Voters_PERNO)),
                            smart_str(unicode(data.II_Drivers_License_Permit_Number)),
                            smart_str(unicode(data.II_NSSF_Number)),
                            smart_str(unicode(data.II_Country_ID)),
                            smart_str(unicode(data.II_Country_Issuing_Authority)),
                            smart_str(unicode(data.II_Nationality)),
                            smart_str(unicode(data.II_Police_ID_Number)),
                            smart_str(unicode(data.II_UPDF_Number)),
                            smart_str(unicode(data.II_KACITA_License_Number)),
                            smart_str(unicode(data.II_Public_Service_Pension_Number)),
                            smart_str(unicode(data.II_Teacher_Registration_Number)),
                            smart_str(unicode(data.II_Country_Of_Issue)),
                            smart_str(unicode(data.GSCAFB_Business_Name)),
                            smart_str(unicode(data.GSCAFB_Trading_Name)),
                            smart_str(unicode(data.GSCAFB_Activity_Description)),
                            smart_str(unicode(data.GSCAFB_Industry_Sector_Code)),
                            smart_str(unicode(data.GSCAFB_Date_Registered)),
                            smart_str(unicode(data.GSCAFB_Business_Type_Code)),
                            smart_str(unicode(data.GSCAFB_Surname)),
                            smart_str(unicode(data.GSCAFB_Forename1)),
                            smart_str(unicode(data.GSCAFB_Forename2)),
                            smart_str(unicode(data.GSCAFB_Forename3)),
                            smart_str(unicode(data.GSCAFB_Gender)),
                            smart_str(unicode(data.GSCAFB_Marital_Status)),
                            smart_str(unicode(data.GSCAFB_Date_of_Birth)),
                            smart_str(unicode(data.EI_Employment_Type)),
                            smart_str(unicode(data.EI_Primary_Occupation)),
                            smart_str(unicode(data.EI_Employer_Name)),
                            smart_str(unicode(data.EI_Employee_Number)),
                            smart_str(unicode(data.EI_Employment_Date)),
                            smart_str(unicode(data.EI_Income_Band)),
                            smart_str(unicode(data.EI_Salary_Frequency)),
                            smart_str(unicode(data.pci.PCI_Building_Unit_Number)),
                            smart_str(unicode(data.pci.PCI_Building_Name)),
                            smart_str(unicode(data.pci.PCI_Floor_Number)),
                            smart_str(unicode(data.pci.PCI_Plot_or_Street_Number)),
                            smart_str(unicode(data.pci.PCI_LC_or_Street_Name)),
                            smart_str(unicode(data.pci.PCI_Parish)),
                            smart_str(unicode(data.pci.PCI_Suburb)),
                            smart_str(unicode(data.pci.PCI_Village)),
                            smart_str(unicode(data.pci.PCI_County_or_Town)),
                            smart_str(unicode(data.pci.PCI_District)),
                            smart_str(unicode(data.pci.PCI_Region)),
                            smart_str(unicode(data.pci.PCI_PO_Box_Number)),
                            smart_str(unicode(data.pci.PCI_Post_Office_Town)),
                            smart_str(unicode(data.pci.PCI_Country_Code)),
                            smart_str(unicode(data.pci.PCI_Period_At_Address)),
                            smart_str(unicode(data.pci.PCI_Flag_of_Ownership)),
                            smart_str(unicode(data.pci.PCI_Primary_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.pci.PCI_Primary_Number_Telephone_Number)),
                            smart_str(unicode(data.pci.PCI_Other_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.pci.PCI_Other_Number_Telephone_Number)),
                            smart_str(unicode(data.pci.PCI_Mobile_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.pci.PCI_Mobile_Number_Telephone_Number)),
                            smart_str(unicode(data.pci.PCI_Facsimile_Country_Dialling_Code)),
                            smart_str(unicode(data.pci.PCI_Facsimile_Number)),
                            smart_str(unicode(data.pci.PCI_Email_Address)),
                            smart_str(unicode(data.pci.PCI_Web_site)),
                            smart_str(unicode(data.sci.SCI_Unit_Number)),
                            smart_str(unicode(data.sci.SCI_Unit_Name)),
                            smart_str(unicode(data.sci.SCI_Floor_Number)),
                            smart_str(unicode(data.sci.SCI_Plot_or_Street_Number)),
                            smart_str(unicode(data.sci.SCI_LC_or_Street_Name)),
                            smart_str(unicode(data.sci.SCI_Parish)),
                            smart_str(unicode(data.sci.SCI_Suburb)),
                            smart_str(unicode(data.sci.SCI_Village)),
                            smart_str(unicode(data.sci.SCI_County_or_Town)),
                            smart_str(unicode(data.sci.SCI_District)),
                            smart_str(unicode(data.sci.SCI_Region)),
                            smart_str(unicode(data.sci.SCI_PO_Box_Number)),
                            smart_str(unicode(data.sci.SCI_Post_Office_Town)),
                            smart_str(unicode(data.sci.SCI_Country_Code)),
                            smart_str(unicode(data.sci.SCI_Period_At_Address)),
                            smart_str(unicode(data.sci.SCI_Flag_for_ownership)),
                            smart_str(unicode(data.sci.SCI_Primary_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.sci.SCI_Primary_Number_Telephone_Number)),
                            smart_str(unicode(data.sci.SCI_Other_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.sci.SCI_Other_Number_Telephone_Number)),
                            smart_str(unicode(data.sci.SCI_Mobile_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.sci.SCI_Mobile_Number_Telephone_Number)),
                            smart_str(unicode(data.sci.SCI_Facsimile_Country_Dialling_Code)),
                            smart_str(unicode(data.sci.SCI_Facsimile_Number)),
                            smart_str(unicode(data.sci.SCI_Email_Address)),
                            smart_str(unicode(data.sci.SCI_Web_site)),
                    ])
            return self.response 
        except:
            raise 
        
class ProcessCSVBS(ProcessCSV):
    def __init__(self, filename, dialect, row, headers, delimiter="|"):
        super(ProcessCSVBS, self).__init__(filename, dialect)
        
        self.delimiter = delimiter
        
        self.row = row 
        self.headers = headers 
        
        if(self.headers):
            self.write_headers(self.headers)
            
        if(self.row):
            self.writer.writerow(self.row)
            
    def write_row_data(self, coldata):
        try:
            for data in coldata:
                self.writer.write([
                            smart_str(unicode(data.id)),
                            smart_str(unicode(data.PI_Identification_Code)),
                            smart_str(unicode(data.Branch_Identification_Code)),
                            smart_str(unicode(data.Borrowers_Client_Number)),
                            smart_str(unicode(data.Stakeholder_Type)),
                            smart_str(unicode(data.Stakeholder_Category)),
                            smart_str(unicode(data.Shareholder_Percentage)),
                            smart_str(unicode(data.II_Registration_Certificate_Number)),
                            smart_str(unicode(data.II_Tax_Identification_Number)),
                            smart_str(unicode(data.II_Value_Added_Tax_Number)),
                            smart_str(unicode(data.II_FCS_Number)),
                            smart_str(unicode(data.II_Passport_Number)),
                            smart_str(unicode(data.II_Drivers_Licence_ID_Number)),
                            smart_str(unicode(data.II_Voters_PERNO)),
                            smart_str(unicode(data.II_Drivers_License_Permit_Number)),
                            smart_str(unicode(data.II_NSSF_Number)),
                            smart_str(unicode(data.II_Country_ID)),
                            smart_str(unicode(data.II_Country_Issuing_Authority)),
                            smart_str(unicode(data.II_Nationality)),
                            smart_str(unicode(data.II_Police_ID_Number)),
                            smart_str(unicode(data.II_UPDF_Number)),
                            smart_str(unicode(data.II_KACITA_License_Number)),
                            smart_str(unicode(data.II_Public_Service_Pension_Number)),
                            smart_str(unicode(data.II_Teacher_Registration_Number)),
                            smart_str(unicode(data.II_Country_Of_Issue)),
                            smart_str(unicode(data.GSCAFB_Business_Name)),
                            smart_str(unicode(data.GSCAFB_Trading_Name)),
                            smart_str(unicode(data.GSCAFB_Activity_Description)),
                            smart_str(unicode(data.GSCAFB_Industry_Sector_Code)),
                            smart_str(unicode(data.GSCAFB_Date_Registered)),
                            smart_str(unicode(data.GSCAFB_Business_Type_Code)),
                            smart_str(unicode(data.GSCAFB_Surname)),
                            smart_str(unicode(data.GSCAFB_Forename1)),
                            smart_str(unicode(data.GSCAFB_Forename2)),
                            smart_str(unicode(data.GSCAFB_Forename3)),
                            smart_str(unicode(data.GSCAFB_Gender)),
                            smart_str(unicode(data.GSCAFB_Marital_Status)),
                            smart_str(unicode(data.GSCAFB_Date_of_Birth)),
                            smart_str(unicode(data.EI_Employment_Type)),
                            smart_str(unicode(data.EI_Primary_Occupation)),
                            smart_str(unicode(data.EI_Employer_Name)),
                            smart_str(unicode(data.EI_Employee_Number)),
                            smart_str(unicode(data.EI_Employment_Date)),
                            smart_str(unicode(data.EI_Income_Band)),
                            smart_str(unicode(data.EI_Salary_Frequency)),
                            smart_str(unicode(data.pci.PCI_Building_Unit_Number)),
                            smart_str(unicode(data.pci.PCI_Building_Name)),
                            smart_str(unicode(data.pci.PCI_Floor_Number)),
                            smart_str(unicode(data.pci.PCI_Plot_or_Street_Number)),
                            smart_str(unicode(data.pci.PCI_LC_or_Street_Name)),
                            smart_str(unicode(data.pci.PCI_Parish)),
                            smart_str(unicode(data.pci.PCI_Suburb)),
                            smart_str(unicode(data.pci.PCI_Village)),
                            smart_str(unicode(data.pci.PCI_County_or_Town)),
                            smart_str(unicode(data.pci.PCI_District)),
                            smart_str(unicode(data.pci.PCI_Region)),
                            smart_str(unicode(data.pci.PCI_PO_Box_Number)),
                            smart_str(unicode(data.pci.PCI_Post_Office_Town)),
                            smart_str(unicode(data.pci.PCI_Country_Code)),
                            smart_str(unicode(data.pci.PCI_Period_At_Address)),
                            smart_str(unicode(data.pci.PCI_Flag_of_Ownership)),
                            smart_str(unicode(data.pci.PCI_Primary_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.pci.PCI_Primary_Number_Telephone_Number)),
                            smart_str(unicode(data.pci.PCI_Other_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.pci.PCI_Other_Number_Telephone_Number)),
                            smart_str(unicode(data.pci.PCI_Mobile_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.pci.PCI_Mobile_Number_Telephone_Number)),
                            smart_str(unicode(data.pci.PCI_Facsimile_Country_Dialling_Code)),
                            smart_str(unicode(data.pci.PCI_Facsimile_Number)),
                            smart_str(unicode(data.pci.PCI_Email_Address)),
                            smart_str(unicode(data.pci.PCI_Web_site)),
                            smart_str(unicode(data.sci.SCI_Unit_Number)),
                            smart_str(unicode(data.sci.SCI_Unit_Name)),
                            smart_str(unicode(data.sci.SCI_Floor_Number)),
                            smart_str(unicode(data.sci.SCI_Plot_or_Street_Number)),
                            smart_str(unicode(data.sci.SCI_LC_or_Street_Name)),
                            smart_str(unicode(data.sci.SCI_Parish)),
                            smart_str(unicode(data.sci.SCI_Suburb)),
                            smart_str(unicode(data.sci.SCI_Village)),
                            smart_str(unicode(data.sci.SCI_County_or_Town)),
                            smart_str(unicode(data.sci.SCI_District)),
                            smart_str(unicode(data.sci.SCI_Region)),
                            smart_str(unicode(data.sci.SCI_PO_Box_Number)),
                            smart_str(unicode(data.sci.SCI_Post_Office_Town)),
                            smart_str(unicode(data.sci.SCI_Country_Code)),
                            smart_str(unicode(data.sci.SCI_Period_At_Address)),
                            smart_str(unicode(data.sci.SCI_Flag_for_ownership)),
                            smart_str(unicode(data.sci.SCI_Primary_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.sci.SCI_Primary_Number_Telephone_Number)),
                            smart_str(unicode(data.sci.SCI_Other_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.sci.SCI_Other_Number_Telephone_Number)),
                            smart_str(unicode(data.sci.SCI_Mobile_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.sci.SCI_Mobile_Number_Telephone_Number)),
                            smart_str(unicode(data.sci.SCI_Facsimile_Country_Dialling_Code)),
                            smart_str(unicode(data.sci.SCI_Facsimile_Number)),
                            smart_str(unicode(data.sci.SCI_Email_Address)),
                            smart_str(unicode(data.sci.SCI_Web_site)),
                        ])
            return self.response 
        except:
            raise 
            

class ProcessCSVCCG(ProcessCSV):
    def __init__(self, filename, dialect, row, headers, delimiter="|"):
        super(ProcessCSVCCG, self).__init__(filename, dialect)
        
        self.row = row
        self.delimiter = delimiter
        self.headers = headers 
        
        if(self.headers):
            self.write_headers(self.headers)
            
        if(self.row):
            self.writer.writerow(self.row)
            
    def write_row_data(self, coldata):
        try:
            for data in coldata:
                self.writer.writerow([
                            smart_str(unicode(data.id)),
                            smart_str(unicode(data.PI_Identification_Code)),
                            smart_str(unicode(data.Branch_Identification_Code)),
                            smart_str(unicode(data.Borrowers_Client_Number)),
                            smart_str(unicode(data.Borrower_Account_Reference)),
                            smart_str(unicode(data.Guarantor_Classification)),
                            smart_str(unicode(data.Guarantee_Type)),
                            smart_str(unicode(data.Guarantor_Type)),
                            smart_str(unicode(data.II_Registration_Certificate_Number)),
                            smart_str(unicode(data.II_Tax_Identification_Number)),
                            smart_str(unicode(data.II_Value_Added_Tax_Number)),
                            smart_str(unicode(data.II_FCS_Number)),
                            smart_str(unicode(data.II_Passport_Number)),
                            smart_str(unicode(data.II_Drivers_Licence_ID_Number)),
                            smart_str(unicode(data.II_Voters_PERNO)),
                            smart_str(unicode(data.II_Drivers_License_Permit_Number)),
                            smart_str(unicode(data.II_NSSF_Number)),
                            smart_str(unicode(data.II_Country_ID)),
                            smart_str(unicode(data.II_Country_Issuing_Authority)),
                            smart_str(unicode(data.II_Nationality)),
                            smart_str(unicode(data.II_Police_ID_Number)),
                            smart_str(unicode(data.II_UPDF_Number)),
                            smart_str(unicode(data.II_KACITA_License_Number)),
                            smart_str(unicode(data.II_Public_Service_Pension_Number)),
                            smart_str(unicode(data.II_Teacher_Registration_Number)),
                            smart_str(unicode(data.II_Country_Of_Issue)),
                            smart_str(unicode(data.GSCAFB_Business_Name)),
                            smart_str(unicode(data.GSCAFB_Trading_Name)),
                            smart_str(unicode(data.GSCAFB_Activity_Description)),
                            smart_str(unicode(data.GSCAFB_Industry_Sector_Code)),
                            smart_str(unicode(data.GSCAFB_Date_Registered)),
                            smart_str(unicode(data.GSCAFB_Business_Type_Code)),
                            smart_str(unicode(data.GSCAFB_Surname)),
                            smart_str(unicode(data.GSCAFB_Forename1)),
                            smart_str(unicode(data.GSCAFB_Forename2)),
                            smart_str(unicode(data.GSCAFB_Forename3)),
                            smart_str(unicode(data.GSCAFB_Gender)),
                            smart_str(unicode(data.GSCAFB_Marital_Status)),
                            smart_str(unicode(data.GSCAFB_Date_of_Birth)),
                            smart_str(unicode(data.EI_Employment_Type)),
                            smart_str(unicode(data.EI_Primary_Occupation)),
                            smart_str(unicode(data.EI_Employer_Name)),
                            smart_str(unicode(data.EI_Employee_Number)),
                            smart_str(unicode(data.EI_Employment_Date)),
                            smart_str(unicode(data.EI_Income_Band)),
                            smart_str(unicode(data.EI_Salary_Frequency)),
                            smart_str(unicode(data.pci.PCI_Building_Unit_Number)),
                            smart_str(unicode(data.pci.PCI_Building_Name)),
                            smart_str(unicode(data.pci.PCI_Floor_Number)),
                            smart_str(unicode(data.pci.PCI_Plot_or_Street_Number)),
                            smart_str(unicode(data.pci.PCI_LC_or_Street_Name)),
                            smart_str(unicode(data.pci.PCI_Parish)),
                            smart_str(unicode(data.pci.PCI_Suburb)),
                            smart_str(unicode(data.pci.PCI_Village)),
                            smart_str(unicode(data.pci.PCI_County_or_Town)),
                            smart_str(unicode(data.pci.PCI_District)),
                            smart_str(unicode(data.pci.PCI_Region)),
                            smart_str(unicode(data.pci.PCI_PO_Box_Number)),
                            smart_str(unicode(data.pci.PCI_Post_Office_Town)),
                            smart_str(unicode(data.pci.PCI_Country_Code)),
                            smart_str(unicode(data.pci.PCI_Period_At_Address)),
                            smart_str(unicode(data.pci.PCI_Flag_of_Ownership)),
                            smart_str(unicode(data.pci.PCI_Primary_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.pci.PCI_Primary_Number_Telephone_Number)),
                            smart_str(unicode(data.pci.PCI_Other_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.pci.PCI_Other_Number_Telephone_Number)),
                            smart_str(unicode(data.pci.PCI_Mobile_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.pci.PCI_Mobile_Number_Telephone_Number)),
                            smart_str(unicode(data.pci.PCI_Facsimile_Country_Dialling_Code)),
                            smart_str(unicode(data.pci.PCI_Facsimile_Number)),
                            smart_str(unicode(data.pci.PCI_Email_Address)),
                            smart_str(unicode(data.pci.PCI_Web_site)),
                            smart_str(unicode(data.sci.SCI_Unit_Number)),
                            smart_str(unicode(data.sci.SCI_Unit_Name)),
                            smart_str(unicode(data.sci.SCI_Floor_Number)),
                            smart_str(unicode(data.sci.SCI_Plot_or_Street_Number)),
                            smart_str(unicode(data.sci.SCI_LC_or_Street_Name)),
                            smart_str(unicode(data.sci.SCI_Parish)),
                            smart_str(unicode(data.sci.SCI_Suburb)),
                            smart_str(unicode(data.sci.SCI_Village)),
                            smart_str(unicode(data.sci.SCI_County_or_Town)),
                            smart_str(unicode(data.sci.SCI_District)),
                            smart_str(unicode(data.sci.SCI_Region)),
                            smart_str(unicode(data.sci.SCI_PO_Box_Number)),
                            smart_str(unicode(data.sci.SCI_Post_Office_Town)),
                            smart_str(unicode(data.sci.SCI_Country_Code)),
                            smart_str(unicode(data.sci.SCI_Period_At_Address)),
                            smart_str(unicode(data.sci.SCI_Flag_for_ownership)),
                            smart_str(unicode(data.sci.SCI_Primary_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.sci.SCI_Primary_Number_Telephone_Number)),
                            smart_str(unicode(data.sci.SCI_Other_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.sci.SCI_Other_Number_Telephone_Number)),
                            smart_str(unicode(data.sci.SCI_Mobile_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.sci.SCI_Mobile_Number_Telephone_Number)),
                            smart_str(unicode(data.sci.SCI_Facsimile_Country_Dialling_Code)),
                            smart_str(unicode(data.sci.SCI_Facsimile_Number)),
                            smart_str(unicode(data.sci.SCI_Email_Address)),
                            smart_str(unicode(data.sci.SCI_Web_site)),  
                        ])
            return self.response
        except:
            raise 

class ProcessCSVFMD(ProcessCSV):
    def __init__(self, filename, dialect, row, headers, delimiter="|"):
        super(ProcessCSVFMD, self).__init__(filename, dialect)
        
        self.row = row 
        self.delimiter = delimiter
        self.headers = headers 
        
        if(self.headers):
            self.write_headers(self.headers)
            
        if(self.row):
            self.writer.writerow(self.row)
            
    
    def write_row_data(self, coldata):
        try:
            for data in coldata:
                self.writer.writerow([
                            smart_str(unicode(data.id)),
                            smart_str(unicode(data.PI_Identification_Code)),
                            smart_str(unicode(data.Branch_Identification_Code)),
                            smart_str(unicode(data.Client_Number)),
                            smart_str(unicode(data.Consumer_Classification)),
                            smart_str(unicode(data.Category_Code)),
                            smart_str(unicode(data.Sub_Category_Code)),
                            smart_str(unicode(data.Incident_Date)),
                            smart_str(unicode(data.Loss_Amount)),
                            smart_str(unicode(data.Currency_Type)),
                            smart_str(unicode(data.Incident_Details)),
                            smart_str(unicode(data.Forensic_Information_Available)),
                            smart_str(unicode(data.II_Registration_Certificate_Number)),
                            smart_str(unicode(data.II_Tax_Identification_Number)),
                            smart_str(unicode(data.II_Value_Added_Tax_Number)),
                            smart_str(unicode(data.II_FCS_Number)),
                            smart_str(unicode(data.II_Passport_Number)),
                            smart_str(unicode(data.II_Drivers_Licence_ID_Number)),
                            smart_str(unicode(data.II_Voters_PERNO)),
                            smart_str(unicode(data.II_Drivers_License_Permit_Number)),
                            smart_str(unicode(data.II_NSSF_Number)),
                            smart_str(unicode(data.II_Country_ID)),
                            smart_str(unicode(data.II_Country_Issuing_Authority)),
                            smart_str(unicode(data.II_Nationality)),
                            smart_str(unicode(data.II_Police_ID_Number)),
                            smart_str(unicode(data.II_UPDF_Number)),
                            smart_str(unicode(data.II_KACITA_License_Number)),
                            smart_str(unicode(data.II_Public_Service_Pension_Number)),
                            smart_str(unicode(data.II_Teacher_Registration_Number)),
                            smart_str(unicode(data.II_Country_Of_Issue)),
                            smart_str(unicode(data.GSCAFB_Business_Name)),
                            smart_str(unicode(data.GSCAFB_Trading_Name)),
                            smart_str(unicode(data.GSCAFB_Activity_Description)),
                            smart_str(unicode(data.GSCAFB_Industry_Sector_Code)),
                            smart_str(unicode(data.GSCAFB_Date_Registered)),
                            smart_str(unicode(data.GSCAFB_Business_Type_Code)),
                            smart_str(unicode(data.GSCAFB_Surname)),
                            smart_str(unicode(data.GSCAFB_Forename1)),
                            smart_str(unicode(data.GSCAFB_Forename2)),
                            smart_str(unicode(data.GSCAFB_Forename3)),
                            smart_str(unicode(data.GSCAFB_Gender)),
                            smart_str(unicode(data.GSCAFB_Marital_Status)),
                            smart_str(unicode(data.GSCAFB_Date_of_Birth)),
                            smart_str(unicode(data.EI_Employment_Type)),
                            smart_str(unicode(data.EI_Primary_Occupation)),
                            smart_str(unicode(data.EI_Employer_Name)),
                            smart_str(unicode(data.EI_Employee_Number)),
                            smart_str(unicode(data.EI_Employment_Date)),
                            smart_str(unicode(data.EI_Income_Band)),
                            smart_str(unicode(data.EI_Salary_Frequency)),
                            smart_str(unicode(data.pci.PCI_Building_Unit_Number)),
                            smart_str(unicode(data.pci.PCI_Building_Name)),
                            smart_str(unicode(data.pci.PCI_Floor_Number)),
                            smart_str(unicode(data.pci.PCI_Plot_or_Street_Number)),
                            smart_str(unicode(data.pci.PCI_LC_or_Street_Name)),
                            smart_str(unicode(data.pci.PCI_Parish)),
                            smart_str(unicode(data.pci.PCI_Suburb)),
                            smart_str(unicode(data.pci.PCI_Village)),
                            smart_str(unicode(data.pci.PCI_County_or_Town)),
                            smart_str(unicode(data.pci.PCI_District)),
                            smart_str(unicode(data.pci.PCI_Region)),
                            smart_str(unicode(data.pci.PCI_PO_Box_Number)),
                            smart_str(unicode(data.pci.PCI_Post_Office_Town)),
                            smart_str(unicode(data.pci.PCI_Country_Code)),
                            smart_str(unicode(data.pci.PCI_Period_At_Address)),
                            smart_str(unicode(data.pci.PCI_Flag_of_Ownership)),
                            smart_str(unicode(data.pci.PCI_Primary_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.pci.PCI_Primary_Number_Telephone_Number)),
                            smart_str(unicode(data.pci.PCI_Other_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.pci.PCI_Other_Number_Telephone_Number)),
                            smart_str(unicode(data.pci.PCI_Mobile_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.pci.PCI_Mobile_Number_Telephone_Number)),
                            smart_str(unicode(data.pci.PCI_Facsimile_Country_Dialling_Code)),
                            smart_str(unicode(data.pci.PCI_Facsimile_Number)),
                            smart_str(unicode(data.pci.PCI_Email_Address)),
                            smart_str(unicode(data.pci.PCI_Web_site)),
                            smart_str(unicode(data.sci.SCI_Unit_Number)),
                            smart_str(unicode(data.sci.SCI_Unit_Name)),
                            smart_str(unicode(data.sci.SCI_Floor_Number)),
                            smart_str(unicode(data.sci.SCI_Plot_or_Street_Number)),
                            smart_str(unicode(data.sci.SCI_LC_or_Street_Name)),
                            smart_str(unicode(data.sci.SCI_Parish)),
                            smart_str(unicode(data.sci.SCI_Suburb)),
                            smart_str(unicode(data.sci.SCI_Village)),
                            smart_str(unicode(data.sci.SCI_County_or_Town)),
                            smart_str(unicode(data.sci.SCI_District)),
                            smart_str(unicode(data.sci.SCI_Region)),
                            smart_str(unicode(data.sci.SCI_PO_Box_Number)),
                            smart_str(unicode(data.sci.SCI_Post_Office_Town)),
                            smart_str(unicode(data.sci.SCI_Country_Code)),
                            smart_str(unicode(data.sci.SCI_Period_At_Address)),
                            smart_str(unicode(data.sci.SCI_Flag_for_ownership)),
                            smart_str(unicode(data.sci.SCI_Primary_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.sci.SCI_Primary_Number_Telephone_Number)),
                            smart_str(unicode(data.sci.SCI_Other_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.sci.SCI_Other_Number_Telephone_Number)),
                            smart_str(unicode(data.sci.SCI_Mobile_Number_Country_Dialling_Code)),
                            smart_str(unicode(data.sci.SCI_Mobile_Number_Telephone_Number)),
                            smart_str(unicode(data.sci.SCI_Facsimile_Country_Dialling_Code)),
                            smart_str(unicode(data.sci.SCI_Facsimile_Number)),
                            smart_str(unicode(data.sci.SCI_Email_Address)),
                            smart_str(unicode(data.sci.SCI_Web_site)),
                    ])
            return self.response 
        except:
            raise 
            
                            
