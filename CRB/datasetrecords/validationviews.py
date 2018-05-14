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
from subsystems import csvhandler
from reportlab.pdfgen import canvas
import datetime
import time
from django.forms.models import inlineformset_factory
import importlib
from datasets import models as record_models
from datasetrecords import models as datamodels
from datasets import forms as dataset_forms 

mytitle = "Swirling Credit System"

def get_datarecords():
    """
    Return all available dataset records.
    """
    try:
        return record_models.Dataset.objects.all()
    except:
        raise
            

class ValidationRules(View):
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
    
    
    def load_rules_template(self, template):
        if(len(template)):
            try:
                return loader.get_template(template)
            except:
                raise 
        else:
            return False 
            
    def process_context(self, request, record):
        try:
            self.template = self.load_search_template("validationrules.html")
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
                

