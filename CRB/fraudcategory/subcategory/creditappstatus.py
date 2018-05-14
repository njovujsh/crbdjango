#  creditappstatus.py
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


class CreditAppliationStatus(object):
    def __init__(self):
        self.status = (     ('0',"Approved"),
                            ('1',"Cancelled by Borrower"),
                            ('2', "Pending"),
                            ('6', "Rejected by PI"),
                            ('5', "Rejected by Borrower"),
                            ('4',"Credit Application Rejected Pre Bureau"),
                        )
                    
    def get_status(self):
        return self.status

    def tuple_to_dict(self, tuples):
        d = {}
        for v in tuples:
            d[v[0]]=v[1]
        return d
        

def get_class_status():
    credit = CreditAppliationStatus()
    return credit.get_status()
    
def get_class_dict():
    credit = CreditAppliationStatus()
    return credit.tuple_to_dict(credit.get_status())
