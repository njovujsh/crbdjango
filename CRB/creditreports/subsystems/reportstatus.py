#  reportstatus.py
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

import numpy as np


class ReportStatus(object):
    """
    Object providing the reporting of 
    failed records.
    """
    def __init__(self, model_data, records=None):
        self.model_data  = model_data
        self.records = records 
        self.passed = 0
        self.failed = 0 
        
        self.data_count = self.model_data.count()
        
    def evaluate_records(self, v_record):
        """
        Perform an evaluation of records.
        """
        if((self.get_mandatory(v_record) == True) and (self.get_enforcement(v_record) == True) and self.get_format(v_record) == True):
            return True
        else:
            return False
            
    def get_mandatory(self, records):
        """
        Given the records
        return the status of the 
        mandatory.
        """
        if(records):
            if(records.get("Mandatory")):
                return records.get("Mandatory")
                
            elif(records.get("Conditional")):
                return records.get("Conditional")
                
            else:
                return records.get("Optional")
        else:
            return False 
        
    def get_enforcement(self, records):
        """
        Return the status of the enforcements.
        """
        if(records):
            return records.get("ENF")
        else:
            return False 
            
    def get_format(self, records):
        """
        Get the formats.
        """
        if(records):
            return records.get("FORMAT")
        else:
            return False 
        
    def analyse_failed_passed(self, r):
        """
        Returns the number of failed records.
        """
        for key in r.itervalues():
            for value, keys in enumerate(key):
                for v_values in key.get(keys).itervalues():
                    if(self.evaluate_records(v_values) == True):
                        self.passed += 1
                    else:
                        self.failed += 1
   
    def get_failed(self):
        return self.failed
        
    def get_passed(self):
        return self.passed
        
    def get_data_count(self):
        return self.data_count
        

