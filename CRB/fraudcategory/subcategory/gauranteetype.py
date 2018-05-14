#  gaurantortype.py
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

class GuaranteeType(object):
    def __init__(self):
        self.guaranteetype = (
                            ('0', "Full"),
                            ('1', "Partial")
                          )
                          
        self.guaranteetype_dict = {
                            '0':"Full",
                            '1':"Partial"
                          }
        
        
    def get_guaranteetype(self):
        return self.guaranteetype

    def get_dict(self):
        return self.guaranteetype_dict

    def search(self, value):
        if(value):
            return self.get_dict().get(value)
            
def get_guaranteetype():
    G = GuaranteeType()
    return G.get_guaranteetype()    


