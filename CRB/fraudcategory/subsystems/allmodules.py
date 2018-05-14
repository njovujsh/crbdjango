#  allmodules.py
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
from fraudcategory.subsystems import falseid
from fraudcategory.subsystems import aidabetconspire
from fraudcategory.subsystems import defaultingfirstpayment
from fraudcategory.subsystems import evadingliability
from fraudcategory.subsystems import falseemployerdetails
from fraudcategory.subsystems import illegalsale
from fraudcategory.subsystems import insurancecliamfraud
from fraudcategory.subsystems import others
from fraudcategory.subsystems import personaunknownfraud
from fraudcategory.subsystems import suspectfrauddeclined
from fraudcategory.subsystems import victim



FRAUD_CHOICES = {
            "FALSE IDENTITY":falseid.FalseID,
            "FALSE EMPLOYER DETAILS":falseemployerdetails.FalseEmployerDetails,
            "ILLEGAL SALE":illegalsale.IllegalSale,
            "OTHERS":others.Others,
            "EVADING LIABILITY":evadingliability.EvadingLiability,
            "AID, ABET OR CONSPIRE":aidabetconspire.AidBetConspire,
            "INSURANCE CLAIMED FRAUD":insurancecliamfraud.InsuranceCliamFraud,
            "DEFAULTING FIRST PAYMENT":defaultingfirstpayment.DefaultFirstPayment,
            "PERSONA UNKNOWN FRAUD":personaunknownfraud.PersonaUnknownFraud,
            "SUSPECT FRAUD-DECLINED":suspectfrauddeclined.SuspectFraudDeclined,
            "VICTIM":victim.Victim,
}

FRAUD_CHOICES_BY_ID = {
            1:falseid.FalseID,
            2:falseemployerdetails.FalseEmployerDetails,
            3:illegalsale.IllegalSale,
            4:others.Others,
            5:evadingliability.EvadingLiability,
            6:aidabetconspire.AidBetConspire,
            8:insurancecliamfraud.InsuranceCliamFraud,
            9:defaultingfirstpayment.DefaultFirstPayment,
            10:personaunknownfraud.PersonaUnknownFraud,
            11:suspectfrauddeclined.SuspectFraudDeclined,
            12:victim.Victim,
}

def get_module(module):
    global FRAUD_CHOICES
    try:
        if(module):
            try:
                mode = FRAUD_CHOICES.get(module.upper())
                if(mode):
                    return mode(module)
                else:
                    return None
            except KeyError as error:
                raise  
            except:
                raise  
        else:
            return False 
    except:
        raise 

def get_module_by_id(ID):
    global FRAUD_CHOICES_BY_ID
    try:
        if(ID):
            try:
                try:
                    module = FRAUD_CHOICES_BY_ID.get(int(ID))
                    if(module):
                        return module(ID)
                    else:
                        return None
                except ValueError as error:
                    raise 
            except KeyError as error:
                raise
            except:
                raise 
        else:
            return False 
    except:
        raise 
