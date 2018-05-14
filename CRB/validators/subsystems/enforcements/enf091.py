#  enf091.py
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

class ENF091(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF091, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        
    def validate_field(self, record):
        try:
            if(record.Credit_Account_Date > record.Date_of_First_Payment and len(str(record.Last_Payment_Amount)) == 0):
                if(record.Credit_Account_Arrears_Date):
                    return True
                else:
                    return False
                    
            elif(record.Credit_Account_Type == "7" or record.Credit_Account_Type == "8" or record.Credit_Account_Type == "3" and len(str(record.Last_Payment_Amount)) == 0):
                if(record.Credit_Account_Arrears_Date):
                    return True
                else:
                    return False
            else:
                return True  
        except:
            raise 
            
    def validate_otherfields(self, mobject):
        try:
            for values in mobject:
                if(values.Credit_Account_Arrears_Date != 0):
                    return True
                else:
                    return False
        except:
            raise 

