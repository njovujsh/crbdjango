from datasetrecords import models 
from validators.subsystems import enforcement as enfs
from validators.subsystems import picode 



class IBCode(picode.PICode):
    def __init__(self, bsmodel, datacode):
        super(IBCode, self).__init__(bsmodel, datacode)
        
        self.modelstatus = True 
    
    def join_field_rule(self, ret_all=False):
        self.results = {}
        self.ret_field = None 
        
        self.pi_code = self.make_code(self.datacode)
        
        for field in self.extract():
            #print " We are inside ", field 
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
                
                elif(field == "Branch_Name"):
                    self.ret_field = [enfs.data_status()["mandatory"], "AS100",
                                       enfs.get_enf_by_number(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field) 
                    
                elif(field == "Branch_Type"):
                    self.ret_field = [enfs.data_status()["mandatory"], "A1",
                                       enfs.get_enf_by_number(70)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "Date_Opened"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N8",
                                       {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(7)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                else:
                    print "Fields are not Equal ", field 
                    
                if (ret_all == False):
                    yield self.results 
                    
            except:
                raise 
            
        yield self.results 
