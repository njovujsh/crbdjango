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

from creditreports.subsystems import pivalidatereport 
from creditreports.subsystems import ibvalidatereport 
from creditreports.subsystems import pisvalidatereport 
from creditreports.subsystems import capvalidatereport 
from creditreports.subsystems import capvalidatereport 
from creditreports.subsystems import cbavalidatereport 
from creditreports.subsystems import bcvalidatereport 
from creditreports.subsystems import fmdvalidatereport 
from creditreports.subsystems import cmcvalidatereport 
from creditreports.subsystems import ccgvalidatereport 
from creditreports.subsystems import bsvalidatereport 
from datasetrecords import models 

def load_val_modules():
    VALIDATION_MODULE={
        "BORROWERSTAKEHOLDER":bsvalidatereport.ReportBSValidate(),
        "BOUNCEDCHEQUES":bcvalidatereport.ReportBCValidate(),
        "COLLATERAL CREDIT GUARANTOR":ccgvalidatereport.ReportCCGValidate(),
        "COLLATERAL MATERIAL COLLATERAL":cmcvalidatereport.ReportCMCValidate(),
        "CREDITBORROWERACCOUNT":cbavalidatereport.ReportCBAValidate(),
        "CREDIT APPLICATION":capvalidatereport.ReportCAPValidate(),
        #"EMPLOYMENT_INFORMATION":eivalidate.EIValidate,
        "FINANCIAL MALPRACTICE DATA":fmdvalidatereport.ReportFMDValidate(),
        #"GSCAFB_INFORMATION":gscafbvalidate.GSCAFBValidate,
        #"IDENTIFICATION INFORMATION":iivalidate.IIValidate,
        "INSTITUTION BRANCH":ibvalidatereport.ReportIBValidate(),
        "PARTICIPATINGINSTITUTIONSTAKEHOLDER":pisvalidatereport.ReportPISValidate(),
        "PARTICIPATING INSTITUTION":pivalidatereport.ReportPIValidate()
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
            return load_module_c().get(modulename.upper())
        else:
            return False
    except:
        pass 
       
def load_modules(modulename):
    try:
        if(modulename):
            return load_val_modules().get(modulename.replace("_", " ", len(modulename)).upper())
        else:
            return None
    except:
        pass 
        
