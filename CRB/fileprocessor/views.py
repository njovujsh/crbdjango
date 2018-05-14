from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.template import Context, loader, RequestContext
from fileprocessor import forms as fileforms 
import os
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
from fileprocessor import models as filemodels 
from fileprocessor import forms as fileforms 
from processrecords.subsystems import excelreader
from processrecords.subsystems import excelthreadhandler
from CRB import settings 
from processrecords import models as processmodels 
from fileprocessor.subsystems.exceptions import integrity 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

mytitle = "Upload file for processing"

class FileUploader(View):
    @method_decorator(login_required)
    def get(self, request):
        try:
            if(request.user.is_authenticated()):
                self.fileform = self.get_fileforms()
                self.template = self.get_template()
                self.rendered = self.context_handler(request, self.fileform, self.template)
                return HttpResponse(self.rendered)
            else:
                return HttpResponseRedirect("/")
        except:
            raise

    def get_template(self, *template):
        try:
            if(template):
                return loader.get_template(template)
            else:
                return loader.get_template("fileupload.html")
        except:
            raise

    def context_handler(self, request, form, template):
        try:
            #self.file_count = datamodels.FileUpload.objects.all().count()
            self.datasetrecords = self.get_datarecords()

            self.now = time.ctime()
            self.processed_context = RequestContext(request, {"fileform":form, #"count":self.file_count,
                                                    "displaytimes":self.now, "uploadtitle":"File uploading sub system",
                                                    "basetitle":mytitle,"datasetrecords":self.datasetrecords

                                                    })
            return template.render(self.processed_context)
        except:
            raise
            
    def get_fileforms(self):
        return fileforms.FileForms()
        
    def get_datarecords(self):
        """
        Return all available dataset records.
        """
        try:
            return record_models.Dataset.objects.all()
        except:
            raise
            
    @method_decorator(login_required)
    def post(self, request):
        try:
            if(request.user.is_authenticated()):
                if(request.method == "POST"):

                    self.file_being_uploaded = request.FILES
                    self.content_type = self.file_being_uploaded["uploaded_name"].content_type
                    self.content_size = self.file_being_uploaded["uploaded_name"].size
                    
                    self.users = filemodels.FileUploader(uploaded_by=request.user, content_type=self.content_type,
                                                        file_size=self.content_size
                                                        )
                    self.ret_form_status = fileforms.FileForms(request.POST, request.FILES, instance=self.users)
                    if(self.ret_form_status.is_valid()):
                        #file is saved
                        self.ret_form_status.save()
                        return HttpResponseRedirect("/file/display/success/url/upload")
                        
                    elif(self.ret_form_status.errors):

                        self.file_count = filemodels.FileUploader.objects.all().count()
                        self.left_navs = filemodels.FileUploader.objects.all()
                        self.datasetrecords = self.get_datarecords()
                        
                        return render_to_response("fileupload.html", {"fileform":self.ret_form_status, "count":self.file_count,
                                                                    "uploadtitle":"File uploading sub system",
                                                                    "basetitle":mytitle,"datasetrecords":self.datasetrecords
                                                                    },
                                                 context_instance=RequestContext(request))
                    else:
                        return HttpResponseServerError("An error occured while uploading file try again later.")
                   
                else:
                    return HttpResponseRedirect("/")
        except:
            raise
            

class DisplayFiles(View):
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
            return loader.get_template("filedisplay.html")
        except:
            raise

    def render_context(self, request, template):
        try:
            self.all_files = filemodels.FileUploader.objects.all()
            self.mfiles =  self.parse_model_fields(filemodels.FileUploader)
            self.file_count = filemodels.FileUploader.objects.all().count()
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
            self.refilter = self.filter_model_field(self.mfiles, "content type")
            self.our_context = RequestContext(request, {"file_headers":self.refilter, "availablefiles":self.page_obj,
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
            
    def filter_model_field(self, mfiles, types):
        l = []
        for m in mfiles:
            if m == types:
                pass 
            else:
                #print l
                l.append(m)
        return l
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

        for model_fields in self.mfields:
                if(model_fields.name in self.fields):
                    pass
                else:
                    #print model_fields.name 
                    self.fields.append(model_fields.name.replace("_", " ", len(model_fields.name)))

        return self.fields


class ProcessFiles(View):
    @method_decorator(login_required)
    def get(self, request, fileID):
        try:
            self.template = self.load_template()
            if(self.template):
                try:
                    #print "ID ", fileID
                    self.rendered = self.process_context(request, self.template, int(fileID))
                    if(self.rendered):
                        return HttpResponse(self.rendered)
                    else:
                        return HttpResponseServerError("Failure")
                except:
                    raise 
            else:
                return HttpResponseServerError("FAILURE")
        except:
            raise 
        
    def load_template(self, *templates):
        try:
            if(templates):
                return loader.get_template(templates)
            else:
                return loader.get_template("fileprocessing.html")
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
            
    def process_context(self, request, template, fid):
        try:
            if(template):
                self.datasetrecords = self.get_datarecords()
                self.loadfile = self.load_files_byid(fid)
                
                self.context = RequestContext(request, {"datasetrecords":self.datasetrecords,
                                                "file":self.loadfile, "process":"File processing action select"})
                return template.render(self.context)
            else:
                return False 
        except:
            raise 
             
    def load_files_byid(self, file_id):
        try:
            return filemodels.FileUploader.objects.get(id=int(file_id))
        except Exception as e:
            return HttpResponse(self.render_doesnot_exists(e) )
            
    @method_decorator(login_required)
    def post(self, request, fileID):
        try:
            self.formats = request.POST.get("outputformat", "")
            self.dataset = request.POST.get("dataset", "")
            
            try:
                self.filename = self.load_files_byid(int(fileID))
            except:
                raise 
            else:
                self.file_ret_status = self.process_file(request, self.filename.uploaded_name,  self.filename)
                if(self.file_ret_status == True):
                    return HttpResponseRedirect("/processing/displayprocessed/sheets/")
                else:
                    return HttpResponse(self.file_ret_status)
        except:
            raise 
        
    def process_file(self, request, filename, db_file_object):
        """
        Given the filename begin processing the file.
        """
        try:
            if(self.detect_filetype(filename.path)):
                if(self.is_file(filename.path)):
                    try:
                        self.reader = excelreader.ReadExcelXLSX(filename.path)
                        try:
                            self.numsheets = self.reader.get_num_sheets()
                            #print "Number of sheet ", self.numsheets
                            for i in range(self.numsheets):
                                #print "HERE ", i
                                self.task = excelthreadhandler.ExcelSheetReaderThread(self.reader, self.reader.get_sheet_by_name(self.reader.get_sheet_by_index(i)), 
                                                    self.reader.get_sheetname(self.reader.get_sheet_by_name(self.reader.get_sheet_by_index(i))),
                                                    i, settings.MEDIA_ROOT
                                                    )
                                self.task.start()
                                #print "PATH ", self.task.get_path()
                                self.status = self.save_sheet_in_database(self.task.get_path(), db_file_object)
                                if(self.status == True):
                                    return True  
                                else:
                                    return self.status 
                        except:
                            raise  
                    except:
                        raise 
                else:
                    print "Not file", filename.path 
            else:
                return HttpResponse(self.render_error(request, "Attempted file processing failed, Perhaps file not processable! or not excel"))
        except:
            raise 
                
                
    def render_error(self, request, errormsg):
        self.datasetrecords = self.get_datarecords()
        self.template = loader.get_template("filedisplay.html") 
        self.context = RequestContext(request, {"datasetrecords":self.datasetrecords, "ERROR":errormsg, "customtitle":"FAILURE on processing"})
        return self.template.render(self.context)
        
    def save_sheet_in_database(self, sheetpath, fileobject):
        """
        Given the path of our sheet save it inside the database.
        """
        try:
            self.sheet_modelboject = processmodels.ExcelSheets()
            self.sheet_modelboject.excelname = fileobject
            self.sheet_modelboject.sheetname.name = sheetpath
            self.sheet_modelboject.save()
        except Exception as e:
            return HttpResponse(self.render_doesnot_exists(e))
        else:
            return True 
            
            
    def render_doesnot_exists(self, error):
        self.datasetrecords = self.get_datarecords()
        self.errors = integrity.IntegrityErrors(error)
        try:
            self.context = Context({"datasetrecords":self.datasetrecords, "ERROR":error, "details":self.errors.get_error()})
            
            self.exception_template = loader.get_template("doesnotexist.html")
            if(self.exception_template):
                try:
                    return self.exception_template.render(self.context)
                except:
                    return HttpResponse("Server enccountered an error")
        except: 
            return HttpResponse("ERror processsing error templates")
            
    def detect_filetype(self, filename):
        """
        Detect the given file type.
        """
        try:
            if(".csv" in filename):
                return "csv"
            elif(".xls" in filename):
                return "xls"
            elif(".xlsx" in filename):
                return "xlsx"
            else:
                return False 
        except:
            raise 
            
    def is_file(self, filename):
        """
        Detect and findout if this is a real file.
        """
        try:
            if(os.path.isfile(filename)):
                return True 
            else:
                return False 
        except:
            raise 
