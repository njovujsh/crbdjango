#  enf038.py
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
from validators.subsystems.enforcements import enf001 

class ENF038(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF038, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        self.must_be_empty = False 

        self.bonds = "8"
        self.guarantees = "11"
        self.overdrafts = "7"
        
    def validate_field(self, field, records=None):
        try:
            if(records.Borrowers_Client_Number.Credit_Account_or_Loan_Product_Type == self.bonds or records.Borrowers_Client_Number.Credit_Account_or_Loan_Product_Type == self.guarantees or records.Borrowers_Client_Number.Credit_Account_or_Loan_Product_Type == self.overdrafts):
                if(records.Term):
                   return True
                else:
                    return False
            else:
                return True
        except:
            raise 
            
    
    def sub_validate(self, field):
        if(field == "Bonds" or  field == "Drafs"):
            self.must_be_empty = True 
        else:
            self.must_be_empty = False 

