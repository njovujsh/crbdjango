from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.template import Context, loader, RequestContext
from fileprocessor import forms as fileforms
from django.views.generic import View
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
from datasetrecords import loadmodels
from datasets import forms as dataset_forms
from validators.subsystems import loadvalidationmodule
from validators.subsystems.csvwriters import processcsvs
from validators.subsystems.csvwriters import pivalidatecsv
from validators.subsystems.csvwriters import loadcsvmodules
import simplejson
from validators.subsystems.datasets import validationstatus
from validators.subsystems import loadcodes
from processrecords.subsystems import filenaming
from processrecords.subsystems import datasetmatch 
from creditreports.subsystems import loadreporting
from creditreports.subsystems import reportstatus
from creditreports import loadreportmodels
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from branchcode import models as branchmodel 
from creditanalysis import models as analysismodel 
from processrecords.subsystems import filenaming
from processrecords.subsystems import datasetmatch 

mytitle = "Swirling Credit System"

class Graphic(View):
    @method_decorator(login_required)
    def get(self, request):
        try:
            self.rendered_context = self.process_context(request)
            if(self.rendered_context):
                try:
                    return HttpResponse(self.rendered_context)
                except:
                    raise
            else:
                return HttpResponseServerError("FAILURE")
        except:
            raise


    def load_rules_template(self, template):
        if(len(template)):
            try:
                return loader.get_template(template)
            except:
                raise
        else:
            return False

    def process_context(self, request):
        try:
            self.template = self.load_rules_template("validationrules.html")
            if(self.template):
                try:
                    self.datasetrecords = get_datarecords()
                    
                    self.context = RequestContext(request, {"basetitle":mytitle,"datasetrecords":self.datasetrecords,
                                                            "records_to_search":"Rules"
                                                            })
                    return self.template.render(self.context)
                except:
                    raise
            else:
                return None
        except:
            raise


mytitle = "CRB Data"

def get_datarecords():
        """
        Return all available dataset records.
        """
        try:
            return record_models.Dataset.objects.all()
        except:
            raise
            
class RecordSearching(View):
    def get(self, request,record):
        try:
            self.rendered_context = self.process_context(request, record)
            if(self.rendered_context):
                try:
                    return HttpResponse(self.rendered_context)
                except:
                    raise 
            else:
                return HttpResponseServerError("FAILURE")
        except:
            raise 
    
    
    def load_search_template(self, template):
        if(len(template)):
            try:
                return loader.get_template(template)
            except:
                raise 
        else:
            return False 

    def process_context(self, request, record):
        try:
            self.template = self.load_search_template("analysispage.html")
            if(self.template):
                try:
                    self.datasetrecords = get_datarecords()
                    self.data_extension = datasetmatch.load_file_extension(record)
                    self.all_returned = self.return_allfiltered(self.data_extension)
                    
                    self.paginated_gra = Paginator(self.all_returned, 1)
                
                    self.next_page = request.GET.get("page")
                    try:
                        self.gra_page = self.paginated_gra.page(self.next_page)
                    except PageNotAnInteger:
                        self.gra_page = self.paginated_gra.page(1) 
                    except EmptyPage:
                        self.gra_page = self.paginated_gra.page(self.paginated_gra.num_pages)
                        
                    self.context = RequestContext(request, {"basetitle":mytitle,"datasetrecords":self.datasetrecords,
                                                            "records_to_search":record, "Exenstion":self.data_extension,
                                                            "allgraphed":self.gra_page
                                                            })
                    return self.template.render(self.context)
                except:
                    raise 
            else:
                return None 
        except:
            raise 
            
    def return_allfiltered(self, ext):
        try:
            return analysismodel.SuccessFullFailedGraph.objects.filter(record_type=ext)
        except:
            raise 
                
class RecordSearchingAJAX(View):
    def get(self, request, record):
        try:
            self.search_records = request.GET.get("dataset", "")
            self.model = self.load_module_modules(record)
            if(self.model == None):
                pass 
            else:
                self.allrecords = self.load_records_in_model(self.model)
            return HttpResponse("works")
        except:
            raise 
    
    
    def load_search_template(self, template):
        if(len(template)):
            try:
                return loader.get_template(template)
            except:
                raise 
        else:
            return False 

    def process_context(self, request, record):
        try:
            self.template = self.load_search_template("searchpage.html")
            if(self.template):
                try:
                    self.datasetrecords = get_datarecords()
                    
                    self.context = RequestContext(request, {"basetitle":mytitle,"datasetrecords":self.datasetrecords,
                                                            "records_to_search":record 
                                                            })
                    return self.template.render(self.context)
                except:
                    raise 
            else:
                return None 
        except:
            raise 
            
    def load_module_modules(self, record_slug):
        """
        Load the given module.
        """
        try:
            if(record_slug):
                return loadmodels.load_model_replace_underscore(record_slug)
            else:
                return False
        except:
            raise
            
    def load_records_in_model(self, model):
        try:
            return loadmodels.load_all_data(model)
        except:
            raise
