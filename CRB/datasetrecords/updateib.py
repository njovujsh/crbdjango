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

mytitle = "Updating data"


class UpdateIB(View):
    @method_decorator(login_required)
    def get(self, request,  dataset, recordID):
        try:
            if(request.user.is_authenticated()):
                self.template = "ibupdate.html"
                self.templates = loader.get_template(self.template) 
                
                self.rendered = self.context_processor(request, self.templates, dataset, recordID)
                return HttpResponse(self.rendered)
            else:
                return HttpResponseRedirect("/")
                
        except Exception as e:
            return HttpResponse(self.render_doesnot_exists(e, dataset))
            
    def get_template(self, *template):
        try:
            if(template):
                try:
                    return loader.get_template(template)
                except TemplateDoesNotExists:
                    raise
            else:
                return loader.get_template("database.html")
        except Exception as e:
            return HttpResponse(self.render_doesnot_exists(e, "NONE"))
    
    def get_datarecords(self):
        """
        Return all available dataset records.
        """
        try:
            return record_models.Dataset.objects.all()
        except Exception as e: 
            return HttpResponse(self.render_doesnot_exists(e, "NONE"))
            
    def get_modelsdb(self, dataset):
        try:
            #search for the given data from the database
            self.api = models.DataSetRecords.objects.all()
            for api in self.api:
                if(self.dataset.upper() == api.upper()):
                    return api
                else:
                    return False
        except Exception as e: 
            return HttpResponse(self.render_doesnot_exists(e, dataset))
            
    def getforms(self, dataset, insert=False):
        if(dataset.upper() == "INSTITUTION_BRANCH"):
            if(insert==False):
                return dataset_forms.IB_Forms
            else:  
                return dataset_forms.IB_Forms
     
    def get_PCIForms(self, insert=False):
        if(insert==False):
            return dataset_forms.PCIForms
        else:
            return dataset_forms.PCIForms
                 
    def load_forms_insert(self, record_info):
        if(record_info.dataset_record == "INSTITUTION_BRANCH"):
            return dataset_forms.IB_Forms
                 
    def context_processor(self, request, template, dataset, dataID):
        self.datasetrecords = self.get_datarecords()
        self.formsib = self.getforms(dataset, insert=False)
        self.model = self.get_models(dataset)
        self.pciforms = self.get_PCIForms(insert=False)
        
        try:
            self.ret_query = self.query_model_byID(self.model, dataID, dataset)
            if(self.ret_query):
                self.formset  = self.ib_form_instance(self.formsib, self.ret_query, dataset)
                self.pciformset =self.pci_form_updating(self.pciforms, self.ret_query, dataset)
                try:
                    self.pciid = self.ret_query.pci.id
                except Exception as e: 
                    return HttpResponse(self.render_doesnot_exists(e, dataset)) 
                else:
                    self.context = RequestContext(request,{"datasetforms":self.formset, "datasetrecords":self.datasetrecords,
                                                        "dataid":dataID, "basetitle":mytitle,
                                                        "pciforms":self.pciformset, "dataid":dataID, "pciID":self.pciid,
                                                        'dataset_active':dataset, "datasetupdate":dataset 
                                                    })
                    return template.render(self.context)
            else:
                return HttpResponse(self.render_doesnot_exists("Record to be updated does not exists", dataset))
                
        except Exception as e:
            return HttpResponse(self.render_doesnot_exists(e, dataset)) 
                
    def get_models(self, dataset):
        if(dataset.upper() == "INSTITUTION_BRANCH"):
            return datamodels.INSTITUTION_BRANCH
    
    def ib_form_instance(self, form, dataupdating,dataset):
        try:
            if(form and dataupdating):
                return form(instance=dataupdating, prefix="standard_forms")
            else:
                return None 
        except Exception as e:
            return HttpResponse(self.render_doesnot_exists(e, dataset)) 
            
    def pci_form_updating(self, pciform, updating_pci, dataset):
        try:
            if(pciform and updating_pci):
                return pciform(instance=updating_pci.pci, prefix="PCI_Forms")
            else:
                return None
        except Exception as e:
            return HttpResponse(self.render_doesnot_exists(e, dataset)) 
            
    def query_model_byID(self, model, ID, dataset):
        
        return model.objects.get(id=int(ID))
                
    def render_doesnot_exists(self, error, dataset):
        self.datasetrecords = self.get_datarecords()
        print "Rendering errors "
        try:
            self.context = Context({"datasetrecords":self.datasetrecords, 'dataset_active':dataset, "iberrors":error})
            
            self.exception_template = loader.get_template("ibupdate.html")
            if(self.exception_template):
                try:
                    return self.exception_template.render(self.context)
                except:
                    return HttpResponse("Server enccountered an error")
        except: 
            return HttpResponse("ERror processsing error templates")
            
    def load_record_information(self, slug, dataset):
        """
        Load and return the information of any
        record.
        """
        try:
            return record_models.Dataset.objects.get(slug=slug)
        except Exception as e:
            return HttpResponse(self.render_doesnot_exists("ERROR", dataset))
            
    @method_decorator(login_required)
    def post(self, request, record_slug, ibID, pciID):
        try:
            if(request.user.is_authenticated()):
                if(request.method == "POST"):
                    try:
                        self.datasetrecords = self.get_datarecords()
                        self.template = loader.get_template("ibupdate.html")
                        self.dataset_infor = self.load_record_information(record_slug, record_slug)
                        self.standard_form = self.load_forms_insert(self.dataset_infor)
                        self.pci_form = self.get_PCIForms(insert=False)
                        
                        self.pci_model = self.get_PCIModel()
                        self.pci_update_data = self.query_pci_byid(self.pci_model, pciID)
                        
                        #update
                        self.update_pci = self.pci_form(request.POST, instance=self.pci_update_data, prefix="PCI_Forms")
                        self.ib_model = self.get_models(record_slug)
                        self.query_updating_data = self.query_model_byID(self.ib_model, ibID, record_slug)                     
                        self.insert_ib = self.standard_form(request.POST,
                                                                instance=self.query_updating_data,
                                                                prefix="standard_forms"
                                                                )
                                                                                             
                        self.context_dict = {"datasetforms":self.insert_ib,"datasetrecords":self.datasetrecords,
                                "datasetinput":record_slug,
                                "pciforms":self.update_pci,"dataset_active":record_slug,
                                }
                                
                        try:
                            if(self.update_pci):
                                try:
                                    if(self.update_pci.is_valid()):
                                        self.pci_ret_instance = self.update_pci.save()
                                    else:
                                        return HttpResponse("ERROR")
                                except:
                                    return HttpResponse("ERROR") 
                                else:
                                    if(self.pci_ret_instance):
                                        if(self.standard_form):
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
                                                except Exception as e:
                                                    self.context_dict = self.context_dict["iberrors"]=e 
                                                    return HttpResponse(self.template.render(self.context_dict))
                                            else:
                                                self.context_dict["iberrors"]=self.insert_ib.errors 
                                                return HttpResponse(self.template.render(self.context_dict))
                                        else:
                                            self.context_dict["iberrors"]="Unable to load formset for this" 
                                            return HttpResponse(self.template.render(self.context_dict))
                                    else:
                                        self.context_dict["iberrors"]="Invalid status from ret pci" 
                                        return HttpResponse(self.template.render(self.context_dict))    
                        except Exception as e:
                            print e
                            self.context_dict["iberrors"]=e 
                            return HttpResponse(self.template.render(self.context_dict)) 
                    except Exception as e:
                        return HttpResponse(self.render_doesnot_exists(e, record_slug))
                else:
                    return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("/")
        except Exception as e:
            return HttpResponse(self.render_doesnot_exists(e, record_slug)) 
            
    def query_pci_byid(self, pcimodel, pciid):
        try:
            if(pcimodel and pciid):
                try:
                    return pcimodel.objects.get(id=(int(pciid)))
                except Exception as e: 
                    return HttpResponse(self.render_doesnot_exists(e, "institution_branch")) 
            else:
                return HttpResponse(self.render_doesnot_exists("Invalid models", "institution_branch")) 
        except Exception as e:
            return HttpResponse(self.render_doesnot_exists(e, "institution_branch"))  
            
    def get_PCIModel(self):
        return datamodels.PCI
        
