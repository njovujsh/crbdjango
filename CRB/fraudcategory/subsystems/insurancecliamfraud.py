#  insurancecliamfraud.py
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
from fraudcategory.subsystems import falseid 

class InsuranceCliamFraud(falseid.FalseID):
    def __init__(self,category, code=8,length=13):
        super(InsuranceCliamFraud, self).__init__(category,code=8, length=length)
            
        self.subcategory = ["DISHONEST - MOTOR ACCIDENT", "DISHONEST - MOTOR THEFT",
                            "DISHONEST - THEFT FROM MOTOR", "DISHONEST - DEATH OR DISABILITY",
                            "INFLATED MOTOR VEHICLE", "INFLATED - PERSONAL ACCIDENT", 
                            "DISHONEST - GOODS OR SERVICES", "INFLATED - GOODS OR SERVICES", 
                            "DISHONEST - INSURANCE CLAIM", "DEATH BENEFIT-FALSE CLIAM", 
                            "FALSE RETRENCHMENT CLAIM","FALSE DISABILITY CLAIM", "OTHERS"
                            ]
