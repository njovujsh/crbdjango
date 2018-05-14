#  pitype.py
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

class InstitutionType(object):
    def __init__(self):
        self.ittype = (
                        ("CB", "CB --> Commercial Bank"),
                        ("MDI", "MDI --> Microfinance Deposit Taking Institution"),
                        ("CI", "CI  --> Credit Institution"),
                        ("ACP", "ACP --> Accredited Credit Providers"),
                        ("PSB", "PSB --> Post-Office Saving Bank"),
                        ("MEB", "MEB --> Merchant Bank"),
                        ("MOB", "MOB --> Mortgage Bank"),
                        ("AH", "AH --> Acceptance Houses"),
                        ("FH", "FH --> Finance Houses"),
                        ("DH", "DH --> Discount Houses"),
                        ("CP", "CP"),
                        ("PI", "PI"),
                        )
        
        
    def get_ittype(self):
        return self.ittype
    
def get_ittype():
    B = InstitutionType()
    return B.get_ittype()    

