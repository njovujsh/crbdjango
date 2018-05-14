from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.template import Context, loader, RequestContext
from fileprocessor import forms as fileforms 
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.views import login
from django.views.generic.list import ListView
from django.forms.models import modelform_factory, modelformset_factory
import csv
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.encoding import smart_str
from reportlab.pdfgen import canvas
import datetime
import time
from django.forms.models import inlineformset_factory
import importlib
from datasets import models as record_models
from datasetrecords import models as datamodels
from datasetrecords import forms as dataset_forms 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datasetrecords import accreference 
from branchcode import forms as branchforms
from branchcode import models as branchmodel

class GeneralUpdate(View):
    @method_decorator(login_required)
    def get(self, request, record_slug, recordID):
        try:
           self.rendered = self.update_context(request, record_slug, recordID)
           return HttpResponse(self.rendered) 
        except:
            raise 
        
    def get_PCIModel(self):
        return datamodels.PCI

    def get_clientModel(self):
        return datamodels.ClientInformation
        
    def get_SCIModel(self):
        return datamodels.SCI
        
    def get_PCIForms(self):
        return dataset_forms.PCIForms

    def get_clientforms(self):
        return dataset_forms.ClientInformation_Forms
        
    #def get_stakeholder(self):
        #return dataset_forms.BorrowersStakeDetails_Forms
              
    def get_SCIForms(self):
        return dataset_forms.SCIForms
        
    def get_EIForms(self):
        return dataset_forms.EIForms
        
    def get_IDForms(self):
        return dataset_forms.IDForms
    
    def get_GSCAFBForms(self):
        return dataset_forms.GSCAFBForms
        
    def get_GSCAFB(self):
        return datamodels.GSCAFB_INFORMATION
        
    def get_EImodels(self):
        return datamodels.EMPLOYMENT_INFORMATION
        
    def get_IDmodel(self):
        return datamodels.IDENTIFICATION_INFORMATION
    
    def query_pci_sci_byID(self, pci_sci_model, ID):
        """
        Return the pcidata record given the ID
        """
        try:
            if(pci_sci_model and ID):
                try:
                    return pci_sci_model.objects.get(id=int(ID))
                except:
                    raise 
            else:
                return False 
        except:
            raise 
    
    def get_model_data(self, model, ID):
        try:
            if(model):
                if(ID):
                    self.model_data = model.objects.get(id=ID)
                    if(self.model_data):
                        return self.model_data
                    else:
                        return False
                else:
                    return None
            else:
                return None
        except:
            raise
            
    def get_insert_forms(self, dataset):
        try:
            if(dataset == "FINANCIAL MALPRACTICE DATA"):
                return dataset_forms.FRA_Forms
            elif(dataset == "COLLATERAL CREDIT GUARANTOR"):
                return dataset_forms.CCG_Forms
            elif(dataset == "COLLATERAL MATERIAL COLLATERAL"):
                return dataset_forms.CMC_Forms
            elif(dataset == "BORROWERSTAKEHOLDER"):
                return dataset_forms.BS_Forms
            elif(dataset == "BOUNCEDCHEQUES"):
                return dataset_forms.BC_Forms
            elif(dataset == "CREDIT APPLICATION"):
                return dataset_forms.CAP_Forms
            elif(dataset == "CREDITBORROWERACCOUNT"):
                return dataset_forms.CBA_Forms
            elif(dataset == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return dataset_forms.PIS_Forms
        except:
            raise
            
    def load_forms_insert(self, record_info):
        """
        Return the forms which will be used.
        """
        try:
            if(record_info.dataset_record == "COLLATERAL_MATERIAL_COLLATERAL"):
                return dataset_forms.CMC_Forms
            elif(record_info.dataset_record == "BORROWERSTAKEHOLDER"):
               return dataset_forms.BS_Forms
            elif(record_info.dataset_record == "BOUNCEDCHEQUES"):
                return dataset_forms.BC_Forms 
            elif(record_info.dataset_record == "COLLATERAL_CREDIT_GUARANTOR"):
                return dataset_forms.CCG_Forms
            elif(record_info.dataset_record == "CREDITBORROWERACCOUNT"):
                return dataset_forms.CBA_Forms 
            elif(record_info.dataset_record == "CREDIT_APPLICATION"):
                return dataset_forms.CAP_Forms
            elif(record_info.dataset_record == "FINANCIAL_MALPRACTICE_DATA"):
                return dataset_forms.FRA_Forms
            elif(record_info.dataset_record == "INSTITUTION_BRANCH"):
                return dataset_forms.IB_Forms
            elif(record_info.dataset_record == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return dataset_forms.PIS_Forms
            elif(record_info.dataset_record == "PARTICIPATING_INSTITUTION"):
                return dataset_forms.PI_Forms
            else:
                return False
        except:
            raise
                
    def get_models(self, dataset):
        try:
            if(dataset == "FINANCIAL MALPRACTICE DATA"):
                return datamodels.FINANCIAL_MALPRACTICE_DATA
            elif(dataset == "COLLATERAL CREDIT GUARANTOR"):
                return datamodels.COLLATERAL_CREDIT_GUARANTOR
            elif(dataset == "COLLATERAL MATERIAL COLLATERAL"):
                return datamodels.COLLATERAL_MATERIAL_COLLATERAL
            elif(dataset == "BORROWERSTAKEHOLDER"):
                return datamodels.BORROWERSTAKEHOLDER
            elif(dataset == "BOUNCEDCHEQUES"):
                return datamodels.BOUNCEDCHEQUES
            elif(dataset == "CREDIT APPLICATION"):
                return datamodels.CREDIT_APPLICATION
            elif(dataset == "CREDITBORROWERACCOUNT"):
                return datamodels.CREDITBORROWERACCOUNT
            elif(dataset == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return datamodels.PARTICIPATINGINSTITUTIONSTAKEHOLDER
           
        except:
            raise

    def get_acc_reference(self, saved, cn, how_many=None):
        try:
            if(how_many):
                return accreference.get_reference_number(saved, cn, numtimes=how_many)
            else:
                return accreference.get_reference_number(saved, cn)
        except:
            raise

    def save_borrower_history(self, status, amount, account_reference):
        try:
            if(status):
                self.history = datamodels.BorrowerHistory(borrower_status=status,
                                    amount=amount, account_reference=account_reference
                                    )
                self.history.save()
                return self.history
            else:
                return False
        except:
            raise

    def save_how_manytime(self, value):
        try:
            if(value):
                self.howmany = datamodels.BorrowingTimes(borrower_time=value)
                self.howmany.save()
                return self.howmany
            else:
                return False
        except:
            raise

    def update_track(self, instance, value=1):
        try:
            self.tracker = datamodels.BorrowingTimes.objects.get(id=instance.howmanytimes.id)
            self.tracker.borrower_time += value
            self.tracker.save()
            return self.tracker
        except:
            raise
            
    @method_decorator(login_required)
    def post(self, request, record_slug, recordID, pciID, sciID, ieid, idi, gsid):
        try:
            self.pcimodel = self.get_PCIModel()
            self.scimodel = self.get_SCIModel()
            self.iemodel = self.get_EImodels()
            self.idmodel = self.get_IDmodel()
            self.gsmodel = self.get_GSCAFB()
            self.clientmodel = self.get_clientModel()
            ####
            self.record_info = self.load_record_information(record_slug)
            self.formpost = self.load_forms_insert(self.record_info)

            if(record_slug == "credit_application"):
                self.clientUpdatingID = request.POST.get("clientUpdatingID", "")
                try:
                    #query the data we want to update 
                    self.record_models = self.get_models(self.record_info.dataset_record.replace("_", " ", len(self.record_info.dataset_record)))
                    
                    self.standard_quried = self.get_model_data(self.record_models, recordID)
                    
                    try:
                        #Querry all other associated records
                        self.pci_result = self.get_model_data(self.pcimodel, pciID)
                        self.sci_result = self.get_model_data(self.scimodel, sciID)
                        self.id_result = self.get_model_data(self.idmodel, idi)
                        self.ie_result = self.get_model_data(self.iemodel, ieid)
                        self.gs_result = self.get_model_data(self.gsmodel, gsid)
                        self.client_result = self.get_model_data(self.clientmodel, self.clientUpdatingID)
                    except:
                        raise 
                    else:
                        #Get the forms
                        self.pciform = self.get_PCIForms()
                        self.sciform = self.get_SCIForms()
                        self.id_form = self.get_IDForms()
                        self.ie_form = self.get_EIForms()
                        self.gs_form = self.get_GSCAFBForms()
                        self.client_form = self.get_clientforms()
                        self.pci_ret_result = self.pciform(request.POST, instance=self.pci_result, prefix="PCI_Forms")
                        self.sci_ret_result = self.sciform(request.POST, instance=self.sci_result, prefix="SCI_Forms")
                        self.id_ret_result = self.id_form(request.POST, instance=self.id_result, prefix="IDForms")
                        self.ei_ret_result = self.ie_form(request.POST, instance=self.ie_result, prefix="EIForms")
                        self.gs_ret_result = self.gs_form(request.POST, instance=self.gs_result, prefix="GSCAFBForms")
                        self.standard_ret = self.formpost(request.POST, instance=self.standard_quried, prefix="standard_forms")
                        self.client_instanceform = self.client_form(request.POST, instance=self.client_result, prefix="ClientDForms")
                        self.datasetrecords = self.get_datarecords()
                        
                        self.dicts = {"datasetforms":self.standard_ret, "datasetrecords":self.datasetrecords,
                                                    "dataid":recordID, "datasetupdate":"Updating new header files",
                                                    "basetitle":"CRB Systems",
                                                    'pciforms':self.pci_ret_result, 'sciforms':self.sci_ret_result,
                                                    'ieforms':self.ei_ret_result, 'idforms':self.id_ret_result,
                                                    'gscafbforms':self.gs_ret_result,"dataset_active":record_slug,
                                                    "pciID":pciID, "sciID":sciID, "ieid":ieid,
                                                    "idi":idi, "gsid":gsid, "clientupdatingID":self.clientUpdatingID
                        }
                        self.template = loader.get_template('datasetrecordsupdate.html')
                        try:
                            if(self.pci_ret_result.is_valid()):
                                self.pci_instance = self.pci_ret_result.save()
                                if(self.sci_ret_result.is_valid()):
                                    self.sci_instance = self.sci_ret_result.save()
                                    
                                    if(self.id_ret_result.is_valid()):
                                        self.id_instance = self.id_ret_result.save()
                                        
                                        if(self.ei_ret_result.is_valid()):
                                            self.ei_instance = self.ei_ret_result.save()
                                            
                                            if(self.gs_ret_result.is_valid()):
                                                self.gs_instance = self.gs_ret_result.save()

                                                if(self.client_instanceform.is_valid()):
                                                    self.client_instance = self.client_instanceform.save()
                                                else:
                                                    self.dicts["updateerrors"]=self.client_instanceform.errors
                                                    self.context = RequestContext(request, self.dicts)
                                                    return HttpResponse(self.template.render(self.context))
                                            else:
                                                self.dicts["updateerrors"]=self.gs_ret_result.errors
                                                self.context = RequestContext(request, self.dicts)
                                                return HttpResponse(self.template.render(self.context))
                                        else:
                                            self.dicts["updateerrors"]=self.ei_ret_result.errors
                                            self.context = RequestContext(request, self.dicts)
                                            return HttpResponse(self.template.render(self.context))
                                    else:
                                        self.dicts["updateerrors"]=self.id_ret_result.errors
                                        self.context = RequestContext(request, self.dicts)
                                        return HttpResponse(self.template.render(self.context))
                                else:
                                    self.dicts["updateerrors"]=self.sci_ret_result.errors
                                    self.context = RequestContext(request, self.dicts)
                                    return HttpResponse(self.template.render(self.context))
                            else:
                                self.dicts["updateerrors"]=self.pci_ret_result.errors
                                self.context = RequestContext(request, self.dicts)
                                return HttpResponse(self.template.render(self.context))
                        except Exception as e:
                            self.dicts["updateerrors"]=e
                            self.context = RequestContext(request, self.dicts)
                            return HttpResponse(self.template.render(self.context))
                            #raise 
                        else:
                            if(self.standard_ret.is_valid()):
                                self.CLIENT_NUMBER = request.POST.get("standard_forms-Client_Number", "")
                                try:
                                    self.standard_instance = self.standard_ret.save(commit=False)
                                    self.standard_instance.pci=self.pci_instance
                                    self.standard_instance.sci=self.sci_instance
                                    self.standard_instance.ei=self.ei_instance
                                    self.standard_instance.idi=self.id_instance
                                    self.standard_instance.gscafb=self.gs_instance
                                    self.standard_instance.client_details=self.client_instance
                                    
                                    #finaly save
                                except Exception as e:
                                    self.dicts["updateerrors"]=e
                                    self.context = RequestContext(request, self.dicts)
                                    return HttpResponse(self.template.render(self.context))
                                    #raise 
                                else:
                                    print "Reborrowing...."
                                    self.reborrowing = request.POST.get("reborrowing", "")
                                    self.amounts = request.POST.get('standard_forms-Amount', "")
                                    
                                    if(self.reborrowing):
                                        print "We are in run level two"
                                        if(self.standard_instance.howmanytimes):
                                            self.track_instance = self.update_track(self.standard_instance)
                                        else:
                                            self.track_instance = self.save_how_manytime(1)
                                        
                                        self.standard_instance.save()
                                        self.reference_number = request.POST.get("standard_forms-Credit_Application_Reference", "")
                                        
                                        if(len(self.reference_number) == 0 or self.reference_number == None):
                                            print "We are in run level three..."
                                            self.products_type = request.POST.get("standard_forms-Credit_Account_or_Loan_Product_Type", "")
                                            if(self.products_type):
                                                print "We are in run level four..."
                                                self.reference = self.get_acc_reference(self.products_type, self.CLIENT_NUMBER, self.track_instance.borrower_time)
                                                self.standard_instance.Credit_Application_Reference=self.reference
                                                self.standard_instance.save()

                                                print "We are in run level five and I filed he is reborrowing.."
                                                self.bhistory = self.save_borrower_history(self.track_instance.borrower_time, self.amounts, self.reference)
                                                #self.standard_instance.history=self.bhistory
                                                self.standard_instance.save()
                                                self.standard_instance.history.add(self.bhistory)
                                                self.standard_ret.save_m2m()
                                                
                                                url = "/view/dataview/request/%s/" % str(self.record_info.slug)
                                                return HttpResponseRedirect(url)
                                                
                                            else:
                                                print "HOW MANY ", self.track_instance.borrower_time
                                                self.reference = self.get_acc_reference(self.products_type, self.CLIENT_NUMBER, self.track_instance.borrower_time)
                                                self.standard_instance.Credit_Application_Reference=self.reference
                                                self.standard_instance.save()

                                                self.bhistory = self.save_borrower_history(self.track_instance.borrower_time, self.amounts, self.reference)
                                                #self.standard_instance.history=self.bhistory
                                                self.standard_instance.save()
                                                self.standard_instance.history.add(self.bhistory)
                                                self.standard_ret.save_m2m()
                                                    
                                                url = "/view/dataview/request/%s/" % str(self.record_info.slug)
                                                return HttpResponseRedirect(url)
                                        else:
                                            #print "HOW MANY ", #self.standard_instance.howmanytimes.borrower_time 0170422305711 
                                            #print "We are in run level three..."
                                            self.products_type = request.POST.get("standard_forms-Credit_Account_or_Loan_Product_Type", "")

                                            if(self.products_type):
                                                print "We are in run level four..."
                                                self.reference = accreference.update_reference_number(self.reference_number, self.products_type, self.standard_quried, self.track_instance.borrower_time)
                                                if(self.reference):
                                                    
                                                    self.standard_instance.Credit_Application_Reference=self.reference
                                                    self.standard_instance.howmanytimes = self.track_instance
                                                    self.standard_instance.save()
                                                else:
                                                    self.reference = self.get_acc_reference(self.products_type, self.CLIENT_NUMBER, self.track_instance.borrower_time)
                                                    self.standard_instance.Credit_Application_Reference=self.reference
                                                    self.standard_instance.howmanytimes = self.track_instance
                                                    self.standard_instance.save()

                                                print "We are in run level five woops may fail", self.track_instance.borrower_time, self.reference
                                                
                                                try:
                                                    self.bhistory = self.save_borrower_history(self.track_instance.borrower_time, self.amounts, self.reference)
                                                    self.standard_instance.save()
                                                    self.standard_instance.history.add(self.bhistory) #  save()
                                                    self.standard_instance.save()
                                                    self.standard_ret.save_m2m()
                                                except:
                                                    raise
                                                else:
                                                    url = "/view/dataview/request/%s/" % str(self.record_info.slug)
                                                    return HttpResponseRedirect(url)
                                            else:
                                                self.reference = self.get_acc_reference(self.products_type, self.CLIENT_NUMBER, self.track_instance.borrower_time)
                                                self.standard_instance.Credit_Application_Reference=self.reference
                                                self.standard_instance.save()

                                                self.bhistory = self.save_borrower_history(self.track_instance.borrower_time, self.amounts, self.reference)
                                                #self.standard_instance.history=self.bhistory
                                                self.standard_instance.save()
                                                self.standard_instance.history.add(self.bhistory)
                                                self.standard_ret.save_m2m()
                                                    
                                                url = "/view/dataview/request/%s/" % str(self.record_info.slug)
                                                return HttpResponseRedirect(url)
                                    else:
                                        self.standard_instance.save()
                                        self.reference_number = request.POST.get("standard_forms-Credit_Application_Reference", "")
                                        
                                        self.howmany_time = 0
                                        if(self.standard_instance.howmanytimes):
                                            self.howmany_time = self.standard_instance.howmanytimes.borrower_time
                                        else:
                                            self.howmany_time = self.save_how_manytime(1)
                                        
                                        if(len(self.reference_number) == 0 or self.reference_number == None):
                                            self.products_type = request.POST.get("standard_forms-Credit_Account_or_Loan_Product_Type", "")
                                            if(self.products_type):
                                                self.reference = self.get_acc_reference(self.products_type, self.CLIENT_NUMBER, self.howmany_time)
                                                self.standard_instance.Credit_Application_Reference=self.reference
                                                self.standard_instance.howmanytimes=self.howmany_time
                                                self.standard_instance.save()

                                                self.bhistory = self.save_borrower_history(self.howmany_time.borrower_time, self.amounts, self.reference)
                                                #self.standard_instance.history=self.bhistory
                                                self.standard_instance.save()
                                                self.standard_instance.history.add(self.bhistory)
                                                self.standard_ret.save_m2m()
                                                
                                            #else:
                                            #    self.reference = self.get_acc_reference(self.products_type, self.track_instance.borrower_time)
                                            #    self.standard_instance.Credit_Application_Reference=self.reference
                                            #    self.standard_instance.save()

                                            #    self.bhistory = self.save_borrower_history(self.howmany_time.borrower_time, self.amounts, self.reference)
                                                #self.standard_instance.history=self.bhistory
                                            #    self.standard_instance.save()
                                            #    self.standard_instance.history.add(self.bhistory)
                                            #    self.standard_ret.save_m2m()
                                            
                                        
                                            url = "/view/dataview/request/%s/" % str(self.record_info.slug)
                                            return HttpResponseRedirect(url)
                                        else:
                                            if(self.standard_instance.howmanytimes):
                                                url = "/view/dataview/request/%s/" % str(self.record_info.slug)
                                                return HttpResponseRedirect(url)
                                            else:
                                                self.bhistory = self.save_borrower_history(self.howmany_time.borrower_time, self.amounts, self.reference_number)
                                                self.standard_instance.save()
                                                self.standard_instance.history.add(self.bhistory) #  save()
                                                self.standard_instance.save()
                                                self.standard_ret.save_m2m()
                                            
                                                url = "/view/dataview/request/%s/" % str(self.record_info.slug)
                                                return HttpResponseRedirect(url)
                                            
                            else:
                                self.dicts["updateerrors"]=self.standard_ret.errors
                                self.context = RequestContext(request, self.dicts)
                                return HttpResponse(self.template.render(self.context))
                                #raise 
                except Exception as e:
                    self.dicts["updateerrors"]=e
                    self.context = RequestContext(request, self.dicts)
                    return HttpResponse(self.template.render(self.context))
                    #raise
                    
            elif record_slug == "borrowerstakeholder":
                self.dicts = {}
                try:
                    #query the data we want to update 
                    self.record_models = self.get_models(self.record_info.dataset_record.replace("_", " ", len(self.record_info.dataset_record)))
                    self.standard_quried = self.get_model_data(self.record_models, recordID)
                    #self.stakeholdermodel = datamodels.BorrowersStakeDetails
                    self.stake_ID = request.POST.get("stakeholderID", "")
                    
                    try:
                        #Querry all other associated records
                        self.pci_result = self.get_model_data(self.pcimodel, pciID)
                        self.sci_result = self.get_model_data(self.scimodel, sciID)
                        self.id_result = self.get_model_data(self.idmodel, idi)
                        self.ie_result = self.get_model_data(self.iemodel, ieid)
                        self.gs_result = self.get_model_data(self.gsmodel, gsid)
                        #self.stakeresult_result = self.get_model_data(self.stakeholdermodel, self.stake_ID)
                    except:
                        raise 
                    else:
                        #Get the forms
                        self.pciform = self.get_PCIForms()
                        self.sciform = self.get_SCIForms()
                        self.id_form = self.get_IDForms()
                        self.ie_form = self.get_EIForms()
                        self.gs_form = self.get_GSCAFBForms()
                        #self.stake_form = self.get_stakeholder()
                        self.pci_ret_result = self.pciform(request.POST, instance=self.pci_result, prefix="PCI_Forms")
                        self.sci_ret_result = self.sciform(request.POST, instance=self.sci_result, prefix="SCI_Forms")
                        self.id_ret_result = self.id_form(request.POST, instance=self.id_result, prefix="IDForms")
                        self.ei_ret_result = self.ie_form(request.POST, instance=self.ie_result, prefix="EIForms")
                        self.gs_ret_result = self.gs_form(request.POST, instance=self.gs_result, prefix="GSCAFBForms")
                        self.standard_ret = self.formpost(request.POST, instance=self.standard_quried, prefix="standard_forms")
                        #self.client_instanceform = self.stake_form(request.POST, instance=self.stakeresult_result, prefix="stakeholderforms")
                        self.datasetrecords = self.get_datarecords()
                        
                        self.dicts["datasetforms"]=self.standard_ret,
                        self.dicts["datasetrecords"]=self.datasetrecords,
                        self.dicts["dataid"]=recordID,
                        self.dicts["datasetupdate"]="Updating new header files",
                        self.dicts["basetitle"]="CRB Systems",
                        self.dicts['pciforms']=self.pci_ret_result,
                        self.dicts['sciforms']=self.sci_ret_result,
                        self.dicts['ieforms']=self.ei_ret_result,
                        self.dicts['idforms']=self.id_ret_result,
                        self.dicts['gscafbforms']=self.gs_ret_result,
                        self.dicts["dataset_active"]=record_slug,
                        self.dicts["pciID"]=pciID,
                        self.dicts["sciID"]=sciID,
                        self.dicts["ieid"]=ieid,
                        self.dicts["idi"]=idi,
                        self.dicts["gsid"]=gsid,
                        self.dicts["stakeholderID"]=self.stake_ID

                        self.template = loader.get_template('datasetrecordsupdate.html')
                        try:
                            if(self.pci_ret_result.is_valid()):
                                self.pci_instance = self.pci_ret_result.save()
                                if(self.sci_ret_result.is_valid()):
                                    self.sci_instance = self.sci_ret_result.save()
                                    
                                    if(self.id_ret_result.is_valid()):
                                        self.id_instance = self.id_ret_result.save()
                                        
                                        if(self.ei_ret_result.is_valid()):
                                            self.ei_instance = self.ei_ret_result.save()
                                            
                                            if(self.gs_ret_result.is_valid()):
                                                self.gs_instance = self.gs_ret_result.save()
                                            else:
                                                self.dicts["updateerrors"]=self.gs_ret_result.errors
                                                self.context = RequestContext(request, self.dicts)
                                                return HttpResponse(self.template.render(self.context)) 
                                        else:
                                            self.dicts["updateerrors"]=self.ei_ret_result.errors
                                            self.context = RequestContext(request, self.dicts)
                                            return HttpResponse(self.template.render(self.context)) 
                                    else:
                                        self.dicts["updateerrors"]=self.id_ret_result.errors
                                        self.context = RequestContext(request, self.dicts)
                                        return HttpResponse(self.template.render(self.context))  
                                else:
                                    self.dicts["updateerrors"]=self.sci_ret_result.errors
                                    self.context = RequestContext(request, self.dicts)
                                    return HttpResponse(self.template.render(self.context)) 
                            else:
                                self.dicts["updateerrors"]=self.pci_ret_result.errors
                                self.context = RequestContext(request, self.dicts)
                                return HttpResponse(self.template.render(self.context))
                        except Exception as e:
                            self.dicts["updateerrors"]=e
                            self.context = RequestContext(request, self.dicts)
                            return HttpResponse(self.template.render(self.context))
                            #raise 
                        else:
                            #if(self.client_instanceform.is_valid()):
                            #self.client_save_ret = self.client_instanceform.save()
                            if(self.standard_ret.is_valid()):
                                try:
                                    self.standard_instance = self.standard_ret.save(commit=False)
                                    self.standard_instance.pci=self.pci_instance
                                    self.standard_instance.sci=self.sci_instance
                                    self.standard_instance.ei=self.ei_instance
                                    self.standard_instance.idi=self.id_instance
                                    self.standard_instance.gscafb=self.gs_instance
                                    #self.standard_instance.borrower_stake_details=self.client_save_ret
                                    
                                    #finaly save
                                except Exception as e:
                                    self.dicts["updateerrors"]=e
                                    self.context = RequestContext(request, self.dicts)
                                    return HttpResponse(self.template.render(self.context))
                                    #raise 
                                else:
                                    self.standard_instance.save()
                                    url = "/view/dataview/request/%s/" % str(self.record_info.slug)
                                    return HttpResponseRedirect(url)
                                    #raise 
                            else:
                                self.dicts["updateerrors"]=self.standard_ret.errors
                                self.context = RequestContext(request, self.dicts)
                                return HttpResponse(self.template.render(self.context))
                                #raise 
                except Exception as e:
                    self.template = loader.get_template("datasetrecordsupdate.html")
                    self.dicts["updateerrors"]=e
                    self.context = RequestContext(request, self.dicts)
                    return HttpResponse(self.template.render(self.context))
                    #raise 
                    
            else:
                try:
                    #query the data we want to update 
                    self.record_models = self.get_models(self.record_info.dataset_record.replace("_", " ", len(self.record_info.dataset_record)))
                    
                    self.standard_quried = self.get_model_data(self.record_models, recordID)
                    
                    try:
                        #Querry all other associated records
                        self.pci_result = self.get_model_data(self.pcimodel, pciID)
                        self.sci_result = self.get_model_data(self.scimodel, sciID)
                        self.id_result = self.get_model_data(self.idmodel, idi)
                        self.ie_result = self.get_model_data(self.iemodel, ieid)
                        self.gs_result = self.get_model_data(self.gsmodel, gsid)
                        #self.client_result = self.get_model_data(self.clientmodel, self.clientUpdatingID)
                    except:
                        raise 
                    else:
                        #Get the forms
                        self.pciform = self.get_PCIForms()
                        self.sciform = self.get_SCIForms()
                        self.id_form = self.get_IDForms()
                        self.ie_form = self.get_EIForms()
                        self.gs_form = self.get_GSCAFBForms()
                        #self.client_form = self.get_clientforms()
                        
                        self.pci_ret_result = self.pciform(request.POST, instance=self.pci_result, prefix="PCI_Forms")
                        self.sci_ret_result = self.sciform(request.POST, instance=self.sci_result, prefix="SCI_Forms")
                        self.id_ret_result = self.id_form(request.POST, instance=self.id_result, prefix="IDForms")
                        self.ei_ret_result = self.ie_form(request.POST, instance=self.ie_result, prefix="EIForms")
                        self.gs_ret_result = self.gs_form(request.POST, instance=self.gs_result, prefix="GSCAFBForms")
                        self.standard_ret = self.formpost(request.POST, instance=self.standard_quried, prefix="standard_forms")
                        #self.client_instanceform = self.client_form(request.POST, instance=self.client_result, prefix="ClientDForms")
                        self.datasetrecords = self.get_datarecords()
                        
                        self.dicts = {"datasetforms":self.standard_ret, "datasetrecords":self.datasetrecords,
                                                    "dataid":recordID, "datasetupdate":"Updating new header files",
                                                    "basetitle":"CRB Systems",
                                                    'pciforms':self.pci_ret_result, 'sciforms':self.sci_ret_result,
                                                    'ieforms':self.ei_ret_result, 'idforms':self.id_ret_result,
                                                    'gscafbforms':self.gs_ret_result,"dataset_active":record_slug,
                                                    "pciID":pciID, "sciID":sciID, "ieid":ieid,
                                                    "idi":idi, "gsid":gsid
                        }
                        self.template = loader.get_template('datasetrecordsupdate.html')
                        try:
                            if(self.pci_ret_result.is_valid()):
                                self.pci_instance = self.pci_ret_result.save()
                                if(self.sci_ret_result.is_valid()):
                                    self.sci_instance = self.sci_ret_result.save()
                                    
                                    if(self.id_ret_result.is_valid()):
                                        self.id_instance = self.id_ret_result.save()
                                        
                                        if(self.ei_ret_result.is_valid()):
                                            self.ei_instance = self.ei_ret_result.save()
                                            
                                            if(self.gs_ret_result.is_valid()):
                                                self.gs_instance = self.gs_ret_result.save()
                                            else:
                                                self.dicts["updateerrors"]=self.gs_ret_result.errors
                                                self.context = RequestContext(request, self.dicts)
                                                return HttpResponse(self.template.render(self.context)) 
                                        else:
                                            self.dicts["updateerrors"]=self.ei_ret_result.errors
                                            self.context = RequestContext(request, self.dicts)
                                            return HttpResponse(self.template.render(self.context)) 
                                    else:
                                        self.dicts["updateerrors"]=self.id_ret_result.errors
                                        self.context = RequestContext(request, self.dicts)
                                        return HttpResponse(self.template.render(self.context))  
                                else:
                                    self.dicts["updateerrors"]=self.sci_ret_result.errors
                                    self.context = RequestContext(request, self.dicts)
                                    return HttpResponse(self.template.render(self.context)) 
                            else:
                                self.dicts["updateerrors"]=self.pci_ret_result.errors
                                self.context = RequestContext(request, self.dicts)
                                return HttpResponse(self.template.render(self.context))
                        except Exception as e:
                            self.dicts["updateerrors"]=e
                            self.context = RequestContext(request, self.dicts)
                            return HttpResponse(self.template.render(self.context))
                        else:
                            if(self.standard_ret.is_valid()):
                                try:
                                    self.standard_instance = self.standard_ret.save(commit=False)
                                    self.standard_instance.pci=self.pci_instance
                                    self.standard_instance.sci=self.sci_instance
                                    self.standard_instance.ei=self.ei_instance
                                    self.standard_instance.idi=self.id_instance
                                    self.standard_instance.gscafb=self.gs_instance
                                    
                                    #finaly save
                                except Exception as e:
                                    self.dicts["updateerrors"]=e
                                    self.context = RequestContext(request, self.dicts)
                                    return HttpResponse(self.template.render(self.context))
                                else:
                                    self.standard_instance.save()
                                    url = "/view/dataview/request/%s/" % str(self.record_info.slug)
                                    return HttpResponseRedirect(url)
                            else:
                                self.dicts["updateerrors"]=self.standard_ret.errors
                                self.context = RequestContext(request, self.dicts)
                                return HttpResponse(self.template.render(self.context))
                                
                except Exception as e:
                    self.dicts["updateerrors"]=e
                    self.context = RequestContext(request, self.dicts)
                    return HttpResponse(self.template.render(self.context))
        except:
            raise 
            

    def get_headers_from_instance(self, query_instance):
        """
        Given the model query install from main dataset.
        return the corresponding query sets of defaultheaders by performing reverse lookup.
        """
        return query_instance.PI_Identification_Code.defaultheaders_set.get_queryset()

    def get_default_headerform(self):
        """
        Return the forms for defaultheaders.
        """
        return branchforms.DefaultHeadersForms
        
    def get_default_branch(self):
        """
        Return the forms for defaultheaders.
        """
        return branchforms.RequiredHeaderForm

    def get_queryset_updated(self, query_instance):
        try:
            
            #query_header = query_instance.PI_Identification_Code.defaultheaders_set
            return query_instance.Branch_Identification_Code
            #ID = 0
          
        except:
            raise
            
    def update_context(self, request, record_slug, dataID):
        self.datasetrecords = self.get_datarecords()
        try:
            self.record_details = self.load_record_information(record_slug)
            self.forms = self.get_insert_forms(self.record_details.dataset_record.replace("_", " ", len(self.record_details.dataset_record)))
            self.model = self.get_models(self.record_details.dataset_record.replace("_", " ", len(self.record_details.dataset_record)))
            self.updating_instance = self.get_model_data(self.model, dataID)
            self.formset = self.load_form_instance(self.forms, self.updating_instance, prefix="standard_forms")
            
            self.pciform = self.get_PCIForms()
            self.sciform = self.get_SCIForms()
            self.ieform = self.get_EIForms()
            self.idform = self.get_IDForms()
            self.gscafbforms = self.get_GSCAFBForms()
            self.client_detailsformset = self.get_clientforms()
            #self.stake_detailsformset = self.get_stakeholder()
            
            # Get the default header query and the forms
            if(record_slug == "participating_institution" or record_slug == "participatinginstitutionstakeholder"):
                self.header_form_instance = None
            else:
                self.default_headers_set = self.get_queryset_updated(self.updating_instance)
                if(self.default_headers_set):
                    self.header_forms = self.get_default_branch()
                    
                    #Pass the instance into the form
                    self.header_form_instance = self.load_form_instance(self.header_forms, self.updating_instance.Branch_Identification_Code, prefix="defaultheaders")
                else:
                    self.header_form_instance = None #self.load_form_instance(self.header_forms, self.default_headers_set, prefix="defaultheaders") 
            
            #print "SLUG ", record_slug
            if(record_slug == "creditborroweraccount"):
                self.pciformset = self.load_form_instance(self.pciform, self.updating_instance.Borrowers_Client_Number.pci, prefix="PCI_Forms")
                self.sciformset = self.load_form_instance(self.sciform, self.updating_instance.Borrowers_Client_Number.sci, prefix="SCI_Forms")
                self.ieformset = self.load_form_instance(self.ieform, self.updating_instance.Borrowers_Client_Number.ei, prefix="EIForms")
                self.idformset = self.load_form_instance(self.idform, self.updating_instance.Borrowers_Client_Number.idi, prefix="IDForms")
                self.gscafbformsset = self.load_form_instance(self.gscafbforms, self.updating_instance.Borrowers_Client_Number.gscafb, prefix="GSCAFBForms")
                self.user_detailsformset = self.load_form_instance(self.client_detailsformset, self.updating_instance.Borrowers_Client_Number.client_details, prefix="ClientDForms")
                try:
                    self.pcid = self.updating_instance.Borrowers_Client_Number.pci.id
                    self.sciid = self.updating_instance.Borrowers_Client_Number.sci.id
                    self.ieid = self.updating_instance.Borrowers_Client_Number.ei.id
                    self.idi = self.updating_instance.Borrowers_Client_Number.idi.id
                    self.gsid = self.updating_instance.Borrowers_Client_Number.gscafb.id
                    self.clientupdatid = self.updating_instance.Borrowers_Client_Number.client_details.id
                except Except:
                    self.template = loader.get_template('datasetrecordsupdate.html')
                    self.context = RequestContext(request, {"generrors":e})
                    return HttpResponse(self.template.render(self.context))  
                try:
                    self.context = RequestContext(request, {"datasetforms":self.formset, "datasetrecords":self.datasetrecords,
                                                            "dataid":dataID, "datasetupdate":"Updating new header files",
                                                            "basetitle":"CRB Systems",
                                                            'pciforms':self.pciformset, 'sciforms':self.sciformset,
                                                            'ieforms':self.ieformset, 'idforms':self.idformset,
                                                            'gscafbforms':self.gscafbformsset,"dataset_active":record_slug,
                                                            "pciID":self.pcid, "sciID":self.sciid, "ieid":self.ieid,
                                                            "idi":self.idi, "gsid":self.gsid,"clientform":self.user_detailsformset,
                                                            "clientupdatingID":self.clientupdatid, "updating_instance":self.updating_instance,
                                                            "header_form_instance":self.header_form_instance, "default_headers":self.header_form_instance,
                                                            "ClientNumber":self.updating_instance.Borrowers_Client_Number
                                                  })
                except Exception as e:
                    self.template = loader.get_template('datasetrecordsupdate.html')
                    self.context = RequestContext(request, {"generrors":e})
                    return HttpResponse(self.template.render(self.context))
                    #raise 
                else:
                    self.template = self.get_template()
                    return self.template.render(self.context)
                    
            if(record_slug == "bouncedcheques"):
                self.pciformset = self.load_form_instance(self.pciform, self.updating_instance.Borrowers_Client_Number.pci, prefix="PCI_Forms")
                self.sciformset = self.load_form_instance(self.sciform, self.updating_instance.Borrowers_Client_Number.sci, prefix="SCI_Forms")
                self.ieformset = self.load_form_instance(self.ieform, self.updating_instance.Borrowers_Client_Number.ei, prefix="EIForms")
                self.idformset = self.load_form_instance(self.idform, self.updating_instance.Borrowers_Client_Number.idi, prefix="IDForms")
                self.gscafbformsset = self.load_form_instance(self.gscafbforms, self.updating_instance.Borrowers_Client_Number.gscafb, prefix="GSCAFBForms")
                self.user_detailsformset = self.load_form_instance(self.client_detailsformset, self.updating_instance.Borrowers_Client_Number.client_details, prefix="ClientDForms")

                try:
                    self.pcid = self.updating_instance.Borrowers_Client_Number.pci.id
                    self.sciid = self.updating_instance.Borrowers_Client_Number.sci.id
                    self.ieid = self.updating_instance.Borrowers_Client_Number.ei.id
                    self.idi = self.updating_instance.Borrowers_Client_Number.idi.id
                    self.gsid = self.updating_instance.Borrowers_Client_Number.gscafb.id
                    self.clientupdatid = self.updating_instance.Borrowers_Client_Number.client_details.id
                except Exception as e:
                    self.template = loader.get_template('datasetrecordsupdate.html')
                    self.context = RequestContext(request, {"generrors":e})
                    return HttpResponse(self.template.render(self.context))
                try:
                    self.context = RequestContext(request, {"datasetforms":self.formset, "datasetrecords":self.datasetrecords,
                                                            "dataid":dataID, "datasetupdate":"Updating new header files",
                                                            "basetitle":"CRB Systems",
                                                            'pciforms':self.pciformset, 'sciforms':self.sciformset,
                                                            'ieforms':self.ieformset, 'idforms':self.idformset,
                                                            'gscafbforms':self.gscafbformsset,"dataset_active":record_slug,
                                                            "pciID":self.pcid, "sciID":self.sciid, "ieid":self.ieid,
                                                            "idi":self.idi, "gsid":self.gsid,"clientform":self.user_detailsformset,
                                                            "clientupdatingID":self.clientupdatid, "updating_instance":self.updating_instance,
                                                            "default_headers":self.header_form_instance, "ClientNumber":self.updating_instance.Borrowers_Client_Number
                                                  })
                except Exception as e:
                    self.template = loader.get_template('datasetrecordsupdate.html')
                    self.context = RequestContext(request, {"generrors":e})
                    return HttpResponse(self.template.render(self.context))
                else:
                    self.template = self.get_template()
                    return self.template.render(self.context)
                    
            elif(record_slug == "financial_malpractice_data"):
                self.pciformset = self.load_form_instance(self.pciform, self.updating_instance.Borrowers_Client_Number.pci, prefix="PCI_Forms")
                self.sciformset = self.load_form_instance(self.sciform, self.updating_instance.Borrowers_Client_Number.sci, prefix="SCI_Forms")
                self.ieformset = self.load_form_instance(self.ieform, self.updating_instance.Borrowers_Client_Number.ei, prefix="EIForms")
                self.idformset = self.load_form_instance(self.idform, self.updating_instance.Borrowers_Client_Number.idi, prefix="IDForms")
                self.gscafbformsset = self.load_form_instance(self.gscafbforms, self.updating_instance.Borrowers_Client_Number.gscafb, prefix="GSCAFBForms")
                self.user_detailsformset = self.load_form_instance(self.client_detailsformset, self.updating_instance.Borrowers_Client_Number.client_details, prefix="ClientDForms")
                try:
                    self.pcid = self.updating_instance.Borrowers_Client_Number.pci.id
                    self.sciid = self.updating_instance.Borrowers_Client_Number.sci.id
                    self.ieid = self.updating_instance.Borrowers_Client_Number.ei.id
                    self.idi = self.updating_instance.Borrowers_Client_Number.idi.id
                    self.gsid = self.updating_instance.Borrowers_Client_Number.gscafb.id
                    self.clientupdatid = self.updating_instance.Borrowers_Client_Number.client_details.id
                except Exception as e:
                    self.template = loader.get_template('datasetrecordsupdate.html')
                    self.context = RequestContext(request, {"generrors":e})
                    return HttpResponse(self.template.render(self.context))  
                try:
                    self.context = RequestContext(request, {"datasetforms":self.formset, "datasetrecords":self.datasetrecords,
                                                            "dataid":dataID, "datasetupdate":"Updating new header files",
                                                            "basetitle":"CRB Systems",
                                                            'pciforms':self.pciformset, 'sciforms':self.sciformset,
                                                            'ieforms':self.ieformset, 'idforms':self.idformset,
                                                            'gscafbforms':self.gscafbformsset,"dataset_active":record_slug,
                                                            "pciID":self.pcid, "sciID":self.sciid, "ieid":self.ieid,
                                                            "idi":self.idi, "gsid":self.gsid,"clientform":self.user_detailsformset,
                                                            "clientupdatingID":self.clientupdatid, "updating_instance":self.updating_instance,
                                                            "default_headers":self.header_form_instance, "ClientNumber":self.updating_instance.Borrowers_Client_Number
                                                  })
                except Exception as e:
                    self.template = loader.get_template('datasetrecordsupdate.html')
                    self.context = RequestContext(request, {"generrors":e})
                    return HttpResponse(self.template.render(self.context))
                else:
                    self.template = self.get_template()
                    return self.template.render(self.context)
                    
            elif(record_slug == "collateral_material_collateral"):
                self.pciformset = self.load_form_instance(self.pciform, self.updating_instance.Borrowers_Client_Number.pci, prefix="PCI_Forms")
                self.sciformset = self.load_form_instance(self.sciform, self.updating_instance.Borrowers_Client_Number.sci, prefix="SCI_Forms")
                self.ieformset = self.load_form_instance(self.ieform, self.updating_instance.Borrowers_Client_Number.ei, prefix="EIForms")
                self.idformset = self.load_form_instance(self.idform, self.updating_instance.Borrowers_Client_Number.idi, prefix="IDForms")
                self.gscafbformsset = self.load_form_instance(self.gscafbforms, self.updating_instance.Borrowers_Client_Number.gscafb, prefix="GSCAFBForms")
                self.user_detailsformset = self.load_form_instance(self.client_detailsformset, self.updating_instance.Borrowers_Client_Number.client_details, prefix="ClientDForms")

                try:
                    self.pcid = self.updating_instance.Borrowers_Client_Number.pci.id
                    self.sciid = self.updating_instance.Borrowers_Client_Number.sci.id
                    self.ieid = self.updating_instance.Borrowers_Client_Number.ei.id
                    self.idi = self.updating_instance.Borrowers_Client_Number.idi.id
                    self.gsid = self.updating_instance.Borrowers_Client_Number.gscafb.id
                    self.clientupdatid = self.updating_instance.Borrowers_Client_Number.client_details.id
                except Exception as e:
                    self.template = loader.get_template('datasetrecordsupdate.html')
                    self.context = RequestContext(request, {"generrors":e})
                    return HttpResponse(self.template.render(self.context))  
                try:
                    self.context = RequestContext(request, {"datasetforms":self.formset, "datasetrecords":self.datasetrecords,
                                                            "dataid":dataID, "datasetupdate":"Updating new header files",
                                                            "basetitle":"CRB Systems",
                                                            'pciforms':self.pciformset, 'sciforms':self.sciformset,
                                                            'ieforms':self.ieformset, 'idforms':self.idformset,
                                                            'gscafbforms':self.gscafbformsset,"dataset_active":record_slug,
                                                            "pciID":self.pcid, "sciID":self.sciid, "ieid":self.ieid,
                                                            "idi":self.idi, "gsid":self.gsid,"clientform":self.user_detailsformset,
                                                            "clientupdatingID":self.clientupdatid, "updating_instance":self.updating_instance,
                                                            "default_headers":self.header_form_instance, "ClientNumber":self.updating_instance.Borrowers_Client_Number
                                                  })
                except Exception as e:
                    self.template = loader.get_template('datasetrecordsupdate.html')
                    self.context = RequestContext(request, {"generrors":e})
                    return HttpResponse(self.template.render(self.context))  
                else:
                    self.template = self.get_template()
                    return self.template.render(self.context)
                    
            elif(record_slug == "collateral_credit_guarantor"):
                self.pciformset = self.loadpciinstance(self.pciform, self.updating_instance.pci, prefix="PCI_Forms", initial=True)
                self.sciformset = self.load_form_instance(self.sciform, self.updating_instance.sci, prefix="SCI_Forms")
                self.ieformset = self.load_form_instance(self.ieform, self.updating_instance.ei, prefix="EIForms")
                self.idformset = self.load_form_instance(self.idform, self.updating_instance.idi, prefix="IDForms")
                self.gscafbformsset = self.load_form_instance(self.gscafbforms, self.updating_instance.gscafb, prefix="GSCAFBForms")
                self.user_detailsformset = self.load_form_instance(self.client_detailsformset, self.updating_instance.Borrowers_Client_Number.client_details, prefix="ClientDForms")

                try:
                    self.pcid = self.updating_instance.pci.id
                    self.sciid = self.updating_instance.sci.id
                    self.ieid = self.updating_instance.ei.id
                    self.idi = self.updating_instance.idi.id
                    self.gsid = self.updating_instance.gscafb.id
                    self.clientupdatid = self.updating_instance.Borrowers_Client_Number.client_details.id
                except Exception as e:
                    self.template = loader.get_template('datasetrecordsupdate.html')
                    self.context = RequestContext(request, {"generrors":e})
                    return HttpResponse(self.template.render(self.context)) 
                try:
                    self.context = RequestContext(request, {"datasetforms":self.formset, "datasetrecords":self.datasetrecords,
                                                            "dataid":dataID, "datasetupdate":"Updating Records",
                                                            'pciforms':self.pciformset, 'sciforms':self.sciformset,
                                                            'ieforms':self.ieformset, 'idforms':self.idformset,
                                                            'gscafbforms':self.gscafbformsset,"dataset_active":record_slug,
                                                            "pciID":self.pcid, "sciID":self.sciid, "ieid":self.ieid,
                                                            "idi":self.idi, "gsid":self.gsid, "title":"CRB",
                                                            "clientform":self.user_detailsformset, "clientupdatingID":self.clientupdatid,
                                                            "updating_instance":self.updating_instance, "default_headers":self.header_form_instance,
                                                            "ClientNumber":self.updating_instance.Borrowers_Client_Number
                                                  })
                except Exception as e:
                    self.template = loader.get_template('datasetrecordsupdate.html')
                    self.context = RequestContext(request, {"generrors":e})
                    return HttpResponse(self.template.render(self.context))
                else:
                    self.template = self.get_template()
                    return self.template.render(self.context)
                    
            elif(record_slug == "borrowerstakeholder"):
                self.pciformset = self.loadpciinstance(self.pciform, self.updating_instance.pci, prefix="PCI_Forms", initial=True)
                self.sciformset = self.load_form_instance(self.sciform, self.updating_instance.sci, prefix="SCI_Forms")
                self.ieformset = self.load_form_instance(self.ieform, self.updating_instance.ei, prefix="EIForms")
                self.idformset = self.load_form_instance(self.idform, self.updating_instance.idi, prefix="IDForms")
                self.gscafbformsset = self.load_form_instance(self.gscafbforms, self.updating_instance.gscafb, prefix="GSCAFBForms")
                self.user_detailsformset = self.load_form_instance(self.client_detailsformset, self.updating_instance.Borrowers_Client_Number.client_details, prefix="ClientDForms")
                try:
                    self.pcid = self.updating_instance.pci.id
                    self.sciid = self.updating_instance.sci.id
                    self.ieid = self.updating_instance.ei.id
                    self.idi = self.updating_instance.idi.id
                    self.gsid = self.updating_instance.gscafb.id
                    self.clientupdatid = self.updating_instance.Borrowers_Client_Number.client_details.id
                except Exception as e:
                    self.template = loader.get_template('datasetrecordsupdate.html')
                    self.context = RequestContext(request, {"generrors":e})
                    return HttpResponse(self.template.render(self.context)) 
                try:
                    self.context = RequestContext(request, {"datasetforms":self.formset, "datasetrecords":self.datasetrecords,
                                                            "dataid":dataID, "datasetupdate":"Updating Records",
                                                            'pciforms':self.pciformset, 'sciforms':self.sciformset,
                                                            'ieforms':self.ieformset, 'idforms':self.idformset,
                                                            'gscafbforms':self.gscafbformsset,"dataset_active":record_slug,
                                                            "pciID":self.pcid, "sciID":self.sciid, "ieid":self.ieid,
                                                            "idi":self.idi, "gsid":self.gsid, "title":"CRB",
                                                            "clientform":self.user_detailsformset, "clientupdatingID":self.clientupdatid,
                                                            "updating_instance":self.updating_instance, "default_headers":self.header_form_instance,
                                                            "ClientNumber":self.updating_instance.Borrowers_Client_Number
                                                  })
                except Exception as e:
                    self.template = loader.get_template('datasetrecordsupdate.html')
                    self.context = RequestContext(request, {"generrors":e})
                    return HttpResponse(self.template.render(self.context))
                else:
                    self.template = self.get_template()
                    return self.template.render(self.context)
                    
            elif(record_slug == "credit_application"):
                #get_clientforms
                #print "AM NOT HIM ", record_slug

                #self.pciforms = self.pciform(initial={'PCI_District': "Wangolo JOel"})
                self.pciformset = self.loadpciinstance(self.pciform, self.updating_instance.pci, prefix="PCI_Forms", initial=True)
                self.sciformset = self.load_form_instance(self.sciform, self.updating_instance.sci, prefix="SCI_Forms")
                self.ieformset = self.load_form_instance(self.ieform, self.updating_instance.ei, prefix="EIForms")
                self.idformset = self.load_form_instance(self.idform, self.updating_instance.idi, prefix="IDForms")
                self.gscafbformsset = self.load_form_instance(self.gscafbforms, self.updating_instance.gscafb, prefix="GSCAFBForms")
                self.user_detailsformset = self.load_form_instance(self.client_detailsformset, self.updating_instance.client_details, prefix="ClientDForms")
                #print self.pciformset #= self.pciformset(initial={'PCI_District': "Wangolo JOel"})
                try:
                    self.pcid = self.updating_instance.pci.id
                    self.sciid = self.updating_instance.sci.id
                    self.ieid = self.updating_instance.ei.id
                    self.idi = self.updating_instance.idi.id
                    self.gsid = self.updating_instance.gscafb.id
                    self.clientupdatid = self.updating_instance.client_details.id
                except Exception as e:
                    self.template = loader.get_template('datasetrecordsupdate.html')
                    self.context = RequestContext(request, {"generrors":e})
                    return HttpResponse(self.template.render(self.context)) 
                try:
                    self.context = RequestContext(request, {"datasetforms":self.formset, "datasetrecords":self.datasetrecords,
                                                            "dataid":dataID, "datasetupdate":"Updating Records",
                                                            'pciforms':self.pciformset, 'sciforms':self.sciformset,
                                                            'ieforms':self.ieformset, 'idforms':self.idformset,
                                                            'gscafbforms':self.gscafbformsset,"dataset_active":record_slug,
                                                            "pciID":self.pcid, "sciID":self.sciid, "ieid":self.ieid,
                                                            "idi":self.idi, "gsid":self.gsid, "title":"CRB",
                                                            "clientform":self.user_detailsformset, "clientupdatingID":self.clientupdatid,
                                                            "updating_instance":self.updating_instance, "default_headers":self.header_form_instance,
                                                            "ClientNumber":self.updating_instance.Client_Number
                                                  })
                except Exception as e:
                    self.template = loader.get_template('datasetrecordsupdate.html')
                    self.context = RequestContext(request, {"generrors":e})
                    return HttpResponse(self.template.render(self.context))
                else:
                    self.template = self.get_template()
                    return self.template.render(self.context)

            elif (record_slug == "participatinginstitutionstakeholder"):
                #get_clientforms
                #print "AM NOT HIM ", record_slug
                self.pciformset = self.load_form_instance(self.pciform, self.updating_instance.pci, prefix="PCI_Forms")
                self.sciformset = self.load_form_instance(self.sciform, self.updating_instance.sci, prefix="SCI_Forms")
                self.ieformset = self.load_form_instance(self.ieform, self.updating_instance.ei, prefix="EIForms")
                self.idformset = self.load_form_instance(self.idform, self.updating_instance.idi, prefix="IDForms")
                self.gscafbformsset = self.load_form_instance(self.gscafbforms, self.updating_instance.gscafb, prefix="GSCAFBForms")

                #if(self.updating_instance.gscafb.id)
                try:
                    self.pcid = self.updating_instance.pci.id
                    self.sciid = self.updating_instance.sci.id
                    self.ieid = self.updating_instance.ei.id
                    self.idi = self.updating_instance.idi.id
                    self.gsid = self.updating_instance.gscafb.id
                except Exception as e:
                    self.template = loader.get_template('datasetrecordsupdate.html')
                    self.context = RequestContext(request, {"generrors":e})
                    return HttpResponse(self.template.render(self.context)) 
                try:
                    self.context = RequestContext(request, {"datasetforms":self.formset, "datasetrecords":self.datasetrecords,
                                                            "dataid":dataID, "datasetupdate":"Updating Records",
                                                            'pciforms':self.pciformset, 'sciforms':self.sciformset,
                                                            'ieforms':self.ieformset, 'idforms':self.idformset,
                                                            'gscafbforms':self.gscafbformsset,"dataset_active":record_slug,
                                                            "pciID":self.pcid, "sciID":self.sciid, "ieid":self.ieid,
                                                            "idi":self.idi, "gsid":self.gsid, "title":"CRB",
                                                            "updating_instance":self.updating_instance,
                                                            "default_headers":self.header_form_instance,
                                                            #"ClientNumber":self.updating_instance.Borrowers_Client_Number
                                                  })
                except Exception as e:
                    self.template = loader.get_template('datasetrecordsupdate.html')
                    self.context = RequestContext(request, {"generrors":e})
                    return HttpResponse(self.template.render(self.context))
                    raise 
                     
                else:
                    self.template = self.get_template()
                    return self.template.render(self.context)
            else:
                #get_clientforms
                #print "AM NOT HIM ", record_slug
                self.pciformset = self.load_form_instance(self.pciform, self.updating_instance.pci, prefix="PCI_Forms")
                self.sciformset = self.load_form_instance(self.sciform, self.updating_instance.sci, prefix="SCI_Forms")
                self.ieformset = self.load_form_instance(self.ieform, self.updating_instance.ei, prefix="EIForms")
                self.idformset = self.load_form_instance(self.idform, self.updating_instance.idi, prefix="IDForms")
                self.gscafbformsset = self.load_form_instance(self.gscafbforms, self.updating_instance.gscafb, prefix="GSCAFBForms")

                #if(self.updating_instance.gscafb.id)
                try:
                    self.pcid = self.updating_instance.pci.id
                    self.sciid = self.updating_instance.sci.id
                    self.ieid = self.updating_instance.ei.id
                    self.idi = self.updating_instance.idi.id
                    self.gsid = self.updating_instance.gscafb.id
                except Exception as e:
                    self.template = loader.get_template('datasetrecordsupdate.html')
                    self.context = RequestContext(request, {"generrors":e})
                    return HttpResponse(self.template.render(self.context)) 
                try:
                    self.context = RequestContext(request, {"datasetforms":self.formset, "datasetrecords":self.datasetrecords,
                                                            "dataid":dataID, "datasetupdate":"Updating Records",
                                                            'pciforms':self.pciformset, 'sciforms':self.sciformset,
                                                            'ieforms':self.ieformset, 'idforms':self.idformset,
                                                            'gscafbforms':self.gscafbformsset,"dataset_active":record_slug,
                                                            "pciID":self.pcid, "sciID":self.sciid, "ieid":self.ieid,
                                                            "idi":self.idi, "gsid":self.gsid, "title":"CRB",
                                                            "ClientNumber":self.updating_instance.Borrowers_Client_Number
                                                  })
                except Exception as e:
                    self.template = loader.get_template('datasetrecordsupdate.html')
                    self.context = RequestContext(request, {"generrors":e})
                    return HttpResponse(self.template.render(self.context))                     
                else:
                    self.template = self.get_template()
                    return self.template.render(self.context)
                    
        except Exception as e:
            self.template = loader.get_template('datasetrecordsupdate.html')
            self.context = RequestContext(request, {"generrors":e, "datasetrecords":self.datasetrecords})
            return HttpResponse(self.template.render(self.context))             
           
    def loadgscafbinstance(self, form, gscafb):
        try:
            return form(instance=gscafb.gscafb)
        except:
            raise 
            
    def loadidinstance(self,form, idi):
        try:
            return form(instance=idi.idi)
        except:
            raise 
            
    def loadieinstance(self, form, ei, initial=None):
        try:
            return form(instance=ei.ei)
        except:
            raise 
            
    def loadsciinstance(self, form, sci):
        try:
            return form(instance=sci.sci)
        except:
            raise 
            
    def loadpciinstance(self, form, pci, prefix, initial=None):
        try:
            if(initial):
                #return form(instance=pci, prefix=prefix, initial={"PCI_District":"Mitooma District"})
                return form(instance=pci, prefix=prefix)
            else:
                return form(instance=pci, prefix=prefix)
        except:
            raise 
                
    def load_form_instance(self, form, dataupdating, prefix):
        try:
            #print "FORM IS ", form 
            return form(instance=dataupdating, prefix=prefix)
        except:
            raise 
            
    def load_record_information(self, slug):
        """
        Load and return the information of any
        record.
        """
        try:
            return record_models.Dataset.objects.get(slug=slug)
        except:
            raise
            
    def get_datarecords(self):
        """
        Return all available dataset records.
        """
        try:
            return record_models.Dataset.objects.all()
        except:
            raise
            
    def getforms(self, dataset):
        try:
            if(dataset == "FINANCIAL MALPRACTICE DATA"):
                return dataset_forms.FRA_Forms(prefix="standard_forms")
            elif(dataset == "COLLATERAL CREDIT GUARANTOR"):
                return dataset_forms.CCG_Forms(prefix="standard_forms")
            elif(dataset == "COLLATERAL MATERIAL COLLATERAL"):
                return dataset_forms.CMC_Forms(prefix="standard_forms")
            elif(dataset == "BORROWERSTAKEHOLDER"):
                return dataset_forms.BS_Forms(prefix="standard_forms")
            elif(dataset.upper() == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return dataset_forms.PIS_Forms(prefix="standard_forms")
            elif(dataset == "BOUNCEDCHEQUES"):
                return dataset_forms.BC_Forms(prefix="standard_forms")
            elif(dataset == "CREDIT APPLICATION"):
                return dataset_forms.CAP_Forms(prefix="standard_forms")
            elif(dataset == "CREDITBORROWERACCOUNT"):
                return dataset_forms.CBA_Forms(prefix="standard_forms")
            elif(dataset == "INSTITUTION BRANCH"):
                return dataset_forms.IB_Forms(prefix="standard_forms")
            elif(dataset == "PARTICIPATING INSTITUTION"):
                return dataset_forms.PI_Forms(prefix="standard_forms")
            else:
                return None

        except:
            raise
            
    def get_template(self, *template):
        try:
            if(template):
                try:
                    return loader.get_template(template)
                except TemplateDoesNotExists:
                    raise
            else:
                return loader.get_template("datasetrecordsupdate.html")
        except:
            raise
