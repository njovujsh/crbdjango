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

class BussinessCode(object):
    def __init__(self):
        self.bcodes = (
                        ('0', "Cooperative"),
                        ('2', "Limited by Guarantee"),
                        ('3', "Limited Liability Company"),
                        ('4', "Non-Governmental Organizations"),
                        ('5', "Partnership"),
                        ('6', "Public Instituion"),
                        ('8', "Sole Proprietorship"),
                        ('9', "Trust"),
                        ('10', "Community Based Organizations (CBOs)"),
                        ('11', "Clubs and Associations"),
                        )
                        
        self.codes = {'0':"Cooperative",
                        '2':"Limited by Guarantee",
                        '3':"Limited Liability Company",
                        '4':"Non-Governmental Organizations",
                        '5':"Partnership",
                        '6':"Public Instituion",
                        '8':"Sole Proprietorship",
                        '9':"Trust",
                        '10':"Community Based Organizations (CBOs)",
                        '11':"Clubs and Associations",
                        }
        
    def get_codes(self):
        return self.bcodes
        
    def search_code(self, value):
        return self.codes.get(value)
    
def get_bcodes():
    B = BussinessCode()
    return B.get_codes()    
