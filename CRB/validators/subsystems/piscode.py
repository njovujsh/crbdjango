from datasetrecords import models 
from validators.subsystems import enforcement as enfs
from validators.subsystems import picode



class PISCode(picode.PICode):
    def __init__(self, bsmodel, datacode):
        super(PISCode, self).__init__(bsmodel, datacode)
        
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
                    
                elif(field == "Stakeholder_Type"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N1",
                                       enfs.get_enf_by_number(71)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field) 
                
                elif(field == "Stakeholder_Category"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N2",
                                       enfs.get_enf_by_number(43)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field) 
                elif(field == "Shareholder_Percentage"):
                    self.ret_field = [enfs.data_status()["mandatory"], "D3.2",
                                       enfs.get_enf_by_number(37)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                else:
                    pass 
                    
                if (ret_all == False):
                    yield self.results
                
            except:
                raise 
                 
        yield self.results 
