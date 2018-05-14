#  enf112.py
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

from fraudcategory.subcategory import creditindicator 
from fraudcategory.subcategory import creditaccountstatus 
from validators.subsystems.enforcements import enf001 

class ENF112(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF112, self).__init__(mobject, field, priority, action)

        self.enfo = "ENF005"
        self.product_type = ['6','10','11']
        
    def validate_field(self, records):
        try:
            if(records):
                if(records.Borrowers_Client_Number is None):
                    return False
                else:
                    if(records.Borrowers_Client_Number.Credit_Account_or_Loan_Product_Type in self.product_type and records.Credit_Account_Status == "4"):
                        if(records.Current_Balance_Amount):
                            return True
                        else:
                            return False 
                    else:
                        return True
            else:
                return False 
        except:
            raise 
    
    def tuple_to_dict(self, code):
        try:
            return {code[0], code[1]}
        except:
            raise
        
    def check_credit_status(self, value=4):
        for values in self.get_credit_status():
            tuples = self.tuple_to_dict(values)
            for key in tuples:
                if(key == value):
                    return True
                else:
                    return False   
                      
    def get_credit_status(self):
        return creditaccountstatus.get_status()
