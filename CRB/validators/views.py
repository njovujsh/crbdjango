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
from CRB import settings 
from creditanalysis import models as analysismodel 
from creditanalysis.subsystem import  dataplot 
import os
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

mytitle = "Swirling Credit System"

def get_allsettings():
    return branchmodel.DefaultHeaders.objects.all()
    
def get_datarecords():
    """
    Return all available dataset records.
    """
    try:
        return record_models.Dataset.objects.all()
    except:
        raise


class ValidationRules(View):
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


class BeginValidation(View):
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
            self.template = self.load_rules_template("beginvalidation.html")
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


class SuccessfulValidation(View):
    @method_decorator(login_required)
    def get(self, request):
        try:
            if(request.is_ajax()):
                self.data = {}
                self.dataset = request.GET.get('validationsdataset')
                self.ret =  self.load_report_record(self.dataset).objects.all()
                self.date_dict = self.contruct_dict(self.ret)
                self.data["recordsbydate"]=self.date_dict
                try:
                    return HttpResponse(simplejson.dumps(self.data), content_type="application/json")
                except:
                    raise 
            else:
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

    
    def contruct_dict(self, records):
        """
        Construct and return a dictionary.
        """
        FORMAT  = "%Y-%m-%d-%H-%M-%S"
        self.record_dict = {}
        for r in records:
            self.record_dict[r.id]=r.validation_date.strftime(FORMAT)
        return self.record_dict
        
    def load_report_record(self, model):
        try:
            return loadreportmodels.load_report_model_(model)
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
            self.template = self.load_rules_template("successfulvalidation.html")
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

class FailedValidation(View):
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
            self.template = self.load_rules_template("failedvalidation.html")
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



class ValidateDatesetsAJAX(View):
    @method_decorator(login_required)
    def get(self, request):
        try:
            self.dataset = self.get_v_dataset(request)
            #print "GOT RECORD ", self.dataset
            self.count = self.load_module_counts(self.dataset)
            #print "RETURNED ", self.count 
            self.allenforcements = loadcodes.ret_all_joined(loadcodes.get_set_code(self.dataset))
            self.dict_value = {"Records to be validated": "Validating:  %s" % self.dataset,
                                "Count": "Record Total: %d" % int(self.count),
                               "enforcements":self.allenforcements}
            try:
                try:
                    return HttpResponse(simplejson.dumps(self.dict_value), content_type="application/json")
                except:
                    raise
                else:
                    return HttpResponse(simplejson.dumps({"Invalid Records":False}), content_type="application/json")
            except:
                raise
        except:
            raise

    def get_v_dataset(self, request):
        try:
            return request.GET.get("validationsdataset", "")
        except:
            raise


    def load_module_counts(self, dataset):
        try:
            #print "MODULE IS HERE ", dataset 
            return loadvalidationmodule.load_modules(dataset)
        except:
            raise

    @method_decorator(login_required)
    def post(self, request):
        try:
            self.dataset = request.POST.get("datasetselected", "")
            
            if(len(self.dataset) >=5):
                self._csv_module = self.load_csv_validated_module(self.dataset)
                self.model = self.load_module_modules(self.dataset)
                self.records = self.load_records_in_model(self.model)
                self.validation_code = self.load_validation_code(self.dataset)
                
                #grab the headers
                #self.h = self.load_headers()
                self.h = self.load_headers_from_settings()
                #self.lheaders = self.append_headers_to_list(self.h)
                self.lheaders = self.append_headers_to_list_fromsettings(self.h)
                
                self.ret = self.make_validation_report(self.records, self.validation_code, self.dataset, self.h)
                
                #self.outputname = self.load_filenames(self.h.pi_identification_code, self.dataset)
                #self.csvfile = self.write_csv(self.outputname, self.records, self._csv_module, self.validation_code, self.lheaders)
                if(self.ret):
                    try:
                        #self.path = "/creport/instantview/%s/"% str(self.dataset)
                        self.path = "/validation/recentvalidation/successful/" #% str(self.dataset)
                        #return HttpResponse(self.path) #self.csvfile
                        return HttpResponseRedirect(self.path) #self.csvfile
                    except:
                        raise
                else:
                    return HttpResponse("FAILURE")
            else:
                self.template = loader.get_template("beginvalidation.html")
                self.datasetrecords = get_datarecords()
                self.context = RequestContext(request, {"basetitle":"Missing dataset","datasetrecords":self.datasetrecords,
                                                        "records_to_search":"Rules", "verrors":"Missing dataset please select"
                                                        })
                return HttpResponse(self.template.render(self.context))
        except Exception as e:
            self.template = loader.get_template("beginvalidation.html")
            self.datasetrecords = get_datarecords()
            print "Some errors here ", e.args, e.message
            self.context = RequestContext(request, {"basetitle":mytitle,"datasetrecords":self.datasetrecords,
                                                   "records_to_search":"Rules", "verrors":e
                                                    })
            return HttpResponse(self.template.render(self.context))
            
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
            return loadreporting.load_modules(dataset)
        except:
            raise

    def write_csv(self, outputname, records, csv_module, validation_code, lheaders):
        try:
            self.ret_csv = csv_module(filename=outputname, dialect=None,row=lheaders, headers=lheaders, delimiter="|")
            self.validated_file = self.ret_csv.write_row_data(records, validation_code)
            return self.validated_file
        except:
            raise

    def load_headers(self, ID=1):
        try:
            self.hlists = []
            self.all_hsettings = branchmodel.DefaultHeaders.objects.all()
            for setting in self.all_hsettings:
                self.hlists.append(setting.id)
            if(self.hlists):
                return branchmodel.DefaultHeaders.objects.get(id=min(self.hlists))
            #return datamodels.RequiredHeader.objects.get(id=ID)
        except:
            raise

    def append_headers_to_list(self, headers):
        self.hlist = []
        self.hlist.append(headers.default_headers.header)
        self.hlist.append(headers.default_headers.pi_identification_code)
        self.hlist.append(headers.default_headers.institution_name)
        self.hlist.append(headers.default_headers.submission_date.replace("-", "", len(headers.default_headers.submission_date)))
        self.hlist.append(headers.default_headers.version_number)
        self.hlist.append(headers.default_headers.creation_date.replace("-", "", len(headers.default_headers.creation_date)))
        return self.hlist
        
    def append_headers_to_list_fromsettings(self, headers):
        self.hlist = []
        self.hlist.append(headers.header)
        self.hlist.append(headers.pi_identification_code.pi_identification_code)
        self.hlist.append(headers.pi_identification_code.insitution_Name)
        self.hlist.append(headers.submission_date.replace("-", "", len(headers.submission_date)))
        self.hlist.append(headers.version_number)
        self.hlist.append(headers.creation_date.replace("-", "", len(headers.creation_date)))
        return self.hlist

    def load_headers_from_settings(self, by_branch_id=None):
        try:
            if(by_branch_id):
                return branchmodel.RequiredHeader.objects.get(branch_code=by_branch_id)
            else:
                return branchmodel.RequiredHeader.objects.get(branch_code=settings.BRANCH_IDENTIFICATION_CODE)
        except:
            raise
            
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
    
    def make_validation_report(self, model, validation_module, dataset, headers=None):
        """
        Create a validation Report.
        """
        self.reporter = reportstatus.ReportStatus(model_data=model)
        self.report_model = loadreportmodels.load_report_model_module(dataset)
        
        self.dataset_name = datasetmatch.load_file_extension(dataset)
        
        if(self.reporter and self.report_model):
            try:
                validation_module.begin_validation()
                self.validation_result = validation_module.get_real_passed()
                
                #print self.validation_result
                self.reporter.analyse_failed_passed(self.validation_result)
                #print "PASSED FIELDS ", self.reporter.get_passed()
                #print "FAILED FIELD ", self.reporter.get_failed()
                #print "TOTAL COUNT ", self.reporter.get_data_count()
                validation_module.analysis_records()
                #print "PASSED RECORDS ", validation_module.get_passed_records()
                #print "FAILED RECORDS ", validation_module.get_failed_records()
                #print validation_module.get_passed_by_id()
                self.save_status = self.save_report_results(self.report_model, self.reporter, validation_module, self.dataset_name, headers)
                if(self.save_status):
                    #return self.save_status
                    self.analysed = self.plot_graph(validation_module, self.reporter, self.dataset_name)
                    if(self.analysed):
                        return self.save_status
                    else:
                        return False 
                else:
                    return self.save_status
                return True
            except:
                raise 
        else:
            return False 
            
    def plot_graph(self, v_module, reporter, datasetname):
        self.model = analysismodel.SuccessFullFailedGraph()
        self.analysis_plot = dataplot.PlotValidatedRecords()
        self.date = datetime.datetime.now()
        self.FORMAT  = "%Y-%m-%d-%H-%M-%S-%w"
        try:
            self.name = "Graphed Analysis for Record [ %s ] " % datasetname
            self.format_time = self.date.strftime(self.FORMAT)
            self.saving_name = datasetname + self.format_time
            
            self.savename = os.path.join(settings.IMAGE_UPLOAD_PATH, self.saving_name)
            self.analysis_plot.set_label(["Total Number of Records", "Successful Validations", "Unsuccessful Validations"])
            self.analysis_plot.set_record([reporter.get_data_count(), v_module.get_passed_records(), v_module.get_failed_records()])
            self.savename = self.savename + ".png"
            self.analysis_plot.set_savepath(self.savename)
            self.analysis_plot.set_title(self.name)
            self.analysis_plot.plot_pie()
            #Save now in the models
            self.model.graph_image = self.analysis_plot.get_savepath()
            self.model.record_type = str(datasetname)
            self.model.imagename = str(self.saving_name)
            self.model.save()
        except:
            raise 
        else:
            return True 
        
    def save_report_results(self, model, reporter, validation_module, dataset_name,headers):
        """
        Save the reporting to the database.
        """
        try:

            #print "Data count", reporter.get_data_count()
            #print "Passed Records", validation_module.get_passed_records()
            #print "Field Records.", validation_module.get_failed_records()
            #print "Passed Fields.", reporter.get_passed()
            #print "Failed Fields.", reporter.get_failed()

            if(model and reporter and validation_module):
                model.total_records = reporter.get_data_count()
                model.successful_records = validation_module.get_passed_records()
                model.failed_records = validation_module.get_failed_records()
                model.number_of_fields_passed = reporter.get_passed()
                model.number_of_fields_failed = reporter.get_failed()
                model.record_type = dataset_name
                model.validation_date = time.asctime()
                
                if(headers):
                    model.pi_name = headers.pi_identification_code
                if(model):
                    try:
                        #print "Saving records", model 
                        model.save()
                    except:
                        raise 
                    else:
                        return True 
            else:
                return None 
        except:
            raise 
        else:
            return True 
            
                
class ValidateDatesets(View):
    @method_decorator(login_required)
    def get(self, request):
        try:
            if(self.validate_code):
                self._csv_module = self.load_csv_validated_module(self.dataset)
                self.model = self.load_module_modules(self.dataset)
                self.records = self.load_records_in_model(self.model)
                self.validation_code = self.load_validation_code(self.dataset)

                #grab the headers
                self.h = self.load_headers()
                self.lheaders = self.append_headers_to_list(self.h)
                self.filename = self.load_filenames(self.h.pi_identification_code, record_slug)
                
                self.csvfile = self.write_csv(self.records, self._csv_module, self.validation_code, self.lheaders)

                try:
                    return self.csvfile
                except:
                    raise
            else:
                return HttpResponse("FAILURE ")
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

    def write_csv(self, records, csv_module, validation_code, lheaders):
        try:
            self.ret_csv = csv_module(filename="ValidatedRecords.csv", dialect=None,row=lheaders, headers=lheaders,delimiter="|")
            self.validated_file = self.ret_csv.write_row_data(records, validation_code)
            return self.validated_file
        except:
            raise

    def load_headers(self, ID=1):
        try:
            return datamodels.RequiredHeader.objects.get(id=ID)
        except:
            raise

    def append_headers_to_list(self, headers):
        self.hlist = []

        self.hlist.append(headers.header)
        self.hlist.append(headers.pi_identification_code.pi_identification_code)
        self.hlist.append(headers.pi_identification_code.institution_name)
        self.hlist.append(headers.submission_date.replace("-", "", len(headers.submission_date)))
        self.hlist.append(headers.version_number)
        self.hlist.append(headers.creation_date.replace("-", "", len(headers.creation_date)))
        return self.hlist
    
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

class ImportRecords(View):
    @method_decorator(login_required)
    def get(self, request, record_slug):
        try:
            try:
                self.val_module =  self.load_validation_module(record_slug)
            except:
                pass 
            else:
                self.load_csv_module = self.load_dataset_csv(record_slug)
                self.models = self.load_module_modules(record_slug.upper())
                self.allrecords = self.load_records_in_model(self.models)
                #self.load_records_in_model(self.load_module_modules(record_slug))
                
                self.h = self.load_headers()
                self.hs = self.append_headers_to_list(self.h)
                self.filename = self.load_filenames(self.h.pi_identification_code, record_slug)
                self.extension = self.dataset = datasetmatch.load_file_extension(record_slug)
                
                self.hs.append(self.extension)
                self.ret = self.write_csv(self.filename, self.allrecords , self.hs, self.load_csv_module)
                return self.ret
        except:
            pass 

    def load_dataset_csv(self, dataset):
        try:
            return loadcsvmodules.load_csv_module(dataset)
        except:
            raise

    def load_module_modules(self, record_slug):
        """
        Load the given module.
        """
        try:
            if(record_slug):
                return loadmodels.load_model_module(record_slug.upper())
            else:
                return False
        except:
            raise

    def load_records_in_model(self, model):
        try:
            return loadmodels.load_all_data(model)
        except:
            raise

    def load_validation_module(self, dataset):
        try:
            return loadvalidationmodule.load_modules(dataset.replace("_", " ", len(dataset)))
        except:
            raise

    def load_validation_status(self, validated_dict):
        try:
            return validationstatus.validation_status(validated_dict)
        except:
            pass

    def write_csv(self, outputname, model, headers, csvmodule):
        try:
            self.csvmodule = csvmodule(outputname,  None, row=headers, headers=headers, delimiter="|")
            self.ret = self.csvmodule.write_row_data(model)
            return self.ret
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
        self.hlist.append(headers.submission_date.replace("-", "", len(headers.submission_date)))
        self.hlist.append(headers.version_number)
        self.hlist.append(headers.creation_date.replace("-", "", len(headers.creation_date)))
        return self.hlist
        
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

class ValidateAndImport(View):
    @method_decorator(login_required)
    def get(self, request, record_slug):
        try:
            try:
                try:
                    self.val_module =  self.load_validation_module(record_slug)
                except:
                    raise
                else:
                    self._csv_module = self.load_csv_validated_module(record_slug)
                    self.models = self.load_module_modules(record_slug.upper())
                    self.allrecords = self.load_records_in_model(self.models)

                    self.h = self.load_headers()
                    self.lheaders = self.append_headers_to_list(self.h)
                    self.filename = self.load_filenames(self.h.pi_identification_code, record_slug)
                    self.extension = datasetmatch.load_file_extension(record_slug)
                    self.lheaders.append(self.extension)
                    
                    self.retcsvs = self.write_v_csv(self.filename, self.allrecords, self._csv_module,
                                                    self.val_module, self.lheaders)
                    return self.retcsvs 
            except:
                raise
        except:
            raise

    def load_validation_code(self, dataset):
        try:
            return loadvalidationmodule.load_modules(dataset)
        except:
            raise

    def load_module_modules(self, record_slug):
        """
        Load the given module.
        """
        try:
            if(record_slug):
                return loadmodels.load_model_module(record_slug.upper())
            else:
                return False
        except:
            raise

    def load_validation_module(self, dataset):
        try:
            return self.load_validation_code(dataset.replace("_", " ", len(dataset)))
        except:
            raise

    def load_validation_status(self, validated_dict):
        try:
            return validationstatus.validation_status(validated_dict)
        except:
            pass

    def load_records_in_model(self, model):
        try:
            return loadmodels.load_all_data(model)
        except:
            raise

    def load_csv_validated_module(self, dataset):
        try:
            return loadcsvmodules.load_csv_validated_module(dataset.upper())
        except:
            raise

    def write_v_csv(self, outputname, model_record, csvwriter, validator, headers):
        try:
            #print "PI ", csvwriter
            self.csv = csvwriter(outputname, "|", row=headers, headers=headers)
            self.retcsv = self.csv.write_row_data(model_record, validator)
            return self.retcsv
        except:
            raise

    def load_headers(self, by_branch_id=None):
        try:
            if(by_branch_id):
                return branchmodel.RequiredHeader.objects.get(branch_code=by_branch_id)
            else:
                return branchmodel.RequiredHeader.objects.get(branch_code=settings.BRANCH_IDENTIFICATION_CODE)
        except:
            raise

    def append_headers_to_list(self, headers):
        self.hlist = []

        self.hlist.append(headers.header)
        self.hlist.append(headers.pi_identification_code.pi_identification_code)
        self.hlist.append(headers.pi_identification_code.insitution_Name)
        self.hlist.append(headers.submission_date.replace("-", "", len(headers.submission_date)))
        self.hlist.append(headers.version_number)
        self.hlist.append(headers.creation_date.replace("-", "", len(headers.creation_date)))
        return self.hlist
        
    def load_filenames(self, pi_code, dataset):
        """
        Load and return the filename.filenaming
        """
        try:
            self.dataset = datasetmatch.load_file_extension(dataset)
            if(self.dataset):
                self.filenames = filenaming.make_filename(pi_code=pi_code, filename=self.dataset)
                print "HERE WE ARE ", self.filenames, self.dataset, pi_code, dataset 
                return self.filenames
            else:
                return False 
        except:
            raise 
