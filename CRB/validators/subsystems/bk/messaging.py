#  messaging.py
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


class Messaging(object):
    """
    MSG object.
    """
    def __init__(self):
        self.NONENFORCMENT = (
            "There is no enforcment rule attached to this filed",
            "The Values is clear of enforcments" ),
            
        self.ENF007 = "Must be Date Authentic, with format YYYYMMDD(e.g. 20103102 is invalid, 20100115 is valid)"
        
        self.ENF129 = (
                    "Fields characters must be composed of only alphabetic-numeric and non-ASCII characters",
                    "These are defined in section 3. Dataset Submission Status and Data Field Formats." )
                    
        self.ENF014 = ("Field must not be empty" )
        self.ENF069 = ( "Must be equal to one of the following","CB, MDI, PI, CP, PSB, MEB, MOB, AH, FH, DH" )
        
         
