#  enf040.py
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

class ENF040(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF040, self).__init__(mobject, field, priority, action)

        self.enfo = "ENF005"
        self.mobject = mobject
        self.other_fields = ["Letter of Credit", "Guarantees", "Overdrafts","Bonds"]
        
    def validate_field(self, records, re_enfor=None):
        try:
            if(records):
                if(records.Borrowers_Client_Number is None):
                    return False
                else:
                    if(records.Last_Payment_Date < records.Credit_Account_Date):
                        if(records.Last_Payment_Date):
                            return True
                        else:
                            return False 
                        
                    elif(records.Borrowers_Client_Number.Credit_Account_or_Loan_Product_Type in self.other_fields):
                        if(records.Last_Payment_Date):
                            return True
                        else:
                            return False
                    else:
                        return True
            else:
                return False 

        except:
            raise 
    
