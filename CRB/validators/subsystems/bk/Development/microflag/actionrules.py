#  actionrules.py
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

class ActionRule(object):
    def __init__(self):
        self.rr = "Reject Record"
        self.isp = "Inform Submitting PI"
        self.cl = "Clear"
        
        self.rule_dict = {"RR":"Reject Record", "ISP":"Inform Submitting PI", "CL":"Clear"}
        
        self.action_taken = None 
        
    def get_actiontaken(self):
        return self.action_taken
        
    def set_actiontaken(self, action):
        self.action_taken = action 
        
    def actionrule(self, action):
        self.action_taken = action 
        
    
    def get_rule(self, code):
        try:
            if(code):
                return rule_dict.get(code.upper())
            else:
                return None 
        except:
            raise 
