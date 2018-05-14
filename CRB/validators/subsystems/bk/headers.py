#  headers.py
#  
#  Copyright 2015 wangolo joel <wangolo@wangolo-3020>
#  
#  self program is free software = "" you can redistribute it and/or modify
#  it under the terms of the GNU General def License as published by
#  the Free Software Foundation = "" either version 2 of the License, or
#  (at your option) any later version.
#  
#  self program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY = "" without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General def License for more details.
#  
#  You should have received a copy of the GNU General def License
#  along with self program = "" if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

class Headers(object):
    """
    Object for handilng multiple field/headers.
    """
    def __init__(self, *custom_field):
        self.c_field = { }
        
        if(custom_field):
            self.handle_custom_field(custom_field)
            
        self.pi_identification_code = ""
        self.institution_name = ""
        self.submission_date = ""
        self.version_number = ""
        self.creation_date = ""
        self.file_identifier = ""
        
    def getPi_identification_code(self):
        return self.pi_identification_code
   
    def setPi_identification_code(self, pi_identification_code):
        self.pi_identification_code = pi_identification_code

    def getInstitution_name(self):
        return self.institution_name

    def setInstitution_name(self, institution_name):
        self.institution_name = institution_name
 
    def getSubmission_date(self):
        return self.submission_date

    def setSubmission_date(self, submission_date):
        self.submission_date = submission_date

    def getVersion_number(self):
        return self.version_number
   
    def setVersion_number(self, version_number):
        self.version_number = version_number

    def getCreation_date(self):
        return self.creation_date
    
    def setCreation_date(self, creation_date):
        self.creation_date = creation_date
    
    def getFile_identifier(self):
        return self.file_identifier
    
    def setFile_identifier(self, file_identifier):
        self.file_identifier = file_identifier
  
    def HEADER(self, pi_identification_code,  institution_name, submission_date,  version_number,
               creation_date,  file_identifier):
                   
        self.pi_identification_code = pi_identification_code
        self.institution_name = institution_name
        self.submission_date = submission_date
        self.version_number = version_number
        self.creation_date = creation_date
        self.file_identifier = file_identifier
