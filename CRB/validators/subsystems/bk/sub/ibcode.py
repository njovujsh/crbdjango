from datasetrecords import models 
from validators.subsystems import enforcement
from validators.subsystems import picode 



class IBCode(picode.PICode):
    def __init__(self, bsmodel, datacode):
        super(IBCode, self).__init__(bsmodel, datacode)
        
        self.modelstatus = True 
    
    def join_field_rule(self, ret_all=False):
        self.results = {}
        self.ret_field = None 
        
        self.pi_code = self.make_code(self.datacode)
        
        #loop through all records
        for field in self.extract():
            try:
                if(field == "PI_Identification_Code"):
                    self.ret_field = [enforcement.data_status()["mandatory"], "A6",
                                       self.enforce.get(68)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field) 
                elif(field == "Branch_Identification_Code"):
                    self.ret_field = [enforcement.data_status()["mandatory"], "N3",
                                       self.enforce.get(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field) 
                
                elif(field == "Branch_Name"):
                    self.ret_field = [enforcement.data_status()["mandatory"], "AS100",
                                       self.enforce.get(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field) 
                elif(field == "Branch_Type"):
                    self.ret_field = [enforcement.data_status()["mandatory"], "A1",
                                       self.enforce.get(70)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "Date_Opened"):
                    self.ret_field = [enforcement.data_status()["mandatory"], "N8",
                                       self.enforce.get(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                else:
                    pass 
                    
            except:
                pass 
        yield self.results 



