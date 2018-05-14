#  validationstatus.py
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

def get_record_keys(validated_record):
    try:
        
        for key in validated_record.keys():
            yield key
    except Exception as e:
        pass  
        
def validation_status(validated_record):
    try:
        if(validated_record):
            final_status = []
            for rec_key in get_record_keys(validated_record):
                if(get_format(validated_record[rec_key]) and get_condition(validated_record[rec_key]) and get_format(validated_record[rec_key])):
                    yield rec_key 
                   
                elif(get_enf(validated_record[rec_key]) == False):
                    yield -1 #for failed enforcements
                    
                elif(get_condition(validated_record[rec_key]) == False):
                    yield -2 #for valied conditions
                    
                elif(get_format(validated_record[rec_key]) == False):
                    yield -3 #for falied format
                     
                else:
                    yield False 
    except Exception as e:
        #log
        pass  

def get_format(validated_record):
    try:
        return validated_record.get("FORMAT")
    except:
        raise 
        
def get_enf(validated_record):
    try:
        return validated_record.get("ENF")
    except Exception as e:
        pass 
        
def get_condition(validated_record):
    try:
        for key in validated_record.iterkeys():
            if(key == "Mandatory"):
                return validated_record.get(key)
            elif(key == "Conditional"):
                return validated_record.get(key)
            elif(key == "Optional"):
                return validated_record.get(key)
                
    except Exception as e:
        pass  
