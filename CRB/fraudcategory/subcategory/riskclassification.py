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

class RiskClassification(object):
    def __init__(self):
        self.risk = [
                ('1', "Substandard"),
                ('2', "Watch"),
                ('3',  "Doubtful"),
                ('4',  "Loss"),
                ('5', "Normal")
                ]
                
        self.riskd = {
                '1':"Substandard",
                '2':"Watch",
                '3':"Doubtful",
                "4":"Loss",
                '5':"Normal"
                }
               
         
    def get_risk(self):
        return tuple(self.risk)
        
    def add_new_risk(self, code, risk):
        if(code and risk):
            self.risk.append((code, risk))
        else:
            return False 
            
    def search_value(self, code):
        if(code):
            return self.riskd.get(code)
    
    def tuple_to_dict(self, tuple_two):
        if(len(tuple_two) != 3):
            return None 
        else:
            try:
                return {tuple_two[0], tuple_two[1]}
            except:
                raise
                    
def get_risk():
    R = RiskClassification()
    return R.get_risk()
