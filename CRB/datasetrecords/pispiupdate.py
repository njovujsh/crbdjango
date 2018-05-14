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
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
mytitle = "CRB Data"


class PIPISUpdate(View):
    @method_decorator(login_required)
    def get(self, request,  dataset, recordID):
        try:
            if(request.user.is_authenticated()):
                self.template = "pipisupdate.html"
                self.templates = loader.get_template(self.template) 
                self.rendered = self.context_processor(request, self.templates, dataset, recordID)
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
                return loader.get_template("database.html")
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
            
    def getforms(self, dataset, insert=False):
        if(dataset.upper() == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
            return dataset_forms.PIS_Forms
            
        elif(dataset.upper() == "PARTICIPATING_INSTITUTION"):
            return dataset_forms.PI_Forms
            
    def get_PCIForms(self, insert=False):
        if(insert==False):
            return dataset_forms.PCIForms
        else:
            return dataset_forms.PCIForms
                 
               
    def get_SCIForms(self):
        return dataset_forms.SCIForms
          
    def context_processor(self, request, template, dataset, dataID):
        self.datasetrecords = self.get_datarecords()
        
        self.pciforms = self.get_PCIForms(insert=False)
        self.sciforms = self.get_SCIForms()
        
        self.pcimodel = self.get_PCIModel()
        self.scimodel = self.get_SCIModel()
        
        self.dataset_infor = self.load_record_information(dataset)
        self.standard_form = self.load_forms_insert(self.dataset_infor)
        self.model = self.get_models(self.dataset_infor.dataset_record)
        
        try:
            self.ret_query = self.query_model_byID(self.model, dataID)
            
            if(self.ret_query):
                
                self.formset  = self._form_instance(self.standard_form, self.ret_query, prefix="standard_forms")
                self.pciformset =self._form_instance(self.pciforms, self.ret_query.pci, prefix="PCI_Forms")
                #self.sciformset = self._form_instance(self.sciforms, self.ret_query.sci, prefix="SCI_Forms")
                try:
                    self.pciid = self.ret_query.pci.id
                    #self.sciid = self.ret_query.sci.id
                except:
                    raise 
                else:
                    self.context = RequestContext(request,{"datasetforms":self.formset, "datasetrecords":self.datasetrecords,
                                                        "dataid":dataID, "basetitle":mytitle,
                                                        "pciforms":self.pciformset, "dataid":dataID, "pciID":self.pciid,
                                                        'dataset_active':dataset, "datasetupdate":dataset ,
                                                    })
                    return template.render(self.context)
            else:
                self.dicts = {"datasetforms":self.formset, "datasetrecords":self.datasetrecords,
                                "dataid":dataID, "basetitle":mytitle,
                                "pciforms":self.pciformset, 'dataset_active':dataset, "datasetupdate":"ERROR IN request"
                            }
                return HttpResponse(self.render_error_back(request, self.dicts, template))
                
        except Exception as e:
            self.dicts = {"datasetforms":None, "datasetrecords":self.datasetrecords,
                                "dataid":dataID, "basetitle":mytitle, "exception":True,
                                'dataset_active':dataset, "datasetupdate":"ERROR IN request",
                                "fullpath":request.get_full_path(), "e":e
                            } 
            return HttpResponse(self.render_error_back(request, self.dicts, template))
    
    def render_error_back(self, request, dictvalue, template):
        try:
            self.ccontext = RequestContext(request, dictvalue)
            return template.render(self.ccontext)
        except:
            raise 
            
    def _form_instance(self, form, dataupdating, prefix):
        try:
            if(form and dataupdating):
                return form(instance=dataupdating, prefix=prefix)
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
    
    def load_record_information(self, slug):
        """
        Load and return the information of any
        record.
        """
        try:
            return record_models.Dataset.objects.get(slug=slug)
        except:
            raise
    @method_decorator(login_required)
    def post(self, request, record_slug, recordID,  pciID):
        try:
            if(request.user.is_authenticated()):
                if(request.method == "POST"):
                    try:
                        self.dataset_infor = self.load_record_information(record_slug)
                        self.standard_form = self.load_forms_insert(self.dataset_infor)
                        self.pci_form = self.get_PCIForms(insert=False)
                        try:
                            self.pci_model = self.get_PCIModel()
                            self.pci_update_data = self.query_pci_byid(self.pci_model, pciID)
                            
                            #update
                            self.update_pci = self.pci_form(request.POST, instance=self.pci_update_data, prefix="PCI_Forms")
                            if(self.update_pci):
                                
                                try:
                                    if(self.update_pci.is_valid()):
                                        self.pci_ret_instance = self.update_pci.save()
                                    else:
                                        self.ret = self.load_error_form_instance(request, 
                                                                    self.insert_ib,
                                                                    recordID,  pciID,
                                                                    record_slug, self.update_pci,
                                                                    )
                                        try:
                                            return HttpResponse(self.ret)
                                        except:
                                            raise 
                                except:
                                    raise 
                                else:
                                    if(self.pci_ret_instance):
                                        self._model = self.get_models(record_slug)
                                        if(self._model):
                                            try:
                                                self.query_updating_data = self.query_model_byID(self._model, recordID)
                                            except:
                                                raise 
                                            else:
                                                if(self.query_updating_data):
                                                    self.insert_ib = self.standard_form(request.POST,
                                                                                        instance=self.query_updating_data,
                                                                                        prefix="standard_forms"
                                                                                        )
                                                                   
                                                    if(self.insert_ib.is_valid()):
                                                        try:
                                                            self.ret_status = self.insert_ib.save(commit=False)
                                                            self.ret_status.pci = self.pci_ret_instance
                                                            self.ret_status.save()
                                                            if("submits" in request.POST):
                                                                return HttpResponseRedirect("/home/dashboard/")
                                                            elif("submitviews" in request.POST):
                                                                url = "/view/dataview/request/%s/" % str(record_slug)
                                                                return HttpResponseRedirect(url)
                                                        except:
                                                            raise 
                                                    else:
                                                        #load error template
                                                        #print "ERROR  in save instance"
                                                        self.ret = self.load_error_form_instance(request, 
                                                                                    self.insert_ib,
                                                                                    recordID,  pciID,
                                                                                    record_slug, self.update_pci,
                                                                                    )
                                                        try:
                                                            return HttpResponse(self.ret)
                                                        except:
                                                            raise 
                                                else:
                                                    self.ret = self.load_error_form_instance(request, 
                                                                                    self.insert_ib,
                                                                                    recordID,  pciID,
                                                                                    record_slug, self.update_pci,
                                                                                    )
                                                    try:
                                                        return HttpResponse(self.ret)
                                                    except:
                                                        raise 
                                        else:
                                            self.ret = self.load_error_form_instance(request, 
                                                    self.insert_ib,
                                                    recordID,  pciID,
                                                    record_slug, self.update_pci,
                                                    )
                                            try:
                                                return HttpResponse(self.ret)
                                            except:
                                                raise 
                                    else:
                                        self.ret = self.load_error_form_instance(request, 
                                                self.insert_ib,
                                                recordID,  pciID,
                                                record_slug, self.update_pci,
                                                )
                                        try:
                                            return HttpResponse(self.ret)
                                        except:
                                            raise        
                            else:
                                self.ret = self.load_error_form_instance(request, 
                                    self.insert_ib,
                                    recordID,  pciID, sciID,
                                    record_slug, self.update_pci,
                                    self.update_sci
                                    )
                                try:
                                    return HttpResponse(self.ret)
                                except:
                                    raise 
                        except:
                            self.ret = self.load_error_form_instance(request, 
                                self.insert_ib,
                                recordID,  pciID, sciID,
                                record_slug, self.update_pci,
                                self.update_sci
                                )
                            try:
                                return HttpResponse(self.ret)
                            except:
                                raise
                                
                    except Exception as e:
                        self.template = "pipisupdate.html"
                        self.templates = loader.get_template(self.template)
                
                        self.ret = {"Error":e
                                }
                        return HttpResponse(self.render_error_back(request, self.ret, self.templates))
                else:
                    return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("/")
        except:
            raise 
            
    def render_error_back(self, request, dictvalue, template):
        try:
            self.ccontext = RequestContext(request, dictvalue)
            return template.render(self.ccontext)
        except:
            raise 
            
    def load_error_form_instance(self,request, forminstance, dataID, pciid, sciid,record, pciformset, sci):
        try:
            self.datasetrecords = self.get_datarecords()
            self.template = "pipisupdate.html"
            self.templates = loader.get_template(self.template) 
            self.context = RequestContext(request, {"datasetrecords":self.datasetrecords, "datasetforms":forminstance,
                                                    "dataid":dataID,"pciID":pciid,"sciID":sciid,'dataset_active':record,
                                                    "basetitle":mytitle,"pciforms":pciformset,"sciforms":sci,
                                                    "error":forminstance.errors
                                            })
            return self.templates.render(self.context)
        except:
            raise 
            
    def query_pci_byid(self, pcimodel, pciid):
        try:
            if(pcimodel and pciid):
                try:
                    return pcimodel.objects.get(id=(int(pciid)))
                except:
                    raise 
            else:
                return None
        except:
            raise 
            
    def get_PCIModel(self):
        return datamodels.PCI
        
    def get_SCIModel(self):
        return datamodels.SCI
        
    def load_forms_insert(self, record_info):
        """
        Return the forms which will be used.
        """
        try:
            if(record_info.dataset_record == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return dataset_forms.PIS_Forms
                
            elif(record_info.dataset_record == "PARTICIPATING_INSTITUTION"):
                return dataset_forms.PI_Forms
                
            else:
                return False
        except:
            raise
            
    def get_models(self, dataset):
        try:
            if(dataset.upper() == "PARTICIPATING_INSTITUTION"):
                return datamodels.PARTICIPATING_INSTITUTION
                
            elif(dataset.upper() == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return datamodels.PARTICIPATINGINSTITUTIONSTAKEHOLDER
        except:
            raise
            
