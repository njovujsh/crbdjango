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


class SingleDataUpdate(View):
    def get(self, request,  record_slug, recordID):
        try:
            if(request.user.is_authenticated()):
                self.template = "datasetrecords.html"
                self.templates = loader.get_template(self.template) 
                
                self.rendered = self.update_context(request, record_slug, recordID)
                return HttpResponse(self.rendered)
            else:
                return HttpResponseRedirect("/")
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
                return loader.get_template("datasetrecordreupdate.html")
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
            
    def update_context(self, request, record_slug, dataID):
        try:
            self.datasetrecords = self.get_datarecords()
            self.record_details = self.load_record_information(record_slug)
            
            self.forms = self.get_insert_forms(self.record_details.dataset_record.replace("_", " ", len(self.record_details.dataset_record)))
            self.model = self.get_models(self.record_details.dataset_record.replace("_", " ", len(self.record_details.dataset_record)))
            
            self.updating_instance = self.get_model_data(self.model, dataID)
            self.formset = self.load_form_instance(self.forms, self.updating_instance, prefix="standard_forms")
         
            try:
                self.context = RequestContext(request, {"datasetforms":self.formset, "datasetrecords":self.datasetrecords,
                                                        "dataid":dataID, "dsshupdate":"Updating new header files",
                                                        "dataset_active":record_slug,
                                                        
                                              })
            except:
                raise 
            else:
                self.template = self.get_template()
                return self.template.render(self.context)
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
            
    def load_record_information(self, slug):
        """
        Load and return the information of any
        record.
        """
        try:
            return record_models.Dataset.objects.get(slug=slug)
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
            
    def load_form_instance(self, form, dataupdating, prefix):
        try:
            return form(instance=dataupdating, prefix=prefix)
        except:
            raise 
    
    def post(self, request, record_slug, recordID):
        try:
            print "It's me bs updating ", record_slug
            self.record_info = self.load_record_information(record_slug)
            self.formpost = self.load_forms_insert(self.record_info)
            try:
                self.record_models = self.get_models(self.record_info.dataset_record.replace("_", " ", len(self.record_info.dataset_record)))
                self.standard_quried = self.get_model_data(self.record_models, recordID)
                
                self.standard_ret = self.formpost(request.POST, instance=self.standard_quried, prefix="standard_forms")
                if(self.standard_ret.is_valid()):
                    try:
                        self.standard_instance = self.standard_ret.save()
                    except:
                        raise 
                    else:
                        if("submits" in request.POST):
                            return HttpResponseRedirect("/home/redo/")
                            
                        elif("submitviews" in request.POST):
                            url = "/view/dataview/request/%s/" % str(self.record_info.slug)
                            return HttpResponseRedirect(url)
                else:
                    return HttpResponse(self.render_doesnot_exists(self.standard_ret.errors))

            except:
                raise 
        except:
            raise 
            
    def render_doesnot_exists(self, error):
        self.datasetrecords = self.get_datarecords()
        try:
            self.context = Context({"datasetrecords":self.datasetrecords, "ERROR":error, "details":None})
            
            self.exception_template = loader.get_template("doesnotexist.html")
            if(self.exception_template):
                try:
                    return self.exception_template.render(self.context)
                except:
                    return HttpResponse("Server enccountered an error")
        except:
            raise 
            return HttpResponse("ERror processsing error templates")
