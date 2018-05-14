#  riskclassification.py
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

class CreditAccountStatus(object):
    def __init__(self):
        self.status = (
                ('1', "Outstanding and beyond terms"),
                ('2', "Restructured credit facility - a new facility is creted after the previous account is settled"),
                ('3',  "Write-off"),
                ('4',  "Fully Paid"),
                ('5', "Current and Within Terms"),
                ('6', "Written Off Recovery"),
                )
               
         
    def get_status(self):
        return tuple(self.status)
        
    def add_new_risk(self, code, status):
        if(code and status):
            self.status.append((code, status))
        else:
            return False 
            
    def search_value(self, code):
        self.dictify = self.tuple_to_dict(self.status)
        return self.dictify.get(code)

    def tuple_to_dict(self, tuples):
        d = {}
        for v in tuples:
            d[v[0]]=v[1]
        return d
        
    def search_code(self, code):
        def tuple_to_dict(self, tuple_two):
            if(len(tuple_two) != 3):
                return None 
            else:
                try:
                    return {tuple_two[0], tuple_two[1]}
                except:
                    raise
                    
        for code in self.get_status():
            for key in tuple_to_dict(code):
                if(code == key):
                    return key 
                else:
                    return None 

def get_status():
    R = CreditAccountStatus()
    return R.get_status()

def get_dict_version():
    R = CreditAccountStatus()
    return R.tuple_to_dict(R.get_status())

