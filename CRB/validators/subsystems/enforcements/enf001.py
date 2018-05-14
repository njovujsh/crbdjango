#  enfrules.py
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


class ENF001(object):
    def __init__(self, mobject, field, priority, action, value=3):
        self.field = field
        self.priority = priority
        self.action = action 
        self.mobject = mobject
        self.value = value 
        self.validation_result = { }
        
    def validate_field(self, field):
        
        if(field):
            try:
                if(field.Credit_Account_Status == "3"):
                    if(field.Current_Balance_Amount and field.Credit_Account_Arrears_Date):
                        return True
                    else:
                        return False 
                else:
                    return True
                    
            except ValueError as error:
                pass  
            except:
                pass 
        else:
            return False 
                
    def get_field(self):
        for fields in self.mobject.objects.all():
            yield fields 
                    
    def set_field(self, newfield):
        self.field = newfield 
        
    def get_all(self):
        for i in self.field:
            yield i
            
    def validate_otherfields(self, field):
        """
        Validate other fields associated with the credit status
        """
        try:
            if(field):
                for mobject in field.obejcts.all():
                    if(mobject.Current_Balance_Amount != 0 and mobject.Credit_Account_Arrears_Date != 0 and mobject.Credit_Amount != 0):
                        return True 
                    else:
                        return False 
            else:
                return False 
        except:
            raise 
    
    def set_result(self, field, status):
        self.validation_result[field]=status 
        
    def get_result(self):
        return self.validation_result
    
    def set_value(self, newvalue):
        self.value = newvalue
        
    def get_priority(self):
        return self.priority
