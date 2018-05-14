#  enf2.py
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
from microflag import actionrules

class ENF2(object):
    """
    Enforcement handling object.
    """
    def __init__(self):
        self.ENF007 = {"P":2, "R":actionrules.get_rule("RR")}
        self.ENF001 = {"P":1, "R":actionrules.get_rule("RR")}
        self.ENF002 = {"P":2, "R":actionrules.get_rule("RR")}
        self.ENF068 = {"P":2, "R":actionrules.get_rule("RR")}
        self.ENF069 = {"P":2, "R":actionrules.get_rule("RR")}
        self.ENF129 = {"P":1, "R":actionrules.get_rule("RR")}
        self.ENF014 = {"P":1, "R":actionrules.get_rule("RR")}
        self.ENF025 = {"P":3, "R":actionrules.get_rule("ISP")}, 
        self.ENF021 = {"P":3, "R":actionrules.get_rule("ISP")}, 
        self.ENF036 = {"P":2,  "R":actionrules.get_rule("RR")}, 
        self.ENF049 = {"P":3, "R":actionrules.get_rule("ISP")}, 
        self.ENF054 = {"P":2,  "R":actionrules.get_rule("RR")}, 
        self.ENF116 = {"P":2, "R":actionrules.get_rule("RR")}, 
        self.ENF065 = {"P":2, "R":actionrules.get_rule("RR")}, 
        self.ENF084 = {"P":2, "R":actionrules.get_rule("RR")}, 
        self.ENF085 = {"P":2, "R":actionrules.get_rule("RR")}, 
        self.ENF086 = {"P":2, "R":actionrules.get_rule("RR")}, 
        self.ENF056 = {"P":2, "R":actionrules.get_rule("RR")}, 
        self.NONENFORCMENT =  {"P":0, "R":actionrules.get_rule("CL")};
        
        self.priority = None 
        
        self.action_onrule  = actionrules
        
    def get_actionrule(self):
        return self.action_onrule
        
    def set_action_onrule(self, action_ruleobj):
        self.action_onrule = action_ruleobj
        
    def get_priority(self):
        return self.priority
        
    def set_priority(self, priority):
        self.priority = priority
        
    def _enf2(self, priority, action_rule):
        self.priority = priority
        self.action_onrule = action_rule
    
