from creditreports import models as creditsmodels 
from django.db import models


ASSOCIATED_MODELS = {
    "BORROWERSTAKEHOLDER":creditsmodels.BSValidationReport(),
    "BOUNCEDCHEQUES":creditsmodels.BCValidationReport(),
    "COLLATERAL_CREDIT_GUARANTOR":creditsmodels.CCGValidationReport(),
    "COLLATERAL_MATERIAL_COLLATERAL":creditsmodels.CMCValidationReport(),
    "CREDITBORROWERACCOUNT":creditsmodels.CBAValidationReport(),
    "CREDIT_APPLICATION":creditsmodels.CAPValidationReport(),
    "INSTITUTION_BRANCH":creditsmodels.IBValidationReport(),
    "PARTICIPATINGINSTITUTIONSTAKEHOLDER":creditsmodels.PISValidationReport(),
    "PARTICIPATING_INSTITUTION":creditsmodels.PIValidationReport(),
    "FINANCIAL_MALPRACTICE_DATA":creditsmodels.FRAValidationReport()
}

ASSOCIATED_MODELS_QUERY = {
    "BORROWERSTAKEHOLDER":creditsmodels.BSValidationReport,
    "BOUNCEDCHEQUES":creditsmodels.BCValidationReport,
    "COLLATERAL_CREDIT_GUARANTOR":creditsmodels.CCGValidationReport,
    "COLLATERAL_MATERIAL_COLLATERAL":creditsmodels.CMCValidationReport,
    "CREDITBORROWERACCOUNT":creditsmodels.CBAValidationReport,
    "CREDIT_APPLICATION":creditsmodels.CAPValidationReport,
    "INSTITUTION_BRANCH":creditsmodels.IBValidationReport,
    "PARTICIPATINGINSTITUTIONSTAKEHOLDER":creditsmodels.PISValidationReport,
    "PARTICIPATING_INSTITUTION":creditsmodels.PIValidationReport,
    "FINANCIAL_MALPRACTICE_DATA":creditsmodels.FRAValidationReport
}

def load_report_model_module(modelname):
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
        
def load_report_model_(modelname):
    try:
        if(len(modelname)):
            try:
                return ASSOCIATED_MODELS_QUERY.get(modelname.upper().replace(' ', "_", len(modelname)))
            except Exception as e:
                return e 
        else:
            return None
    except Exception as e:
        return e 
