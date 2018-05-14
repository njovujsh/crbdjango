#  checkstatus.py
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

def is_mandatory(status):
    if(len(status)):
        if(status == "M"):
            return True
        else:
            return False 
    else:
        return None
        
def is_conditional(status):
    if(len(status)):
        if(status == "C"):
            return True 
        else:
            return False 
    else:
        return None 
        
def is_optional(status):
    if(len(status)):
        if(status == "O"):
            return True 
        else:
            return False 
    else:
        return None 
        
    
if __name__=="__main__":
    if(is_optional("O")):
        print "Data is Optional"
        
    if(is_conditional("C")):
        print "It's conditional"
        
    if(is_mandatory("M")):
        print "It's mandatory"    

#if re.match('^[a-zA-Z0-9_]+$',playerName): 
#if playerName and re.match("^[a-zA-Z0-9]*_?[a-zA-Z0-9]*$", playerName):
#if re.match("[a-zA-Z0-9]+.",playerName):
