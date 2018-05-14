#  ENF.py
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


class ENFO01(object):
    """
    Object handling enforcement oo1
    """
    def __init__(self, code, rules, priority):
        self.code = code 
        self.rules = self.rules 
        self.priority = priority
        
    def validate_field(self, field, *otherfield):
        if(field == 3):
            for values in otherfield:
                if(values != 0 ):
                    return values,True 
                    
                else:
                    return values,False 
                 

