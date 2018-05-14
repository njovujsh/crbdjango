#  enf047.py
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
from fraudcategory.subcategory import collateralclassification


class ENF047(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF047, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        
        self.collateral = collateralclassification.CollateralClassification()
        
    def validate_field(self, field):
        try:
            if(self.collateral.get_value(field)):
                return True
            else:
                return False  
        except:
            raise 
    
    def get_classification(self):
        try:
            return collateralclassification.get_collateral()
        except:
            raise 
            
    def other_fields(self, field, *varss):
        """
        """
        if(field in varss):
            return True
        else:
            return False 
            
        

