from datasetrecords import models 
from validators.subsystems import enforcement as enfs
from validators.subsystems import picode 


class IICode(picode.PICode):
    def __init__(self, bsmodel, datacode):
        super(IICode, self).__init__(bsmodel, datacode)
        
        self.modelstatus = True
        
    def join_field_rule(self, ret_all=False):
        self.results = {}
        self.ret_field = None 
        
        self.pi_code = self.make_code(self.datacode)
        
        for field in self.extract():
            try:
                if(field == "II_Registration_Certificate_Number"):
                    self.ret_field = [enfs.data_status()["conditional"], "A20",
                                       {"ENF":[enfs.get_enf_by_number(93), enfs.get_enf_by_number(95)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field) 
                elif(field == "II_Tax_Identification_Number"):
                    self.ret_field = [enfs.data_status()["conditional"], "A20",
                                       {"ENF":[enfs.get_enf_by_number(92),
                                        enfs.get_enf_by_number(93), enfs.get_enf_by_number(96)]}
                                       ]
                                       
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field) 
                
                elif(field == "II_Value_Added_Tax_Number"):
                    self.ret_field = [enfs.data_status()["conditional"], "A20",
                                       {"ENF":[enfs.get_enf_by_number(93), enfs.get_enf_by_number(97)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field) 
                    
                elif(field == "II_FCS_Number"):
                    self.ret_field = [enfs.data_status()["conditional"], "A13",
                                       {"ENF":[enfs.get_enf_by_number(12), enfs.get_enf_by_number(87),
                                         enfs.get_enf_by_number(27), enfs.get_enf_by_number(88),
                                         enfs.get_enf_by_number(89), enfs.get_enf_by_number(90),
                                         enfs.get_enf_by_number(92), enfs.get_enf_by_number(93)
                                       ]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "II_Passport_Number"):
                    self.ret_field = [enfs.data_status()["conditional"], "A20",
                                       {"ENF":[enfs.get_enf_by_number(92), enfs.get_enf_by_number(98)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "II_Drivers_Licence_ID_Number"):
                    self.ret_field = [enfs.data_status()["conditional"], "A20",
                                       {"ENF":[enfs.get_enf_by_number(92), enfs.get_enf_by_number(99)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "II_Voters_PERNO"):
                    self.ret_field = [enfs.data_status()["conditional"], "A20",
                                       {"ENF":[enfs.get_enf_by_number(92), enfs.get_enf_by_number(100)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "II_Drivers_License_Permit_Number"):
                    self.ret_field = [enfs.data_status()["conditional"], "A20",
                                       {"ENF":[enfs.get_enf_by_number(92), enfs.get_enf_by_number(101)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "II_NSSF_Number"):
                    self.ret_field = [enfs.data_status()["conditional"], "A20",
                                       {"ENF":[enfs.get_enf_by_number(92), enfs.get_enf_by_number(102)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "II_Country_ID"):
                    self.ret_field = [enfs.data_status()["conditional"], "A20",
                                       {"ENF":[enfs.get_enf_by_number(92), enfs.get_enf_by_number(103)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "II_Country_Issuing_Authority"):
                    self.ret_field = [enfs.data_status()["conditional"], "A2",
                                       enfs.get_enf_by_number(104)
                                      ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "II_Nationality"):
                    self.ret_field = [enfs.data_status()["conditional"], "A2",
                                       {"ENF":[enfs.get_enf_by_number(67), enfs.get_enf_by_number(65),enfs.get_enf_by_number(105)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "II_Police_ID_Number"):
                    self.ret_field = [enfs.data_status()["conditional"], "A20",
                                       {"ENF":[enfs.get_enf_by_number(92), enfs.get_enf_by_number(106)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "II_UPDF_Number"):
                    self.ret_field = [enfs.data_status()["conditional"], "A20",
                                        {"ENF":[enfs.get_enf_by_number(92), enfs.get_enf_by_number(107)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "II_KACITA_License_Number"):
                    self.ret_field = [enfs.data_status()["conditional"], "A20",
                                        {"ENF":[enfs.get_enf_by_number(93), enfs.get_enf_by_number(108)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "II_Public_Service_Pension_Number"):
                    self.ret_field = [enfs.data_status()["conditional"], "A20",
                                        {"ENF":[enfs.get_enf_by_number(92), enfs.get_enf_by_number(109)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "II_Teacher_Registration_Number"):
                    self.ret_field = [enfs.data_status()["conditional"], "A20",
                                        {"ENF":[enfs.get_enf_by_number(92), enfs.get_enf_by_number(110)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "II_Country_Of_Issue"):
                    self.ret_field = [enfs.data_status()["conditional"], "A2",
                                        {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(65), enfs.get_enf_by_number(104)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                else:
                    pass 
                if (ret_all == False):
                    yield self.results
            except:
                raise 
 
    
    


