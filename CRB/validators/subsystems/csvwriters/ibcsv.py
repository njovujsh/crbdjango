#  ibcsv.py
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

class ProcessCSVIB(processcsvs.ProcessCSV):
    def __init__(self, filename, dialect, row, headers, delimiter="|", response=None):
        super(ProcessCSVIB, self).__init__(filename, dialect, response=response)
        
        self.delimiter = delimiter
        self.row = row 
        
        if(headers):
            self.write_headers(headers)
            
    def write_row_data(self, coldata):
        try:
            for data in coldata:
                self.writer.writerow([
                                self.get_data_id(),
                                smart_str(unicode(data.PI_Identification_Code.pi_identification_code )),
                                smart_str(unicode(data.Branch_Identification_Code )),
                                smart_str(unicode(data.Branch_Name )),
                                smart_str(unicode(data.Branch_Type )),
                                smart_str(unicode(data.Date_Opened)),
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
                                smart_str(unicode(data.pci.PCI_Web_site))
                        ])
            return self.response 
        except:
            raise 
            
class CSVIBValidated(pivalidatecsv.CSVPIValidated):
    def __init__(self, filename, dialect, row, headers, delimiter="|", response=None):
        super(CSVIBValidated, self).__init__(filename, dialect, row, headers, delimiter=delimiter, response=response)
        #filename, dialect, row, headers, delimiter="|"
        self.delimiter = delimiter
        self.row = row 
        
    def write_row_data(self, coldata, val):
        try:
            
            self.validated_field = self.validate_and_return(val)
            self.pi_field = self.load_validated_field(self.validated_field.get("PI_Identification_Code"))
            self.bic_field = self.load_validated_field(self.validated_field.get("Branch_Identification_Code"))
            self.branch_name = self.load_validated_field(self.validated_field.get("Branch_Name"))
            self.branch_field = self.load_validated_field(self.validated_field.get("Branch_Type"))
            self.date_field = self.load_validated_field(self.validated_field.get("Date_Opened"))
            
            self.date_field = self.replace_date(self.date_field)
            
            self.pci_validation = pcivalidate.PCIValidate()
            self.pci_validation.begin_validation()
            self.validated_pci_dict = self.pci_validation.get_real_dict()
            
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
            
            for data in coldata:
                self.writer.writerow([
                            self.get_data_id(),
                            self.value_in(smart_str(unicode(data.PI_Identification_Code)), self.pi_field), 
                            self.value_in(smart_str(unicode(data.Branch_Identification_Code)), self.bic_field), 
                            self.value_in(smart_str(unicode(data.Branch_Name)), self.branch_name), 
                            self.value_in(smart_str(unicode(data.Branch_Type)), self.branch_field),
                            self.value_in(smart_str(unicode(data.Date_Opened.replace("-", "", len(data.Date_Opened)))), self.date_field),
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
                        ])
            return self.response 
        except:
            raise 
            
    
    def load_validated_field(self, field):
        
        self.appendlist = []
        for f in validationstatus.validation_status(field):
            self.appendlist.append(f)
        return self.appendlist
        
    def validate_and_return(self, module):
        try:
            self.v = module.begin_validation()
            return module.get_real_dict()
        except:
            raise 
            
    def value_in(self, data, l):
        if(data in l):
            return data 
        else:
            pass  
