#  ENF085.py
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
import ENF086

class ENF085(ENF086.ENF086):
    def __init__(self):
        super(ENF085, self).__init__()
        
        self.formal_employment={0:"Formal Employment"}
        self.informal_employmen={1:"Informal Employment"}
        self.self_employed={2:"Self Employed"}
        self.un_employed = {3:"Unemployed"} 
        
        self.employement_status = None 
        self.employement_statuscode = None
        
    def ENF085(self, emp_code, emp_status):
        if(isinstance(emp_status, str)):
            self.employement_status = self.employement_status
            
        if(isinstance(emp_code, int)):
            self.employement_statuscode = emp_code
