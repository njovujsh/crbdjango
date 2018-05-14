#  enf071.py
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

class ENF071(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF071, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        self.x_one = 0
        self.x_two = 1
        
    def validate_field(self, field):
        try:
            try:
                if(field):
                    if(int(field) == self.x_one or int(field) == self.x_two):
                        return True
                    else:
                        return False
                else:
                    return False 
            except ValueError:
                return False 
            except:
                raise 
                #return None  
        except:
            raise 

"""
Aplication classification M N1, EN071
"""
