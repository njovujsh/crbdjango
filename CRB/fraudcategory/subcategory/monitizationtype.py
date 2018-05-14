#  monitizationtype.py
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

class CreditMonitization(object):
    def __init__(self):
        self.status = [
                ('0', "Fixed Instalment"),
                ('1', "Straight Line"),
                ('2',  "Single Payment Loan"),
                ('3',  "Irregular Repayment Schedule"),
                ]
               
         
    def get_status(self):
        return tuple(self.status)
        
    def add_new_risk(self, code, status):
        if(code and status):
            self.status.append((code, status))
        else:
            return False 
            
    def search_value(self, code):
        def tuple_to_dict(self, tuple_two):
            if(len(tuple_two) != 3):
                return None 
            else:
                try:
                    return {tuple_two[0], tuple_two[1]}
                except:
                    raise 
          
        for codes in self.get_status():  
            if(tuple_to_dict(codes).get(code)):
                return tuple_to_dict(codes).get(code)
            else:
                return None     
    
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

    def dictify(self):
        D = {}
        for v in self.get_status():
            D[v[0]]=v[1]
        return D

def get_status():
    R = CreditMonitization()
    return R.get_status()

