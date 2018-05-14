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
from datasetrecords import models as record_models
from datasetrecords import models as datamodels
from datasetrecords import forms as dataset_forms 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from branchcode import forms as branchforms 
from branchcode import models as branchmodels 
from processrecords.subsystems import csvread
from datasets import models as datafield
import simplejson

mytitle = "New data submission specifications"

class AddNewDSS(View):
    @method_decorator(login_required)
    def get(self, request):
        try:
            self.template = self.load_dss_template()
            self.rendered = self.process_context(request, self.template,  None)
            if(self.rendered):
                return HttpResponse(self.rendered)
            else:
                return HttpResponseServerError("FAILURE WAS DETECTED.")
        except:
            raise

    def load_dss_template(self, *template):
        try:
            if(template):
                return loader.get_template(template)
            else:
                return loader.get_template("new_dssheaders.html")
        except:
            raise

    def process_context(self, request, template, who):
        try:
            if(template):
                try:
                    #self.dss_forms = self.get_dssforms()
                    self.datasetrecords = self.get_datarecords()
                    self.dsshforms = self.get_dssforms()
                    
                    self.context = RequestContext(request, {"who":who,  "datasetrecords":self.datasetrecords,
                                                             "newheaders":"Add New Data submission headers",
                                                             "basetitle":mytitle, #"formset":self.dss_forms,
                                                             "dssformset":self.dsshforms
                                                        })
                    self.rend = template.render(self.context)
                    return self.rend
                except:
                    raise
            else:
                return False
        except:
            raise

    def get_dssforms(self, insertmode=False):
        if(insertmode):
            return branchforms.DatasetRecordForms()
        else:
            return branchforms.DatasetRecordForms

    def get_datarecords(self):
        """
        Return all available dataset records.
        """
        try:
            return datafield.Dataset.objects.all()
        except:
            raise
            
    @method_decorator(login_required)
    def post(self, request):
        try:
            if(request.user.is_authenticated() and request.user.is_superuser):
                try:
                    self.forms = self.get_dssforms(insertmode=False)
                    self.insertdata = self.forms(request.POST)
                    
                    if(self.insertdata.is_valid()):
                        self.insertdata.save()
                        return HttpResponseRedirect("/dssh/view/dsshe/")
                    elif(self.insertdata.errors):
                        print self.insertdata.errors
                        #return HttpResponse("Errors where found in your form")
                        
                        self.datasetrecords = self.get_datarecords()
                        #self.dsshforms = self.get_dssforms()
                        self.template = self.load_dss_template()
                        self.context = RequestContext(request, {"who":'unnown',  "datasetrecords":self.datasetrecords,
                                                                 "newheaders":"Add New Data submission headers",
                                                                 "basetitle":mytitle, #"formset":self.dss_forms,
                                                                 "dssformset":self.insertdata, "ERRORS":self.insertdata.errors
                                                            })
                        self.rend = self.template.render(self.context)
                        return HttpResponse(self.rend)
                    else:
                        return HttpResponseServerError("FAILURE")
                except:
                    raise
            else:
                return HttpResponseRedirect("/")
        except:
            raise
            
class ViewDSS(View):
    @method_decorator(login_required)
    def get(self, request):
        try:
            self.template = self.load_dss_view_template()
            if(self.template):
                self.rendered = self.process_context(request, self.template)
                if(self.rendered):
                    return HttpResponse(self.rendered)
                else:
                    return HttpResponse("Failure")
            else:
                return HttpResponseServerError("FAILURE")
        except:
            raise


    def load_dss_view_template(self, *template):
        try:
            if(template):
                return loader.get_template(template)
            else:
                return loader.get_template("view_dss.html")
        except:
            raise

    def process_context(self, request, template):
        try:
            if(template):
                try:
                    
                    self.available_headers = self.load_dss_headers()
                    self.paginatator = Paginator(self.available_headers, 8)
                    self.next_page = request.GET.get("page")
                    
                    try:
                        self.page_obj = self.paginatator.page(self.next_page)
                    except PageNotAnInteger:
                        self.page_obj = self.paginatator.page(1)
                    except EmptyPage:
                        self.page_obj = self.paginatator.page(self.paginatator.num_pages)
                    
                    self.hfields = self.parse_model_fields(branchmodels.RequiredHeader)
                    self.hfields =  self.re_parse_fields(self.hfields)
                    self.datasetrecords = self.get_datarecords()
                    #self.loadedrecords = self.load_datarecords()
                    self.context = RequestContext(request, {"datasetrecords":self.datasetrecords, "avilabledssh":self.available_headers,
                                                            "dss_headers":self.hfields, "headers":self.page_obj,
                                                            "viewdssh":"Data Submission specification"
                                                        })
                    self.rend = template.render(self.context)
                    return self.rend
                except:
                    raise
            else:
                return False
        except:
            raise

    def re_parse_fields(self, mfields):
        s = []
        for f in mfields:
            if(f == "creationdate"):
                pass
            elif(f == "header"):
                pass 
            elif(f == "submission date"):
                pass 
            elif(f == "creation date"):
                pass 
            elif(f == "version number"):
                pass 
            else:
                s.append(f)
        return s
        
    def get_datarecords(self):
        """
        Return all available dataset records.
        """
        try:
            return datafield.Dataset.objects.all()
        except:
            raise
            
    def load_datarecords(self):
        """
        Return all available dataset records.
        """
        try:
            return record_models.RequiredHeader.objects.all()
        except:
            raise

    def parse_model_fields(self, model_data):
        """
        Returns the fields coresponding to particular models.
        """
        self.fields = [ ]
        self.mfields = model_data._meta.fields
        for field in self.mfields:
            if(field.name == "creationdate"):
                pass
            elif(field.name == "header"):
                pass 
            elif(field.name == "submissiondate"):
                pass 
            elif(field.name == "creationdate"):
                pass 
            elif(field.name == "versionnumber"):
                pass 
            elif field.name in self.fields:
                pass
            else:
                if("_" in field.name):
                    self.fields.append(field.name.replace("_", " ", len(field.name)))
                    
                elif(field.name == "slug"):
                    pass
                else:
                    self.fields.append(field.name)
            
        #return the model fields
        return self.fields

    def load_dss_headers(self):
        try:
            self.dssh = branchmodels.RequiredHeader.objects.all()
            return self.dssh
        except:
            raise
            

mytitle = "Data Processing System"

class UpdateHeaderFiles(View):
    @method_decorator(login_required)
    def get(self, request, dsshID):
        try:
            self.template = self.load_template()
            if(self.template):
                self.rend = self.handle_context(request, self.template, dsshID)
                return HttpResponse(self.rend)
            else:
                raise ValueError("Unable to load templates.")
        except:
            raise  
        
    def load_template(self, *template):
        try:
            if(template):
                return loader.get_template(template)
            else:
                return loader.get_template("updateheaders.html")
        except:
            raise 
             
        
    def handle_context(self, request, template, hid):
        try:
            self.datarecords = self.load_datarecords()
            self.data_updating = self.get_headers_byID(hid)
            self.header_form = self.get_updateform()
            
            self.formset = self.get_form_instance(self.header_form, self.data_updating)
            
            if(self.formset):
                try:
                    self.context = RequestContext(request, {"dsshforms":self.formset, "datasetrecords":self.datarecords,
                                                            "id":hid, "dsshupdate":"Updating new header files"
                                                            })
                except:
                    raise 
                else:
                    return template.render(self.context)
            else:
                return None 
        except:
            raise 
            
    def get_form_instance(self, headerform, data_updating):
        try:
            if(headerform and data_updating):
                return headerform(instance=data_updating)
            else:
                return False 
        except:
            raise 
            
    @method_decorator(login_required)
    def post(self, request, updatingID):
        try:
            if(request.user.is_authenticated()):
                if(request.user.is_superuser):
                    try:
                        self.update_forms = self.get_updateform()
                        self.headermodel = self.get_headermodels()
                        try:
                            self.headers_tobe_updated = self.get_headers_byID(updatingID)
                        except:
                            raise 
                        else:
                            self.insert = self.update_forms(request.POST, instance=self.headers_tobe_updated)
                            if(self.insert.is_valid()):
                                self.insert.save()
                                return HttpResponseRedirect("/dssh/view/dsshe/")
                            elif(self.insert.errors):
                                return HttpResponse("Failure")
                            else:
                                return HttpResponse("Real FAILURE")
                    except:
                        raise 
                else:
                    return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("/")
        except:
            raise 
            
        
    def load_datarecords(self):
        """
        Return all available dataset records.
        """
        try:
            return datafield.Dataset.objects.all()
        except:
            raise 
    
    def get_updateform(self):
        try:
            return branchforms.DatasetRecordForms 
        except:
            raise 
    
    def get_headermodels(self):
        try:
            return branchmodels.RequiredHeader
        except:
            raise 
            
    def get_headers_byID(self, hid):
        try:
            try:
                self.id_to_int = int(hid)
                self.headers = branchmodels.RequiredHeader.objects.get(id=self.id_to_int)
                return self.headers
            except ValueError as error:
                raise 
            except:
                raise 
        except:
            raise 
            
            
class UploadBranchCode(View):
    def post(self, request):
        self.uploadedfilename = request.FILES.get("branchcode")
        #print "FILENAME IS ", self.uploadedfilename.name 
        #print "FILENAME TYPE ", help(self.uploadedfilename)
        if(self.uploadedfilename):
            self.openedcsv = csvread.ReadCSV(self.uploadedfilename)
            self.ready = self.openedcsv.read_csvs(ready_to_read=True)
            for branch in self.ready:
                if(self.first_query_branch(branch)):
                    print "IT's true it has been found"
                    pass
                else:
                    print "This is not true"
                    self.save_branchdetails(branch)
            return HttpResponseRedirect("/dssh/view/dsshe/")
        #print "FILENAME TYPE  NAME", type(self.uploadedfilename.name)
        else:
            return HttpResponseRedirect("/dssh/view/dsshe/")
            #return HttpResponse("Welcome back to the world of works.")

    def get(self, request):
        return HttpResponse("Welcome")

    def save_branchdetails(self, listdetails):
        """
        """
        try:
            if(listdetails):
                if(len(listdetails) == 2):
                    print "Saving ", listdetails
                    self.branch = branchmodels.BranchNames()
                    self.branch.Branch_Code = listdetails[0]
                    self.branch.Branch_name = listdetails[1]
                    self.branch.save()
        except:
            raise


    def first_query_branch(self, listdetails):
        """
        """
        try:
            if(len(listdetails) == 2):
                print "LEN IS TRUE "
                self.Branch_Code = listdetails[0]
                self.Branch_name = listdetails[1]
                
                self.intify = int(float(self.Branch_Code))
                self.Branch_Code = str(self.intify)
                
                self.querybranch = branchmodels.BranchNames.objects.filter(Branch_Code=self.Branch_Code, Branch_name=self.Branch_name)
                if(self.querybranch):
                    return True
                else:
                    return False
        except:
            raise
            
class QueryBranchInformation(View):
    def get(self, request):
        try:
            if(request.is_ajax()):
                try:
                   self.ID = request.GET.get("biID")
                   self.query = self.query_pi_name(self.ID)
                   #self.PI = self.filtere_pi(self.query)
                   return HttpResponse(simplejson.dumps(self.query), content_type="application/json")
                   
                except Exception as e:
                    self.errordict = {}
                    self.msg = "ERROR: %s " % e.message 
                    self.errordict[self.msg]=self.msg 
                    return HttpResponse(simplejson.dumps(self.errordict), content_type="application/json")
       
            else:
                try:
                   self.ID = request.GET.get("biID")
                   self.query = self.query_pi_name(self.ID)
                   ##self.PI = self.filtere_pi(self.query)
                   return HttpResponse(simplejson.dumps(self.query), content_type="application/json")
                   
                except Exception as e:
                    self.errordict = {}
                    self.msg = "ERROR: %s " % e.message 
                    self.errordict[self.msg]=self.msg 
                    return HttpResponse(simplejson.dumps(self.errordict), content_type="application/json") 
        except Exception as e:
            self.error_msg = "SYS ERROR '%s' " % str(e.message)
            return HttpResponse(simplejson.dumps(self.error_msg), content_type="application/json")

    def query_pi_name(self, pivalue):
        """
        Query the pi return value.
        """
        try:
            self.D = {}
            print "VALUE IS ", pivalue 
            self.pi_code = branchmodels.BranchNames.objects.get(id=pivalue)
            self.D["BRANCHCODE"]=self.pi_code.Branch_Code
            return self.D
        except:
            raise  
