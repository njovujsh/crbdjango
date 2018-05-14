from validators.subsystems.csvwriters import processcsvs
from django.utils.encoding import smart_str 
from validators.subsystems.datasets import validationstatus 
from django.http import HttpResponse
from validators.subsystems.datasets import pcivalidate 
from validators.subsystems.datasets import scivalidate 

class CSVPIValidated(processcsvs.ProcessCSV):
    def __init__(self,filename, dialect, row, headers, delimiter="|",response=None):
        super(CSVPIValidated, self).__init__(filename, dialect,delimiter,response=response)
        
        self.delimiter = delimiter
        self.row = row 
        
        if(headers):
            self.write_headers(headers)
         
    def write_row_data(self, coldata, val):
        try:
            self.validated_field = self.validate_and_return(val)
            
            #handle the pcivalidation
            self.pci_validation = pcivalidate.PCIValidate()
            #self.sci_validation = scivalidate.SCIValidate()
            
            #self.sci_validation.begin_validation()
            self.pci_validation.begin_validation()
            self.validated_pci_dict = self.pci_validation.get_real_dict()
            #self.validated_sci_dict = self.sci_validation.get_real_dict()
            
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
            
            #self.SCI_Unit_Number =  self.load_validated_field(self.validated_sci_dict.get("SCI_Unit_Number"))
            #self.SCI_Unit_Name =  self.load_validated_field(self.validated_sci_dict.get("SCI_Unit_Name"))
            #self.SCI_Floor_Number =  self.load_validated_field(self.validated_sci_dict.get("SCI_Floor_Number"))
            #self.SCI_Plot_or_Street_Number =  self.load_validated_field(self.validated_sci_dict.get("SCI_Plot_or_Street_Number"))
            #self.SCI_LC_or_Street_Name =  self.load_validated_field(self.validated_sci_dict.get("SCI_LC_or_Street_Name"))
            #self.SCI_Parish =  self.load_validated_field(self.validated_sci_dict.get("SCI_Parish"))
            #self.SCI_Suburb =  self.load_validated_field(self.validated_sci_dict.get("SCI_Suburb"))
            #self.SCI_Village =  self.load_validated_field(self.validated_sci_dict.get("SCI_Village"))
            #self.SCI_County_or_Town =  self.load_validated_field(self.validated_sci_dict.get("SCI_County_or_Town"))
            #self.SCI_District =  self.load_validated_field(self.validated_sci_dict.get("SCI_District"))
            #self.SCI_Region =  self.load_validated_field(self.validated_sci_dict.get("SCI_Region"))
            #self.SCI_PO_Box_Number =  self.load_validated_field(self.validated_sci_dict.get("SCI_PO_Box_Number"))
            #self.SCI_Post_Office_Town =  self.load_validated_field(self.validated_sci_dict.get("SCI_Post_Office_Town"))
            #self.SCI_Country_Code =  self.load_validated_field(self.validated_sci_dict.get("SCI_Country_Code"))
            #self.SCI_Period_At_Address =  self.load_validated_field(self.validated_sci_dict.get("SCI_Period_At_Address"))
            #self.SCI_Flag_of_Ownership =  self.load_validated_field(self.validated_sci_dict.get("SCI_Flag_for_ownership"))
            #self.SCI_Primary_Number_Country_Dialling_Code =  self.load_validated_field(self.validated_sci_dict.get("SCI_Primary_Number_Country_Dialling_Code"))
            #self.SCI_Primary_Number_Telephone_Number =  self.load_validated_field(self.validated_sci_dict.get("SCI_Primary_Number_Telephone_Number"))
            #self.SCI_Other_Number_Country_Dialling_Code =  self.load_validated_field(self.validated_sci_dict.get("SCI_Other_Number_Country_Dialling_Code"))
            #self.SCI_Other_Number_Telephone_Number = self.load_validated_field(self.validated_sci_dict.get("SCI_Other_Number_Telephone_Number"))
            #self.SCI_Mobile_Number_Country_Dialling_Code =  self.load_validated_field(self.validated_sci_dict.get("SCI_Mobile_Number_Country_Dialling_Code"))
            #self.SCI_Mobile_Number_Telephone_Number =  self.load_validated_field(self.validated_sci_dict.get("SCI_Mobile_Number_Telephone_Number"))
            #self.SCI_Facsimile_Country_Dialling_Code =  self.load_validated_field(self.validated_sci_dict.get("SCI_Facsimile_Country_Dialling_Code"))
            #self.SCI_Facsimile_Number =  self.load_validated_field(self.validated_sci_dict.get("SCI_Facsimile_Number"))
            #self.SCI_Email_Address =  self.load_validated_field(self.validated_sci_dict.get("SCI_Email_Address"))
            #self.SCI_Web_site =  self.load_validated_field(self.validated_sci_dict.get("SCI_Web_site"))
            
            self.pi_field = self.load_validated_field(self.validated_field.get("PI_Identification_Code"))
            self.it_field = self.load_validated_field(self.validated_field.get("Institution_Type"))
            self.in_field = self.load_validated_field(self.validated_field.get("Institution_Name"))
            self.date_field = self.load_validated_field(self.validated_field.get("License_Issuing_Date")) #.replace("-", "", len(self.validated_field.get("License_Issuing_Date")))
            
            self.date_field = self.replace_date(self.date_field)
            
            for data in coldata:
                self.writer.writerow([
                            self.get_data_id(),
                            self.value_in(smart_str(unicode(data.PI_Identification_Code)), self.pi_field, field=None), 
                            self.value_in(smart_str(unicode(data.Institution_Type)), self.it_field), 
                            self.value_in(smart_str(unicode(data.Institution_Name)), self.in_field), 
                            self.value_in(smart_str(unicode(data.License_Issuing_Date.replace("-", "", len(data.License_Issuing_Date)))), self.date_field),
                            self.value_in(smart_str(unicode(data.pci.PCI_Building_Unit_Number)), self.PCI_Building_Unit_Number),
                            self.value_in(smart_str(unicode(data.pci.PCI_Building_Name)), self.PCI_Building_Name),
                            self.value_in(smart_str(unicode(data.pci.PCI_Floor_Number)), self.PCI_Floor_Number),
                            self.value_in(smart_str(unicode(data.pci.PCI_Plot_or_Street_Number)), self.PCI_Plot_or_Street_Number),
                            self.value_in(smart_str(unicode(data.pci.PCI_LC_or_Street_Name)), self.PCI_LC_or_Street_Name),
                            self.value_in(smart_str(unicode(data.pci.PCI_Parish)), self.PCI_Parish),
                            self.value_in(smart_str(unicode(data.pci.PCI_Suburb)), self.PCI_Suburb),
                            self.value_in(smart_str(unicode(data.pci.PCI_Village)), self.PCI_Village),
                            self.value_in(smart_str(unicode(data.pci.PCI_County_or_Town)), self.PCI_County_or_Town),
                            self.value_in(smart_str(unicode(data.pci.PCI_District)), self.PCI_District),
                            self.value_in(smart_str(unicode(data.pci.PCI_Region)), self.PCI_Region),
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
                            #'''
                            #self.value_in(smart_str(unicode(data.sci.SCI_Unit_Number)), self.SCI_Unit_Number),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Unit_Name)), self.SCI_Unit_Name),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Floor_Number)), self.SCI_Floor_Number),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Plot_or_Street_Number)), self.SCI_Plot_or_Street_Number),
                            #self.value_in(smart_str(unicode(data.sci.SCI_LC_or_Street_Name)), self.SCI_LC_or_Street_Name),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Parish)), self.SCI_Parish),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Suburb)), self.SCI_Suburb),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Village)), self.SCI_Village),
                            #self.value_in(smart_str(unicode(data.sci.SCI_County_or_Town)), self.SCI_County_or_Town),
                            #self.value_in(smart_str(unicode(data.sci.SCI_District)), self.SCI_District),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Region)), self.SCI_Region),
                            #self.value_in(smart_str(unicode(data.sci.SCI_PO_Box_Number)), self.SCI_PO_Box_Number),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Post_Office_Town)), self.SCI_Post_Office_Town),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Country_Code)), self.SCI_Country_Code),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Period_At_Address)), self.SCI_Period_At_Address),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Flag_for_ownership)), self.SCI_Flag_of_Ownership),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Primary_Number_Country_Dialling_Code)), self.SCI_Primary_Number_Country_Dialling_Code),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Primary_Number_Telephone_Number)), self.SCI_Primary_Number_Telephone_Number),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Other_Number_Country_Dialling_Code)), self.SCI_Other_Number_Country_Dialling_Code),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Other_Number_Telephone_Number)), self.SCI_Other_Number_Telephone_Number),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Mobile_Number_Country_Dialling_Code)), self.SCI_Mobile_Number_Country_Dialling_Code),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Mobile_Number_Telephone_Number)), self.SCI_Mobile_Number_Telephone_Number),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Facsimile_Country_Dialling_Code)), self.SCI_Facsimile_Country_Dialling_Code),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Facsimile_Number)), self.SCI_Facsimile_Number),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Email_Address)), self.SCI_Email_Address),
                            #self.value_in(smart_str(unicode(data.sci.SCI_Web_site)), self.SCI_Web_site)
                            #'''
                        ])
            return self.response 
        except:
            raise 
            
    
    def load_validated_field(self, field):
        
        self.appendlist = []
        #print "FIELD ", field 
        for f in validationstatus.validation_status(field):
            self.appendlist.append(f)
        return self.appendlist
        
    def validate_and_return(self, module):
        try:
            self.validator = module.begin_validation()
            return module.get_real_dict()
        except:
            raise 
            
    def value_in(self, data, l, field=None):
        self.failed = 0
        if(data in l):
            return data 
        else:
            pass 
          
    def replace_date(self, d):
        self.date_dict = []
        for date in d:
            self.date_dict.append(str(date).replace("-", "", len(str(date))))
        return self.date_dict
        
    
class ProcessCSVPI(processcsvs.ProcessCSV):
    def __init__(self, filename, dialect, row, headers, delimiter="|",response=None):
        super(ProcessCSVPI, self).__init__(filename, dialect,delimiter=delimiter,response=response)
        
        self.delimiter = delimiter
        #print "DELIMTER ", self.delimiter
        self.row = row
        
        if(headers):
            self.write_headers(headers)
         
    def write_row_data(self, coldata):
        try:
            for data in coldata:
                #print "Writing rows"
                self.writer.writerow([
                            self.get_data_id(),
                            smart_str(unicode(data.PI_Identification_Code)), 
                            smart_str(unicode(data.Institution_Type)), 
                            smart_str(unicode(data.Institution_Name)), 
                            smart_str(unicode(data.License_Issuing_Date.replace("-", "", len(data.License_Issuing_Date)))),
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
                            #smart_str(unicode(data.pci.PCI_Primary_Number_Country_Dialling_Code)),  
                            smart_str(unicode(data.pci.PCI_Primary_Number_Telephone_Number)),  
                            #smart_str(unicode(data.pci.PCI_Other_Number_Country_Dialling_Code)),  
                            smart_str(unicode(data.pci.PCI_Other_Number_Telephone_Number)),  
                            #smart_str(unicode(data.pci.PCI_Mobile_Number_Country_Dialling_Code)),  
                            smart_str(unicode(data.pci.PCI_Mobile_Number_Telephone_Number)),  
                            #smart_str(unicode(data.pci.PCI_Facsimile_Country_Dialling_Code)),  
                            smart_str(unicode(data.pci.PCI_Facsimile_Number)), 
                            smart_str(unicode(data.pci.PCI_Email_Address)),  
                            smart_str(unicode(data.pci.PCI_Web_site)),  
                            #'''
                            #smart_str(unicode(data.sci.SCI_Unit_Number)),  
                            #smart_str(unicode(data.sci.SCI_Unit_Name)),  
                            #smart_str(unicode(data.sci.SCI_Floor_Number)), 
                            #smart_str(unicode(data.sci.SCI_Plot_or_Street_Number)),  
                            #smart_str(unicode(data.sci.SCI_LC_or_Street_Name)),  
                            #smart_str(unicode(data.sci.SCI_Parish)),  
                            #smart_str(unicode(data.sci.SCI_Suburb)),  
                            #smart_str(unicode(data.sci.SCI_Village)),  
                            #smart_str(unicode(data.sci.SCI_County_or_Town)),  
                            #smart_str(unicode(data.sci.SCI_District)), 
                            #smart_str(unicode(data.sci.SCI_Region)),  
                            #smart_str(unicode(data.sci.SCI_PO_Box_Number)),  
                            #smart_str(unicode(data.sci.SCI_Post_Office_Town)),  
                            #smart_str(unicode(data.sci.SCI_Country_Code)), 
                            #smart_str(unicode(data.sci.SCI_Period_At_Address)),  
                            #smart_str(unicode(data.sci.SCI_Flag_for_ownership)),  
                            #smart_str(unicode(data.sci.SCI_Primary_Number_Country_Dialling_Code)),  
                            #mart_str(unicode(data.sci.SCI_Primary_Number_Telephone_Number)),  
                            #smart_str(unicode(data.sci.SCI_Other_Number_Country_Dialling_Code)),  
                            #smart_str(unicode(data.sci.SCI_Other_Number_Telephone_Number)),  
                            #smart_str(unicode(data.sci.SCI_Mobile_Number_Country_Dialling_Code)),  
                            #smart_str(unicode(data.sci.SCI_Mobile_Number_Telephone_Number)),  
                            #smart_str(unicode(data.sci.SCI_Facsimile_Country_Dialling_Code)),  
                            #smart_str(unicode(data.sci.SCI_Facsimile_Number)),  
                            #smart_str(unicode(data.sci.SCI_Email_Address)),
                            #smart_str(unicode(data.sci.SCI_Web_site))
                            #'''
                        ])
            return self.response 
        except:
            raise 
