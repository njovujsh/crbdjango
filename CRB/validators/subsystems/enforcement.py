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
                if(i == 111):
                    formated = enforce_code + "112"
                    store[i]=formated 
                elif(i == 112):
                    formated = enforce_code + "112"
                    store[i]=formated  
                else:
                    formated = enforce_code + "%03d" % (i,)
                    store[i]=formated 
                    
            return store 
        else:
            return None 
    except:
        raise 
            
def get_enforcement():
    return construct_enforn("ENF", enforcements, 130)

def data_status():
    try:
        status["mandatory"]="M"
        status["optional"]="O"
        status["conditional"]="C"
        return status  
    except:
        raise 

enforcement_with_priority={}

def enf_and_priority(enf):
    if(enf == "ENF001"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF002"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF003"):
        enforcement_with_priority[enf]={"P":1}
    elif(enf == "ENF004"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF005"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF006"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF007"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF008"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF009"):
        enforcement_with_priority[enf]={"P":1}
    elif(enf == "ENF010"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF011"):
        enforcement_with_priority[enf]={"P":3}
    elif(enf == "ENF012"):
        enforcement_with_priority[enf]={"P":1}
    elif(enf == "ENF013"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF014"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF015"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF016"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF017"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF018"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF019"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF020"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF021"):
        enforcement_with_priority[enf]={"P":3}
    elif(enf == "ENF022"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF023"):
        enforcement_with_priority[enf]={"P":3}
    elif(enf == "ENF024"):
        enforcement_with_priority[enf]={"P":3}
    elif(enf == "ENF025"):
        enforcement_with_priority[enf]={"P":3}
    elif(enf == "ENF026"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF027"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF028"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF029"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF030"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF031"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF032"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF033"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF034"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF035"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF036"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF037"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF038"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF039"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF040"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF041"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF042"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF043"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF044"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF045"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF046"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF047"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF048"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF049"):
        enforcement_with_priority[enf]={"P":3}
    elif(enf == "ENF050"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF051"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF052"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF053"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF054"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF055"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF056"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF057"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF058"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF059"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF060"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF061"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF062"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF063"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF064"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF065"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF066"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF067"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF068"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF069"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF070"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF071"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF072"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF073"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF074"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF075"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF076"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF077"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF078"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF079"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF080"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF081"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF082"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF083"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF084"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF085"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF086"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF087"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF088"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF089"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF090"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF091"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF092"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF093"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF094"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF095"):
        enforcement_with_priority[enf]={"P":1}
    elif(enf == "ENF096"):
        enforcement_with_priority[enf]={"P":1}
    elif(enf == "ENF097"):
        enforcement_with_priority[enf]={"P":1}
    elif(enf == "ENF098"):
        enforcement_with_priority[enf]={"P":1}
    elif(enf == "ENF099"):
        enforcement_with_priority[enf]={"P":1}
    elif(enf == "ENF100"):
        enforcement_with_priority[enf]={"P":1}
    elif(enf == "ENF101"):
        enforcement_with_priority[enf]={"P":1}
    elif(enf == "ENF102"):
        enforcement_with_priority[enf]={"P":1}
    elif(enf == "ENF103"):
        enforcement_with_priority[enf]={"P":1}
    elif(enf == "ENF104"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF105"):
        enforcement_with_priority[enf]={"P":2}
    elif(enf == "ENF106"):
        enforcement_with_priority[enf]={"P":1}
    elif(enf == "ENF107"):
        enforcement_with_priority[enf]={"P":1}
    elif(enf == "ENF108"):
        enforcement_with_priority[enf]={"P":1}
    elif(enf == "ENF109"):
        enforcement_with_priority[enf]={"P":1}
    elif(enf == "ENF110"):
        enforcement_with_priority[enf]={"P":1}
    elif(enf == "ENF112"):
        enforcement_with_priority[enf]={"P":2}
    else:
        pass 
      
    return enforcement_with_priority
    
def build_enforcements():
    for enf in get_enforcement().values():
        ret = enf_and_priority(enf)
        
    return ret 

def enforcements_and_numbers():
    store = {}
    for i in range(1, len(build_enforcements())+1):
        print i
    return store   

def get_enf_by_number(number):
    try:
        return {get_enforcement().get(number):build_enforcements().get(get_enforcement().get(number))}
    except KeyError as error:
        pass 

#print get_enforcement().get(111)
#print get_enf_by_number(111)
