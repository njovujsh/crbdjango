#  enf062.py
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

from fraudcategory.subcategory import creditaccountclosure 
from validators.subsystems.enforcements import enf001 

class ENF062(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF062, self).__init__(mobject, field, priority, action)
        
        self.status = ['3','4'] 
        
    def validate_field(self, status, reason):
        try:
            #print "Status ", status, "REASONG ", reason 
            if(status in self.status):
                #print "---FOUND ONE VICTIM ", status 
                if(reason):
                    #print "-----Reason was also found to be there"
                    return True
                else:
                    return False
            else:
                return True
                '''
                if (field == s):
                    return True
                else:
                    return False
                '''
        except:
            raise 
    
    def add_status(self, newstatus):
        if(newstatus):
            self.status.append(newstatus)
            
