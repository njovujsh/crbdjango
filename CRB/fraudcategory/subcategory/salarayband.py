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

class SalaryBand(object):
    def __init__(self):
        self.salary = (
                        ('9', "0 - 80,000"),
                        ('10', "80,001 - 165,000"),
                        ('11', "165,001 - 350,000"),
                        ('12', "350,001 - 650,000"),
                        ('13', "650,001 - 1,2000,000"),
                        ('14', "1,200,001 - 2,000,000"),
                        ('15', "2,000,001 - 2,800,000"),
                        ('16', "2,800,001 - 4,000,000"),
                        ('17', "4,000,001 - 6,000,000"),
                        ('19', "6,000,001, - 10,000,000"),
                        ('20', "10,000,001 - 15,000,000"),
                        ('21', "15,000,001 - 20,000,000"),
                        ('22', "20,000, 001 - Above"),
                        )
        
        self.salary_dict = {'9':"0 - 80,000",
                        '10':"80,001 - 165,000",
                        '11':"165,001 - 350,000",
                        '12':"350,001 - 650,000",
                        '13':"650,001 - 1,2000,000",
                        '14':"1,200,001 - 2,000,000",
                        '15':"2,000,001 - 2,800,000",
                        '16':"2,800,001 - 4,000,000",
                        '17':"4,000,001 - 6,000,000",
                        '19':"6,000,001, - 10,000,000",
                        '20':"10,000,001 - 15,000,000",
                        '21':"15,000,001 - 20,000,000",
                        '22':"20,000, 001 - Above"
                        }
        
        
    def get_salary(self):
        return self.salary
        
    def search_salary(self, value):
        return self.salary_dict.get(value)
    
def get_salary():
    C = SalaryBand()
    return C.get_salary()    
