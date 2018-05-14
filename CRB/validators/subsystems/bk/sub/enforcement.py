#  enforcement.py
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

import string 
from collections import Counter 


enforcements = { }
priorities = { }
status = { }

def construct_enforn(enforce_code, store, range_value):
    try:
        if(range_value != 0):
            for i in range(1, range_value + 1):
                formated = enforce_code + "%03d" % (i,)
                store[i]=formated 
            return store 
        else:
            return None 
    except:
        raise 
        
def get_enforcement():
    return construct_enforn("ENF", enforcements, 150)
    
g = get_enforcement()
for i in g:
    print g[i]
    
def priority(store, range_value):
    try:
        if(range_value != 0):
            for i in range(1, range_value + 1):
                store[i]=i
            return store 
        else:
            return None
    except:
        raise 

        
def data_status():
    try:
        status["mandatory"]="M"
        status["optional"]="O"
        status["conditional"]="C"
        return status  
    except:
        raise 

