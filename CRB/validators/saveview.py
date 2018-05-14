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
from processrecords import models as pmodels 
import os
from CRB import settings 
from creditreports import loadreportmodels
from validators import models as validatmodels 
from processrecords.subsystems import filenaming
from processrecords.subsystems import datasetmatch 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from branchcode import models as branchmodel 

mytitle = "Credstat Credit System"

def get_datarecords():
    """
    Return all available dataset records.
    """
    try:
        return record_models.Dataset.objects.all()
    except:
        raise
            


class ValidateAndSave(View):
    @method_decorator(login_required)
    def get(self, request, record_slug):
        try:
            if(record_slug):
                self._csv_module = self.load_csv_validated_module(record_slug)
                self.model = self.load_module_modules(record_slug)
                self.records = self.load_records_in_model(self.model)
                self.validation_code = self.load_validation_code(record_slug)
                
                #grab the headers
                self.h = self.load_headers()
                self.lheaders = self.append_headers_to_list(self.h)
                self.h.pi_identification_code
                self.filename = self.load_filenames(self.h.pi_identification_code, record_slug)
                self.extension =  datasetmatch.load_file_extension(record_slug)
                self.lheaders.append(self.extension)
                
                try:
                    self.joined = os.path.join(settings.MEDIA_ROOT, self.filename)
                    self.filelineno = self.create_file_object(self.joined)
                    self.csvfile = self.write_csv(self.records, self.filename, self._csv_module, self.validation_code, self.lheaders, self.filelineno)
                    self.ret = self.save_validation_in_database(self.joined, self.filename, self.filelineno)
                    if(self.ret):
                        return HttpResponseRedirect("/importdata/showsaved/andvalidated/")
                    else:
                        return HttpResponseServerError(self.ret)
                    self.filelineno.close()
                except:
                    raise 
                return HttpResponse("Working")
            else:
                return HttpResponse("FAILURE ")
        except:
            raise 
                
    
    def create_file_object(self, filenameandpath):
        try:
            if(filenameandpath):
                return open(filenameandpath, "wb")
            else:
                return False 
        except:
            raise 
            
    def begin_data_validation(self, validation_code):
        """
        """
        try:
            if(validation_code):
                return validation_code.begin_validation()
            else:
                return False
        except:
            raise 
            
    def construct_dictionary(self, value, key):
        return {key:value}
        
    def get_v_dataset(self, request):
        try:
            return request.GET.get("validationsdataset", "")
        except:
            raise 
            
    def load_validation_code(self, dataset):
        try:
            return loadvalidationmodule.load_modules(dataset)
        except:
            raise 
            
    def load_module_counts(self, dataset):
        try:
            return loadvalidationmodule.load_module_count(dataset)
        except:
            raise 
        
    def load_csv_validated_module(self, dataset):
        try:
            return loadcsvmodules.load_csv_validated_module(dataset)
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
            
    def load_validation_code(self, dataset):
        try:
            return loadvalidationmodule.load_modules(dataset)
        except:
            raise 
            
    def write_csv(self, records, fname, csv_module, validation_code, lheaders, filelineno):
        try:
            #print csv_module
            self.ret_csv = csv_module(filename=fname, dialect="excel", delimiter="|", row=lheaders, headers=lheaders, response=filelineno)
            self.validated_file = self.ret_csv.write_row_data(records, validation_code)
            return self.validated_file
        except:
            raise  
    
    def load_headers(self, ID=1):
        try:
            return branchmodel.RequiredHeader.objects.get(id=ID)
        except:
            raise 
            
    def append_headers_to_list(self, headers):
        self.hlist = []
       
        self.hlist.append(headers.header)
        self.hlist.append(headers.pi_identification_code.pi_identification_code)
        self.hlist.append(headers.pi_identification_code.insitution_Name)
        self.hlist.append(str(headers.submission_date).replace("-", "", 10))
        self.hlist.append(headers.version_number)
        self.hlist.append(str(headers.creation_date).replace("-", "", 10))
        return self.hlist 
        
    def save_validation_in_database(self, vpath, fname,  fileobject):
        """
        Given the path of our sheet save it inside the database.
        """
        try:
            self.sheet_modelboject = validatmodels.ValidatedAndSaved()
            self.sheet_modelboject.name = fname
            self.sheet_modelboject.filename.name = vpath
            self.sheet_modelboject.save()
            return True 
        except Exception as e:
            print e.message 
            print e.args
        else:
            return True 
    
    def load_filenames(self, pi_code, dataset):
        """
        Load and return the filename.filenaming
        """
        try:
            self.dataset = datasetmatch.load_file_extension(dataset)
            if(self.dataset):
                return filenaming.make_filename(pi_code=pi_code, filename=self.dataset)
            else:
                return False 
        except:
            raise 
            
class ShowSavedValidated(View):
    @method_decorator(login_required)
    def get(self, request):
        try:
            if(request.user.is_authenticated()):
                self.template = self.get_templates()
                self.rendered = self.render_context(request, self.template)
                return HttpResponse(self.rendered)
            else:
                return HttpResponseRedirect("/")
        except:
            raise

    def get_templates(self):
        try:
            return loader.get_template("showsaved.html")
        except:
            raise

    def render_context(self, request, template):
        try:
            #validatmodels.ValidatedAndSaved()
            self.all_files = validatmodels.ValidatedAndSaved.objects.all()
            self.mfiles =  self.parse_model_fields(validatmodels.ValidatedAndSaved)
            self.file_count = validatmodels.ValidatedAndSaved.objects.all().count()
            #print "All in All ", self.file_count
            self.datasetrecords = self.get_datarecords()
            self.paginatator = Paginator(self.all_files, 6)

            self.next_page = request.GET.get("page")
            try:
                self.page_obj = self.paginatator.page(self.next_page)
            except PageNotAnInteger:
                self.page_obj = self.paginatator.page(1)
            except EmptyPage:
                self.page_obj = self.paginatator.page(self.paginatator.num_pages)

            self.now = time.ctime()
            self.our_context = RequestContext(request, {"file_headers":self.mfiles, "availablefiles":self.page_obj,
                                                        "totalsaved":self.file_count, "datasetrecords":self.datasetrecords,
                                                        "displaytimes":self.now, 'basetitle':mytitle,
                                                        "customtitle":"validated and uploaded Files"
                                                        })

            try:
                return template.render(self.our_context)
            except:
                raise
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
            
    def parse_model_fields(self, data):
        self.fields = [ ]
        self.mfields = data._meta.fields
        self.passed = []
        for model_fields in self.mfields:
                if(model_fields.name in self.fields):
                    pass
                else:
                    self.fields.append(model_fields.name.replace("_", " ", len(model_fields.name)))
        
        for f in self.fields:
            if f == "imagename":
                pass 
            else:
                self.passed.append(f)
        return self.passed


class GetValidationRecordsStatus(View):
    @method_decorator(login_required)
    def get(self, request):
        if(request.is_ajax()):
            try:
                self.json_dict = {}
                datamodel = request.GET.get("validationsdataset")
                record_id = request.GET.get("validationdate")
                
                self.djangomodel =  self.load_report_record(datamodel)
                self.records_retrieved =  self.get_record_by_id(self.djangomodel, record_id)
                self.ret_dict = self.parse_record(self.records_retrieved)
                #print self.ret_dict
                #print len(self.ret_dict)
                #self.json_dict["validation_status"]=self.ret_dict
                try:
                    return HttpResponse(simplejson.dumps(self.ret_dict), content_type="application/json")
                except:
                    raise
            except:
                raise 
        else:
            return HttpResponse("It's not ajax")
            
    def parse_record(self, records):
        try:
            FORMAT  = "%Y-%m-%d-%H-%M-%S"
            self.record_dict = {}
            self.record_dict["ID"]= "Unique Validation Identification : %d " % records.id
            self.record_dict["picode"]=" PI Unique Code %s " % records.pi_name
            self.record_dict["date"]= "Record Validation Date : %s " % records.validation_date.strftime(FORMAT)
            self.record_dict["rtype"]="Data Type : %s " % records.record_type
            self.record_dict["total"]="Total Records Validated : %s " % records.total_records
            self.record_dict["successful"]= "Successfully Validated Records : %s " % records.successful_records
            self.record_dict["failed"]="Unsuccessful/Failed Validated Records : %s " % records.failed_records
            self.record_dict["pfield"]="Successfully Validated Fields : %s " % records.number_of_fields_passed
            self.record_dict["ffield"]="Unsuccessful/Failed Validated Fields : %s " % records.number_of_fields_failed
            return self.record_dict
        except:
            pass 
        
    def load_report_record(self, model):
        try:
            return loadreportmodels.load_report_model_(model)
        except:
            raise
            
    def get_record_by_id(self, model, ID):
        """
        Given the model and records return the
        id.
        """
        try:
            return model.objects.get(id=int(ID))
        except:
            raise  
    
    def save_validation_in_database(self, vpath, fname,  fileobject):
        """
        Given the path of our sheet save it inside the database.
        """
        try:
            self.sheet_modelboject = validatmodels.ValidatedAndSaved()
            self.sheet_modelboject.name = fname
            self.sheet_modelboject.filename.name = vpath
            self.sheet_modelboject.save()
        except Exception as e:
            return HttpResponse("FAILURE") #self.render_doesnot_exists(e))
        else:
            return True 
           
            
    def load_headers(self, ID=1):
        try:
            return datamodels.RequiredHeader.objects.get(id=ID)
        except:
            raise

    def append_headers_to_list(self, headers):
        self.hlist = []

        self.hlist.append(headers.header)
        self.hlist.append(headers.pi_identification_code)
        self.hlist.append(headers.institution_name)
        self.hlist.append(headers.submission_date.replace("-", "", len(headers.submission_date)))
        self.hlist.append(headers.version_number)
        self.hlist.append(headers.creation_date.replace("-", "", len(headers.creation_date)))
        return self.hlist


class DownloadSaved(View):
    @method_decorator(login_required)
    def get(self, request, FID):
        try:
            self.loadedfile = self.load_files_byid(FID)
            if(self.loadedfile):
                response = HttpResponse(self.loadedfile.filename.read(), content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename=%s' % self.loadedfile.name
                response['Content-Length'] = self.loadedfile.filename.size
                return response
            else:
                return HttpResponse("FAILED")
        except:
            raise 
        
        
    def load_files_byid(self, FID):
        try:
            if(FID):
                self.filename =  validatmodels.ValidatedAndSaved.objects.get(id=FID)
                if(self.filename):
                    return self.filename 
                else:
                    return None
            else:
                return False 
        except:
            raise 
            

class SearchClientRootDetails(View):
    @method_decorator(login_required)
    def get(self, request):
        #if(request.is_ajax()):
        try:
            self.clientRoot = request.GET.get("clientRoot")
            
            
            self.json_dict = self.filter_client_records(self.clientRoot)
            #print "JSONED ", self.json_dict
            try:
                return HttpResponse(simplejson.dumps(self.json_dict), content_type="application/json")
            except:
                raise
        except:
            raise 
        #else:
        #    return HttpResponse("It's not ajax")

    def filter_client_records(self, clientRoot):
        """
        Search all the clients records.
        """
        try:
            self.filtered = datamodels.CREDIT_APPLICATION.objects.filter(Client_Number=clientRoot)
            if(len(self.filtered) > 1):
                return True
            else:
                #print "FILTERED ", self.filtered
                self.dictified = self.dictify_query(self.filtered, clientRoot)
                return self.dictified 
                
        except Exception as e:
            pass

    def dictify_query(self, rec, clientRoot):
        """
        Return a json dictionary.
        """
        try:
            self.D = {}
            #print rec 
            for details in rec:
                self.D["Surname"]= details.client_details.surname
                self.D["Firstname"]= details.client_details.firstname
                self.D["Business"]= details.client_details.business_name 
                self.D["BusinessDetails"]=details.client_details.business_name + "  " + clientRoot
                self.D["ClientRoot"]= str(clientRoot)
            #print "Details ", self.D
            return self.D
        except:
            raise
            
class SearchDetailedInformation(View):
    @method_decorator(login_required)
    def get(self, request):
        #if(request.is_ajax()):
        try:
            self.clientRoot = request.GET.get("clientRoot")
            self.json_dict = self.filter_client_records(self.clientRoot)
            #print "JSONED ", self.json_dict
            try:
                return HttpResponse(simplejson.dumps(self.json_dict), content_type="application/json")
            except:
                raise
        except:
            raise 
        #else:
        #    return HttpResponse("It's not ajax")

    def filter_client_records(self, clientRoot):
        """
        Search all the clients records.
        """
        self.GEN_DICT = {}
        try:
            self.filtered = datamodels.CREDIT_APPLICATION.objects.filter(Client_Number=clientRoot)
            if(len(self.filtered) > 1):
                self.dictified = self.dictify_query(self.filtered)
                self.GEN_DICT["CBA_Accounts"]=self.dictified
                self.INFO = self.dictify_query_name(self.filtered, clientRoot)
                self.GEN_DICT["Client_Infor"]=self.INFO
                return self.GEN_DICT 
            else:
                self.dictified = self.dictify_query(self.filtered)
                self.GEN_DICT["CBA_Accounts"]=self.dictified
                self.INFO = self.dictify_query_name(self.filtered, clientRoot)
                self.GEN_DICT["Client_Infor"]=self.INFO
                return self.GEN_DICT 
                
        except Exception as e:
            pass

    def dictify_query(self, CBA):
        """
        Return a json dictionary.
        """
        try:
            self.D = {}
            #print rec
            for cba in CBA:
                self.all_cba = cba.creditborroweraccount_set.all()
                for rec in self.all_cba:
                    self.D[rec.get_all()]=rec.id
                return self.D
        except:
            raise

    def dictify_query_name(self, rec, clientRoot):
        """
        Return a json dictionary.
        """
        try:
            self.names = {}
            #print rec 
            for details in rec:
                #print "S ", details.client_details.surname, "F ", details.client_details.firstname, "B ", details.client_details.business_name
                self.names["Surname"]= details.client_details.surname
                self.names["Firstname"]=details.client_details.firstname
                self.names["Business"]= details.client_details.business_name 
                self.names["BusinessDetails"]=details.client_details.business_name + "  " + clientRoot
                self.names["ClientRoot"]= str(clientRoot)
            #print "Details ", self.D
            return self.names
        except:
            raise
