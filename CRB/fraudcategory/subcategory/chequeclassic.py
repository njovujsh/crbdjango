#  chequeclassic.py
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

class ChequeClassification(object):
    def __init__(self):
        self.cheque_classific = (
                            ('0', "Individual"),
                            ('1', "Commercial"),
                            ('2', "Public Entity Account")
                            )
                            
        self.cheque_classific_dict = {'0':"Individual",
                            '1':"Commercial",
                             '2':"Public Entity Account"
                            }
      
    def get_cheque(self):
        return self.cheque_classific
    
    def get_classic(self, v):
        return self.cheque_classific_dict.get(v)
 
def get_cheque():
    C = ChequeClassification()
    return C.get_cheque()    
