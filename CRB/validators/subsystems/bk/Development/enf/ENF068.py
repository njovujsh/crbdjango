#  ENF068.py
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
import  ENF086 

class ENF068(ENF086.ENF086):
    def __init__(self):
        super(ENF068, self).__init__()
        
        self._enf068_dict = { }
        
        self.cb_len = 28
        self.ci_len = 5
        self.mdi_len = 8
        
        #This methods will be called automatically
        self.construct_cb("CB", self.cb_len)
        self.construct_ci("CI", self.ci_len)
        self.construct_mdi("MDI", self.mdi_len) 
        
    def get_cb_len(self):
        return self.cb_len 
    def get_ci_len(self):
        return self.ci_len 
    def get_mdi_len(self):
        return self.mdi_len
        
    def set_mdi_len(self, newlen):
        self.mdi_len = newlen
    def set_cb_len(self, newlen):
        self.cb_len = newlen
    def set_ci_len(self, newlen):
        self.ci_len = newlen 
    
    def construct_cb(self, code, cb_len):
        """
        Given the cb_len automatically generate the
        code.
        """
        if(cb_len):
            for c in range(1, cb_len+1):
                self.c_code = code + "%03d" % (c,)
                self.set_code(self.c_code, self.c_code)
    
    def construct_ci(self, code, ci_len):
        if(ci_len):
            for ci in range(1, ci_len):
                self.ci_code = code + "%03d" % (ci,)
                self.set_code(self.ci_code, self.ci_code)
                
    def construct_mdi(self, code, mdi_len):
        if(mdi_len):
            for mdi in range(1, mdi_len):
                self.mdi_code = code + "%03d" % (mdi,)
                self.set_code(self.mdi_code, self.mdi_code)
    
    def set_code(self, key, value):
        self._enf068_dict[key]=value 
    
    def get_enf068_codes(self):
        return self._enf068_dict 
        
    def get_code(self, code):
        if(code):
            try:
                return self.get_enf068_codes().get(code)
            except KeyError as error:
                return "Code not found"
            except:
                print "Error retreiving code"
        else:
            return None 
                
if __name__=="__main__":
    e = ENF068()
    
