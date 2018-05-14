#  enf058.py
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
from fraudcategory.subcategory import paymentfrequency 

class ENF058(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF058, self).__init__(mobject, field, priority, action)

        self.enfo = "ENF005"
        self.product_type = [6,10,11]
        self.frequency = paymentfrequency.PaymentFrequency()

        self.dictify = self.frequency.dictify()
        
    def validate_field(self, records):
        try:
            if(records):
                if(records.Credit_Payment_Frequency):
                    if(self.dictify.get(records.Credit_Payment_Frequency)):
                        return True
                    else:
                        return False 
                else:
                    return False 
            else:
                return False
        except:
            raise 
    
    def tuple_to_dict(self, code):
        try:
            return {code[0], code[1]}
        except:
            raise
            
    def get_credit_status(self):
        return paymentfrequency.get_status()
