import csv
from django.http import HttpResponse
from django.utils.encoding import smart_str
from validators.subsystems.csvwriters import processcsvs
from validators.subsystems.csvwriters import pivalidatecsv

class ProcessCSVCMC(processcsvs.ProcessCSV):
    def __init__(self, filename, dialect, row, headers, delimiter="|",response=None):
        super(ProcessCSVCMC, self).__init__(filename, dialect,response=response)
        
        self.delimiter = delimiter
        self.row = row 
        
        if(headers):
            self.write_headers(headers)
            
    def write_row_data(self, coldata):
        try:
            for data in coldata:
                self.writer.writerow([
                                    self.get_data_id(),
                                    smart_str(unicode(data.PI_Identification_Code)),
                                    smart_str(unicode(data.Branch_Identification_Code.branch_code)),
                                    smart_str(unicode(data.Borrowers_Client_Number.Client_Number)),
                                    smart_str(unicode(data.Borrower_Account_Reference.Credit_Account_Reference)),
                                    smart_str(unicode(data.Borrower_Classification)),
                                    smart_str(unicode(data.Collateral_Type_Identification)),
                                    smart_str(unicode(data.Collateral_Reference_Number)),
                                    smart_str(unicode(data.Collateral_Description)),
                                    smart_str(unicode(data.Collateral_Currency)),
                                    smart_str(unicode(data.Collateral_Open_Market_Value)),
                                    smart_str(unicode(data.Collateral_Forced_Sale_Value)),
                                    smart_str(unicode(data.Collateral_Valuation_Expiry_Date)),
                                    smart_str(unicode(data.Instrument_of_Claim)),
                                    smart_str(unicode(data.Valuation_Date)),
                            ])
            return self.response 
        except:
            raise 
            
class CSVPCMCValidated(pivalidatecsv.CSVPIValidated):
    def __init__(self,filename, dialect, row, headers, delimiter="|",response=None):
        super(CSVPCMCValidated, self).__init__(filename, dialect,delimiter, headers,response=response)
        
        self.delimiter = delimiter
        self.row = row 
       
    def write_row_data(self, coldata, val):
        try:
            
            self.validated_field = self.validate_and_return(val)
            self.pi_field = self.load_validated_field(self.validated_field.get("PI_Identification_Code"))
            self.bic_field = self.load_validated_field(self.validated_field.get("Branch_Identification_Code"))
            self.bcn_field = self.load_validated_field(self.validated_field.get("Borrowers_Client_Number"))
            self.bar_field = self.load_validated_field(self.validated_field.get("Borrower_Account_Reference"))
            self.bac_field = self.load_validated_field(self.validated_field.get("Borrower_Classification"))
            self.cti_field = self.load_validated_field(self.validated_field.get("Collateral_Type_Identification"))
            self.crn_field = self.load_validated_field(self.validated_field.get("Collateral_Reference_Number"))
            self.cd_field = self.load_validated_field(self.validated_field.get("Collateral_Description"))
            self.cc_field = self.load_validated_field(self.validated_field.get("Collateral_Currency"))
            self.comv_field = self.load_validated_field(self.validated_field.get("Collateral_Open_Market_Value"))
            self.cfsv_field = self.load_validated_field(self.validated_field.get("Collateral_Forced_Sale_Value"))
            self.cved_field = self.load_validated_field(self.validated_field.get("Collateral_Valuation_Expiry_Date"))
            self.ioc_field = self.load_validated_field(self.validated_field.get("Instrument_of_Claim"))
            self.vd_field = self.load_validated_field(self.validated_field.get("Valuation_Date"))
            
            for data in coldata:
                self.writer.writerow([
                                    self.get_data_id(),
                                    self.value_in(smart_str(unicode(data.PI_Identification_Code)),self.pi_field),
                                    self.value_in(smart_str(unicode(data.Branch_Identification_Code.branch_code)), self.bic_field),
                                    self.value_in(smart_str(unicode(data.Borrowers_Client_Number.Client_Number)), self.bcn_field),
                                    self.value_in(smart_str(unicode(data.Borrower_Account_Reference.Credit_Account_Reference)), self.bar_field),
                                    self.value_in(smart_str(unicode(data.Borrower_Classification)), self.bac_field),
                                    self.value_in(smart_str(unicode(data.Collateral_Type_Identification)),self.cti_field),
                                    self.value_in(smart_str(unicode(data.Collateral_Reference_Number)),self.crn_field),
                                    self.value_in(smart_str(unicode(data.Collateral_Description)), self.cd_field),
                                    self.value_in(smart_str(unicode(data.Collateral_Currency)), self.cc_field),
                                    self.value_in(smart_str(unicode(data.Collateral_Open_Market_Value)), self.comv_field),
                                    self.value_in(smart_str(unicode(data.Collateral_Forced_Sale_Value)), self.cfsv_field),
                                    self.value_in(smart_str(unicode(data.Collateral_Valuation_Expiry_Date)), self.cved_field),
                                    self.value_in(smart_str(unicode(data.Instrument_of_Claim)), self.ioc_field),
                                    self.value_in(smart_str(unicode(data.Valuation_Date)), self.vd_field),
                        ])
            return self.response 
        except:
            raise 
            
