#  status.py
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

class Status(object):
    m = "M"
    o = "O"
    c = "C"
    
    def get_mandatory(self):
        return self.mandatory
    def get_optional(self):
        return self.optional
    def get_conditional(self):
        return self.conditional
    
    def set_mandatory(self, m):
        self.mandatory = m 
    
    def set_optional(self, o):
        self.optional = o 
    def set_conditional(self, c):
        self.conditional =   c 
        
    def __str__(self):
        return "Mandatory:[ %s ] Conditional [ %s ] Optional [ %s ]" % (self.get_mandatory(), self.get_conditional(), self.get_optional())
    
if __name__=="__main__":
    s = Status()
    print s.get_conditional()
    print s.get_optional()
    print s.get_mandatory()
    
    s.set_mandatory("MMM")
    print s.get_mandatory()
