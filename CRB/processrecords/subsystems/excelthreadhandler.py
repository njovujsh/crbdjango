#  excelthreadhandler.py
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

import threading 
import sys
import traceback
import time 
import excelwriter 
from django.utils.encoding import smart_str 
import os 

class ExcelSheetReaderThread(threading.Thread):
    """
    Threads responsible for reading sheets
    Threads will be executed based on number of
    sheets.
    """
    def __init__(self, xl_object, sheetname, name, index, path, endswith=".csv"):
        super(ExcelSheetReaderThread, self).__init__(name=name)
        
        self.names = sheetname
        self.path = path 
        self.xlx_lock = threading.Lock()
        self.xlobject = xl_object
        self.index = index 
        self.excelwriter = excelwriter.ExcelWriter(xl_object, self.names.name, self.names.name)
        
        self.endswith = endswith #".csv"
        self.csvname = str(self.names.name) + self.endswith
        
        self.filepath = os.path.join(self.path, self.csvname)
        
        print "Am running ", self.getName()
    def run(self):
        """
        Real heavey duty is being performed right
        here.
        """
        try:
            self.xlx_lock.acquire()
            
            print "Sheets", self.xlobject.get_num_sheets()
            rows =  self.names.nrows 
           
            print "\n\n------------Threading [ %s ] Am starting -----------------\n" % self.names.name 
            self.openfile = self.excelwriter.openfilename(self.filepath)
            self.excelfile = self.excelwriter.create_csvobject(self.openfile)
            
            for r in range(rows):
                content = self.xlobject.get_row_values(int(self.index), r)
                
                self.excelfile.writerows(tuple(content))
                #print "Writing ", self.openfile
                
            self.xlx_lock.release()
        except:
            raise  
    
    def get_path(self):
        return self.filepath
