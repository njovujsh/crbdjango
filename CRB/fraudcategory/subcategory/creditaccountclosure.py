#  creditaccountclosure.py
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


class CreditAccountClosureReasons(object):
    def __init__(self):
        self.values = [
                        ('0',"Restructured"),('1', "Settled - Foreclosure"),
                       ('2', "Fully Paid"), ('3', "Written Off"),
                       ('4', "Settled - Early(Pre-paid)"),('5', "Cooling - Off")
                      ]
        
        self.stake = stakeholdercategory.StakeHolderCategory()
        
    def get_values(self):
        return tuple(self.values)
        
    def add_new(self, code, value):
        if(value and code):
            self.valus.append(self.stake.make_tuple(code, values))
        else:
            return False

    def dictify(self, value):
        self.tmp_dct = {}
        for v in value:
            for indx in range(len(v)):
                self.tmp_dct[value[0]]=value[1]
        return self.tmp_dct

def get_closure():
    closure = CreditAccountClosureReasons()
    return closure.get_values()
    
def get_closure_dict():
    closure = CreditAccountClosureReasons()
    return closure.dictify(closure.get_values())
    
