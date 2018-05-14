#  collateralclassification.py
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

class CollateralClassification(object):
    def __init__(self):
        self.collateral = (
                            ('1', "Concessions and Other Contractual Rights"),
                            ('3', "Guarantee"), ('4', "Motor Vehicles/Carriers"),
                            ('5', "Negative Pledge"), ('6', "Other Assets (non financial"),
                            ('7', "Other Assets (financial)"), ('8', "Plant and Machinery"),
                            ('9', "Properties (mortage)"), ('10', "Quoted Shares"),
                            ('11', "Supportive Letters"),
                            ('13', "Unit Trusts"), ('14', "Unquoted"),
                            ('15', "Chattel")
                            )
                            
        self.collateral_dict = {'1':"Concessions and Other Contractual Rights",
                            '3':"Guarantee", '':"Motor Vehicles/Carriers",
                            '5':"Negative Pledge", '6':"Other Assets (non financial",
                            '7':"Other Assets (financial)", '8':"Plant and Machinery",
                            '9':"Properties (mortage)", '0':"Quoted Shares",
                            '11':"Supportive Letters",
                            '13':"Unit Trusts", '4':"Unquoted",
                            '15':"Chattel"
                            }
        
        
    def get_collateral(self):
        return self.collateral
    
    def get_value(self, key):
        return self.collateral_dict.get(key)
        
def get_collateral():
    C = CollateralClassification()
    return C.get_collateral()    
