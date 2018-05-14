#  csvreaders.py
#  
#  Copyright 2015 Wangolo Joel <wangolo@wangolo-OptiPlex-3020>
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

try:
    import unicodecsv.py2 as unicodecsv
except ImportError as error:
    print "Some import error"
    import unicodecsv
    
#import unicodecsv #for unicode reader
import csv #not csv



class ReadCSV(object):
    """
    CSV reader object for reading csv files.
    """
    def __init__(self, filename, **kwargs):
        
        self.filename = filename 
        if(kwargs):
            self.dialects = kwargs.get("dialect")
            
    def return_fileobject(self, filename):
        return open(filename, "rb")
        
    
    def read_csvs(self, ready_to_read=False):
        """
        Reads and write csv.
        """
        try:
            if(ready_to_read):
                #self.fileobject = self.return_fileobject(self.filename)
                self.reader = unicodecsv.UnicodeReader(self.filename)
                self.reader.next()
                for row in self.reader:
                    yield row 
            else:
                self.fileobject = self.return_fileobject(self.filename)
                self.reader = unicodecsv.UnicodeReader(self.fileobject)
                self.reader.next()
                for row in self.reader:
                    yield row
        except:
            raise 
       

if __name__=="__main__":
    r = ReadCSV("CBA-Client_Uploads3.csv")
    print r.read_csvs()
