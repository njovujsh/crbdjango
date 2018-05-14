#  chequebounceresons.py
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


class ChequeBounceReason(object):
    def __init__(self):
        self.reasons = (
                        ('0', "Insufficient Funds"),
                        ('17', "Cheque Unpaid and Retained Because of Suspected Activity")
                        )
        
        self.dicts = {0:"Insufficient Funds", 17:"Cheque Unpaid and Retained Because of Suspected Activity"}
        
    def get_reasons(self):
        return self.reasons
        
    def get_dict(self):
        return self.dicts 
        
        
def get_all():
    C = ChequeBounceReason()
    return C.get_reasons()
