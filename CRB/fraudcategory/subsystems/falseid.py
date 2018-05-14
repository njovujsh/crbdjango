#  falseid.py
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
class FalseID(object):
    def __init__(self, category, code=1, length=7):
        self.category = category
        self.length = length 
        self.code = code 
        self.subcategory = ["FALSE NAME ", "FALSE IDENTIFICATION",
                            "FALSE SURNAME", "FALSE ADDRESS",
                            "USING IDENTITY OF DECEASED",
                            "USING IDENTITY OF OTHERS"
                            ]
                            
    def make_subcategory(self, *listc):
        self.subdict = {}
        self.num = self.gen_num()
        self.return_category = {}
        
        for i in self.subcategory:
            try:
                self.subdict[str(i)]=str(self.num.next())
            except StopIteration as error:
                pass 
            
        self.return_category[self.get_category()]=self.subdict 
        return self.return_category
        
    def gen_num(self):
        for i in range(1, self.length+1):
            yield str(i)
            
    def yield_one(self, num=1):
        for i in range(self.length):
            yield str(num )
    
    def get_category(self):
        return self.category
   
    def add_newcategory(self, new):
        self.subcategory.append(new)
        
    def get_subcategory(self):
        return self.subcategory
        
    def get_subcategory_by_dict(self):
        return self.make_subcategory()
        
    def get_code(self):
        return self.code 
        
