#  applicationclassification.py
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

class ApplicantClassification(object):
    def __init__(self):
        self.class_ = ["Individual", "Non Individual"]
        self.class_dict = {}
        
        self.application_class = (
                                    ("0", "Individual"),
                                   ("1", "Non Individual")
                                 )
        
        self.stake = stakeholdercategory.StakeHolderCategory()
        
    def match_by_code(self):
        for i in self.class_:
            for  r in self.make_code():
                self.class_dict[i]=r
        return self.class_dict 
            
    def make_code(self):
        for i in range(2):
            yield i 
        
    def return_in_tuple(self):
        self.ret_list = [ ]
        for i in self.make_code():
            self.ret_list.append(self.stake.make_tuple(str(i), self.class_[i]))
        return self.ret_list
    

def get_app_class():
    A = ApplicantClassification()
    return A.return_in_tuple()
