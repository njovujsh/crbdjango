#  loadmodels.py
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

ASSOCIATED_MODELS = {
    "BORROWERSTAKEHOLDER":rmodels.BORROWERSTAKEHOLDER,
    "BOUNCEDCHEQUES":rmodels.BOUNCEDCHEQUES,
    "COLLATERAL_CREDIT_GUARANTOR":rmodels.COLLATERAL_CREDIT_GUARANTOR,
    "COLLATERAL_MATERIAL_COLLATERAL":rmodels.COLLATERAL_MATERIAL_COLLATERAL,
    "CREDITBORROWERACCOUNT":rmodels.CREDITBORROWERACCOUNT,
    "CREDIT_APPLICATION":rmodels.CREDIT_APPLICATION,
    "INSTITUTION_BRANCH":rmodels.INSTITUTION_BRANCH,
    "PARTICIPATINGINSTITUTIONSTAKEHOLDER":rmodels.PARTICIPATINGINSTITUTIONSTAKEHOLDER,
    "PARTICIPATING_INSTITUTION":rmodels.PARTICIPATING_INSTITUTION,
    "FINANCIAL_MALPRACTICE_DATA":rmodels.FINANCIAL_MALPRACTICE_DATA
}

def load_model_module(modelname):
    try:
        if(len(modelname)):
            try:
                return ASSOCIATED_MODELS.get(modelname.upper())
            except Exception as e:
                return e 
        else:
            return None
    except Exception as e:
        return e 
        

def load_model_replace_underscore(modelname):
    try:
        if(len(modelname)):
            try:
                return ASSOCIATED_MODELS.get(modelname.replace(" ", "_", len(modelname)).upper())
            except Exception as e:
                return e
        else:
            return None 
    except Exception as e:
        return e
        
def load_all_data(model):
    """
    Given the model of the dataset return all the records available.
    """
    
    try:
        if(model):
            try:
                return model.objects.all()
            except Exception as e:
                return e
        else:
            #Not the instance of our database records
            return False 
    except Exception as e:
        return e 
