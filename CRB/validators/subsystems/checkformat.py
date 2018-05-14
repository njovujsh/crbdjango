#  checkformat.py
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

import re

def compile_re_pattern(stri):
    """
    Given the string return the compiled version
    in regular expression format.
    """
    try:
        if(stri):
            return re.compile(stri)
        else:
            return None 
    except:
        raise 
        
    
def extract_numbers(stri):
    """
    Given the string extract the numbers in that
    string.
    """
    try:
        if(stri):
            return re.findall("\d+", stri)
        else:
            return None 
    except:
        raise 
 
''' 
def is_alapnumeric(s):
    try:
        #string = re.compile('^[a-zA-Z0-9_]+$')    
        string = re.compile(r"^[a-zA-Z]+.*")
        if(string):
            if(string.match(s)):
                return True
            else:
                return False
        else:
            return False 
    except:
        raise 
'''
       
def is_alapnumeric(s):
    try:   
        string_with_alpha = re.compile(r"^[a-zA-Z]+.*\d+$")

        if(string_with_alpha):
            if(string_with_alpha.match(s)):
                return True
            else:
                return False
        else:
            return False 
    except:
        raise 

def sub_alphanumeric(s):
    try:   
        string_with_alpha = re.compile(r"^[a-zA-Z]+.*")

        if(string_with_alpha):
            if(string_with_alpha.match(s)):
                return True
            else:
                return False
        else:
            return False 
    except:
        raise 
        
def is_numeric(s):
    try:
        return str(s).isdigit()
    except:
        raise 

def is_float(s):
    try:
        if(float(s)):
            return True
        else:
            return False
    except ValueError as error:
        return False 
        

def has_numerics(input_string):
    return any(char.isdigit() for char in input_string)

def has_numerics_re(input_string):
    return bool(re.search(r'\d', input_string))
    
