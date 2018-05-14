#  filenaming.py
#  
#  Copyright 2015 wangolo joel <wangolo@wangolo-3020>
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

import datetime 

def format_todays(date_format=None):
    """
    Format and return the current date of today.
    """
    FORMAT=None 
    
    if(date_format == None):
        FORMAT="%Y-%m-%d"
        return FORMAT 
    else:
        FORMAT=date_format
        return FORMAT
    
def get_todays_date():
    """
    Return todays date.
    """
    return datetime.datetime.today()

        

def format_todays_date(date, formats):
    """
    Given the date and form return formated.
    """
    if(date and formats):
        return date.strftime(formats)
    else:
        return False 
        
#print format_todays_date(get_todays_date(), format_todays())

def purge_dashed(data):
    """
    Replace the dashed of our date.
    """
    return str(data).replace("-", "", len(str(data)))
    
#print purge_dashed(format_todays_date(get_todays_date(), format_todays()))

def make_filename(pi_code, filename, ext=".csv"):
    """
    Given the pi_code and filename,
    return the required combination of names.
    """
    try:
        gen_date = purge_dashed(format_todays_date(get_todays_date(), format_todays()))
        filedate = gen_date + filename + ext
        return pi_code.pi_identification_code + filedate
    except:
        raise
        
def make_filename2(pi_code, filename, ext=".csv"):
    """
    Given the pi_code and filename,
    return the required combination of names.
    """
    try:
        gen_date = purge_dashed(format_todays_date(get_todays_date(), format_todays()))
        filedate = gen_date + filename + ext
        return pi_code + filedate
    except:
        raise 
        
#print make_filename("CRB001", "PI")
