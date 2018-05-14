#  piprocesscsvs.py
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
from django.http import HttpResponse
from django.utils.encoding import smart_str
from validators.subsystems.csvwriters import processcsvs

class ProcessCSVPI(processcsvs.ProcessCSV):
    def __init__(self, filename, dialect, row, headers, delimiter="|",response=None):
        super(ProcessCSVPI, self).__init__(filename, dialect,delimiter,response=response)
        
        self.delimiter = delimiter
        self.row = row
        
        if(headers):
            self.write_headers(headers)
         
    def write_row_data(self, coldata):
        try:
            for data in coldata:
                self.writer.writerow([
                            smart_str(unicode(data.PI_Identification_Code)), 
                            smart_str(unicode(data.Institution_Type)), 
                            smart_str(unicode(data.Institution_Name)), 
                            smart_str(unicode(data.License_Issuing_Date)),
                        ])
            return self.response 
        except:
            raise 
