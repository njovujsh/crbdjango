from django.shortcuts import render
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
from subsystems import csvhandler
from reportlab.pdfgen import canvas
import datetime
import time
from django.forms.models import inlineformset_factory
import importlib
from datasets import models as field_records
from datasetrecords import models as record_models
from datasets import models as set_models
from datasetrecords import models as datamodels
from datasetrecords import forms as dataset_forms
from processrecords import models as processmodels
from validators.subsystems.csvwriters import loadcsvmodules
from validators.subsystems import loadvalidationmodule
from datasetrecords import loadmodels
from processrecords.subsystems import filenaming
from processrecords.subsystems import datasetmatch
from processrecords.subsystems import excelreader
from processrecords.subsystems import csvread 

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datasetrecords import legacyimport
#from import_export import resources
mytitle = "Swirling Credit System"
from processrecords import forms as processforms
from processrecords import models as processmodels
from processrecords import  legacyinsert
import os
from CRB import settings
from branchcode import models as branchmodel
from branchcode import forms as branchforms

class GetVersionNumber(View):
    @method_decorator(login_required)
    def get(self, request):
        try:
            self.template = loader.get_template("versionselect.html")
            self.dssh = self.load_dss_headers()
            self.datasetrecords = self.get_datarecords()

            self.contexts = RequestContext(request, {"dssh":self.dssh, "datasetrecords":self.datasetrecords,"basetitle":mytitle,
                                                     "customtitle":"Select corresponding version",
                                                  "versions":self.dssh
                                             })
            self.render = self.template.render(self.contexts)
            return HttpResponse(self.render)
        except:
            raise

    def load_dss_headers(self):
        try:
            self.dssh = branchmodel.RequiredHeader.objects.all()
            return self.dssh
        except:
            raise

    def get_datarecords(self):
        """
        Return all available dataset records.
        """
        try:
            return field_records.Dataset.objects.all()
        except:
            raise


class GetSelectedVersion(View):
    @method_decorator(login_required)
    def post(self, request):
        try:
            try:
                try:
                    self.header_id = request.POST.get("file_identifier", "")
                    try:
                        self.redirect_path = "/processing/data/existing/byID/%d/" % int(self.header_id)
                    except ValueError as error:
                        self.msg = "ERROR verifying selected headers [ %s ] Its considered invalid" % str(self.header_id)
                        self.render_error = self.render_error(request, self.msg, self.header_id)
                        return HttpResponse(self.render_error)
                    else:
                        return HttpResponseRedirect(self.redirect_path)
                except Exception as e:
                    self.msg = "ERROR: %s " % e.message
                    return HttpResponse(self.render_error(request, self.msg, "ERROR"))
            except Exception as e:
                 self.msg = "ERROR: %s " % e.message
                 return HttpResponse(self.render_error(request, self.msg, "ERROR"))
        except Exception as e:
            self.msg = "ERROR: %s " % e.message
            return HttpResponse(self.render_error(requst, self.msg, "ERROR"))

    def get_header_byID(self, header_id):
        try:
            if(header_id):
                self.headers = branchmodel.RequiredHeader.objects.get(id=int(header_id))
                if(self.headers):
                    return self.headers
                else:
                    return None
            else:
                return False
        except:
            raise

    def get_updateform(self):
        try:
            return branchforms.DatasetRecordForms
        except:
            raise

    def get(self, request, headerID):
        try:
            self.template = self.get_processing_template()
            if(self.template):
                self.rendered = self.process_context(request, self.template, headerID)
                if(self.rendered):
                    return HttpResponse(self.rendered)
                else:
                    return HttpResponseServerError("Failure")
            else:
                return HttpResponseServerError("FAILED")
        except:
            raise

    def get_processing_template(self, *template):
        try:
            if(template):
                return loader.get_template(template)
            else:
                return loader.get_template("dataprocessingview.html")
        except:
            raise

    def render_error(self, request, error_msg, result):
        try:
            self.template = loader.get_template("versionselect.html") # self.get_processing_template()
            try:
                self.datasetrecords = self.get_datarecords()
                self.headerforms = self.get_updateform()
                self.headers = branchmodel.RequiredHeader.objects.all()
                self.context = RequestContext(request, {"datasetrecords":self.datasetrecords,
                                                         "basetitle":mytitle, "customtitle":"Processing Records",
                                                         "herrors":error_msg, "result":result, "versions":self.headers
                                                    })
                return self.template.render(self.context)
            except:
                raise
        except:
            raise

    def get_form_instance(self, headerform, headerID):
        try:
            if(headerform and headerID):
                try:
                    return headerform(instance=self.get_header_byID(int(headerID)))
                except:
                    raise
            else:
                return False
        except:
            raise


    def process_context(self, request, template, headerID):
        try:
            if(template):
                try:
                    self.datasetrecords = self.get_datarecords()
                    self.headerforms = self.get_updateform()
                    self.formset = self.get_form_instance(self.headerforms, headerID)
                    self.context = RequestContext(request, {"forms":self.formset, "datasetrecords":self.datasetrecords,
                                                             "basetitle":mytitle, "customtitle":"Processing Records"
                                                                 })
                    return template.render(self.context)

                except Exception as e:
                    self.datasetrecords = self.get_datarecords()
                    self.headerforms = self.get_updateform()
                    self.headers = record_models.RequiredHeader.objects.all()
                    self.context = RequestContext(request, {"datasetrecords":self.datasetrecords,
                                                  "basetitle":mytitle, "herrors":e.message, "customtitle":"Processing Records",
                                                  "versions":self.headers
                                                  })
                    self.template = loader.get_template("versionselect.html")
                    return HttpResponse(self.template.render(self.context))
            else:
                self.datasetrecords = self.get_datarecords()
                self.headers = record_models.RequiredHeader.objects.all()
                self.context = RequestContext(request, {"datasetrecords":self.datasetrecords,
                            "basetitle":mytitle, "herrors":"Unable to load templates", "customtitle":"Processing Records",
                                "versions":self.headers
                              })
                self.template = loader.get_template("versionselect.html")
                return HttpResponse(self.template.render(self.context))
        except Exception as e:
                self.datasetrecords = self.get_datarecords()
                self.headers = branchmodel.RequiredHeader.objects.all()
                self.context = RequestContext(request, {"datasetrecords":self.datasetrecords,
                                                     "basetitle":mytitle, "herrors":e.message, "customtitle":"Processing Records",
                                                     "versions":self.headers
                                                     })
                self.template = loader.get_template("versionselect.html")
                return HttpResponse(self.template.render(self.context))

    def get_datarecords(self):
        """
        Return all vailable dataset records.
        """
        try:
            return field_records.Dataset.objects.all()
        except:
            raise

class ProcessOutput(View):
    def get(self, request):
        try:
            return HttpResponseRedirect("/home/dashboard/")
        except:
            return HttpResponse("FAILED")

    def get_datarecords(self):
        """
        Return all vailable dataset records.
        """
        try:
            return field_records.Dataset.objects.all()
        except:
            raise

    @method_decorator(login_required)
    def post(self, request):
        """
        Process the post request.
        """
        self.template = loader.get_template("dataprocessingview.html")
        try:
            self.headers = request.POST.get("header", "")
            self.pi_code = request.POST.get("pi_identification_code", "")
            self.insitution_name = request.POST.get("institution_name","")
            self.sub_date = request.POST.get("submission_date", "")
            self.version = request.POST.get("version_number" "")
            self.creation_date = request.POST.get("creation_date", "")
            
            self.query_picode =  self.query_PIIdentificationCode(self.pi_code)
            
            self.outputformat = request.POST.get("outputformat", "")
            self.sub_date = self.sub_date.replace("-", "", len(self.sub_date))
            
            self.validated = request.POST.get("validated")
            self.dataset = request.POST.get("dataset", "")
            self.dataset = self.dataset.replace(" ", "_", len(self.dataset)).lower()
            self.extension = datasetmatch.load_file_extension(self.dataset)
            self.data_headers = [self.headers, self.pi_code, self.insitution_name, self.sub_date,self.version,self.creation_date.replace('-',"", len(self.creation_date)), self.extension]

            if(self.first_validate(self.validated)):
                try:
                    #A request to first perform the validation of data.
                    self.data_validator = self.load_validation_module(self.dataset)
                    self.load_csv = self.load_csv_module(self.dataset)
                    self.model = self.load_model(self.dataset)
                    self.allrecords = self.load_records(self.model)

                    try:
                        self.filename = self.load_filenames(self.query_picode, self.dataset)
                        self.validated_csv = self.write_csv(self.filename, self.allrecords, self.load_csv, self.data_validator, self.data_headers)
                        if(self.validated_csv):
                            return self.validated_csv
                        else:#perrors
                            self.datasetrecords = self.get_datarecords()
                            self.context = RequestContext(request, {"perrors":"ERROR Processing request pliz report or try again with properly formated dadta",
                                                                "datasetrecords":self.datasetrecords,
                                                                })
                            return HttpResponse(self.template.render(self.context))
                    except Exception as e:

                        self.datasetrecords = self.get_datarecords()
                        self.context = RequestContext(request, {"perrors":e.message,
                                                            "datasetrecords":self.datasetrecords,
                                                            })
                        return HttpResponse(self.template.render(self.context))

                        raise
                         
                except Exception as e:


                    self.datasetrecords = self.get_datarecords()
                    self.context = RequestContext(request, {"perrors":e.message,
                                                        "datasetrecords":self.datasetrecords,
                                                        })
                    return HttpResponse(self.template.render(self.context))

                    raise 
            else:
                try:
                    self.model = self.load_model(self.dataset)
                    self.allrecords = self.load_records(self.model)
                    self.csvmodel = self.load_none_validated_csv(self.dataset)
                    self.filename = self.load_filenames(self.query_picode, self.dataset)
                    self.returned_csv = self.write_none_csv(self.filename, self.allrecords, self.csvmodel, headers=self.data_headers)
                    if(self.returned_csv):
                        return self.returned_csv
                    else:
                        self.datasetrecords = self.get_datarecords()
                        self.context = RequestContext(request, {"perrors":"ERRO performing processing",
                                                            "datasetrecords":self.datasetrecords,
                                                            })
                        return HttpResponse(self.template.render(self.context))
                except Exception as e:
                    '''
                    self.datasetrecords = self.get_datarecords()
                    self.context = RequestContext(request, {"perrors":e.message,
                                                        "datasetrecords":self.datasetrecords,
                                                        })
                    return HttpResponse(self.template.render(self.context))
                    '''
                    raise 
        except Exception as e:

            self.datasetrecords = self.get_datarecords()
            self.context = RequestContext(request, {"perrors":e.message,
                                                "datasetrecords":self.datasetrecords,
                                                })
            return HttpResponse(self.template.render(self.context))

            raise 
    def load_none_validated_csv(self, dataset):
        try:
            return loadcsvmodules.load_csv_module(dataset)
        except:
            raise

    def load_dataset_csv(self, dataset):
        try:
            return loadcsvmodules.load_csv_module(dataset)
        except:
            raise

    def load_validation_module(self, dataset):
        try:
            return loadvalidationmodule.load_modules(dataset.upper())
        except:
            raise

    def load_records(self, model):
        try:
            return loadmodels.load_all_data(model)
        except:
            raise

    def load_csv_module(self, dataset):
        try:
            return loadcsvmodules.load_csv_validated_module(dataset)
        except:
            raise

    def load_model(self, dataset):
        try:
            return loadmodels.load_model_replace_underscore(dataset)
        except:
            raise

    def write_csv(self, outputname, records, csvwriter, validationmodule, headers):
        try:
            self.csv = csvwriter(filename=outputname, dialect=None,row=headers, headers=headers,delimiter="|")
            self.writtencsv = self.csv.write_row_data(records, validationmodule)

            if(self.writtencsv):
                return self.writtencsv
            else:
                return False
        except:
            raise


    def write_none_csv(self, outputname, records, csvwriters, headers):
        try:
            self.csvw = csvwriters(outputname, None, delimiter="|", row=headers, headers=headers)
            self.retcsv = self.csvw.write_row_data(records)
            if(self.retcsv):
                return self.retcsv
            else:
                return NOne
        except:
            raise

    def first_validate(self, validated):
        """
        Check if we first have to validated the records.
        """
        try:
            if(validated == "True"):
                return True
            else:
                return False
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

    def query_PIIdentificationCode(self, ID):
        try:
            return branchmodel.PIIdentificationCode.objects.get(id=int(ID))
        except:
            raise
            
class ExtractedSheets(View):
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
            return loader.get_template("displayprocessed.html")
        except:
            raise

    def render_context(self, request, template):
        try:
            self.all_files = processmodels.ExcelSheets.objects.all()
            self.mfiles =  self.parse_model_fields(processmodels.ExcelSheets)
            self.file_count = processmodels.ExcelSheets.objects.all().count()
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
                                                        "count":self.file_count, "datasetrecords":self.datasetrecords,
                                                        "displaytimes":self.now, 'basetitle':mytitle,
                                                        "customtitle":"Uploaded Files"
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
            return set_models.Dataset.objects.all()
        except:
            raise

    def parse_model_fields(self, data):
        self.fields = [ ]
        self.mfields = data._meta.fields

        for model_fields in self.mfields:
                if(model_fields.name in self.fields):
                    pass
                else:
                    self.fields.append(model_fields.name.replace("_", " ", len(model_fields.name)))

        return self.fields

class InsertLegacyRecords(View):
    def get(self, request):
        pass

    @method_decorator(login_required)
    def post(self, request):
        try:
            self.fileform  = processforms.ExcelLegacyForms(request.POST, request.FILES)
            self.uploadedfilename = request.FILES.get("excel")
            self.import_to  = request.POST.get("importto")
            self.custom_list = []
            
            if(self.uploadedfilename):
                if(self.detect_filename(self.uploadedfilename.name, default=".xlsx")):
                    self.saved = self.fileform.save()
                    self.just_uploadedfile = self.get_savedfile(self.saved) #self.join_path(self.uploadedfilename.name)
         
                    if(os.path.exists(self.just_uploadedfile.excel.path)):
                        self.excel_reader = excelreader.ReadExcelXLSX(self.just_uploadedfile.excel.path, content_passed=False)
                        self.num_sheets =  self.excel_reader.get_num_sheets()
                        #for sheets in range(self.num_sheets):
                        self.num_rows = self.excel_reader.get_sheet_by_name(self.excel_reader.get_sheet_by_index(0)).nrows
                        
                        if(self.import_to == "credit_application"):
                            self.loadedmodels = loadmodels.load_model_replace_underscore(self.import_to)
                            self.legacy = legacyinsert.CPInsert(self.loadedmodels)
                            for n in range(self.num_rows):
                                if(n):
                                    self.row_data = self.excel_reader.get_row_values(0, n)
                                    try:
                                        self.legacy.filter_datainsert(self.row_data)
                                    except datamodels.CREDIT_APPLICATION.MultipleObjectsReturned:
                                        continue
                                    except:
                                        raise
                                         
                            self.path = self.make_view_path(self.import_to)
                            return HttpResponseRedirect(self.path)
                            
                        elif(self.import_to == "bouncedcheques"):
                            self.loadedmodels = loadmodels.load_model_replace_underscore(self.import_to)
                            
                            self.legacy = legacyinsert.BCInsert(self.loadedmodels, cpmodel=datamodels.CREDIT_APPLICATION)
                            
                            for n in range(self.num_rows):
                                if(n):
                                    self.row_data = self.excel_reader.get_row_values(0, n)
                                    try:
                                        self.legacy.filter_datainsert(self.row_data)
                                    except datamodels.CREDIT_APPLICATION.MultipleObjectsReturned:
                                        continue
                                    except:
                                        raise 
                                        #continue
                            self.path = self.make_view_path(self.import_to)
                            return HttpResponseRedirect(self.path)
                        
                        elif(self.import_to=="creditborroweraccount"):
                            self.loadedmodels = loadmodels.load_model_replace_underscore(self.import_to)
                            self.legacy = legacyinsert.CBAInsert(self.loadedmodels)
                            for n in range(self.num_rows):
                                if(n):
                                    self.row_data = self.excel_reader.get_row_values(0, n)
                                    try:
                                        self.legacy.filter_datainsert(self.row_data)
                                    except datamodels.CREDIT_APPLICATION.MultipleObjectsReturned:
                                        print "MUltile object returned"
                                        continue
                                    except:
                                        raise 
                                        #continue
                            self.path = self.make_view_path(self.import_to)
                            return HttpResponseRedirect(self.path)
                        else:
                            self.error = "Corresponding import record on %s is not supported " % self.import_to
                            return HttpResponse(self.error)
                            
                    else:
                        self.path = self.make_view_path(self.import_to)
                        return HttpResponseRedirect(self.path)
                        
                elif(self.detect_filename(self.uploadedfilename.name, default=".csv")):
                    self.saved = self.fileform.save()
                    self.just_uploadedfile = self.get_savedfile(self.saved) #self.join_path(self.uploadedfilename.name)
                    
                    if(os.path.exists(self.just_uploadedfile.excel.path)):
                        self.excel_reader = csvread.ReadCSV(self.just_uploadedfile.excel.path)
                        
                        if(self.import_to == "credit_application"):
                            self.loadedmodels = loadmodels.load_model_replace_underscore(self.import_to)
                            self.legacy = legacyinsert.CPInsert(self.loadedmodels)
                            
                            self.row_data = self.excel_reader.read_csvs()
                            for rows in self.row_data:
                                print "Row ", rows 
                                try:
                                    self.legacy.filter_datainsert(rows)
                                except datamodels.CREDIT_APPLICATION.MultipleObjectsReturned:
                                    continue 
                                except:
                                    raise
                                #else:
                            self.path = self.make_view_path(self.import_to)
                            return HttpResponseRedirect(self.path)
                            
                        elif(self.import_to == "bouncedcheques"):
                            self.loadedmodels = loadmodels.load_model_replace_underscore(self.import_to)
                            self.legacy = legacyinsert.BCInsert(self.loadedmodels, cpmodel=datamodels.CREDIT_APPLICATION)
                           
                            self.row_data = self.excel_reader.read_csvs()
                            for rows in self.row_data:
                                try:
                                    self.legacy.filter_datainsert(rows)
                                except datamodels.CREDIT_APPLICATION.MultipleObjectsReturned:
                                    continue   
                                except:
                                    raise 
                                    #continue
                                #else:    
                            self.path = self.make_view_path(self.import_to)
                            return HttpResponseRedirect(self.path)
                        
                        elif(self.import_to=="creditborroweraccount"):
                            self.loadedmodels = loadmodels.load_model_replace_underscore(self.import_to)
                            self.legacy = legacyinsert.CBAInsert(self.loadedmodels)
                            
                            self.row_data = self.excel_reader.read_csvs()
                            for rows in self.row_data:
                                try:
                                    self.legacy.filter_datainsert(rows)
                                except datamodels.CREDIT_APPLICATION.MultipleObjectsReturned:
                                    print "MUltile object returned"
                                    continue
                                except:
                                    raise 
                            self.path = self.make_view_path(self.import_to)
                            return HttpResponseRedirect(self.path)
                        else:
                            self.error = "Corresponding import record on %s is not supported " % self.import_to
                            self.template = self.load_template()
                            self.context = self.process_context(request, self.template, self.import_to, self.error)
                            return HttpResponse(self.context)
                else:
                    self.msg = "File you uploaded could be corrupt on invalid only (csv and excel allowed)."
                    self.template = self.load_template()
                    self.context = self.process_context(request, self.template, self.import_to, self.msg)
                    return HttpResponse(self.context)
            else:
                #set the error message session
                self.msg = "Import ERROR expected  file got none instead... please upload one"
                self.template = self.load_template()
                self.context = self.process_context(request, self.template, self.import_to, self.msg)
                return HttpResponse(self.context)

        except Exception as e: 
            #self.template = self.load_template()
            #self.context = self.process_context(request, self.template, self.import_to, e)
            #return HttpResponse(self.context)
            raise 
           

    def load_legacymodel(self, modelname):
        try:
            if(modelname):
                return loadmodels.load_model_module(modelname)
        except:
            raise

    def make_path(self, dataset):
        try:
            return "/app/process/datasetrecord/%s/" % str(dataset).lower()
        except:
            raise
            
    def make_view_path(self, dataset):
        try:
            return "/view/dataview/request/%s/" % str(dataset).lower()
        except:
            raise

    def get_picode(self, data):
        return data[0]

    def join_path(self, filename):
        storagepath = os.path.join(settings.MEDIA_ROOT, "legacyuploads")
        return os.path.join(storagepath, filename)

    def get_savedfile(self, saveobject):
        try:
            return processmodels.TemporaryExcelUploader.objects.get(id=saveobject.id)
        except:
            raise

    def search_header(self, code):
        if(code):
            return branchmodel.RequiredHeader.objects.get(pi_identification_code=code)
            
    def search_defaultheader(self, code):
        if(code):
            return branchmodel.DefaultHeaders.objects.get(Branch_Code=code)
            
    def search_clientnumber(self, clientnum):
        if(clientnum):
            return datamodels.CREDIT_APPLICATION.objects.get(Client_Number=clientnum)

    def get_clientnumberbyid(self, clientobj):
        if(clientobj):
            return datamodels.CREDIT_APPLICATION.objects.get(Client_Number=clientobj.id)
            
    def save_branchode(self, code):
        if(code):
            try:
                self.branchsaved = branchmodel.RequiredHeader(pi_identification_code=code)
                self.branchsaved.save()
                return self.branchsaved
            except:
                raise
                
    def save_defaultbranchode(self, code):
        if(code):
            try:
                self.branchsaved = branchmodel.DefaultHeaders(Branch_Code=code)
                self.branchsaved.save()
                return self.branchsaved
            except:
                raise

    def detect_filename(self, filetype, default=".csv"):
        try:
            if(filetype.endswith(default)):
                return True
            else:
                return False
        except:
            raise
            
    def get_gscafb(self):
        self.gs = datamodels.GSCAFB_INFORMATION()
        self.gs.save()
        return self.gs

    def get_idi(self):
        self.ie = datamodels.IDENTIFICATION_INFORMATION()
        self.ie.save()
        return self.ie

    def get_employerinfo(self):
        self.info = datamodels.EMPLOYMENT_INFORMATION()
        self.info.save()
        return self.info

    def get_sci(self):
        self.sci = datamodels.SCI()
        self.sci.save()
        return self.sci

    def get_pci(self):
        self.pci = datamodels.PCI()
        self.pci.save()
        return self.pci

    def process_context(self, request, template, dataset_slug, errormsg):
        try:
            if(template):
                self.datasetforms = self.load_forms_by_slug(dataset_slug)
                self.pciforms = self.get_PCIForms()
                self.sciforms = self.get_SCIForms()
                self.gscafbforms = self.get_GSCAFBForms()
                self.idforms = self.get_IDForms()
                self.getieforms = self.get_EIForms()
                self.clientform = self.get_clientforms()
                
                self.process_forms = processforms.ExcelLegacyForms()
                self.datasetrecords = self.get_datarecords()
                self.data_rights = None
                self.userdetails = self.load_user_creds(request)
                
                if(self.userdetails == True):
                    pass
                else:
                    self.data_rights = self.userdetails.data_access_rights.all()
                    
                self.context  = RequestContext(request, {"datasetforms":self.datasetforms,"datasetrecords":self.datasetrecords,
                                                        "datasetinput":dataset_slug.upper().replace("_", " ", len(str(dataset_slug))),
                                                        "pciforms":self.pciforms,"sciforms":self.sciforms, "dataset_active":dataset_slug,
                                                        "gscafbforms":self.gscafbforms, "idforms":self.idforms,
                                                        "ieforms":self.getieforms, "userrights":self.data_rights, "fileimporterror":errormsg,
                                                        "process_forms":self.process_forms, "clientform":self.clientform
                                                        })

                return template.render(self.context)
            else:
                return None
        except:
            raise

    def load_forms_by_slug(self, record_info):
        """
        Return the forms which will be used.
        """
        try:
            if(record_info.upper() == "COLLATERAL_MATERIAL_COLLATERAL"):
                return dataset_forms.CMC_Forms(prefix="standard_forms")
            elif(record_info.upper() == "BORROWERSTAKEHOLDER"):
               return dataset_forms.BS_Forms(prefix="standard_forms")
            elif(record_info.upper() == "BOUNCEDCHEQUES"):
                return dataset_forms.BC_Forms(prefix="standard_forms")
            elif(record_info.upper() == "COLLATERAL_CREDIT_GUARANTOR"):
                return dataset_forms.CCG_Forms(prefix="standard_forms")
            elif(record_info.upper() == "CREDITBORROWERACCOUNT"):
                return dataset_forms.CBA_Forms(prefix="standard_forms")
            elif(record_info.upper() == "CREDIT_APPLICATION"):
                return dataset_forms.CAP_Forms(prefix="standard_forms")
            elif(record_info.upper() == "FINANCIAL_MALPRACTICE_DATA"):
                return dataset_forms.FRA_Forms(prefix="standard_forms")
            elif(record_info.upper() == "INSTITUTION_BRANCH"):
                return dataset_forms.IB_Forms(prefix="standard_forms")
            elif(record_info.upper() == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return dataset_forms.PIS_Forms(prefix="standard_forms")
            elif(record_info.upper() == "PARTICIPATING_INSTITUTION"):
                return dataset_forms.PI_Forms(prefix="standard_forms")
            else:
                return False
        except:
            raise

    def get_clientforms(self):
        return dataset_forms.ClientInformation_Forms(prefix="clientdetails")
        
    def get_PCIForms(self):
        return dataset_forms.PCIForms(prefix="PCI_Forms")

    def get_SCIForms(self):
        return dataset_forms.SCIForms(prefix="SCI_Forms")
    
    def get_GSCAFBForms(self, post=False):
        if(post):
            return dataset_forms.GSCAFBForms
        else:
            return dataset_forms.GSCAFBForms(prefix="GSCAFBForms")
        
    def get_IDForms(self, post=False):
        if(post):
            return dataset_forms.IDForms
        else:
            return dataset_forms.IDForms(prefix="IDForms")
        
    def get_EIForms(self, post=False):
        if(post):
            return dataset_forms.EIForms
        else:
            return dataset_forms.EIForms(prefix="EIForms")

    def get_datarecords(self):
        """
        Return all available dataset records.
        """
        try:
            return set_models.Dataset.objects.all()
        except:
            raise

    def load_user_creds(self, request):
        try:
            if(request.user.is_superuser):
                return True
            else:
                return usermodels.CreditInstitutionStaff.objects.get(username=request.user)
        except:
            raise

    def load_template(self, custom_template=None):
        try:
            if(custom_template):
                return loader.get_template(custom_template)
            else:
                return loader.get_template("datasetrecords.html")
        except:
            raise

                
