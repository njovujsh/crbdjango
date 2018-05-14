from datasetrecords import models 
from validators.subsystems import enforcement
from validators.subsystems import picode 
from validators.subsystems import enforcement as enfs

class BCCode(picode.PICode):
    def __init__(self, bsmodel, datacode):
        super(BCCode, self).__init__(bsmodel, datacode)
        
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
                    self.ret_field = [enfs.data_status()["mandatory"], "AS100",
                                       enfs.get_enf_by_number(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field) 
                    
                elif(field == "PI_Client_Classification"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N1",
                                       enfs.get_enf_by_number(71)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Cheque_Account_Reference_Number"):
                    self.ret_field = [enfs.data_status()["mandatory"], "AS30",
                                       enfs.get_enf_by_number(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Cheque_Account_Opened_Date"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N8",
                                       {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(7)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "Cheque_Account_Classification"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N1",
                                       enfs.get_enf_by_number(79)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "Cheque_Account_Type"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N1",
                                       enfs.get_enf_by_number(80)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "Cheque_Number"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N10",
                                       enfs.get_enf_by_number(14)
                                       ]
                                       
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "Cheque_Amount"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N21",
                                       enfs.get_enf_by_number(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Cheque_Currency"):
                    self.ret_field = [enfs.data_status()["mandatory"], "A3",
                                       {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(50)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "Beneficiary_Name_Or_Payee"):
                    self.ret_field = [enfs.data_status()["mandatory"], "AS50",
                                       enfs.get_enf_by_number(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Cheque_Bounce_Date"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N8",
                                       {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(7)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Cheque_Account_Bounce_Reason"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N2",
                                       {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(57)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                else:
                    pass 
                    #print "Fields are not Equal ", field 
                    
                if (ret_all == False):
                    yield self.results 
                    
            except:
                raise 
  
        yield self.results 
