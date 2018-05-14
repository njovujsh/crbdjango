#  ccgcode.py
#  
#  Copyright 2015 Wangolo Joel <wangolo@developer>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from datasetrecords import models 
from validators.subsystems import enforcement
from validators.subsystems import picode 
from validators.subsystems import enforcement as enfs

class CMCCode(picode.PICode):
    def __init__(self, bsmodel, datacode):
        super(CMCCode, self).__init__(bsmodel, datacode)
        
        self.modelstatus = True 
    
    def join_field_rule(self, ret_all=False):
        self.results = {}
        self.ret_field = None 
        
        self.pi_code = self.make_code(self.datacode)
        
        for field in self.extract():
            try:
                
                if(field == "PI_Identification_Code"):
                    self.ret_field = [enfs.data_status()["mandatory"], "A6",
                                       {"ENF":[enfs.get_enf_by_number(68), enfs.get_enf_by_number(94)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field) 
                elif(field == "Branch_Identification_Code"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N3",
                                       {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(94)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field) 
                
                elif(field == "Borrowers_Client_Number"):
                    self.ret_field = [enfs.data_status()["mandatory"], "AS30",
                                       {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(94)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field) 
                    
                elif(field == "Borrower_Account_Reference"):
                    self.ret_field = [enfs.data_status()["mandatory"], "AS30",
                                       enfs.get_enf_by_number(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Borrower_Classification"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N1",
                                       enfs.get_enf_by_number(71)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Collateral_Type_Identification"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N2",
                                       enfs.get_enf_by_number(47)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Collateral_Reference_Number"):
                    self.ret_field = [enfs.data_status()["mandatory"], "AS20",
                                       enfs.get_enf_by_number(14)
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
                    
                elif(field == "Collateral_Open_Market_Value"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N21",
                                       enfs.get_enf_by_number(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Collateral_Forced_Sale_Value"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N21",
                                       enfs.get_enf_by_number(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "Collateral_Valuation_Expiry_Date"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N8",
                                       {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(7)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                elif(field == "Instrument_of_Claim"):
                    self.ret_field = [enfs.data_status()["mandatory"], "A30",
                                       enfs.get_enf_by_number(14)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Valuation_Date"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N8",
                                       {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(63), enfs.get_enf_by_number(7)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                else:
                    pass 
                if (ret_all == False):
                    yield self.results
                     
            except:
                raise  

        yield self.results 
