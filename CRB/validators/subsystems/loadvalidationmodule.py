#  loadvalidationmodule.py
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

from validators.subsystems.datasets import pivalidate
from validators.subsystems.datasets import ibvalidate
from validators.subsystems.datasets import ccgvalidate
from validators.subsystems.datasets import cmcvalidate
from validators.subsystems.datasets import bcvalidate
from validators.subsystems.datasets import bsvalidate
from validators.subsystems.datasets import pisvalidate
from validators.subsystems.datasets import capvalidate
from validators.subsystems.datasets import fmdvalidate
from validators.subsystems.datasets import cbavalidate
from datasetrecords import models 

def load_val_modules():
    VALIDATION_MODULE={
        "BORROWERSTAKEHOLDER":bsvalidate.BSValidate(),
        "BOUNCEDCHEQUES":bcvalidate.BCValidate(),
        "COLLATERAL CREDIT GUARANTOR":ccgvalidate.CCGValidate(),
        "COLLATERAL MATERIAL COLLATERAL":cmcvalidate.CMCValidate(),
        "CREDITBORROWERACCOUNT":cbavalidate.CBAValidate(),
        "CREDIT APPLICATION":capvalidate.CAPValidate(),
        #"EMPLOYMENT_INFORMATION":eivalidate.EIValidate,
        "FINANCIAL MALPRACTICE DATA":fmdvalidate.FMDValidate(),
        #"GSCAFB_INFORMATION":gscafbvalidate.GSCAFBValidate,
        #"IDENTIFICATION INFORMATION":iivalidate.IIValidate,
        "INSTITUTION BRANCH":ibvalidate.IBValidate(),
        "PARTICIPATINGINSTITUTIONSTAKEHOLDER":pisvalidate.PISValidate(),
        "PARTICIPATING INSTITUTION":pivalidate.PIValidate()
    }
    return VALIDATION_MODULE
    
def load_module_c():
    VALIDATION_MODULE_COUNT={
        "BORROWERSTAKEHOLDER":models.BORROWERSTAKEHOLDER.objects.all().count(),
        "BOUNCEDCHEQUES":models.BOUNCEDCHEQUES.objects.all().count(),
        "COLLATERAL CREDIT GUARANTOR":models.COLLATERAL_CREDIT_GUARANTOR.objects.all().count(),
        "COLLATERAL MATERIAL COLLATERAL":models.COLLATERAL_MATERIAL_COLLATERAL.objects.all().count(),
        "CREDITBORROWERACCOUNT":models.CREDITBORROWERACCOUNT.objects.all().count(),
        "CREDIT APPLICATION":models.CREDIT_APPLICATION.objects.all().count(),
        #"EMPLOYMENT_INFORMATION":eivalidate.EIValidate,
        "FINANCIAL MALPRACTICE DATA":models.FINANCIAL_MALPRACTICE_DATA.objects.all().count(),
        #"GSCAFB_INFORMATION":gscafbvalidate.GSCAFBValidate,
        #"IDENTIFICATION INFORMATION":iivalidate.IIValidate,
        "INSTITUTION BRANCH":models.INSTITUTION_BRANCH.objects.all().count(),
        "PARTICIPATINGINSTITUTIONSTAKEHOLDER":models.PARTICIPATINGINSTITUTIONSTAKEHOLDER.objects.all().count(),
        "PARTICIPATING INSTITUTION":models.PARTICIPATING_INSTITUTION.objects.all().count()
    }
    return VALIDATION_MODULE_COUNT
    
def load_module_count(modulename):
    try:
        if(modulename):
            return load_module_c().get(modulename.replace("_", " ", len(modulename)).upper())
        else:
            return False
    except:
        raise 
       
def load_modules(modulename):
    try:
        if(modulename):
            return load_val_modules().get(modulename.replace("_", " ", len(modulename)).upper())
        else:
            return None
    except:
        raise 
        
