#  stakeholdercategory.py
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

class StakeHolderCategory(object):
    def __init__(self, values=None, codes=None):
        self.values = ["Directory", "Manager", "Shareholder", 
                        "Director Shareholder", "Signatory",
                        "Entrepreneur/Owner"
                    ]
                    
        self.category_dict  = {}
        #populate the values if stakehoder category
        self.add_category()
        
    def add_category(self):
        try:
            for i in self.gen_numbers():
                try:
                    self.category_dict[str(i)] = self.values[i] #= str(i)
                except:
                    raise                     
        except:
            raise 
        return self.category_dict
         
    def get_stake(self, v):
        return self.category_dict.get(v)
        
    def make_tuple(self, x, y):
        return (str(x), str(y))
        
    def get_values_in_tuple(self):
        self.value_list = []
        for i in self.gen_numbers():
            try:
                self.value_list.append(self.make_tuple(str(i), str(self.values[i])))
            except:
                raise 
        return tuple(self.value_list)
        
    def gen_numbers(self, length=None, start=None):
        if(length==None):
            if(start):
                for i in range(start, len(self.values)):
                    yield i 
            else:
                for i in range(len(self.values)):
                    yield i 
        else:
            if(start):
                for i in range(start, length):
                    yield i
            else:
                for i in range(length):
                    yield i  
    
    def percentage(self):
        self.percentage_list = []
        for i in self.gen_numbers(length=501, start=1):
            try:
                self.per = "%.2f" % float(i)
                self.percentage_list.append(self.make_tuple(self.per, self.per + " %"))
            except:
                raise 
        return tuple(self.percentage_list)
        
def get_category():
    try:
        S = StakeHolderCategory()
        return S.get_values_in_tuple()
    except:
        raise 
        

def get_percentage():
    try:
        S = StakeHolderCategory()
        return S.percentage()
    except:
        raise
if __name__=="__main__":
    
    S = StakeHolderCategory()
    print S.get_values_in_tuple()
    #print S.gen_numbers().next()
    print S.add_category()
