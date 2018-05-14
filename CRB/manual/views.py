from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.template import Context, loader, RequestContext
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.views import login
from datasets import models as record_models
from userlogin import forms as userloginforms 
from userlogin import models as usermodels 
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage 

BASE_TITLE="Welcome to Inbuilt System manaul"

def get_datarecords():
    """
    Return all available dataset records.
    """
    try:
        return record_models.Dataset.objects.all()
    except:
        raise
        
class UserManual(View):
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
            self.template = self.load_rules_template("sysmanual.html")
            if(self.template):
                try:
                    self.datasetrecords = get_datarecords()
                    
                    self.context = RequestContext(request, {"basetitle":BASE_TITLE,"datasetrecords":self.datasetrecords,
                                                            "records_to_search":"Rules" 
                                                            })
                    return self.template.render(self.context)
                except:
                    raise 
            else:
                return None 
        except:
            raise 

class Maintainers(View):
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
            self.template = self.load_rules_template("sysmaintainers.html")
            if(self.template):
                try:
                    self.datasetrecords = get_datarecords()
                    
                    self.context = RequestContext(request, {"basetitle":"Contact system maintainers","datasetrecords":self.datasetrecords,
                                                            "records_to_search":"Rules" 
                                                            })
                    return self.template.render(self.context)
                except:
                    raise 
            else:
                return None 
        except:
            raise 
