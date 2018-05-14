#  creditindicator.py
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

from fraudcategory.subcategory import stakeholdercategory


class PropertyOwner(object):
    def __init__(self):
        self.propertyes = (
                    ('O',"Owner"), 
                    ('T',"Tenant"),
                    ('R',"Others"),
                    )
                    
        self.propert_dict = {
                    'O':"Owner", 
                    'T':"Tenant",
                    'R':"Others",
                    }
                    
    def get_propertyes(self):
        return self.propertyes 
        
    
    def get_p_dict(self, v):
        return self.propert_dict.get(v)
        
def get_class_owner():
    propertys = PropertyOwner()
    return propertys.get_propertyes()
