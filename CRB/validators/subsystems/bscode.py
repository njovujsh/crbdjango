#  bscode.py
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
from validators.subsystems import enforcement as enfs
from validators.subsystems import picode


class BSCode(picode.PICode):
    def __init__(self, bsmodel, datacode):
        super(BSCode, self).__init__(bsmodel, datacode)
        
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
                    self.ret_field = [enfs.data_status()["mandatory"], "A30",
                                       {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(94)]}
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field) 
                    
                elif(field == "Stakeholder_Type"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N1",
                                       enfs.get_enf_by_number(71)
                                       ]
                    self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                    
                elif(field == "Stakeholder_Category"):
                    self.ret_field = [enfs.data_status()["mandatory"], "N1",
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
                    
            except:
                pass 
        yield self.results 
