#  enfrules.py
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


class ENF001(object):
    def __init__(self, mobject, field, priority, action):
        self.field = field, 
        self.priority = priority
        self.action = action 
        self.mobject = mobject
        
        self.validation_result = { }
        
    def validate_field(self, *field):
        if(field):
            self.set_field(field)
            
        if(self.get_field().Credit_Account_Status == 3):
            self.validate_otherfields(self.mobject)
                
    def get_field(self):
        return self.field 
        
    def set_field(self, newfield):
        self.field = newfield 
        
    def validate_otherfields(self, mobject):
        """
        Validate other fields associated with the credit status
        """
        try:
            if(mobject):
                for v in mobject:
                    if(v.Current_Balance_Amount):
                        self.validation_result["Current_Balance_Amount"]=True
                    else:
                        self.validation_result["Current_Balance_Amount"]=False
                        
                    if(v.Credit_Account_Arrears_Date):
                        self.validation_results['Credit_Account_Arrears_Date']=True
                    else:
                        self.validation_result["Credit_Account_Arrears_Date"]=False 
                        
                    if(v.Credit_Amount):
                        self.validation_result["Credit_Amount"]=True
                    else:
                        self.validation_result["Credit_Amount"]=False 
            else:
                return False 
        except:
            raise 
    
    def get_result(self):
        return self.validation_result
