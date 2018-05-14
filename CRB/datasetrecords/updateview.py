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
#from datasetsystem import processcsvs
from reportlab.pdfgen import canvas
import datetime
import time
from django.forms.models import inlineformset_factory
import importlib
from datasets import models as record_models
from datasetrecords import models as datamodels
from datasetrecords import forms as dataset_forms 

import forms

mytitle = "CRB Data"

class NewDataUpdate(View):
    def get(self, request,  dataset, recordID):
        try:
            if(request.user.is_authenticated()):
                self.template = "datasetrecords.html"
                self.templates = loader.get_template(self.template) 
                
                self.rendered = self.context_processor(request, self.templates, dataset, recordID)
                return HttpResponse(self.rendered)
            else:
                return HttpResponseRedirect("/")
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
            elif(dataset == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
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

    def get_modelsdb(self, dataset):
        try:
            #search for the given data from the database
            self.api = models.DataSetRecords.objects.all()
            for api in self.api:
                if(self.dataset.upper() == api.upper()):
                    return api
                else:
                    return False
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
                return loader.get_template("database.html")
        except:
            raise

    def context_processor(self, request, template, dataset, dataID):
        try:
            if(record_slug.upper() == 'INSTITUION_BRANCH'):
                self.process_ib(request, template, dataset, dataID)
            elif(record_slug.upper() == 'CREDITBORROWERACCOUNT'):
                self.process_all(request, template, dataset, dataID)
            elif(record_slug.upper() == 'CREDIT_APPLICATION'):
                self.process_all(request, template, dataset, dataID)
            elif(record_slug.upper() == 'BOUNCEDCHEQUES'):
                self.process_all(request, template, dataset, dataID)
            elif(record_slug.upper() == 'BORROWERSTAKEHOLDER'):
                self.process_all(request, template, dataset, dataID)
            elif(record_slug.upper() == 'COLLATERAL_MATERIAL_COLLATERAL'):
                self.process_all(request, template, dataset, dataID)
            elif(record_slug.upper() == 'COLLATERAL_CREDIT_GUARANTOR'):
                self.process_all(request, template, dataset, dataID)
            elif(record_slug.upper() == 'FINANCIAL_MALPRACTICE_DATA'):
                self.process_all(request, template, dataset, dataID)
            elif(record_slug.upper() == 'PARTICIPATINGINSTITUTIONSTAKEHOLDER'):
                self.process_pis_pi(request, template, dataset, dataID)
            elif(record_slug.upper() == 'PARTICIPATING_INSTITUTION'):
                self.process_pis_pi(request, template, dataset, dataID)
            else:
                pass 
                
        except:
            raise
    
    def get_PCIForms(self, insert=False):
        if(insert==False):
            return forms.PCIForms(prefix="PCI_Forms")
        else:
            return forms.PCIForms
            
    def get_SCIForms(self, insert=False):
        if(insert==False):
            return forms.SCIForms(prefix="SCI_Forms")
        else:
            return forms.SCIForms
           
    def get_PCIModel(self):
        return datamodels.PCI
        
    def get_SCIModel(self):
        return datamodels.SCI 
        
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
            if(models):
                if(ID):
                    self.model_data = models.objects.get(id=ID)
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

    def post(self, request, record_slug, dataID, pciID, sciID):
        """
        Method handles post called automatically.
        """
        
        try:
            if(request.user.is_authenticated()):
                if(request.method == "POST"):
                    try:
                        self.dataset_infor = self.load_record_information(record_slug)
                        self.standard_form = self.load_forms_insert(self.dataset_infor)
                        self.pci_form = self.get_PCIForms(insert=True)
                        self.sci_form = self.get_SCIForms(insert=True)
                
                        try:
                            self.pci_model = self.get_PCIModel()
                            self.sci_model = self.get_SCIModel()
                            
                            self.pci_update_data = self.query_pci_sci_byID(self.pci_model, pciID)
                            self.sci_update_data = self.query_pci_sci_byID(self.sci_model, sciID)
                            
                            self.pci_update_status = self.pci_form(request.POST, prefix="PCI_Forms", instance=self.pci_update_data)
                            self.sci_update_status = self.sci_form(request.POST, prefix="SCI_Forms", instance=self.sci_update_data)
                            
                            if(self.pci_update_status and self.sci_update_status):
                                if(self.pci_update_status.is_valid() and self.sci_update_status.is_valid()):
                                    self.pci_update_retcode = self.pci_update_status.save()
                                    self.sci_update_retcode = self.sci_update_status.save()
                                else:
                                    return HttpResponse(self.pci_update_status.errors + self.sci_update_status.errors)
                        except:
                            raise 
                        else:
                            if(self.standard_form):
                                self.form_model = self.load_models_update_records(record_slug)
                                if(self.form_model):
                                    self.updating_record = self.query_model_byID(self.form_model, int(dataID))
                                    
                                    if(self.updating_record):
                                        try:
                                            #print "Here is the record ", request.POST.get("Institution_Type", "")
                                            self.standard_insert = self.standard_form(request.POST, 
                                                                            instance=self.updating_record,
                                                                            prefix="standard_forms"
                                                                            
                                                                            )
                                            
                                            
                                            if(self.standard_insert):
                                                self.standard_insert_status = self.standard_insert.save(commit=False)
                                                
                                                self.standard_insert_status.pci=self.pci_update_retcode
                                                self.standard_insert_status.sci=self.sci_update_retcode
                                                
                                                self.standard_insert_status.save()
                                                
                                            else:
                                                print "Failure CODE 1"
                                        except:
                                            raise 
                                        else:
                                            if("submits" in request.POST):
                                                return HttpResponseRedirect("/home/dashboard/")
                                                
                                            elif("submitviews" in request.POST):
                                                url = "/view/dataview/request/%s/" % str(record_slug)
                                                return HttpResponseRedirect(url)
                                                
                                            else:
                                                print "Unkonwnoption received"
            
                                            return HttpResponse("Data inserted successfuly.")
                                    else:
                                        print "ERROR CODE 4"
                                else:
                                    print"Failure CODE 3"
                                #self.data_updating = self.data_models.objects.get(id=int(dataID))
                                #self.insert_data = self.data_form(request.POST, instance=self.data_updating)
                            else:
                                return HttpResponse("Forms Critical.")
                    except:
                        raise
                else:
                    return HttpResponse("This was not a post")
            else:
                return HttpResponseRedirect("/")
        except:
            raise

    def parse_model_fields(self, model_data):
        """
        Returns the fields coresponding to particular models.
        """
        self.fields = [ ]
        self.mfields = model_data._meta.fields

        for field in self.mfields:
            if field.name in self.fields:
                pass
            else:
                self.fields.append(field.name)

        #return the model fields
        return self.fields

    def get_insert_forms(self, dataset):
        try:
            if(dataset == "FINANCIAL MALPRACTICE DATA"):
                return forms.FRA_Forms
            elif(dataset == "COLLATERAL CREDIT GUARANTOR"):
                return forms.CCG_Forms
            elif(dataset == "COLLATERAL MATERIAL COLLATERAL"):
                return forms.CMC_Forms
            elif(dataset == "BORROWERSTAKEHOLDER"):
                return forms.BS_Forms
            elif(dataset == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return forms.PIS_Forms
            elif(dataset == "BOUNCEDCHEQUES"):
                return forms.BC_Forms
            elif(dataset == "CREDIT APPLICATION"):
                return forms.CAP_Forms
            elif(dataset == "CREDITBORROWERACCOUNT"):
                return forms.CBA_Forms
            elif(dataset == "INSTITUTION BRANCH"):
                return forms.IB_Forms
            elif(dataset == "PARTICIPATING INSTITUTION"):
                return forms.PI_Forms

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
            elif(dataset == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return datamodels.PARTICIPATINGINSTITUTIONSTAKEHOLDER
            elif(dataset == "BOUNCEDCHEQUES"):
                return datamodels.BOUNCEDCHEQUES
            elif(dataset == "CREDIT APPLICATION"):
                return datamodels.CREDIT_APPLICATION
            elif(dataset == "CREDITBORROWERACCOUNT"):
                return datamodels.CREDITBORROWERACCOUNT
            elif(dataset == "INSTITUTION BRANCH"):
                self.template = "IB_dataview.html"
                return datamodels.INSTITUTION_BRANCH
            elif(dataset == "PARTICIPATING INSTITUTION"):
                return datamodels.PARTICIPATING_INSTITUTION
        except:
            raise

    def get_model_templates(self, dataset):
        try:
            if(dataset == "FINANCIAL MALPRACTICE DATA"):
                return "fmd_dataview.html"
            elif(dataset == "COLLATERAL CREDIT GUARANTOR"):
                return "ccg_dataview.html"
            elif(dataset == "COLLATERAL MATERIAL COLLATERAL"):
                return "cmc_dataview.html"
            elif(dataset == "BORROWERSTAKEHOLDER"):
                return "bs_dataview.html"
            elif(dataset == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return "pis_dataview.html"
            elif(dataset == "BOUNCEDCHEQUES"):
                return "bc_dataview.html"
            elif(dataset == "CREDIT APPLICATION"):
                return "cp_dataview.html"
            elif(dataset == "CREDITBORROWERACCOUNT"):
                return "cba_dataview.html"
            elif(dataset == "INSTITUTION BRANCH"):
                self.templates = "IB_dataview.html"
                return self.templates
            elif(dataset == "PARTICIPATING INSTITUTION"):
                return "pi_dataview.html"
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
        
    def load_forms_by_slug(self, record_info):
        """
        Return the forms which will be used.
        """
        try:
            if(record_info.dataset_record == "COLLATERAL_MATERIAL_COLLATERAL"):
                return forms.CMC_Forms(prefix="standard_forms")
            elif(record_info.dataset_record == "BORROWERSTAKEHOLDER"):
               return forms.BS_Forms(prefix="standard_forms")
            elif(record_info.dataset_record == "BOUNCEDCHEQUES"):
                return forms.BC_Forms(prefix="standard_forms")
            elif(record_info.dataset_record == "COLLATERAL_CREDIT_GUARANTOR"):
    
                return forms.CCG_Forms(prefix="standard_forms")
            elif(record_info.dataset_record == "CREDITBORROWERACCOUNT"):
                return forms.CBA_Forms(prefix="standard_forms")
            elif(record_info.dataset_record == "CREDIT_APPLICATION"):
                return forms.CAP_Forms(prefix="standard_forms")
            elif(record_info.dataset_record == "FINANCIAL_MALPRACTICE_DATA"):
                return forms.FRA_Forms(prefix="standard_forms")
            elif(record_info.dataset_record == "INSTITUTION_BRANCH"):
                return forms.IB_Forms(prefix="standard_forms")
            elif(record_info.dataset_record == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return forms.PIS_Forms(prefix="standard_forms")
            elif(record_info.dataset_record == "PARTICIPATING_INSTITUTION"):
                return forms.PI_Forms(prefix="standard_forms")
            else:
                return False
        except:
            raise
        
        
    def load_models_update_records(self, model_slug):
        try:#datamodels
            if(model_slug.upper() == "COLLATERAL_MATERIAL_COLLATERAL"):
                return datamodels.COLLATERAL_MATERIAL_COLLATERAL
            elif(model_slug.upper() == "BORROWERSTAKEHOLDER"):
                return datamodels.BORROWERSTAKEHOLDER
            elif(model_slug.upper() == "BOUNCEDCHEQUES"):
                return datamodels.BOUNCEDCHEQUES
            elif(model_slug.upper() == "COLLATERAL_CREDIT_GUARANTOR"):
                return datamodels.COLLATERAL_CREDIT_GUARANTOR
            elif(model_slug.upper() == "CREDITBORROWERACCOUNT"):
                return datamodels.CREDITBORROWERACCOUNT
            elif(model_slug.upper() == "CREDIT_APPLICATION"):
                return datamodels.CREDIT_APPLICATION
            elif(model_slug.upper() == "FINANCIAL_MALPRACTICE_DATA"):
                return datamodels.FINANCIAL_MALPRACTICE_DATA
            elif(model_slug.upper() == "INSTITUTION_BRANCH"):
                return datamodels.INSTITUTION_BRANCH
            elif(model_slug.upper() == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return datamodels.PARTICIPATINGINSTITUTIONSTAKEHOLDER
            elif(model_slug.upper() == "PARTICIPATING_INSTITUTION"):
                return datamodels.PARTICIPATING_INSTITUTION
            else:
                return None 
        except:
            raise 
            
            
    def query_model_byID(self, model, ID):
        try:
            if(model and ID):
                try:
                    return model.objects.get(id=int(ID))
                except:
                    raise 
            else:
                return False 
        except:
            raise 
            
    def load_forms_insert(self, record_info):
        """
        Return the forms which will be used.
        """
        try:
            if(record_info.dataset_record == "COLLATERAL_MATERIAL_COLLATERAL"):
                return forms.CMC_Forms
            elif(record_info.dataset_record == "BORROWERSTAKEHOLDER"):
               return forms.BS_Forms
            elif(record_info.dataset_record == "BOUNCEDCHEQUES"):
                return forms.BC_Forms 
            elif(record_info.dataset_record == "COLLATERAL_CREDIT_GUARANTOR"):

                return forms.CCG_Forms
            elif(record_info.dataset_record == "CREDITBORROWERACCOUNT"):
                return forms.CBA_Forms 
            elif(record_info.dataset_record == "CREDIT_APPLICATION"):
                return forms.CAP_Forms
            elif(record_info.dataset_record == "FINANCIAL_MALPRACTICE_DATA"):
                return forms.FRA_Forms
            elif(record_info.dataset_record == "INSTITUTION_BRANCH"):
                return forms.IB_Forms
            elif(record_info.dataset_record == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return forms.PIS_Forms
            elif(record_info.dataset_record == "PARTICIPATING_INSTITUTION"):
                return forms.PI_Forms
            else:
                return False
        except:
            raise
