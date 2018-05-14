#  excelwriter.py
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

import csv
import threading 
import time 
import unicodecsv 
import os 

class ExcelWriter(object):
    """
    Object used by threadings to write
    excel files.
    """
    def __init__(self, excel_object, sheetname, threadname):
        
        
        self.excel_object = excel_object
        self.sheetname = sheetname
        self.writelock = threading.Lock()
        self.csvlock = threading.Lock()
        self.filepath = None

    def create_csvobject(self, fileobject, qoutechar='"', delimiter=",", dialect=csv.excel):
        """
        Create and return the csv object.
        """
        try:
            self.csvlock.acquire()
            try:
                return unicodecsv.UnicodeWriter(fileobject,encoding='utf-8', quotechar=qoutechar, quoting=csv.QUOTE_ALL, delimiter=delimiter, dialect=dialect)
            except:
                raise 
            finally:
                if(self.csvlock.locked()):
                    self.csvlock.release()
        except:
            raise 
        finally:
            if(self.csvlock.locked()):
                self.csvlock.release()
                
    def write_contents(self, thread, csvwriter, rowdata):
        try:
            self.writelock.acquire()
            try:
                csvwriter.writerow(tuple(rowdata))
            except UnicodeEncodeError as error:
                print error 
            else:
                self.writelock.release()
        except:
            raise 
        finally:
            if(self.writelock.locked()):
                self.writelock.release()
                
            
    def openfilename(self, path):
        """
        Return a filename opened for writing
        """
        try:
            return open(path, "wb")
        except:
            raise 
            
    def get_path(self):
        return self.filepath
        
if __name__=="__main__":
    a = ExcelWriter("joel", "wangolo", "wangolo")
    b = a.create_csvobject()
