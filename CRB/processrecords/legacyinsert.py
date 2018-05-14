
from datasetrecords import models as datamodels
from branchcode import models as branchmodel
from datasetrecords import accreference 
from CRB import settings

class BCInsert(object):
    def __init__(self, bcmodel, cpmodel):
        self._bcmodel = bcmodel
        self._cpmodel = cpmodel
        self._arglist = []
        
    def cleanse_date(self, date):
        try:
            if(date):
                return str(date).replace("-", "", len(str(date))).strip().lstrip().rstrip().replace("/", "", len(str(date))).replace(".", "", len(str(date)))
            else:
                return  date
        except:
            raise

    def cleanse_uploaded_data(self, value):
        try:
            if("." in value):
                return int(float(value))
            else:
                return value
                
        except ValueError as error:
            return value
            
    def save_legacy(self, listdata, get_clientnumber, found_headers, brancheader):
        try:
            for e in range(len(listdata)):
                self.bc = self._bcmodel()
                self.bc.PI_Identification_Code=found_headers
                self.bc.Branch_Identification_Code=brancheader
                self.bc.Borrowers_Client_Number=get_clientnumber
                self.bc.PI_Client_Classification=int(float(listdata[0]))
                self.bc.Cheque_Account_Reference_Number=listdata[1]
                self.bc.Cheque_Account_Opened_Date=listdata[2]
                self.bc.Cheque_Account_Classification=int(float(listdata[3]))
                self.bc.Cheque_Account_Type=int(float(listdata[4]))
                self.bc.Cheque_Number=listdata[5]
                self.bc.Cheque_Amount=listdata[6]
                self.bc.Cheque_Currency=listdata[7]
                self.bc.Beneficiary_Name_Or_Payee=listdata[8]
                self.bc.Cheque_Bounce_Date=listdata[9]
                self.bc.Cheque_Account_Bounce_Reason=listdata[10]
            self.bc.save()
        except:
            raise
            
    def get_acc_reference(self,saved):
        try:
            return accreference.get_reference_number(saved.id, saved.Credit_Account_or_Loan_Product_Type)
        except:
            raise
            
    def filter_datainsert(self, num_rows):
        """
        Filters the records and attempts to insert.
        """
        try:
            self.furbished = self.strip_data_identifier(num_rows)
            #print self.furbished
            self.pi_code = self.extract_at_index(self.furbished, 0)
            self.bi_code = self.extract_at_index(self.furbished, 1)
            self.client_code = self.extract_at_index(self.furbished, 2)

            self.saved_pi =  self.query_or_save(self.pi_code)
            #print "SAVED PI ", self.saved_pi
            self.saved_bi =  self.query_or_save_bi(self.saved_pi, self.bi_code)
            
            self.remaining_data = self.strip_data_identifier(self.furbished, index=3)
            try:
                self.search_number = self.search_clientnumber(self.client_code)
                self.save_legacy(self.remaining_data, self.search_number, self.saved_pi, self.saved_bi)
            except datamodels.CREDIT_APPLICATION.DoesNotExist as e:
                print e, self.client_code
                pass 
             
        except Exception as e:
            print "BC ERROR ", e
            pass 
            #raise

    def strip_data_identifier(self, data_list, index=1):
        if(data_list):
            data = data_list[index:]
            return data

    def extract_at_index(self, data_list, index):
        try:
            return data_list[index]
        except:
            raise

    def query_all_headers(self):
        try:
            return branchmodel.RequiredHeader.objects.all()
        except:
            raise

    def query_pi_byid(self, ID):
        try:
            return branchmodel.RequiredHeader.objects.get(id=ID)
        except:
            raise
            
    def query_or_save(self, picode):
        try:
            self.all_query = branchmodel.PIIdentificationCode.objects.all()
            if(self.all_query):
                self.filtered_pi = self.all_query.get(pi_identification_code=str(picode))
                return self.filtered_pi
            else:
                #Save and return
                self.saved = branchmodel.PIIdentificationCode(pi_identification_code=picode)
                self.saved.save()
                return self.saved
        except:
            raise

    def query_all_branch(self):
        try:
            return branchmodel.DefaultHeaders.objects.all()
        except:
            raise
    
    def query_bi_byid(self, ID):
        try:
            return branchmodel.DefaultHeaders.objects.get(id=ID)
        except:
            raise

    def query_all_headers(self):
        try:
            return branchmodel.RequiredHeader.objects.all()
        except:
            raise

    def query_header_byid(self, ID):
        try:
            return branchmodel.RequiredHeader.objects.get(id=ID)
        except:
            raise
            
    def query_or_save_bi(self, reheader, branch):
        try:
            if(str(branch).strip().lstrip().rstrip()):
                self.branch_ids = float(branch)
                self.branch_ids = int(self.branch_ids)
                self.saved = branchmodel.RequiredHeader.objects.get(branch_code=self.branch_ids)
                return self.saved
        except branchmodel.RequiredHeader.DoesNotExist:
            raise
            
    def get_gscafb(self):
        self.gs = datamodels.GSCAFB_INFORMATION()
        self.gs.save()
        return self.gs

    def get_idi(self):
        self.ie = datamodels.IDENTIFICATION_INFORMATION()
        self.ie.save()
        return self.ie

    def get_employerinfo(self):
        self.info = datamodels.EMPLOYMENT_INFORMATION()
        self.info.save()
        return self.info

    def get_sci(self):
        self.sci = datamodels.SCI()
        self.sci.save()
        return self.sci

    def get_pci(self):
        self.pci = datamodels.PCI()
        self.pci.save()
        return self.pci

    def search_header(self, code):
        if(code):
            return branchmodel.RequiredHeader.objects.get(pi_identification_code=code)
            
    def search_defaultheader(self, code):
        if(code):
            return branchmodel.DefaultHeaders.objects.get(Branch_Code=code)
            
    def search_clientnumber(self, clientnum):
        if(clientnum):
            self.c = str(clientnum).strip().lstrip().rstrip()
            if(self.c):
                self.clientnumber = int(float(self.c))
                return datamodels.CREDIT_APPLICATION.objects.get(Client_Number=str(self.clientnumber))

    def get_clientnumberbyid(self, clientobj):
        if(clientobj):
            return datamodels.CREDIT_APPLICATION.objects.get(Client_Number=clientobj.id)
            
    def save_branchode(self, code):
        if(code):
            try:
                self.branchsaved = branchmodel.RequiredHeader(pi_identification_code=code)
                self.branchsaved.save()
                return self.branchsaved
            except:
                raise

    def get_picode(self, data):
        return data[0]

    def index_firstpost(self, data, defaultindext=3):
        try:
            return data[:defaultindext]
        except:
            raise

    def get_data_by_index(self, data, index=1):
        try:
            if(len(data)):
                return data[index]
        except:
            raise
                
class CPInsert(BCInsert):
    def __init__(self, cpmodel):
        super(CPInsert, self).__init__(bcmodel=cpmodel, cpmodel=cpmodel)
        self.lists = []
        
    def save_legacy(self, listdata, found_headers, brancheader):
        try:
            for e in range(len(listdata)):
                if(len(listdata[0])):
                    self.bc = self._bcmodel()
                    self.bc.PI_Identification_Code=self.found_headers
                    self.bc.Branch_Identification_Code = self.brancheader
                    self.bc.Client_Number=listdata[0]
                    self.bc.Credit_Application_Reference=listdata[1]
                    self.bc.Applicant_Classification=listdata[2]
                    self.bc.Credit_Application_Date=listdata[3]
                    self.bc.Amount=listdata[4]
                    self.bc.Currency=listdata[5]
                    self.bc.Credit_Account_or_Loan_Product_Type= listdata[7]
                    self.bc.Credit_Application_Status=listdata[8]
                    self.bc.Last_Status_Change_Date=listdata[9]
                    self.bc.Credit_Application_Duration=listdata[10]
                    self.bc.Rejection_Reason=listdata[11]
                    self.bc.Client_Consent_flag=listdata[12]
                    self.bc.gscafb = self.get_gscafb()
                    self.bc.idi = self.get_idi()
                    self.bc.ei = self.get_employerinfo()
                    self.bc.pci = self.get_pci()
                    self.bc.sci = self.get_sci()
                    self.bc.save()
        except:
            raise

    def filter_datainsert(self, num_rows):
        """
        Filters the records and attempts to insert.
        """
        try:
            if(len(num_rows) == 6):
                self.branch_id = num_rows[:1]
                self.branch_n_name = num_rows[1:2]
                #print "INDXED BRANCH NAME ", self.branch_n_name
                self.client_number = num_rows[2:3]

                self.pi_code = self.get_picode()

                if(len(self.client_number)):
                    self.client_numb = self.client_number[0]
                        
                    self.query_branch = self.search_save_branch_details(self.branch_id, self.branch_n_name)
                    
                    #self.ret_branch = self.query_or_save_bi(self.pi_code, self.branch_id, self.branch_n_name[0])
                    self.ret_branch = self.query_or_save_bi(self.pi_code, self.query_branch, self.branch_id)
                    #self.client_information = num_rows[len(num_rows)/2:]
                    
                    self.fname = num_rows[3:4]
                    self.lname = num_rows[4:5]
                    self.bname = num_rows[5:6]

                    self.clientnumber = str(self.client_numb).strip().lstrip().rstrip()
                    if(self.clientnumber):
                        self.clientnumber_s = int(float(self.clientnumber))
                        self.client_details = self.save_clientdetails(self.fname, self.lname, self.bname)
                        #self.save_partialdata(self.client_number, self.client_details, self.pi_code, self.ret_branch)
                        self.save_partialdata(self.clientnumber_s, self.client_details, self.pi_code, self.ret_branch)
                        #self.save_partialdata(self, clientnumber_s, clientdetails, picode, branch_code_founds)
                    else:
                        print "Invalid client number by passing!"
                        pass 
                else:
                    print "Can't save data without client number "
                    pass 
              
        except:
            raise

    def query_all_branch(self):
        try:
            return branchmodel.DefaultHeaders.objects.all()
        except:
            raise
            
    def query_all_headers(self):
        try:
            return branchmodel.RequiredHeader.objects.all()
        except:
            raise

    def query_bi_byid(self, ID):
        try:
            return branchmodel.DefaultHeaders.objects.get(id=ID)
        except:
            raise
            
    def query_header_byid(self, ID):
        try:
            return branchmodel.RequiredHeader.objects.get(id=ID)
        except:
            raise


    def search_save_branch_details(self, branch_id, branch_name):
        try:
            self.branch_ = branch_id[0]
            if(str(self.branch_).strip().lstrip().rstrip()):
                
                self.branch_ids = float(self.branch_)
                #print "ID ", self.branch_ids
                self.branch_ids = int(self.branch_ids)
                
                if(self.branch_ids and branch_name):
                    self.branch = branchmodel.BranchNames.objects.get(Branch_Code=self.branch_ids, Branch_name=branch_name[0])
                    if(self.branch):
                        return self.branch
                    else:
                        self.branch = branchmodel.BranchNames(Branch_Code=self.branch_ids, Branch_name=branch_name[0])
                        self.branch.save()
                        return self.branch
        except:
            raise
            
    def query_or_save_bi(self, reheader, branch, branchcode):
        try:
            self.branch_ = branchcode[0]
            if(str(self.branch_).strip().lstrip().rstrip()):
                self.branch_ids = float(self.branch_)
                self.branch_ids = int(self.branch_ids)

                # Search
                try:
                    self.branch_id_saved = self.first_search_required(self.branch_ids)
                    if(self.branch_id_saved):
                        return self.branch_id_saved
                    else:
                        self.saved = branchmodel.RequiredHeader(pi_identification_code=reheader, branch_name=branch, branch_code=self.branch_ids)
                        self.saved.save()
                        return self.saved
                        
                except branchmodel.RequiredHeader.DoesNotExist:
                    self.saved = branchmodel.RequiredHeader(pi_identification_code=reheader, branch_name=branch, branch_code=self.branch_ids)
                    self.saved.save()
                    return self.saved
        except:
            raise

    def first_search_required(self, code):
        try:
            self.get = branchmodel.RequiredHeader.objects.get(branch_code=self.branch_ids)
            if(self.get):
                return self.get
            else:
                return False
        except:
            raise
            
    def save_partialdata(self, clientnumber_s, clientdetails, picode, branch_code_founds):
        try:
            self.bc = self._bcmodel()
            self.bc.client_details=clientdetails
            self.bc.PI_Identification_Code=picode
            self.bc.Branch_Identification_Code = branch_code_founds
            self.bc.Client_Number=clientnumber_s
            self.bc.gscafb = self.get_gscafb()
            self.bc.idi = self.get_idi()
            self.bc.ei = self.get_employerinfo()
            self.bc.pci = self.get_pci()
            self.bc.sci = self.get_sci()
            self.bc.save()
        except:
            raise 
            
    def save_clientdetails(self, fname, lname, bname):
        self.details = datamodels.ClientInformation(surname=fname[0], firstname=lname[0], business_name=bname[0])
        self.details.save()
        return self.details 
        
    def save_branchdetails(self, detaillist, picode=None):
        if(picode):
            if(len(detaillist)):
                self.bcode = branchmodel.DefaultHeaders(Branch_Code=detaillist[0], Branch_name=detaillist[1], default_headers=picode)
                self.bcode.save() 
        else:
            if(len(detaillist)):
                self.bcode = branchmodel.DefaultHeaders(Branch_Code=detaillist[0], Branch_name=detaillist[1])
                self.bcode.save()

    def save_branchdetails2(self, bcode):
        self.bcode = branchmodel.DefaultHeaders(Branch_Code=detaillist[0])
        self.bcode.save()
        return self.bcode
        
    def get_picode(self, ID=1):
        self.all_pi = branchmodel.PIIdentificationCode.objects.all()
        if(self.all_pi):
            try:
                self.query = branchmodel.PIIdentificationCode.objects.get(pi_identification_code=settings.PI_IDENTIFICATION)
                return self.query
            except branchmodel.PIIdentificationCode.DoesNotExist:
                self.query = branchmodel.PIIdentificationCode(pi_identification_code=settings.PI_IDENTIFICATION)
                self.query.save()
                return self.query 
            
class CBAInsert(BCInsert):
    def __init__(self, cpmodel):
        super(CBAInsert, self).__init__(bcmodel=cpmodel, cpmodel=cpmodel)
        self.lists = []
        
    def save_branchdetails2(self, bcode):
        self.bcode = branchmodel.DefaultHeaders(Branch_Code=bcode)
        self.bcode.save()
        return self.bcode
        
    def save_legacy(self, data, clientnum, found_headers, brancheader):
        try:
            self.data = data
            for e in range(len(self.data)):
                #print "Saving Model", self._bcmodel()
                self.cba = self._bcmodel()
                self.cba.PI_Identification_Code=found_headers
                self.cba.Branch_Identification_Code=brancheader
                self.cba.Borrowers_Client_Number=clientnum
                self.cba.Borrower_Classification=int(self.data[0])
                self.cba.Credit_Account_Reference=self.data[1]
                self.cba.Credit_Account_Date=self.cleanse_uploaded_data(self.cleanse_date(self.data[2]))
                self.cba.Credit_Amount=self.data[3]
                self.cba.Facility_Amount_Granted=self.data[3]
                self.cba.Credit_Account_Type=int(self.data[4])
                self.cba.Group_Identification_Joint_Account_Number=self.data[6]
                #self.cba.Transaction_Date
                self.cba.Currency=self.data[7]
                self.cba.Opening_Balance_Indicator=int(self.data[8])
                self.cba.Maturity_Date=self.cleanse_uploaded_data(self.cleanse_date(self.data[9])) #self.data[9]
                self.cba.Type_of_Interest=int(self.data[10])
                self.cba.Interest_Calculation_Method=int(self.data[11])
                self.cba.Annual_Interest_Rate_at_Disbursement=self.data[12]
                #self.cba.Annual_Interest_Rate_at_Reporting
                self.cba.Date_of_First_Payment=self.data[13]
                self.cba.Credit_Amortization_Type=int(self.data[14])
                self.cba.Credit_Payment_Frequency=int(self.data[15])
                self.cba.Number_of_Payments=self.data[16]
                self.cba.Monthly_Instalment_Amount=self.data[17]
                self.cba.Current_Balance_Amount=self.data[18]
                self.cba.Current_Balance_Indicator=int(self.data[19])
                self.cba.Last_Payment_Date=self.cleanse_uploaded_data(self.cleanse_date(self.data[20])) #self.data[20]
                self.cba.Last_Payment_Amount=self.data[21]
                self.cba.Credit_Account_Status=int(self.data[22])
                self.cba.Last_Status_Change_Date=self.cleanse_uploaded_data(self.cleanse_date(self.data[23])) #self.data[23]
                self.cba.Credit_Account_Risk_Classification=int(self.data[24])
                self.cba.Credit_Account_Arrears_Date=self.cleanse_uploaded_data(self.cleanse_date(self.data[25])) #self.data[25]
                self.cba.Number_of_Days_in_Arrears=self.data[26]
                self.cba.Balance_Overdue=self.data[27]
                self.cba.Flag_for_Restructured_Credit=int(self.data[28])
                self.cba.Old_Branch_Code=self.data[29]
                self.cba.Old_Account_Number=self.data[30]
                self.cba.Old_Client_Number=self.data[31]
                self.cba.Balance_Overdue_Indicator=self.data[32]
                self.cba.Credit_Account_Closure_Date=self.cleanse_uploaded_data(self.cleanse_date(self.data[33])) #self.data[33]
                self.cba.Credit_Account_Closure_Reason=self.data[34]
                self.cba.Specific_Provision_Amount=self.data[35]
                self.cba.Client_Consent_Flag=self.data[36]
                self.cba.Client_Advice_Notice_Flag=self.data[37]
                self.cba.Term=self.data[38]
                self.cba.Loan_Purpose=self.data[39]
            self.cba.save()
        except:
            raise   
            
    def filter_datainsert(self, num_rows):
        try:
            if(num_rows):
                self.PI_CODE  = self.get_data_by_index(self.index_firstpost(num_rows))
                print "self.PI_CODE", self.PI_CODE
                if(self.PI_CODE):
                    self.ret_pid = self.query_or_save(self.PI_CODE)
                    
                self.BI_CODE  = self.get_data_by_index(self.index_firstpost(num_rows), index=2)

                print "BI_CODE ", self.BI_CODE
                if(self.BI_CODE):
                    self.ret_bi = self.query_or_save_bi(self.BI_CODE)
                    
                self.CLIENT_ID  = self.get_data_by_index(self.index_firstpost(num_rows, defaultindext=4), index=3)
                print "CLIENT NUMBER ", self.CLIENT_ID
                if(str(self.CLIENT_ID).strip().lstrip().rstrip()):
                    self.ret_clientid = self.search_clientnumber(float(self.CLIENT_ID))
                
                self.remaining_data = num_rows[4:]
                if( self.ret_clientid ):
                    self.save_legacy(self.remaining_data, self.ret_clientid, self.ret_pid, self.ret_bi)
                else:
                    print "Unable to save client with no number "
                        
        except Exception as e:
            #raise 
            print "ERROR ", e


    def query_all_headers(self):
        try:
            return branchmodel.RequiredHeader.objects.all()
        except:
            raise

    def query_pi_byid(self, ID):
        try:
            return branchmodel.RequiredHeader.objects.get(id=ID)
        except:
            raise
            
    def query_or_save(self, picode):
        try:
            self.all_query = branchmodel.PIIdentificationCode.objects.all()
            if(self.all_query):
                self.filtered_pi = self.all_query.get(pi_identification_code=str(picode))
                return self.filtered_pi
            else:
                #Save and return
                self.saved = branchmodel.PIIdentificationCode(pi_identification_code=picode)
                self.saved.save()
                return self.saved
        except:
            raise
            
    def query_all_branch(self):
        try:
            return branchmodel.DefaultHeaders.objects.all()
        except:
            raise

    def query_bi_byid(self, ID):
        try:
            return branchmodel.DefaultHeaders.objects.get(id=ID)
        except:
            raise

    def query_all_headers(self):
        try:
            return branchmodel.RequiredHeader.objects.all()
        except:
            raise

    def query_header_byid(self, ID):
        try:
            return branchmodel.RequiredHeader.objects.get(id=ID)
        except:
            raise

    def search_branch_details(self, branch_id, branch_name):
        try:
            self.branch_ = branch_id
            if(self.branch_.strip().lstrip().rstrip()):
                if(self.branch_ids):
                    self.branch = branchmodel.BranchNames.objects.get(Branch_Code=self.branch_ids)
                    if(self.branch):
                        return self.branch
                    
        except:
            raise
            
    def query_or_save_bi(self, branch):
        try:
            if(str(branch).strip().lstrip().rstrip()):
                self.branch_ids = float(branch)
                self.branch_ids = int(self.branch_ids)
                self.saved = branchmodel.RequiredHeader.objects.get(branch_code=self.branch_ids)
                return self.saved
        except branchmodel.RequiredHeader.DoesNotExist:
            pass 

    def search_clientnumber(self, clientnum):
        if(clientnum):
            try:
                self.c = str(clientnum).strip().lstrip().rstrip()
                if(self.c):
                    self.clientnumber = int(float(self.c))
                    print "Searching ", self.clientnumber
                    return datamodels.CREDIT_APPLICATION.objects.get(Client_Number=str(self.clientnumber))
                else:
                    print "Can't save client with no number"
                    pass 
            except datamodels.CREDIT_APPLICATION.DoesNotExist as e:
                print "Client was not found ", clientnum
            except datamodels.CREDIT_APPLICATION.MultipleObjectsReturned as e:
                print "Multile data returned ", e
