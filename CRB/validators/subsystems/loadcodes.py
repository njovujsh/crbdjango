#  loadcodes.py
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

from datasetrecords import models as rmodels
from django.db import models
from datasetrecords import loadmodels
from validators.subsystems import bscode 
from validators.subsystems import bccode 
from validators.subsystems import picode 
from validators.subsystems import piscode 
from validators.subsystems import cbacode 
from validators.subsystems import ccgcode 
from validators.subsystems import cmccode 
from validators.subsystems import capcode 
from validators.subsystems import ibcode 
from validators.subsystems import fmdcode 

ASSOCIATED_MODELS_PICODE = {
    "BORROWERSTAKEHOLDER":bscode.BSCode(rmodels.BORROWERSTAKEHOLDER, "BS"),
    "BOUNCEDCHEQUES":bccode.BCCode(rmodels.BOUNCEDCHEQUES, "BC"),
    "COLLATERAL_CREDIT_GUARANTOR":ccgcode.CCGCode(rmodels.COLLATERAL_CREDIT_GUARANTOR, "CCG"),
    "COLLATERAL_MATERIAL_COLLATERAL":cmccode.CMCCode(rmodels.COLLATERAL_MATERIAL_COLLATERAL, "CMC"),
    "CREDITBORROWERACCOUNT":cbacode.CBACode(rmodels.CREDITBORROWERACCOUNT, "CBA"),
    "CREDIT_APPLICATION":capcode.CAPCode(rmodels.CREDIT_APPLICATION, "CP"),
    "INSTITUTION_BRANCH":ibcode.IBCode(rmodels.INSTITUTION_BRANCH, "IB"),
    "PARTICIPATINGINSTITUTIONSTAKEHOLDER":piscode.PISCode(rmodels.PARTICIPATINGINSTITUTIONSTAKEHOLDER, "PIS"),
    "PARTICIPATING_INSTITUTION":picode.PICode(rmodels.PARTICIPATING_INSTITUTION, "PI"),
    "FINANCIAL_MALPRACTICE_DATA":fmdcode.FMDCode(rmodels.FINANCIAL_MALPRACTICE_DATA, "FMD")
}

def get_set_code(name):
    try:
        if(name):
            try:
                return ASSOCIATED_MODELS_PICODE.get(str(name).replace(" ", "_", len(str(name))).upper())
            except:
                raise 
        else:
            return False 
    except:
        raise 
        

def ret_all_joined(module):
    try:
        if(module):
            try:
                for m in module.join_field_rule(ret_all=True):
                    return m
            except:
                raise 
        else:
            return None
    except:
        raise 
        
