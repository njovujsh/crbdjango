#  formats.py
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

class Format(object):
    def __init__(self):
        self.formats = ['A1', 'A2',  'A6',  'A3',  'A20',  'AS100',  'N8',  'N1',  
                    'N3',  'AS10',  'AS50',  'A10',  'A50',  'N5',  'N10']
        self.format_dict = { }
        
        self.construct_formats()
        
    def construct_formats(self):
        for f in self.formats:
            self.format_dict[f]=f
            
    def get_format(self, f):
        try:
            return self.format_dict.get(f)
        except KeyError as error:
            raise 
        except:
            raise 
