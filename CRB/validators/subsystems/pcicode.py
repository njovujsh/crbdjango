from datasetrecords import models 
from validators.subsystems import enforcement as enfs
from validators.subsystems import picode 


class PCICode(picode.PICode):
    def __init__(self, pcimodel, datacode):
        super(PCICode, self).__init__(pcimodel, datacode) 
    
    
        self.modelstatus = True 
    
    def join_field_rule(self, ret_all=False):
        
        self.results = {}
        self.ret_field = None 
        
        self.pi_code = self.make_code(self.datacode)
        for field in self.extract():
            try:
                if(field == "PCI_Building_Unit_Number"):
                    self.ret_field = [enfs.data_status()["conditional"], "AS10",
                                       enfs.get_enf_by_number(21)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_Building_Name"):
                    self.ret_field = [enfs.data_status()["conditional"], "AS50",
                                       enfs.get_enf_by_number(21)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_Floor_Number"):
                    self.ret_field = [enfs.data_status()["conditional"], "AS10",
                                       enfs.get_enf_by_number(21)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_Plot_or_Street_Number"):
                    self.ret_field = [enfs.data_status()["optional"], "AS10",
                                       True
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_LC_or_Street_Name"):
                    self.ret_field = [enfs.data_status()["optional"], "AS50",
                                       True
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_Parish"):
                    self.ret_field = [enfs.data_status()["conditional"], "AS50",
                                       {"ENF":[enfs.get_enf_by_number(36), enfs.get_enf_by_number(49)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_Suburb"):
                    self.ret_field = [enfs.data_status()["optional"], "AS50",
                                       True
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_Village"):
                    self.ret_field = [enfs.data_status()["optional"], "AS50",
                                       True
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_County_or_Town"):
                    self.ret_field = [enfs.data_status()["conditional"], "AS10",
                                       {"ENF":[enfs.get_enf_by_number(36), enfs.get_enf_by_number(49)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_District"):
                    self.ret_field = [enfs.data_status()["conditional"], "AS50",
                                       {"ENF":[enfs.get_enf_by_number(36), enfs.get_enf_by_number(49)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_Region"):
                    self.ret_field = [enfs.data_status()["conditional"], "N1",
                                       {"ENF":[enfs.get_enf_by_number(36), enfs.get_enf_by_number(54)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_PO_Box_Number"):
                    self.ret_field = [enfs.data_status()["conditional"], "A10",
                                       enfs.get_enf_by_number(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_Post_Office_Town"):
                    self.ret_field = [enfs.data_status()["conditional"], "A20",
                                       enfs.get_enf_by_number(21)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_Country_Code"):
                    self.ret_field = [enfs.data_status()["mandatory"], "A2",
                                       {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(65)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_Period_At_Address"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N3",
                                       enfs.get_enf_by_number(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_Flag_of_Ownership"):
                    self.ret_field = [enfs.data_status()["mandatory"], "A1",
                                       enfs.get_enf_by_number(84)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_Primary_Number_Country_Dialling_Code"):
                    self.ret_field = [enfs.data_status()["conditional"], "N5",
                                       enfs.get_enf_by_number(56)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_Primary_Number_Telephone_Number"):
                    self.ret_field = [enfs.data_status()["conditional"], "N10",
                                       True
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_Other_Number_Country_Dialling_Code"):
                    self.ret_field = [enfs.data_status()["conditional"], "N5",
                                       enfs.get_enf_by_number(56)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_Other_Number_Telephone_Number"):
                    self.ret_field = [enfs.data_status()["conditional"], "N10",
                                       True
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_Mobile_Number_Country_Dialling_Code"):
                    self.ret_field = [enfs.data_status()["conditional"], "N5",
                                       enfs.get_enf_by_number(56)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_Mobile_Number_Telephone_Number"):
                    self.ret_field = [enfs.data_status()["conditional"], "N10",
                                       True
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_Facsimile_Country_Dialling_Code"):
                    self.ret_field = [enfs.data_status()["conditional"], "N5",
                                       enfs.get_enf_by_number(56)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_Facsimile_Number"):
                    self.ret_field = [enfs.data_status()["conditional"], "N10",
                                      True
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_Email_Address"):
                    self.ret_field = [enfs.data_status()["conditional"], "AS50",
                                       True
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "PCI_Web_site"):
                    self.ret_field = [enfs.data_status()["conditional"], "AS50",
                                       True
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                else:
                    pass 
                if (ret_all == False):
                    yield self.results
                    
            except:
                raise 
        yield self.results        
