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


class SalaryFrequency(object):
    def __init__(self):
        self.frequency = (
                    ('0',"Annually"), 
                    ('1',"Daily"),
                    ('2', "Fortnightly"),
                    ('3', "Irregular Schedule"),
                    ('4', "Monthly"), 
                    ('5', "Quarterly"), 
                    ('6',"Semi / Half Yearly"),
                    ('7',"Weekly"),
                    ('8',"Others"),
                    )
                    
        self.frequency_dict = {
                    '0':"Annually", 
                    '1':"Daily",
                    '2':"Fortnightly",
                    '3':"Irregular Schedule",
                    '4':"Monthly", 
                    '5':"Quarterly", 
                    '6':"Semi / Half Yearly",
                    '7':"Weekly",
                    '8':"Others"
                    }
                    
    def get_frequency(self):
        return self.frequency 
        
    def search_frequency(self, value):
        return self.frequency_dict.get(value)

def get_class_freq():
    credit = SalaryFrequency()
    return credit.get_frequency()

