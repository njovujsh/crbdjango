#  restructured.py
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

class Marital(object):
    def __init__(self):
        self.status = (
                        ('1', "Single (Never Married)"),
                        ('2', "Divorced"),
                        ('3', "Married"),
                        ('4', "Separated"),
                        ('5', "Widowed"),
                        ('6', "Annulled"),
                        ('7', "Cohabitating"),
                        ('8', "Others"),
                        )
        
        self.status_dict = {'1':"Single (Never Married)",
                        '2':"Divorced",
                        '3':"Married",
                        '4':"Separated",
                        '5':"Widowed",
                        '6':"Annulled",
                        '7':"Cohabitating",
                        '8':"Others"
                        }
        
        
    def get_status(self):
        return self.status
        
    def search_status(self, value):
        return self.status_dict.get(value)
    
def get_status():
    C = Marital()
    return C.get_status()    
