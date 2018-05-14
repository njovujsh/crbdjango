from datasetrecords import models 
from validators.subsystems import enforcement
from validators.subsystems import picode 
from validators.subsystems import enforcement as enfs

class FMDCode(picode.PICode):
    def __init__(self, bsmodel, datacode):
        super(FMDCode, self).__init__(bsmodel, datacode)
        
        self.modelstatus = True 
    
    def join_field_rule(self, ret_all=False):
        self.results = {}
        self.ret_field = None 
        
        self.pi_code = self.make_code(self.datacode)
        
        for field in self.extract():
            try:
                
                if(field == "PI_Identification_Code"):
                    self.ret_field = [enfs.data_status()["mandatory"], "A6",
                                       enfs.get_enf_by_number(68)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field) 
                elif(field == "Branch_Identification_Code"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N3",
                                       enfs.get_enf_by_number(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field) 
                
                elif(field == "Borrowers_Client_Number"):
                    self.ret_field = [enfs.data_status()["conditional"], "AS30",
                                       enfs.get_enf_by_number(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field) 
                    
                elif(field == "Consumer_Classification"):
                    self.ret_field = [enfs.data_status()["conditional"], "N1",
                                       enfs.get_enf_by_number(71)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Category_Code"):
                    self.ret_field = [enfs.data_status()["conditional"], "N2",
                                       enfs.get_enf_by_number(51)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Sub_Category_Code"):
                    self.ret_field = [enfs.data_status()["conditional"], "N2",
                                       enfs.get_enf_by_number(52)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Incident_Date"):
                    self.ret_field = [enfs.data_status()["conditional"], "N8",
                                       {"ENF":[enfs.get_enf_by_number(13), enfs.get_enf_by_number(7)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "Collateral_Description"):
                    self.ret_field = [enfs.data_status()["mandatory"], "AS1000",
                                       enfs.get_enf_by_number(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Collateral_Currency"):
                    self.ret_field = [enfs.data_status()["mandatory"], "A3",
                                       {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(50)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Loss_Amount"):
                    self.ret_field = [enfs.data_status()["conditional"], "N21",
                                       enfs.get_enf_by_number(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Currency_Type"):
                    self.ret_field = [enfs.data_status()["conditional"], "A3",
                                       enfs.get_enf_by_number(50)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Incident_Details"):
                    self.ret_field = [enfs.data_status()["conditional"], "AS1000",
                                       enfs.get_enf_by_number(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Forensic_Information_Available"):
                    self.ret_field = [enfs.data_status()["conditional"], "A1",
                                       enfs.get_enf_by_number(83)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                else:
                    pass 
                if (ret_all == False):
                    yield self.results
                     
            except:
                raise  

        yield self.results 

