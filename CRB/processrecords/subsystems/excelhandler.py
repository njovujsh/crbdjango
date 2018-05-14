#  filecsvsubsystem.py
#  
#  Copyright 2014 wangolo joel <wangolo@wangolo-3020>
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
import xlrd
import sys 
import csv
import threading 


            
#-----GRAB and read Excel data------#
class ReadExcelXLSX(object):
    """
    This class object is responsible for reading
    microsoft excel formats.
    """
    def __init__(self, filename):
        self.filename = filename 
        
    def open_xlsx(self, *filename):
        """
        Open and return the object or excel.
        """
        if(filename):
            self.set_filename(filename)
            try:
                return xlrd.open_workbook(self.get_filename())
            except:
                raise 
        else:
            try:
                return xlrd.open_workbook(self.get_filename())
            except:
                raise 
                
    def get_row_values(self, sheet_index, index):
        """
        Return the rows values.
        """
        try:
            self.work_book = self.open_xlsx()
            if(self.work_book):
                try:
                    self.first_sheet = self.work_book.sheet_by_index(sheet_index)
                    return self.first_sheet.row_values(index)
                except:
                    raise
            else:
                raise 
        except:
            raise 
            
    def get_columns(self, sheet_index):
        """
        return the columns.
        """
        self.column_list = [ ]
        try:
            self.sheet_index = self.get_sheet_by_index(sheet_index)
            return self.sheet_index
        except:
            raise 
        else:
            return self.column_list
    
    def get_num_sheets(self, *book):
        """
        get the number of sheets.
        """
        if(book):
            return book.nsheets 
        else:
            self.work_book = self.open_xlsx()
            if(self.work_book):
                return self.work_book.nsheets
                
    def get_sheet_by_index(self, index):
        self.work_book = self.open_xlsx()
        if(self.work_book):
            return self.work_book.sheet_by_index(index).name 
                
    def get_sheet_name(self, *book):
        """
        Return the name of the sheet
        """
        if(book):
            return book.sheet_names()
        else:
            self.work_book = self.open_xlsx()
            if(self.work_book):
                return self.work_book.sheet_names()
    
    def get_sheet_by_name(self, name):
        
        self.work_book = self.open_xlsx()
        try:
            return self.work_book.sheet_by_name(name)
        except xlrd.biffh.XLRDError:
            raise xlrd.biffh.XLRDError("Sheet was not found")
      
    def get_sheetname(self, sheet):
        self.work_book = self.open_xlsx()
        try:
            return sheet.name
        except:
            raise 
            
    #--Getters and Setters/ Mutators and Assesors--#
    def get_filename(self):
        """
        Return the filename.
        """
        return self.filename 
        
    def set_filename(self, filename):
        self.filename = filename 
        
if __name__=="__main__":
    ap = ReadExcelXLSX("PI_Branch_network_as_at_31_March_2014_260614.xlsx")
    #l = ap.get_row_values(0)
    num_sheets = ap.get_num_sheets()
    print ap.get_sheet_name()
    for n in range(num_sheets):
        #print ap.get_sheet_by_index(n)
        print ap.get_columns(n)
    #for i in range(num_sheets):
    #    T = SheetReaderThread(ap, ap.get_sheet_by_name(ap.get_sheet_by_index(i)), ap.get_sheetname(ap.get_sheet_by_name(ap.get_sheet_by_index(i))))
    #    T.start()
       
    #for n in range(num_rows):
    #   print "[ %d ]" % n, ap.get_row_values(0, n)
        
