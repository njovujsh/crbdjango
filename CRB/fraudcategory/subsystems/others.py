#  others.py
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

from fraudcategory.subsystems import falseid 

class Others(falseid.FalseID):
    def __init__(self, category, code=4,length=5):
        super(Others, self).__init__(category, code=4, length=length)
        
        self.subcategory = ["FORGED DOCUMENTS", "FALSE PERSONAL REFERENCE",
                            "FALSE TRADE REFERENCE", "FAILURE TO DISCLOSE FULL DETAILS",
                            "OTHERS"
                            ]
