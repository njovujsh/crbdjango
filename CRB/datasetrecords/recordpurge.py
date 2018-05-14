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
from branchcode import models as branchmodels 
from userlogin import models as usermodels 
from datasetrecords import accreference 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from processrecords import forms as processforms
from datasetrecords import searchfilters
from datasetrecords import loadmodels


class PermanentDelete(View):
    def get(self, request, record_slug, ID, clientID):
        try:
            self.model_2_delfrom = self.load_module_modules(record_slug)
            if(record_slug == "credit_application"):
                self.records = self.query_cp_delete(self.model_2_delfrom, ID, clientID)
                self.ret_delete = self.delete_now(self.records)
                if(self.ret_delete):
                    self.url = self.contruct_redir_parth(record_slug)
                    return HttpResponseRedirect(self.url)
                else:
                    return HttpResponse("Unable to delete records")
                    
            elif(record_slug == "bouncedcheques"):
                self.records = self.query_global_delete(self.model_2_delfrom, ID, clientID)
                self.ret_delete = self.delete_now(self.records, has_associated=False)
                if(self.ret_delete):
                    self.url = self.contruct_redir_parth(record_slug)
                    return HttpResponseRedirect(self.url)
                else:
                    return HttpResponse("Unable to delete records")
                    
            elif(record_slug == "creditborroweraccount"):
                self.records = self.query_global_delete(self.model_2_delfrom, ID, clientID)
                self.ret_delete = self.delete_now(self.records, has_associated=False)
                if(self.ret_delete):
                    self.url = self.contruct_redir_parth(record_slug)
                    return HttpResponseRedirect(self.url)
                else:
                    return HttpResponse("Unable to delete records")
                    
            else:
                return HttpResponse("Selected Record does not support delete operations.")
                    
        except Exception as e:
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

    def query_cp_delete(self, deletemodel, ID, clientID):
        try:
            filter_records = deletemodel.objects.get(id=int(ID), Client_Number=clientID)
            return filter_records
        except datamodels.CREDIT_APPLICATION.ObjectDoesNotExist as e:
            raise
        except Exception as e:
            raise
            
    def query_global_delete(self, deletemodel, ID, clientID):
        try:
            filter_records = deletemodel.objects.get(id=int(ID))
            return filter_records
        except Exception as e:
            raise 

    def delete_now(self, record, has_associated=True):
        try:
            if(has_associated):
                record.delete()
                self.purge_associated(record)
            else:
                record.delete()
        except:
            raise
        else:
            return True

    def contruct_redir_parth(self, record_slug):
        try:
            self.url_string = "/view/dataview/request/%s" % str(record_slug)
            return self.url_string
        except:
            raise

    def purge_associated(self, record):
        """
        Delete te pci, sci, ii,ie, gsca.
        """
        try:
            record.pci.delete()
            record.sci.delete()
            record.gscafb.delete()
            record.idi.delete()
            record.ei.delete()
            if(record.history):
                allmany  = records.history.all()
                try:
                    for m in allmany:
                        record.history.remove(m)
                except:
                    pass  
            record.howmanytimes.delete()
        except ValueError as e:
            print e
            pass 
                

