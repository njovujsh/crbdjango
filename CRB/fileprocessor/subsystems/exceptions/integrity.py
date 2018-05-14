#  integrity.py
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


class IntegrityErrors(object):
    def __init__(self, error):
        self.error = error 
        self.error_list = {}
        
        self.append_error()
        
    def append_error(self):
        self.error_list["Severity"]="Very Low"
        self.error_list["Messsage"]="Data with that ID already exists"
        self.error_list["System Condition"]="Good and Stable"
        self.error_list["ERROR message "]=self.error

    def add_new_error(self, code, error):
        self.error_list[code]=error 
        
    def get_error(self):
        return self.error_list

#s = IntegrityErrors("Wangolo")
#print s.get_error()
