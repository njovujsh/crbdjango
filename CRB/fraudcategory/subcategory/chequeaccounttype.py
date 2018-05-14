#  chequeaccounttype.py
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

class ChequeAccountType(object):
    def __init__(self):
        self.cheque_types = (
                            ('0', "Individual"),
                            ('1', "Shared"),
                            )
        
        self.cheque_dict = {"0":"Individual", "1":"Shared"}
        
    def get_cheque(self):
        return self.cheque_types
    
    def check_num(self):
        return self.cheque_dict
       
def get_cheque():
    C = ChequeAccountType()
    return C.get_cheque()    
