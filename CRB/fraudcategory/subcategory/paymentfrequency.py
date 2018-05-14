#  paymentfrequency.py
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


class PaymentFrequency(object):
    def __init__(self):
        self.frequency = (
                    ('0',"Annually"), 
                    ('1',"Bullet"),
                    ('2', "Daily"),
                    ('3', "Fortnightly"),
                    ('4', "Irregular Schedule"), 
                    ('5', "Monthly"), 
                    ('6',"Other"),
                    ('7',"Quarterly"),
                    ('8',"Revolving"),
                    ('9',"Twice a year"),
                    ('10',"Weekly"),
                    ('11',"Every two months"),
                    ('12',"Thrice a year"),
                    )
                    
    def get_frequency(self):
        return self.frequency

    def dictify(self):
        D = {}
        for v in self.get_frequency():
            D[v[0]]=v[1]
        return D
        

def get_class_freq():
    credit = PaymentFrequency()
    return credit.get_frequency()

