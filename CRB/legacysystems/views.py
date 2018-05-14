from django.shortcuts import render
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
from legacysystems import forms as legacyforms 
from legacysystems import models as legacymodel 
from userlogin import views as userview
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

mytitle = "Data/Scheduler"

def get_datarecords():
    """
    Return all available dataset records.
    """
    try:
        return record_models.Dataset.objects.all()
    except:
        raise

class LegacySystem(View):
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
            self.template = self.load_rules_template("legacysysytems.html")
            if(self.template):
                try:
                    self.datasetrecords = get_datarecords()
                    self.legacyf = self.legacy_forms()
                    self.context = RequestContext(request, {"basetitle":mytitle,"datasetrecords":self.datasetrecords,
                                                            "records_to_search":"Rules", "forms":self.legacyf
                                                            })
                    return self.template.render(self.context)
                except:
                    raise
            else:
                return None
        except:
            raise
            
    def legacy_forms(self):
        return legacyforms.LegacySystemsForms()
        
    def insert_forms(self):
        return legacyforms.LegacySystemsForms
       
    @method_decorator(login_required) 
    def post(self, request):
        if(request.user.is_authenticated):
            try:
                self.legacy_forms = self.insert_forms()
                self.sec_rules = self.legacy_forms(request.POST)
                if(self.sec_rules.is_valid()):
                    self.sec_rules.save()
                    return HttpResponseRedirect("/rlegacy/lview/")
                else:
                    return HttpResponse(self.render_form_with_errors(request, self.sec_rules.errors, self.sec_rules))
            except:
                raise 
        else:
            return HttpResponseRedirect("/")
            
    def render_form_with_errors(self, request, error, forms):
        try:
            self.template = self.load_rules_template("legacysysytems.html")
            if(self.template):
                try:
                    self.datasetrecords = get_datarecords()
                    self.context = RequestContext(request, {"basetitle":mytitle,"datasetrecords":self.datasetrecords,
                                                            "records_to_search":"Rules", "forms":forms,
                                                            "errors":error 
                                                            })
                    return self.template.render(self.context)
                except:
                    raise
            else:
                return None
        except:
            raise
        
class BranchSystem(View):
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
            self.template = self.load_rules_template("multibrach.html")
            if(self.template):
                try:
                    self.datasetrecords = get_datarecords()
                    self.replicationf = self.replication_forms()
                    self.context = RequestContext(request, {"basetitle":mytitle,"datasetrecords":self.datasetrecords,
                                                            "records_to_search":"Rules", "forms":self.replicationf
                                                            })
                    return self.template.render(self.context)
                except:
                    raise
            else:
                return None
        except:
            raise
            
    def replication_forms(self):
        return legacyforms.ReplicationDatabaseForms()
        
    def insert_forms(self):
        return legacyforms.ReplicationDatabaseForms
        
    @method_decorator(login_required)
    def post(self, request):
        if(request.user.is_authenticated):
            try:
                self.legacy_forms = self.insert_forms()
                self.sec_rules = self.legacy_forms(request.POST)
                if(self.sec_rules.is_valid()):
                    self.sec_rules.save()
                    return HttpResponseRedirect("/rlegacy/rview/")
                else:
                    return HttpResponse(self.render_form_with_errors(request, self.sec_rules.errors, self.sec_rules))
            except:
                raise 
        else:
            return HttpResponseRedirect("/")
            
    def render_form_with_errors(self, request, error, forms):
        try:
            self.template = self.load_rules_template("multibrach.html")
            if(self.template):
                try:
                    self.datasetrecords = get_datarecords()
                    self.context = RequestContext(request, {"basetitle":mytitle,"datasetrecords":self.datasetrecords,
                                                            "records_to_search":"Rules", "forms":forms,
                                                            "errors":error 
                                                            })
                    return self.template.render(self.context)
                except:
                    raise
            else:
                return None
        except:
            raise
    
class ViewBranchSystem(View):
    @method_decorator(login_required)
    def get(self, request):
        try:
            if(request.user.is_authenticated()):
                self.rendered_context = self.process_context(request)
                if(self.rendered_context):
                    try:
                        return HttpResponse(self.rendered_context)
                    except:
                        return HttpResponseServerError("ERROR please try againlater")
                else:
                    return HttpResponseServerError("ERROR please try to clear cookies")
            else:
                return HttpResponseRedirect("/")
        except:
            raise 
            
    
    def load_view_template(self, *custom_template):
        """
        Given the template attempt to load and return it.
        """
        try:
            if(custom_template):
                try:
                    return loader.get_template(custom_template)
                except:
                    raise 
            else:
                try:
                    return loader.get_template("viewmbranch.html")
                except:
                    raise 
        except:
            raise
            
    def process_context(self, request):
        """
        Process and return the context.
        """
        try:
            self.template = self.load_view_template()
            if(self.template):
                try:
                    self.datasetrecords = self.get_datarecords()
                    self.available_rules = self.load_all_rules()
                    self.paginated_rules = Paginator(self.available_rules, 8)
                    
                    self.next_page = request.GET.get("page")
                    try:
                        self.rule_page = self.paginated_rules.page(self.next_page)
                    except PageNotAnInteger:
                        self.rule_page = self.paginated_rules.page(1) 
                    except EmptyPage:
                        self.rule_page = self.paginated_rules.page(self.paginated_rules.num_pages)
                        
                    self.model_headers = userview.parse_model_fields(legacymodel.ReplicationDatabase)
                    self.returned = self.excludes(self.model_headers, "destinationpassword")
                    self.context = RequestContext(request, {"basetitle":mytitle,"datasetrecords":self.datasetrecords,
                                                            "srules":self.rule_page,"rule_headers":self.returned
                                                    })
                    return self.template.render(self.context)
                except:
                    raise 
            else:
                return False 
        except:
            raise 
    
    def excludes(self, lists, toex):
        l = []
        for i in lists:
            if i == toex:
                pass 
            else:
                l.append(i)
        return l 
        
    def load_all_rules(self):
        """
        Load and return all staffs.
        """
        try:
            return legacymodel.ReplicationDatabase.objects.all()
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
        
    def post(self, request):
        pass 
        
class ViewLegacy(View):
    @method_decorator(login_required)
    def get(self, request):
        try:
            if(request.user.is_authenticated()):
                self.rendered_context = self.process_context(request)
                if(self.rendered_context):
                    try:
                        return HttpResponse(self.rendered_context)
                    except:
                        return HttpResponseServerError("ERROR please try againlater")
                else:
                    return HttpResponseServerError("ERROR please try to clear cookies")
            else:
                return HttpResponseRedirect("/")
        except:
            raise 
            
    
    def load_view_template(self, *custom_template):
        """
        Given the template attempt to load and return it.
        """
        try:
            if(custom_template):
                try:
                    return loader.get_template(custom_template)
                except:
                    raise 
            else:
                try:
                    return loader.get_template("viewlegacy.html")
                except:
                    raise 
        except:
            raise
            
    def process_context(self, request):
        """
        Process and return the context.
        """
        try:
            self.template = self.load_view_template()
            if(self.template):
                try:
                    self.datasetrecords = self.get_datarecords()
                    self.available_rules = self.load_all_rules()
                    self.paginated_rules = Paginator(self.available_rules, 8)
                    
                    self.next_page = request.GET.get("page")
                    try:
                        self.rule_page = self.paginated_rules.page(self.next_page)
                    except PageNotAnInteger:
                        self.rule_page = self.paginated_rules.page(1) 
                    except EmptyPage:
                        self.rule_page = self.paginated_rules.page(self.paginated_rules.num_pages)
                        
                    self.model_headers = userview.parse_model_fields(legacymodel.LegacyTracker)
                    self.returned = self.excludes(self.model_headers, "databasepassword")
                    self.context = RequestContext(request, {"basetitle":mytitle,"datasetrecords":self.datasetrecords,
                                                            "srules":self.rule_page,"rule_headers":self.returned
                                                    })
                    return self.template.render(self.context)
                except:
                    raise 
            else:
                return False 
        except:
            raise 
    
    def excludes(self, lists, toex):
        l = []
        for i in lists:
            if i == toex:
                pass 
            else:
                print i
                l.append(i)
        return l 
        
    def load_all_rules(self):
        """
        Load and return all staffs.
        """
        try:
            return legacymodel.LegacyTracker.objects.all()
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
        
    def post(self, request):
        pass 


class UpdateSystems(View):
    @method_decorator(login_required)
    def get(self, request, PID):
        try:
            if(request.user.is_authenticated):
                self.rendered_context = self.process_context(request, PID)
                if(self.rendered_context):
                    try:
                        return HttpResponse(self.rendered_context)
                    except:
                        raise
                else:
                    return HttpResponseServerError("FAILURE")
            else:
                return HttpResponseRedirect("/")
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

    def process_context(self, request, PID):
        try:
            self.template = self.load_rules_template("legacysysytems.html")
            if(self.template):
                try:
                    self.datasetrecords = get_datarecords()
                    self.pid_data = self.load_PID_data(PID)
                    self.sforms = self.load_forms(instance=self.pid_data)
                    self.context = RequestContext(request, {"basetitle":mytitle,"datasetrecords":self.datasetrecords,
                                                            "forms":self.sforms, "is_update":True, "RULEID":PID,
                                                            })
                    return self.template.render(self.context)
                except:
                    raise
            else:
                return None
        except:
            raise
            
    def load_PID_data(self, pid):
        try:
            if(pid > 0):
                return legacymodel.LegacyTracker.objects.get(id=int(pid))
            else:
                return pid 
        except:
            pass 
             
    def load_forms(self, instance):
        """
        Return the forms.
        """
        return legacyforms.LegacySystemsForms(instance=instance)
    
    def insert_forms(self):
        return legacyforms.LegacySystemsForms
        
    def post(self, request):
        if(request.user.is_authenticated):
            try:
                self.security_forms = self.insert_forms()
                self.sec_rules = self.security_forms(request.POST)
                if(self.sec_rules.is_valid()):
                    self.sec_rules.save()
                    return HttpResponseRedirect("/srules/sview/")
                else:
                    return HttpResponse("Inavlid")
            except:
                raise 
        else:
            return HttpResponseRedirect("/")
        
    @method_decorator(login_required)
    def post(self, request, PID):
        if(request.user.is_authenticated):
            try:
                self.security_forms = self.insert_forms()
                self.pid_data = self.load_PID_data(PID)
                self.sec_rules = self.security_forms(request.POST, instance=self.pid_data)
                if(self.sec_rules.is_valid()):
                    self.sec_rules.save()
                    self.msg  = "Legacy Corresponding to [ %s ] was updated successfuly." % self.pid_data.database_hostname
                    return HttpResponse(self.process_context_success(request, self.msg))
                else:
                    return HttpResponse("Inavlid")
            except:
                raise 
        else:
            return HttpResponseRedirect("/")

    def process_context_success(self, request, msg):
        """
        Process and return the context.
        """
        try:
            self.template = loader.get_template("viewlegacy.html")
            if(self.template):
                try:
                    self.datasetrecords = self.get_datarecords()
                    
                    self.available_rules = self.load_all_rules()
                    
                    self.paginated_rules = Paginator(self.available_rules, 8)
                    
                    self.next_page = request.GET.get("page")
                    try:
                        self.rule_page = self.paginated_rules.page(self.next_page)
                    except PageNotAnInteger:
                        self.rule_page = self.paginated_rules.page(1) 
                    except EmptyPage:
                        self.rule_page = self.paginated_rules.page(self.paginated_rules.num_pages)
                        
                        #print "PAGE ", self.rule_page
                    self.model_headers = userview.parse_model_fields(legacymodel.LegacyTracker)
                    self.returned = self.excludes(self.model_headers, "databasepassword")
                    self.context = RequestContext(request, {"basetitle":mytitle,"datasetrecords":self.datasetrecords,
                                                            "srules":self.rule_page,"rule_headers":self.returned,
                                                            "msg":msg
                                                    })
                    return self.template.render(self.context)
                except:
                    raise 
            else:
                return False 
        except:
            raise 
    
    def load_all_rules(self):
        """
        Load and return all staffs.
        """
        try:
            return legacymodel.LegacyTracker.objects.all()
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
            
    def excludes(self, lists, toex):
        l = []
        for i in lists:
            if i == toex:
                pass 
            else:
                l.append(i)
        return l 
            
class PurgeUpdateSystems(View):
    @method_decorator(login_required)
    def get(self, request, PID):
        try:
            if(PID):
                self.getdata = self.load_PID_data(PID)
                if(self.getdata):
                    self.msg = "Legacy corresponding to  [ %s ] was deleted successfuly." % self.getdata.database_hostname
                    self.getdata.delete()
                    return HttpResponse(self.process_context(request, self.msg))
                else:
                    return HttpResponseRedirect("/rlegacy/lview/")
            else:
                return HttpResponseRedirect("/rlegacy/lview/")
        except:
            raise 
            
    def load_PID_data(self, pid):
        try:
            if(pid > 0):
                return legacymodel.LegacyTracker.objects.get(id=int(pid))
            else:
                return pid 
        except:
            pass 
            
    def load_view_template(self, *custom_template):
        """
        Given the template attempt to load and return it.
        """
        try:
            if(custom_template):
                try:
                    return loader.get_template(custom_template)
                except:
                    raise 
            else:
                try:
                    return loader.get_template("viewlegacy.html")
                except:
                    raise 
        except:
            raise
            
    def process_context(self, request, msg):
        """
        Process and return the context.
        """
        try:
            self.template = self.load_view_template()
            if(self.template):
                try:
                    self.datasetrecords = self.get_datarecords()
                    
                    self.available_rules = self.load_all_rules()
                    
                    self.paginated_rules = Paginator(self.available_rules, 8)
                    
                    self.next_page = request.GET.get("page")
                    try:
                        self.rule_page = self.paginated_rules.page(self.next_page)
                    except PageNotAnInteger:
                        self.rule_page = self.paginated_rules.page(1) 
                    except EmptyPage:
                        self.rule_page = self.paginated_rules.page(self.paginated_rules.num_pages)
                        
                        #print "PAGE ", self.rule_page
                    self.model_headers = userview.parse_model_fields(legacymodel.LegacyTracker)
                    self.returned = self.excludes(self.model_headers, "databasepassword")
                    self.context = RequestContext(request, {"basetitle":mytitle,"datasetrecords":self.datasetrecords,
                                                            "srules":self.rule_page,"rule_headers":self.returned,
                                                            "msg":msg
                                                    })
                    return self.template.render(self.context)
                except:
                    raise 
            else:
                return False 
        except:
            raise 
    
    def load_all_rules(self):
        """
        Load and return all staffs.
        """
        try:
            return legacymodel.LegacyTracker.objects.all()
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
    
    def excludes(self, lists, toex):
        l = []
        for i in lists:
            if i == toex:
                pass 
            else:
                l.append(i)
        return l 
