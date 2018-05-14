#  dvr.py
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

import enf2 
import status 
import formats
import messaging 

class DVR(object):
    """
    Object holding the data validations.
    """
    def __init__(self):
        self.status = status.Status()
        self.formats = formats.Format()
        self.msg =  messaging.Messaging()
        self.enf2 = enf2.ENF2()
        
        self.PC1001 = {"ALL":"allTheTen", "Field":"PCI Unit_Number", "S":self.status.c, 
                        "F":self.formats.get_format("AS10"), "MSG":msg.ENF021, "ENF":enf2.ENF021},
                        
        self.PCI002 = {"ALL":"allTheTen", "Field":"PCI Unit Name", "S":self.status.c, 
                        "F":self.formats.get_format("AS50"), "MSG":msg.ENF021, "ENF":enf2.ENF021}
                        
        self.PCI003 = {"ALL":"allTheTen", "Field":"PCI Floor Number", "S":self.status.c, 
                        "F":self.formats.get_format("AS10"), "MSG":msg.ENF021, "ENF":enf2.ENF021}
        self.PCI004 = {"ALL":"allTheTen", "Field":"PCI Plot or Street Number", "S":self.status.o, 
                        "F":self.formats.get_format("A10"), "MSG":msg.NONENFORCMENT, "ENF":enf2.NONENFORCMENT}
                        
        self.PCI005 = {"ALL":"allTheTen", "Field":"PCI LC or Street Name", "S":STATUS.o, 
                "F":self.formats.get_format("A50"), "MSG":msg.NONENFORCMENT, "ENF":enf2.NONENFORCMENT}
                
        PCI006("allTheTen", "PCI Parish", STATUS.C, FORMAT.A50, MESSAGES.ENF049,new ENF2[] { ENF2.ENF036, ENF2.ENF049 }), 
        PCI007("allTheTen","PCI Suburb", STATUS.O, FORMAT.A50, MESSAGES.NONENFORCMENT,new ENF2[] { ENF2.NONENFORCMENT }), 
        PCI008("allTheTen","PCI Village", STATUS.O, FORMAT.A50, MESSAGES.NONENFORCMENT,new ENF2[] { ENF2.NONENFORCMENT }), PCI009("allTheTen","PCI County or Town", STATUS.C, FORMAT.A50, MESSAGES.ENF036,new ENF2[] { ENF2.ENF036, ENF2.ENF049 }), 
        PCI010("allTheTen","PCI District", STATUS.C, FORMAT.A50, MESSAGES.ENF036, new ENF2[] {ENF2.ENF036, ENF2.ENF049 }), 
        PCI011("allTheTen","PCI Region", STATUS.C, FORMAT.N1, MESSAGES.ENF036, new ENF2[] {ENF2.ENF036, ENF2.ENF054, ENF2.ENF116 }), 
        PCI012("allTheTen", "PCI PO Box Number", STATUS.C, FORMAT.A10,MESSAGES.ENF014, new ENF2[] { ENF2.ENF014 }), 
        PCI013("allTheTen","PCI Post Office Town", STATUS.C, FORMAT.A20, MESSAGES.ENF014,new ENF2[] { ENF2.ENF014 }), 
        PCI014("allTheTen","PCI Country Code", STATUS.M, FORMAT.A2, MESSAGES.ENF014,new ENF2[] { ENF2.ENF065, ENF2.ENF014 }), PCI015("allTheTen","PCI Period At Address", STATUS.M, FORMAT.N3, MESSAGES.ENF014, new ENF2[] { ENF2.ENF014, ENF2.ENF116 }), 

