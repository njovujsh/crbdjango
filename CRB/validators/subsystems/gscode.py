from datasetrecords import models 
from validators.subsystems import enforcement as enfs
from validators.subsystems import picode 


class GSCAFBCode(picode.PICode):
    def __init__(self, bsmodel, datacode):
        super(GSCAFBCode, self).__init__(bsmodel, datacode)
        
        self.modelstatus = True
        
    def join_field_rule(self, ret_all=False):
        self.results = {}
        self.ret_field = None 
        
        self.pi_code = self.make_code(self.datacode) 
        
        for field in self.extract():
            try:
                if(field == "GSCAFB_Business_Name"):
                    self.ret_field = [enfs.data_status()["conditional"], "AS100",
                                           enfs.get_enf_by_number(26)
                                           ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field,field)
                
                
                elif(field == "GSCAFB_Trading_Name"):
                    self.ret_field = [enfs.data_status()["conditional"], "AS100",
                                           enfs.get_enf_by_number(26)
                                           ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "GSCAFB_Activity_Description"):
                    self.ret_field =[enfs.data_status()["conditional"], "AS100",
                                           enfs.get_enf_by_number(26)
                                           ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field,field)
                    
                elif(field == "GSCAFB_Industry_Sector_Code"):
                    self.ret_field = [enfs.data_status()["conditional"], "N5",
                                           {"ENF":[enfs.get_enf_by_number(26), enfs.get_enf_by_number(48)]}
                                           ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "GSCAFB_Date_Registered"):
                    self.ret_field = [enfs.data_status()["conditional"], "N8",
                                           {"ENF":[enfs.get_enf_by_number(26),enfs.get_enf_by_number(5), enfs.get_enf_by_number(7)]}
                                           ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "GSCAFB_Business_Type_Code"):
                    self.ret_field = [enfs.data_status()["conditional"], "N2",
                                           {"ENF":[enfs.get_enf_by_number(26), enfs.get_enf_by_number(60)]}
                                           ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "GSCAFB_Surname"):
                    self.ret_field = [enfs.data_status()["conditional"], "AS30",
                                           enfs.get_enf_by_number(67)
                                           ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "GSCAFB_Forename1"):
                    self.ret_field = [enfs.data_status()["conditional"], "AS30",
                                           enfs.get_enf_by_number(67)
                                           ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "GSCAFB_Forename2"):
                    self.ret_field = [enfs.data_status()["optional"], "AS30",
                                           True
                                           ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "GSCAFB_Forename3"):
                    self.ret_field = [enfs.data_status()["optional"], "AS30",
                                           True
                                           ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "GSCAFB_Gender"):
                    self.ret_field = [enfs.data_status()["conditional"], "N1",
                                           {"ENF":[enfs.get_enf_by_number(67), enfs.get_enf_by_number(86)]}
                                           ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "GSCAFB_Marital_Status"):
                    self.ret_field = [enfs.data_status()["conditional"], "N2",
                                           {"ENF":[enfs.get_enf_by_number(67), enfs.get_enf_by_number(55)]}
                                           ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "GSCAFB_Date_of_Birth"):
                    self.ret_field = [enfs.data_status()["conditional"], "N8",
                                           {"ENF":[enfs.get_enf_by_number(67),enfs.get_enf_by_number(5), enfs.get_enf_by_number(7)]}
                                           ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                else:
                    pass 
                if (ret_all == False):
                    yield self.results 
            except:
                raise 
