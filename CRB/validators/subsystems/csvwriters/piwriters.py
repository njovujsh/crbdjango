#  piwriters.py
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

from validators.subsystems.datasets import validationstatus 
from validators.subsystems.datasets import pivalidate
import unicodecsv 
import csv 
import os 

class CSVPIWriter(object):
    def __init__(self, pivobject=None, outputname="PI0001.csv", outputpath=None):
        self.outputname=outputname
        self.outputpath=outputpath
        self.vobject = pivobject
        
    def unicodewriter_write(self, fileobject, qoutechar='"', delimiter=",", dialect=csv.excel):
        try:
            if(isinstance(fileobject, file)):
                try:
                    return unicodecsv.UnicodeWriter(fileobject,encoding='utf-8', quotechar=qoutechar, quoting=csv.QUOTE_ALL, delimiter=delimiter, dialect=dialect)
                except Exception as e:
                    return e
            else:
                return False 
        except Exception as e:
            return e 
    
    def openfilename(self, path):
        try:
            if(path):
                self.set_path(path)
                
            try:
                return open("testcsv.csv", "wa")
            except Exception as e:
                return e
        except Exception as e:
            return e 
            
    def write_validated_contents(self, validated_dict):
        try:
            self.fileobject = self.openfilename(self.get_outputname())
            if(self.fileobject):
                self.csvobject = self.unicodewriter_write(self.fileobject)
                print self.csvobject
        except:
            pass 
            
    def get_joined_path(self, filename=None):
        if(filename):
            self.set_outputname(filename)
            
        return os.path.join(self.get_path(), self.get_outputname())
        
    def set_outputname(self, name):
        self.outputname = name 
        
    def get_outputname(self):
        return self.outputname
        
    def set_path(self, path):
        self.outputpath = path 
        
    def get_path(self):
        return self.outputpath
        
    def test_pivalidate(self):
        self.PI = pivalidate.PIValidate()
        self.PI.begin_validation()
        self.D = self.PI.get_real_dict()
        
        self.f  = self.openfilename('/home/wangolo')
        self.csvs = self.unicodewriter_write(self.f)
        
        self.csvs.writerows([
                        validationstatus.validation_status(self.D.get("PI_Identification_Code")),
                        #self.D
                    ])
        self.f.close()

'''   
D = CSVPIWriter()
print D.get_path()
print D.get_outputname()
print D.set_path("/home/wangolo/Documents/")
print D.get_path()
print D.get_joined_path()
'''
