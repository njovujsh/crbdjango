#  creditapprejectionreason.py
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


class CreditAPPRejectionReason(stakeholdercategory.StakeHolderCategory):
    def __init__(self):
        super(CreditAPPRejectionReason, self).__init__()
        
        self.values = (
                ('1', "Exceed sectoral exposure"), ('2', "Exceed single customer limit"),
                ('3', "Existing facility not utilized for intended purpose"),
                ('4', "History of credit default"), ('5',"Inadequate capital commitment/high gearing"),
                ('6', "Inadequate collateral"), ('7', "Industry risk"), ('8',"Low utilization for existing facility"),
                ('9', "Management risk concern"), ('10', "Over dependence on single buyer or supplier"),
                ('11', "Purpose not consistent with business objectives"), ('14', "Forged collaterals"),
                ('15', "Contravenes internal policies"), ('16', "Forged documents"), ('17', "Contravene laws"),
                ('18', "Contravenes regulations"), ('19', "Contravene guidelines"), ('13',"Other Reasons")
                )
                
    def get_values(self):
        return self.values 

    def dictify(self, tuples):
        """
        Given a list of tuple dictify them.
        """
        self.tuple_2_dict = {}
        for t in tuples:
            for i in range(len(t)):
                self.tuple_2_dict[t[0]]=t[1]
        return self.tuple_2_dict
        
def get_reject_reason():
    Credit = CreditAPPRejectionReason()
    return Credit.get_values()

def get_dict_reason():
    Credit = CreditAPPRejectionReason()
    return Credit.dictify(Credit.get_values())
                      
    
