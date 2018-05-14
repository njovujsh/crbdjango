from datasetrecords import models 
from validators.subsystems import enforcement
from validators.subsystems import picode 

class CBACode(picode.PICode):
    def __init__(self, bsmodel, datacode):
        super(CBACode, self).__init__(bsmodel, datacode)
        
        self.modelstatus = True 
    
    def join_field_rule(self, ret_all=False):
        self.results = {}
        self.ret_field = None 
        
        self.pi_code = self.make_code(self.datacode)
        
        #loop through all records
        for field in self.extract():
            try:
                if(field == ""):
                    pass 
            except:
                pass 





