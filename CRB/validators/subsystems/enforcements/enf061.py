#  enf061.py
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
from fraudcategory.appendix import apendx15

class ENF061(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF061, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        
        self.apndx = apendx15.Appendix15()
        
    def validate_field(self, field):
        try:
            if(self.apndx.find_value(str(field))):
                return True
            else:
                return False
        except:
            raise 
    
    def get_apendx(self):
        return apendx15.get_apnx()
        
    def gen_numbers(self, length=10):
        try:
            for i in range(1, length+1):
                yield i
        except:
            pass 

