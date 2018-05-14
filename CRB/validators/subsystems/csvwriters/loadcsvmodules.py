#  loadcsvmodules.py
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

from validators.subsystems.csvwriters import piprocesscsvs
from validators.subsystems.csvwriters import pivalidatecsv
from validators.subsystems.csvwriters import ibcsv
from validators.subsystems.csvwriters import capcsv
from validators.subsystems.csvwriters import cbacsv
from validators.subsystems.csvwriters import bccsv
from validators.subsystems.csvwriters import piscsv
from validators.subsystems.csvwriters import fmdcsv
from validators.subsystems.csvwriters import cmccsv
from validators.subsystems.csvwriters import ccgcsv
from validators.subsystems.csvwriters import bscsv

ASSOCIATED_CSV_MODELS = {
    "BORROWERSTAKEHOLDER":bscsv.ProcessCSVBS,
    "BOUNCEDCHEQUES":bccsv.ProcessCSVBC,
    "COLLATERAL_CREDIT_GUARANTOR":ccgcsv.ProcessCSVCCG,
    "COLLATERAL_MATERIAL_COLLATERAL":cmccsv.ProcessCSVCMC,
    "CREDITBORROWERACCOUNT":cbacsv.ProcessCSVCBA,
    "CREDIT_APPLICATION":capcsv.ProcessCSVCAP,
    "INSTITUTION_BRANCH":ibcsv.ProcessCSVIB,
    "PARTICIPATINGINSTITUTIONSTAKEHOLDER":piscsv.ProcessCSVPIS,
    "PARTICIPATING_INSTITUTION":pivalidatecsv.ProcessCSVPI,
    "FINANCIAL_MALPRACTICE_DATA":fmdcsv.ProcessCSVFMD
}

ASSOCIATED_CSV_VALIDTED_MODELS = {
    "BORROWERSTAKEHOLDER":bscsv.CSVBSValidated,
    "BOUNCEDCHEQUES":bccsv.CSVBCValidated,
    "COLLATERAL_CREDIT_GUARANTOR":ccgcsv.CSVCCGValidated,
    "COLLATERAL_MATERIAL_COLLATERAL":cmccsv.CSVPCMCValidated,
    "CREDITBORROWERACCOUNT":cbacsv.CSVCBAValidated,
    "CREDIT_APPLICATION":capcsv.CSVCAPValidated,
    "INSTITUTION_BRANCH":ibcsv.CSVIBValidated,
    "PARTICIPATINGINSTITUTIONSTAKEHOLDER":piscsv.CSVPISValidated,
    "PARTICIPATING_INSTITUTION":pivalidatecsv.CSVPIValidated,
    "FINANCIAL_MALPRACTICE_DATA":fmdcsv.CSVFMDValidated
}

def load_csv_validated_module(modelname):
    try:
        if(len(modelname)):
            try:
                return ASSOCIATED_CSV_VALIDTED_MODELS.get(modelname.replace(" ", "_", len(modelname)).upper())
            except Exception as e:
                return e 
        else:
            return None
    except Exception as e:
        return e 
        
def load_csv_module(modelname):
    try:
        if(len(modelname)):
            try:
                return ASSOCIATED_CSV_MODELS.get(modelname.replace(" ", "_", len(modelname)).upper())
            except Exception as e:
                return e 
        else:
            return None
    except Exception as e:
        return e 
        
