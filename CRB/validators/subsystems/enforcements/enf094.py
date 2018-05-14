#  enf094.py
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
from CRB import settings 
from validators.subsystems.enforcements import enf001 
from validators.subsystems import startswithnum 

class ENF094(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF094, self).__init__(mobject, field, priority, action)
        
        self.status = False 
        
    def validate_field(self, value, headers=None, compare_b=False, compare_pi=False, b_client=False):
        try:
            if(compare_b):
                if(value):
                    if(value.strip().lstrip().rstrip() == settings.BRANCH_IDENTIFICATION_CODE):
                        return True
                    else:
                        return False
                else:
                    return False
            elif(compare_pi):
                if(value):
                    if(value == settings.PI_IDENTIFICATION):
                        return True
                    else:
                        return False
                else:
                    return False

            elif(b_client):
                if(value):
                    return True
                else:
                    return False 
        except:
            raise 
            
    def match_pi(self, picode):
        pass 
