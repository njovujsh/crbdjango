from datasetrecords import models 
from validators.subsystems import enforcement
from validators.subsystems import picode 
from validators.subsystems import enforcement as enfs

class CAPCode(picode.PICode):
    def __init__(self, bsmodel, datacode):
        super(CAPCode, self).__init__(bsmodel, datacode)
        
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
                
                elif(field == "Client_Number"):
                    self.ret_field = [enfs.data_status()["optional"], "AS30",
                                       enfs.get_enf_by_number(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field) 
                    
                elif(field == "Credit_Application_Reference"):
                    self.ret_field = [enfs.data_status()["mandatory"], "AS30",
                                       enfs.get_enf_by_number(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Applicant_Classification"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N1",
                                       enfs.get_enf_by_number(71)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Credit_Application_Date"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N8",
                                       {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(5), enfs.get_enf_by_number(7)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Amount"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N21",
                                       enfs.get_enf_by_number(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "Currency"):
                    self.ret_field = [enfs.data_status()["mandatory"], "A3",
                                       {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(50)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Credit_Account_or_Loan_Product_Type"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N2",
                                       enfs.get_enf_by_number(61)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Credit_Application_Status"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N1",
                                       enfs.get_enf_by_number(41)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Last_Status_Change_Date"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N8",
                                       {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(63), enfs.get_enf_by_number(7)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Credit_Application_Duration"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N5",
                                       enfs.get_enf_by_number(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Rejection_Reason"):
                    self.ret_field = [enfs.data_status()["conditional"], "N2",
                                       {"ENF":[enfs.get_enf_by_number(42), enfs.get_enf_by_number(64)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Client_Consent_flag"):
                    self.ret_field = [enfs.data_status()["mandatory"], "A1",
                                       enfs.get_enf_by_number(78)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                else:
                    pass 
                if (ret_all == False):
                    yield self.results
                     
            except:
                raise  

        yield self.results 


