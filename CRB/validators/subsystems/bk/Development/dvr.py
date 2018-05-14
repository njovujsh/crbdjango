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
                        "F":self.formats.get_format("AS50"), "MSG":self.msg.ENF021, "ENF":self.enf2.ENF021}
                        
        self.PCI003 = {"ALL":"allTheTen", "Field":"PCI Floor Number", "S":self.status.c, 
                        "F":self.formats.get_format("AS10"), "MSG":self.msg.ENF021, "ENF":self.enf2.ENF021}
        self.PCI004 = {"ALL":"allTheTen", "Field":"PCI Plot or Street Number", "S":self.status.o, 
                        "F":self.formats.get_format("A10"), "MSG":self.msg.NONENFORCMENT, "ENF":self.enf2.NONENFORCMENT}
                        
        self.PCI005 = {"ALL":"allTheTen", "Field":"PCI LC or Street Name", "S":self.status.o, 
                        "F":self.formats.get_format("A50"), "MSG":self.msg.NONENFORCMENT, "ENF":self.enf2.NONENFORCMENT}
                
        self.PCI006 = {"ALL":"allTheTen", "Field":"PCI Parish", "S":self.status.c, 
                    "F":self.formats.get_format("A50"), "MSG":self.msg.ENF049 ,
                    "ENF":{"ENF2.ENF036":"ENF2.ENF036", "ENF2.ENF049":"ENF2.ENF049" }}
                    
        self.PCI007 = {"ALL":"allTheTen", "Field":"PCI Suburb", "S":self.status.o, 
                        "F":self.formats.get_format("A50"), "MSG":msg.NONENFORCMENT ,"ENF":self.enf2.NONENFORCMENT}
        
        self.PCI008 = {"ALL":"allTheTen", "Field":"PCI Village", "S":self.status.o, 
                        "F":self.formats.get_format("A50"), "MSG":self.msg.NONENFORCMENT , "ENF":self.enf2.NONENFORCMENT}
                        
        self.PCI009= {"ALL":"allTheTen", "Field":"PCI County or Town", "S":self.status.c, 
                    "F":self.formats.get_format("A50"), "MSG":self.msg.NONENFORCMENT,
                    "ENF":{"ENF2.ENF036":ENF2.ENF036, "ENF2.ENF049":ENF2.ENF049 }}
                    
        self.PCI010={"ALL":"allTheTen", "Field":"PCI District", "S":self.status.c, 
                    "F":self.formats.get_format("A50"), "MSG":self.msg.ENF036, 
                    {"ENF2.ENF036":ENF2.ENF036, "ENF2.ENF049":ENF2.ENF049 }}
                    
        self.PCI011 = {"ALL":"allTheTen", "Field":"PCI Region", "S":self.status.c, 
                        "F":self.formats.get_format("N1"), "MSG":self.msg.ENF036, 
                        {"ENF2.ENF036":"ENF2.ENF036", "ENF2.ENF054":ENF2.ENF054, 
                        "ENF2.ENF116":"ENF2.ENF116" }}
        
        self.PCI012 = {"ALL":"allTheTen", "Field":"PCI PO Box Number", "S":self.status.c, 
                        "F":self.formats.get_format("A10"), "MSG":self.msg.ENF014, "ENF":self.enf2.ENF014}
                        
        self.PCI013 = {"ALL":"allTheTen", "Field":"PCI Post Office Town", "S":self.status.c, 
                        "F":self.formats.get_format("A20"), "MSG":self.msg.ENF014 ,"ENF":self.enf2.ENF014}    
        self.PCI014 = {"ALL":"allTheTen", "Field":"PCI Country Code","S":self.status.m, 
                    "F":self.formats.get_format("A2"), "MSG":self.msg.ENF014 ,"ENF":self.enf2.ENF014 }
                    
        self.PCI015 = {"Field":"allTheTen", "Field":"PCI Period At Address", "S":self.status.m, 
                    "F":self.formats.get_format("N3"), "MSG":self.msg.ENF014,
                    "ENF2.ENF014":"ENF2.ENF014", "ENF2.ENF116":"ENF2.ENF116" } 
                    
        self.PCI016 = {"ALL":"allTheTen", "Field":"PCI Flag of Ownership", "S":self.status.m, 
                    "F":self.formats.get_format("A1"), "MSG":self.msg.ENF014, "ENF":self.enf2.ENF084 },
        
        self.PCI017 = {"ALL":"allTheTen", "Field":"PCI Primary Number Country Dialling Code", "S":self.status.m, 
                        "F":self.formats.get_format("N5"), "MSG":self.msg.ENF056, 
                        {"ENF2.ENF056":"ENF2.ENF056", "ENF2.ENF116":"ENF2.ENF116"
                        }}
                        
        self.PCI018 = {"ALL":"allTheTen", "Field":"PCI Primary Number Telephone Number", "S":self.status.m, 
                "F":self.formats.get_format("N10"), "MSG":self.msg.ENF116, "ENF":self.enf2.ENF116 }
                
        self.PCI019 = {"ALL":"allTheTen", "Field":"PCI Other Number Country Dialling Code","S":self.status.c, 
                    "F":self.formats.get_format("N5"), "MSG":self.msg.ENF116, 
                    {"ENF2.ENF116":"ENF2.ENF116", "ENF2.ENF056""ENF2.ENF056" }}
                     
        self.PCI020 = {"ALL":"allTheTen", "Field":"PCI Other Number Telephone Number", "S":self.status.c,
                     "F":self.formats.get_format("N10"), "MSG":self.msg.ENF116, "ENF":self.enf2.ENF116 }
                     
        self.PCI021 ={"ALL":"allTheTen", "Field":"PCI Mobile Number Country Dialling Code", "S":self.status.c,
                       "F":self.formats.get_format("N5"), "MSG":self.msg.ENF056, 
                       {"ENF2.ENF116":"ENF2.ENF116", "ENF2.ENF056":"ENF2.ENF056" }}
                       
        self.PCI022={"ALL":"allTheTen", "Field":"PCI Mobile Number Telephone Number", "S":self.status.c,
                    "F":self.formats.get_format("N10"), "MSG":self.msg.ENF116, "ENF":self.enf2.ENF116 }
                    
        self.PCI023 = {"ALL":"allTheTen", "Field":"PCI Facsimile Country Dialling Code", "S":self.status.c,
                        "F":self.formats.get_format("N5"), "MSG":self.msg.ENF116, 
                        {"ENF2.ENF116":"ENF2.ENF116", "ENF2.ENF056":"ENF2.ENF056"}} 
                        
        self.PCI024 = {"ALL":"allTheTen", "Field":"PCI Facsimile Number", "S":self.status.c, 
                        "F":self.formats.get_format("N10") ,"MSG":self.msg.ENF116, "ENF":self.enf2.ENF116 }
                         
        self.PCI025 = {"ALL":"allTheTen", "Field":"PCI Email Address", "S":self.status.c, 
                        "F":self.formats.get_format("AS50"), "MSG":self.msg.ENF129, "ENF":self.enf2.ENF129 }
                        
        self.PCI026 = {"ALL":"allTheTen", "Field":"PCI Website","S":self.status.c, 
                        "F":self.formats.get_format("AS50"), "MSG":self.msg.ENF129, "ENF":self.enf2.ENF129 }
                        
        self.PI001 = {"dataset":"PI", "Field":"PI Identification Code", 
                        "S":self.status.m, "F":self.formats.get_format("A6"),
                        "MSG":self.msg.ENF068, "ENF":self.enf2.ENF068 }, 
                        
        self.PI002 = {"dataset":"PI", "Field":"Institution Type", "S":self.status.m, 
                        "F":self.formats.get_format("A3"), "MSG":self.msg.ENF069,
                        "ENF":self.enf2.ENF069 }
                        
        self.PI003 = {"dataset":"PI", "Field":"Institution Name","S":self.status.m, 
                        "F":self.formats.get_format("AS100"), "MSG":self.msg.ENF129, 
                        {"ENF2.ENF014":"ENF2.ENF014", "ENF2.ENF129":"ENF2.ENF129" }}
                        
        self.PI004 = {"dataset":"PI", "Field":"License Issuing Date",
                    "S":self.status.m, "F":self.formats.get_format("N8"), 
                    "MSG":self.msg.ENF007, {"ENF2.ENF014":"ENF2.ENF014" ,"ENF2.ENF007":"ENF2.ENF007"}}
        
        self.allTheTen = "allTheTen";
        self.dataset;
        self.data_filed;
        '''
        STATUS status;
        FORMAT format;
        MESSAGES reasons;
        ENF2[] enforcmentcodes;
        '''
        
    def _DVR(self, dataset, data_filed, status, formats, mesg, enf, enforcmentcodes):
        self.dataset = dataset 
        self.data_filed = data_filed
        self.status = status 
        self.reason = msg
        self.enforcmentcodes = enforcmentcodes
    
    def get_dataset(self):
        return self.dataset 
        
    def set_dataset(self, dataset):
        self.dataset = dataset 
        
    def get_datafiled(self):
        return self.data_filed
        
    def set_datafiled(self, data):
        self.data_filed = data 
        
    def get_status(self):
        return self.status 
        
    def set_status(self, status):
        self.status = status 
        
    def get_format(self):
        return self.formats 
        
    def set_format(self, formats):
        self.formats = formats 
        
    def get_reasons(self):
        return self.reasons 
    def set_reasons(self, msg):
        self.reasons = msg 
        
    def get_enforcements(self):
        return self.enforcmentcodes
        
    def set_enforcementcode(self,enforcements):
        self.enforcmentcodes = enforcements
