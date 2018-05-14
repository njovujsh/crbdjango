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
import forms
from branchcode import forms as bforms 
from django.db import models
from django.core.exceptions import MultipleObjectsReturned
#message, args

class BouncedExisting(View):
    def get(self, request, record_slug):
        try:
            self.dataset_infor = self.load_record_information(record_slug)
            self.template = self.load_template()
            
            if(self.dataset_infor):
                try:
                    self.rendered = self.process_context(request, self.template, self.dataset_infor)
                    return HttpResponse(self.rendered)
                except:
                    raise
            else:
                return HttpResponse("Failure")
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

    def load_template(self, custom_template=None):
        try:
            if(custom_template):
                return loader.get_template(custom_template)
            else:
                return loader.get_template("clientnumberselect.html")
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
            
    def process_context(self, request, template, dataset_slug):
        try:
            if(template):
                self.datasetforms = self.load_forms_by_slug()
                
                self.datasetrecords = self.get_datarecords()
                self.credit_apps = self.load_credit_applicants()
                self.context  = RequestContext(request, {"datasetrecords":self.datasetrecords, "clientnumber":self.credit_apps,
                                                            "clientnumbertitle":"Select Client Number"
                                                        })
                return template.render(self.context)
            else:
                return None
        except:
            raise

    def load_forms_by_slug(self):
        """
        Return the forms which will be used.
        """
        try:
            return forms.BC_Forms
        except:
            raise
    
    def load_credit_applicants(self):
        try:
            return datamodels.CREDIT_APPLICATION.objects.all()
        except:
            raise 
            
    
    def post(self, request):
        try:
            return HttpResponse(self.process_post_request(request))
        except:
            raise 
            
    def _form_instance(self, form, instance, prefix):
        try:
            return form(instance=instance, prefix=prefix)
        except:
            raise 
            
    def load_applicant_by_number(self, clientnumber):
        try:
            if(clientnumber):
                try:
                    return datamodels.CREDIT_APPLICATION.objects.get(Client_Number=clientnumber)
                except MultipleObjectsReturned as e:
                    raise 
            else:
                return False 
        except:
            raise 
            
    def get_PCIForms(self):
        return forms.PCIForms 
        
    def get_SCIForms(self):
        return forms.SCIForms 
    
    def get_GSCAFBForms(self, post=False):
        return forms.GSCAFBForms 
        
    def get_IDForms(self, post=False):
        return forms.IDForms
       
        
    def get_EIForms(self, post=False):
        return forms.EIForms
        
    
    def process_post_request(self, request):
        try:
            self.clientnumber =  request.POST.get("clientnumber", "")
            if(self.clientnumber):
                try:
                    try:
                        self.app_instance =  self.load_applicant_by_number(self.clientnumber)
                    except MultipleObjectsReturned as e:
                        return HttpResponse(self.render_exception(request, e, self.clientnumber, e))
                    else:
                        self.sci_instance =  self.load_applicant_by_number(self.clientnumber).pci
                        self.pci_instance =  self.load_applicant_by_number(self.clientnumber).sci
                        self.ii_instance = self.load_applicant_by_number(self.clientnumber).idi
                        self.ei_instance = self.load_applicant_by_number(self.clientnumber).ei
                        self.gscafb_instance = self.app_instance.gscafb #self.load_applicant_by_number(self.clientnumber).gscafb
                except:
                    raise 
                    
                try:
                    self.bcform = self.load_forms_by_slug()
                    self.pciform = self.get_PCIForms()
                    self.sciform = self.get_SCIForms()
                    self.gsform = self.get_GSCAFBForms()
                    self.idform = self.get_IDForms()
                    self.eiform = self.get_EIForms()
                    
                    self.bc_formset = self._form_instance(self.bcform, self.app_instance, prefix='standard_forms')
                    self.sci_formset = self._form_instance(self.sciform, self.app_instance.sci, prefix="SCI_Forms")
                    self.pci_formset = self._form_instance(self.pciform, self.app_instance.pci, prefix="PCI_Forms")
                    self.id_formset = self._form_instance(self.idform, self.app_instance.idi, prefix="IDForms")
                    self.gs_formset = self._form_instance(self.gsform, self.app_instance.gscafb, prefix="GSCAFBForms")
                    self.ei_formset = self._form_instance(self.eiform, self.app_instance.ei, prefix="EIForms")
                    
                except:
                    raise 
                else:
                    try:
                        self.datasetrecords = self.get_datarecords()
                        self.context = RequestContext(request, {"datasetforms":self.bc_formset, "datasetrecords":self.datasetrecords,
                                                        "datasetinput":"Bounced Cheques",
                                                        'pciforms':self.pci_formset, 'sciforms':self.sci_formset,
                                                        'ieforms':self.ei_formset, 'idforms':self.id_formset,
                                                        'gscafbforms':self.gs_formset, "dataset_active":"Bouncedcheques",
                                                        "cnumber":self.clientnumber
                                                    })
                        try:
                            self.template = self.load_template(custom_template="bouncedcheque.html")
                            return self.template.render(self.context)
                        except:
                            raise 
                    except:
                        raise
            else:
                self.path = request.get_full_path()
                
                self.datasetforms = self.load_forms_by_slug()
                self.template = loader.get_template("clientnumberselect.html")
                
                self.datasetrecords = self.get_datarecords()
                self.credit_apps = self.load_credit_applicants()
                self.context  = RequestContext(request, {"datasetrecords":self.datasetrecords, "clientnumber":self.credit_apps,
                                                            "clientnumbertitle":"Select Client Number", "errormissing":"Missing client number"
                                                        })
                return self.template.render(self.context)
        except:
            raise 
            
            
    def render_exception(self, request, error, clientnumber, msg):
        """
        Render back the exceptions.
        """
        try:
            self.template = self.load_template()
            if(self.template):
                self.datasetforms = self.load_forms_by_slug()
                
                self.datasetrecords = self.get_datarecords()
                self.credit_apps = self.load_credit_applicants()
                self.context  = RequestContext(request, {"datasetrecords":self.datasetrecords, "clientnumber":self.credit_apps,
                                                            "errormsg":error, "clientnumbererror":clientnumber, "clientnumbertitle":"System Client number ERROR"
                                                        })
                return self.template.render(self.context)
            else:
                return None
        except:
            raise
            
            
