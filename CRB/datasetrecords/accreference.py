#  accreference.py
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
import random 
import string 
from fraudcategory.appendix import apendx15
from CRB import settings
from datasetrecords import models as datamodels

producttype = apendx15.Appendix15()

FORMAT  = "%Y-%m-%d-%H-%M-%S-%w"
FORMAT  = "%Y-%m-%d-%H-%S-%w"

def get_now():
    return datetime.datetime.now()
    
def formats(date, formated=None):
    if(formated):
        return date.strftime(formated)
    else:
        return date.strftime(settings.REFERENCE_FORMAT)

def get_combined_case():
    letters = string.lowercase + string.uppercase 
    return random.choice(letters)
    
DATE =  formats(get_now()).replace('-', "", 10)[::-1]

def get_reference_number(ptype, clientnumber, numtimes=None):
    """
    Given the ID return the ptype.
    """
    current_date = get_now()
    format_date = formats(current_date)
    format_date = format_date.replace("-", "", len(format_date))
    product = product_representation(ptype)
    clientnumbers = ""
    
    if(clientnumber):
        try:
            clientnumbers = int(float(clientnumber))
        except:
            print "ERROR CONVERTING TO INT "
            pass 
    try:
        if(numtimes):
            if(product):
                format_date = formats(current_date)
                format_date = format_date.replace("-", "", len(format_date))
                #shuffled = shuffle_them(format_date[::-1])
                final_reference = str(format_date) + str(clientnumbers) + ":" + str(product)+ ":" + str(numtimes)
                return final_reference
            else:
                format_date = formats(current_date)
                format_date = format_date.replace("-", "", len(format_date))
                #shuffled = shuffle_them(format_date[::-1])
                final_reference = str(format_date) + str(clientnumbers) + ":" + str(numtimes)
                return final_reference
        else:
            if(product):
                format_date = formats(current_date, settings.REFERENCE_FORMAT_TWO)
                format_date = format_date.replace("-", "", len(format_date))
                #shuffled = shuffle_them(format_date[::-1])
                final_reference = str(format_date) + str(clientnumbers) + ":" + str(product)
                return final_reference
            else:
                format_date = formats(current_date, settings.REFERENCE_FORMAT_TWO)
                format_date = format_date.replace("-", "", len(format_date))
                #shuffled = shuffle_them(format_date[::-1])
                final_reference = str(format_date) + str(clientnumbers)
                return final_reference
    except:
        raise 

def shuffle_them(strings):
    if(strings):
        strings = list(strings)
        random.shuffle(strings)
        return "".join(strings)

def product_representation(product_type):
    """
    Given the product type perform a look up on our table and return.
    """
    try:
        value = producttype.get_productclassification(product_type)
        if(value):
            return value
        else:
            return False
    except:
        raise

def index_last_digit(ref_num):
    return ref_num[-1:]

def split_ret_last_or_first(ref_num, get_ref_only=False, last_=True, split_by=":"):
    r = ref_num.split(split_by)
    if(get_ref_only):
        return r[0]
    else:
        if(last_):
            return r[-1:][0]
        else:
            return r[1][:-1]

def increment_index(num):
    try:
        num = int(num)
        num += 1
        return num
    except:
        pass


def query_reference_numbers(reference_number):
    try:
        ref = datamodels.BorrowerHistory.objects.get(account_reference=reference_number)
        return ref
    except:
        raise

def query_all_user_history(QUERY):
    try:
        return QUERY.history.all()
    except:
        raise
        
def filter_queried_by_ptype(all_query, ptype):
    ava = []
    
    if(all_query):
        for Q in all_query:
            splited = Q.account_reference.split(":")
            if(len(splited) == 3):
                if ptype == splited[-2]:
                    ava.append(Q.account_reference)
            else:
                if ptype == splited[-1]:
                    ava.append(Q.account_reference)
        return ava

def split_item_in_list(list_item):
    splited = {}
    for items in list_item:
        splited[items.split(":")[-1]] = items 
    return splited

def filter_max(splited_dict):
    keys = splited_dict.keys()
    return max(keys)

def new_increment_return(ref, ptype, num=1):
    try:
        return str(ref) + ":" + str(ptype) + ":" + str(num)
    except:
        raise
            
def update_reference_number(reference_number, ptype, record, numtimes):
    try:
        product_type = product_representation(ptype)
        if(":" in reference_number):

            #Query all references.
            all_references =  query_all_user_history(record)
            print "HERE ", all_references
            #Attempt a filter
            filtered = filter_queried_by_ptype(all_references, product_type)
            print "FILTERED ", filtered
            if(filtered):
                dictify = split_item_in_list(filtered)
                print "DICTIFY ", dictify
                max_borrow = filter_max(dictify)
                print 'MAX BORROW', max_borrow
                final_ref = dictify.get(max_borrow)
                
                current_ref = split_ret_last_or_first(final_ref, get_ref_only=True)
                p_type = split_ret_last_or_first(final_ref, last_=False)
                num_times = split_ret_last_or_first(final_ref, last_=True)
                
                inc = increment_index(int(max_borrow))
                new_ref_by = current_ref + ":" + str(product_type) + ":" + str(inc)
                return new_ref_by
                
            else:
                current_ref = split_ret_last_or_first(reference_number, get_ref_only=True)
                print "Current REF", current_ref
                return new_increment_return(current_ref, product_type)
            
        else:
            return reference_number 
    except:
        raise 
