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
import simplejson
from django.forms.models import inlineformset_factory
import importlib
from datasets import models as record_models
from datasetrecords import models as datamodels
import forms
from branchcode import forms as bforms
from branchcode import models as branchmodels
from branchcode.subsystem import regionsearch
from userlogin import models as usermodels
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail, EmailMessage
from django.core.mail import get_connection
from datasets import models as record_models
import paramiko
from scp import SCPClient
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#from branchcode import models as umodels 
from util import models as umodels 
from CRB import settings
import os

mytitle = "Cred-Start Data Analysis"

def get_datarecords():
    """
    Return all available dataset records.
    """
    try:
        return record_models.Dataset.objects.all()
    except:
        raise

class EmailSending(View):
    def get(self, request):
        pass

    @method_decorator(login_required)
    def post(self, request):
        #print request.POST
        try:
            try:
                self.bform_valid = bforms.EmailForm(request.POST, request.FILES)
                self.upload_one = request.FILES["upload_one"]
                self.upload_two = request.FILES["upload_two"]
                self.upload_three = request.FILES["upload_three"]
                self.upload_four = request.FILES["upload_four"]
                self.upload_five = request.FILES["upload_five"]

                self.endpoint = request.POST.get("endpoint_address", "")
                self.source  = request.POST.get('source_address', "")
                self.describe = request.POST.get("description", "")
                try:
                    #connection = get_connection(use_tls=True, host='smtp.aol.com', port=587, username='wangoloj@aol.com', password='YahooMail.com')

                    mail = EmailMessage("wangolo", self.describe, to=[self.endpoint])
                    #print help(mail)
                    mail.attach(self.upload_one.name, self.upload_one.read(), self.upload_one.content_type)
                    mail.attach(self.upload_two.name, self.upload_two.read(), self.upload_two.content_type)
                    mail.attach(self.upload_three.name, self.upload_three.read(), self.upload_three.content_type)
                    mail.attach(self.upload_four.name, self.upload_four.read(), self.upload_four.content_type)
                    mail.attach(self.upload_five.name, self.upload_five.read(), self.upload_five.content_type)
                    mail.send()
                    #print mail
                except Exception as e:
                    return HttpResponse(self.render_failure(request, self.bform_valid, e))
            except Exception as e:
                return HttpResponse(self.render_failure(request, self.bform_valid, e))
            else:
                self.context = self.render_success_template(request)
                if(self.context):
                    return HttpResponse(self.context)
                else:
                    return HttpResponse(self.render_failure(request, self.bform_valid, "ERROR"))

        except Exception as e:
            return HttpResponse(self.render_failure(request, self.bform_valid, e))

    def render_failure(self, request, instance,  errors):
        try:
            self.datanavs = get_datarecords()
            self.template = loader.get_template("admindashboard.html")
            self.context = RequestContext(request, {"emailform":instance, "errors":errors, "datasetrecords":self.datanavs})
            return self.template.render(self.context)
        except:
            raise

    def render_success_template(self, request):
        try:
            self.template = loader.get_template("emailsendsuccessful.html")

            self.context = RequestContext(request, {"successtitle":"Successfuly sent"})

            if(self.context and self.template):
                return self.template.render(self.context)
            else:
                return None
        except:
            raise

class SendingSFTP(View):
    def get(self, request):
        return HttpResponseRedirect("/home/dashboard/")

    @method_decorator(login_required)
    def post(self, request):
        try:
            self.context = self.render_success_template(request)
            self.bform_valid = bforms.SFTPForm(request.POST, request.FILES)
            if(self.context):
                #print request.FILES.get("upload_one").temporary_file_path()
                self.upload_one = request.FILES.get("upload_one")
                self.upload_two = request.FILES.get("upload_two")
                self.upload_three = request.FILES.get("upload_three")
                self.upload_four = request.FILES.get("upload_four")
                self.upload_five = request.FILES.get("upload_five")

                self.hostname = request.POST.get("hostname", "")
                self.port = request.POST.get("port", "")
                self.username = request.POST.get("username", "")
                self.password = request.POST.get("password", "")
                try:
                    self._scp_connection = self.open_scp_connection(self.hostname, int(self.port), self.username, self.password)

                    if(self._scp_connection):
                        self._scp_client = self.get_scpclient_connection(self._scp_connection)
                        '''
                        self.file_list = [self.upload_one.temporary_file_path(), self.upload_two.temporary_file_path(),
                                          self.upload_three.temporary_file_path(), self.upload_four.temporary_file_path(),
                                          self.upload_five.temporary_file_path()
                                          ]
                        '''
                        self.file_list = [self.upload_one, self.upload_two,
                                          self.upload_three, self.upload_four,
                                          self.upload_five
                                          ]

                        if(self._scp_client):
                            self.ret = self._send_remote_recursive(self._scp_client, self.file_list)
                            if(self.ret):
                                return HttpResponse(self.context)
                            else:
                                return HttpResponse(self.render_failure(request, self.bform_valid, "Unable to upload to remote host."))
                        else:
                            return HttpResponse(self.render_failure(request, self.bform_valid, "Unable to get  connection credentials to remote host."))
                    else:
                        return HttpResponse(self.render_failure(request, self.bform_valid, "Unable to connect to remote host."))
                except ValueError as error:
                    return HttpResponse(self.render_failure(request, self.bform_valid, error))
                except Exception as e:
                    return HttpResponse(self.render_failure(request, self.bform_valid, e, args=True))
            else:
                return HttpResponseServerError("FAILURE")
        except:
            raise

    def render_success_template(self, request):
        try:
            self.template = loader.get_template("sftpsendsuccessful.html")

            self.context = RequestContext(request, {"successtitle":"Successfuly sent"})

            if(self.context and self.template):
                return self.template.render(self.context)
            else:
                return None
        except:
            raise


    def open_scp_connection(self, server, port, user, password):
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            #client.load_host_keys("/home/wangolo/Working/Keys/KeParis/DatabaseInstance.pem")
            self.pkey = "/home/wangolo/Working/Keys/KeParis/DatabaseInstance.pem"
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(server, port, user, key_filename=self.pkey)
            return client
        except:
            raise

    def get_scpclient_connection(self, ssh_object):
        try:
            return SCPClient(ssh_object.get_transport())
        except:
            raise

    def send_remote_files(self, scp_client, file_list):
        """
        Given a list of files send them to the remove server.
        """
        try:
            scp_client.put(file_list)
        except:
            raise
        else:
            return True

    def _send_remote_recursive(self, scp_client, file_list):
        """
        Given a list of files send them to the remote server.
        """
        try:
            for files in file_list:
                scp_client.put(files.temporary_file_path(), remote_path=os.path.join(settings.SFTP_LOCAL_PATH, files.name))
        except:
            raise
        else:
            return True

    def render_failure(self, request, instance,  errors, args=False):
        try:
            self.datanavs = get_datarecords()
            self.template = loader.get_template("admindashboard.html")
            self.emails_forms = bforms.EmailForm()
            self.context = RequestContext(request, {"sftp_forms":instance,'emailform':self.emails_forms, "sftp_errors":errors,
                                                    "datasetrecords":self.datanavs, "errorargs":args})
            return self.template.render(self.context)
        except:
            raise


class HeaderSettings(View):
    def get(self, request):
        pass

    @method_decorator(login_required)
    def post(self, request):
        try:
            self.headersettingsnew = True
            self.settings_insert = bforms.DefaultHeadersForms(request.POST)

            if(self.settings_insert.is_valid()):
                #print "DOING SOME INSERTING"
                self.settings_insert.save()
                self.datasetrecords = self.get_datarecords()
                self.branchsetting = bforms.DefaultHeadersForms()
                self.emailform = bforms.EmailForm()
                self._sftp_forms = bforms.SFTPForm()

                self.context = RequestContext(request, {"basetitle":"Data processing system", "datasetrecords":self.datasetrecords,
                                                        "user":request.user, "basetitle":mytitle, "emailform":self.emailform,
                                                        "sftp_forms":self._sftp_forms, "headersettings":self.branchsetting,
                                                        "successfulsettings":"Default header settings where set successfuly!!!"
                                                    })

                self.template = loader.get_template("admindashboard.html")
                return HttpResponse(self.template.render(self.context))

            else:
                #print "NOT INSERTING ERRORS"
                self.datasetrecords = self.get_datarecords()
                self.branchsetting = bforms.DefaultHeadersForms()
                self.emailform = bforms.EmailForm()
                self._sftp_forms = bforms.SFTPForm()
                self.context = RequestContext(request, {"basetitle":"Data processing system", "datasetrecords":self.datasetrecords,
                                                        "user":request.user, "basetitle":mytitle,  "emailform":self.emailform,
                                                        "sftp_forms":self._sftp_forms, "headersettings":self.branchsetting,
                                                        "settingserrors":self.settings_insert.errors
                                                    })

                self.template = loader.get_template("admindashboard.html")
                return HttpResponse(self.template.render(self.context))

        except Exception as e:
            #print "ALL IN ALL EXCEPTIONS", e
            self.datasetrecords = self.get_datarecords()
            self.branchsetting = bforms.DefaultHeadersForms()
            self.emailform = bforms.EmailForm()
            self._sftp_forms = bforms.SFTPForm()
            self.context = RequestContext(request, {"basetitle":"Data processing system", "datasetrecords":self.datasetrecords,
                                                    "user":request.user, "basetitle":mytitle,  "emailform":self.emailform,
                                                    "sftp_forms":self._sftp_forms, "headersettings":self.branchsetting,
                                                    "settingserrors":e
                                                })

            self.template = loader.get_template("admindashboard.html")
            return HttpResponse(self.template.render(self.context))


    def get_datarecords(self):
        """
        Return all available dataset records.
        """
        try:
            return record_models.Dataset.objects.all()
        except:
            raise

class UpdateHeaderSettings(View):
    @method_decorator(login_required)
    def post(self, request, settingPID):
        try:
            self.ID = request.POST.get('default_headers',"")
            self.defaultheaders = self.load_headers(self.ID)
            self.current_settings = self.load_current_settings(int(settingPID))

            if(self.current_settings):
                self.settingsform = bforms.DefaultHeadersForms(request.POST, instance=self.current_settings)
                if(self.settingsform.is_valid()):
                    self.settingsform.save()
                    self.datasetrecords = self.get_datarecords()
                    self.branchsetting = bforms.DefaultHeadersForms(instance=self.current_settings)
                    self.emailform = bforms.EmailForm()
                    self._sftp_forms = bforms.SFTPForm()
                    self.context = RequestContext(request, {"basetitle":"Data processing system", "datasetrecords":self.datasetrecords,
                                                            "user":request.user, "basetitle":mytitle, "emailform":self.emailform,
                                                            "sftp_forms":self._sftp_forms, "headersettings":self.branchsetting,
                                                            "hset":self.defaultheaders,
                                                            "successfulsettings":"Default headers curresponding to [ %s ] where updated successfuly." % self.current_settings.default_headers
                                                        })

                    self.template = loader.get_template("admindashboard.html")
                    return HttpResponse(self.template.render(self.context))
                else:
                    self.datasetrecords = self.get_datarecords()
                    self.branchsetting = bforms.DefaultHeadersForms(instance=self.current_settings)
                    self.emailform = bforms.EmailForm()
                    self._sftp_forms = bforms.SFTPForm()
                    self.context = RequestContext(request, {"basetitle":"Data processing system", "datasetrecords":self.datasetrecords,
                                                            "user":request.user, "basetitle":mytitle, "emailform":self.emailform,
                                                            "sftp_forms":self._sftp_forms, "headersettings":self.branchsetting,
                                                            "hset":self.defaultheaders,
                                                            "settingserrors":self.settingsform.errors
                                                        })

                    self.template = loader.get_template("admindashboard.html")
                    return HttpResponse(self.template.render(self.context))
            else:
                self.datasetrecords = self.get_datarecords()
                self.branchsetting = bforms.DefaultHeadersForms(instance=self.current_settings)
                self.emailform = bforms.EmailForm()
                self._sftp_forms = bforms.SFTPForm()
                self.context = RequestContext(request, {"basetitle":"Data processing system", "datasetrecords":self.datasetrecords,
                                                        "user":request.user, "basetitle":mytitle, "emailform":self.emailform,
                                                        "sftp_forms":self._sftp_forms, "headersettings":self.branchsetting,
                                                        "hset":self.defaultheaders,
                                                        "settingserrors":"Invalid settings detected!"
                                                    })

                self.template = loader.get_template("admindashboard.html")
                return HttpResponse(self.template.render(self.context))

        except Exception as e:
            #raise 
            self.datasetrecords = self.get_datarecords()
            self.branchsetting = bforms.DefaultHeadersForms()
            self.emailform = bforms.EmailForm()
            self._sftp_forms = bforms.SFTPForm()

            self.context = RequestContext(request, {"basetitle":"Data processing system", "datasetrecords":self.datasetrecords,
                                                    "user":request.user, "basetitle":mytitle, "emailform":self.emailform,
                                                    "sftp_forms":self._sftp_forms, "headersettings":self.branchsetting,
                                                    "settingserrors":e
                                                })

            self.template = loader.get_template("admindashboard.html")
            return HttpResponse(self.template.render(self.context))

    def load_current_settings(self, pid):
        try:
            return branchmodels.DefaultHeaders.objects.get(id=int(pid))
        except branchmodels.DefaultHeaders.DoesNotExist as e:
            pass

    def load_headers(self, PID):
        try:
            return branchmodels.RequiredHeader.objects.get(id=int(PID))
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

class ParseRegions(View):
    @method_decorator(login_required)
    def get(self, request):
        try:
            if(request.is_ajax()):

                self.region =  request.GET.get("region", "")
                
                try:
                    self.requested_regions = self.get_region(str(self.region))  #regionsearch.get_region_information(self.region)   
                except Exception as e:
                    self.msg  = "Request raised exception [ %s ]" %  e.message
                    self.msg_d = {self.msg:self.msg}
                    return HttpResponse(simplejson.dumps(self.msg_d), content_type="application/json")
                else:             
                    if(self.requested_regions):
                        try:
                            self.districts = self.load_alldistricts()
                            #self.region = 
                            self.filtered_districts = self.filter_d_query(self.districts, self.requested_regions)
                            self.requested_district = self.return_dictionary(self.filtered_districts)
                            
                            return HttpResponse(simplejson.dumps(self.requested_district), content_type="application/json")
                        except Exception as e:
                            self.error_msg = "SYS ERROR '%' " % str(e.message)
                            return HttpResponse(simplejson.dumps(self.error_msg), content_type="application/json")
                    else:
                        self.msg = "ERROR Request '%s' Was not found on region subsystem" % str(self.region)
                        self.error = {self.msg:self.msg}
                        try:
                            return HttpResponse(simplejson.dumps(self.error), content_type="application/json")
                        except Exception as e:
                            self.error_msg = "SYS ERROR '%' " % str(e.message)
                            return HttpResponse(simplejson.dumps(self.error_msg), content_type="application/json")

        except Exception as e:
            self.error_msg = "SYS ERROR '%' " % str(e.message)
            return HttpResponse(simplejson.dumps(self.error_msg), content_type="application/json")
    
    def load_alldistricts(self):
        """
        Return all districts available.
        """
        return umodels.Districts.objects.all()
        
    def filter_d_query(self, model_origin, r_filter_id):
        """
        Given the model return the filter.
        """
        try:
            return model_origin.filter(region_id=r_filter_id.id)
        except:
            raise 
            
    def get_region(self, region):
        try:
            return umodels.Regions.objects.get(name=str(region))
        except:
            raise 
            
    def return_dictionary(self, final_query):
        self.D = {}
        for i in final_query:
            self.D[i.name] = i.name
        return self.D
            
class ParseParishesInDistrict(View):
    @method_decorator(login_required)
    def get(self, request):
        try:
            if(request.is_ajax()):
                try:
                    self.division =  request.GET.get("division", "")
                    self.region = request.GET.get("region", "")
                    
                    try:
                        self.requested_d = self.get_subcounty(self.division.strip().lstrip().rstrip())
                    except Exception as e:
                        self.msg  = "Request raised exception [ %s ]" %  e.message
                        self.msg_d = {self.msg:self.msg}
                        return HttpResponse(simplejson.dumps(self.msg_d), content_type="application/json") 
                    else:
                        self.all_subcounties = self.query_all_parishes()
                        self.filtered_parishes= self.filter_parish_from_subcounty(self.all_subcounties, self.requested_d)
                        self.final_result = self.make_dict_outof_result(self.filtered_parishes)
                        
                        if(self.final_result):
                            try:
                                return HttpResponse(simplejson.dumps(self.final_result), content_type="application/json")
                            except Exception as e:
                                self.error_msg = "SYS ERROR '%' " % str(e.message)
                                return HttpResponse(simplejson.dumps(self.error_msg), content_type="application/json")
                        else:
                            self.msg = "Result Corresponding to  '%s' not found on the system" % str(self.division)
                            self.error = {self.msg:self.msg}
                            try:
                                return HttpResponse(simplejson.dumps(self.error), content_type="application/json")
                            except Exception as e:
                                self.error_msg = "SYS ERROR '%' " % str(e.message)
                                return HttpResponse(simplejson.dumps(self.error_msg), content_type="application/json")
                except Exception as e:
                    self.errordict = {}
                    self.msg = "ERROR: %s " % e.message 
                    self.errordict[self.msg]=self.msg 
                    return HttpResponse(simplejson.dumps(self.errordict), content_type="application/json")
       
            else:
                self.division =  request.GET.get("division", "")
                #self.parseddistrict = self.district.strip("+")
                #print "Searching for ", self.division
                self.division_info = self.get_division(self.division.strip().lstrip().rstrip())
                self.all_subcounties = self.query_all_parishes()
                
                self.filtered_parishes= self.filter_parish_from_subcounty(self.division_info, self.all_subcounties)
                self.final_result = self.make_dict_outof_result(self.filtered_parishes)
               
                return HttpResponse("You are not ajax")

        except: # Exception as e:
            #self.error_msg = "SYS ERROR '%' " % str(e.message)
            #return HttpResponse(simplejson.dumps(self.error_msg), content_type="application/json")
            raise 
    
    
    def get_division(self, division):
        """
        Given district return the given district
        from the database.
        """
        try:
            self._divisions = branchmodels.Subcounties.objects.get(name=str(division.strip().rstrip().lstrip()))
            return self._divisions
        except:
            raise 
            
    def query_all_parishes(self):
        """
        Return all the available subcounties.
        """
        try:
            return umodels.Parishes.objects.all()
        except:
            raise 
            
    def make_dict_outof_result(self, result):
        self.dicts = {}
        for r in result:
            self.dicts[r.name]=r.name 
        return self.dicts 
        
    def load_all_subcounties(self):
        return umodels.Subcounties.objects.all()
        
    def get_subcounty(self, sub):
        try:
            return umodels.Subcounties.objects.get(name=sub)
        except:
            raise
            
    def filter_s_query(self, model_origin, d_filter_id):
        """
        """
        try:
            return model_origin.filter(district_id=d_filter_id.id)
        except:
            raise 
            
    def query_districts(self, districtname):
        try:
            return umodels.Districts.objects.get(name=str(districtname))
        except:
            raise 
            
    def load_allparishes(self):
        return umodels.Parishes.objects.all()
        
    def filter_parish_from_subcounty(self, parishes_db, s_filter_id):
        try:
            return parishes_db.filter(subcounty_id=s_filter_id.id)
        except:
            raise 
            
class ParseCountyInDistrict(View):
    @method_decorator(login_required)
    def get(self, request):
        try:
            if(request.is_ajax()):
                try:
                    self.district =  request.GET.get("district", "")
                    self.parseddistrict = self.district.strip("+")
                    self.district_info = self.get_district(self.parseddistrict.strip().lstrip().rstrip())
                    
                    self.all_subcounties = self.load_all_subcounties()
                    self.filtered_subcounty = self.filter_subcounty_in_district(self.all_subcounties, self.district_info)
                    self.final_result = self.make_dict_outof_result(self.filtered_subcounty)
                    
                    if(self.final_result):
                        try:
                            return HttpResponse(simplejson.dumps(self.final_result), content_type="application/json")
                        except Exception as e:
                            self.error_msg = "SYS ERROR '%' " % str(e.message)
                            return HttpResponse(simplejson.dumps(self.error_msg), content_type="application/json")
                    else:
                        #print "Result was not found ", self.final_result
                        self.msg = "Result Corresponding to  '%s' not found on the system" % str(self.district)
                        self.error = {self.msg:self.msg}
                        try:
                            return HttpResponse(simplejson.dumps(self.error), content_type="application/json")
                        except Exception as e:
                            self.error_msg = "SYS ERROR '%' " % str(e.message)
                            return HttpResponse(simplejson.dumps(self.error_msg), content_type="application/json")
                            
                except Exception as e:
                    self.errordict = {}
                    self.msg = "ERROR: %s " % e.message 
                    self.errordict[self.msg]=self.msg 
                    return HttpResponse(simplejson.dumps(self.errordict), content_type="application/json")
       
            else:
                self.district =  request.GET.get("district", "")
                self.parseddistrict = self.district.strip("+")
                
                
                self.district_info = self.get_district(self.parseddistrict.strip().lstrip().rstrip())
                self.all_subcounties = self.query_all_subcounties()
                
                self.filtered_subcounty = self.filter_districts_from_subcounty(self.district_info, self.all_subcounties)
                #print "FINAL INFORMATION IS ", self.filtered_subcounty
                return HttpResponse("You are not ajax")

        except: # Exception as e:
            #self.error_msg = "SYS ERROR '%' " % str(e.message)
            #return HttpResponse(simplejson.dumps(self.error_msg), content_type="application/json")
            raise 


    def get_subcounty(self, county):
        try:
            self.all_query = branchmodels.Subcounties.objects.get(district=str(county))
        except:
            raise
        else:
            return self.all_query
            
    
    def get_district(self, district):
        """
        Given district return the given district
        from the database.
        """
        try:
            self.get_district = umodels.Districts.objects.get(name=str(district.strip().rstrip().lstrip()))
            return self.get_district
        except:
            raise 
            
    def filter_subcounty_in_district(self, sub_county_db_object, district_db_object):
        """
        Return all the given data. based on the district id.
        """
        try:
            self.all_subcount = sub_county_db_object.filter(district_id=district_db_object.id)
            return self.all_subcount
        except:
            raise 
            
            
    def make_dict_outof_result(self, result):
        self.dicts = {}
        for r in result:
            self.dicts[r.name]=r.name 
        return self.dicts 
        
    #--Latest Query---
    def load_alldistricts(self):
        """
        Return all districts available.
        """
        return umodels.Districts.objects.all()
        
    def filter_d_query(self, model_origin, r_filter_id):
        """
        Given the model return the filter.
        """
        try:
            return model_origin.filter(region_id=r_filter_id.id)
        except:
            raise 
            
    def load_all_subcounties(self):
        return umodels.Subcounties.objects.all()
        
    def filter_s_query(self, model_origin, d_filter_id):
        """
        """
        try:
            return d_filter_id.filter(district_id=model_origin.id)
        except:
            raise
            
class SearchInstitution(View):
    @method_decorator(login_required)
    def get(self, request):
        try:
            if(request.is_ajax()):
                try:
                   self.ID = request.GET.get("ID")
                   self.query = self.query_pi(self.ID)
                   self.PI = self.filtere_pi(self.query)
                   return HttpResponse(simplejson.dumps(self.PI), content_type="application/json")
                   
                except Exception as e:
                    self.errordict = {}
                    self.msg = "ERROR: %s " % e.message 
                    self.errordict[self.msg]=self.msg 
                    return HttpResponse(simplejson.dumps(self.errordict), content_type="application/json")
       
            else:
                try:
                   self.ID = request.GET.get("ID")
                   self.query = self.query_pi(self.ID)
                   self.PI = self.filtere_pi(self.query)
                   return HttpResponse(simplejson.dumps(self.PI), content_type="application/json")
                   
                except Exception as e:
                    self.errordict = {}
                    self.msg = "ERROR: %s " % e.message 
                    self.errordict[self.msg]=self.msg 
                    return HttpResponse(simplejson.dumps(self.errordict), content_type="application/json") 
        except Exception as e:
            self.error_msg = "SYS ERROR '%' " % str(e.message)
            return HttpResponse(simplejson.dumps(self.error_msg), content_type="application/json")

    def query_pi(self, ID):
        """
        """
        try:
            self.filtered = branchmodels.PIIdentificationCode.objects.get(id=int(ID))
            #print "QUERRRIED ", self.filtered, ID
            return self.filtered
        except:
            raise

    def filtere_pi(self, pi_record):
        """
        """
        try:
            self.rec = []
            self.pi_header = pi_record.pi_identification_code
            self.pi_filtered = pi_record.participating_institution_set.all()
            #print "P IS ", pi_record
            #print "ALL ", pi_record.participating_institution_set.all()
            for h in self.pi_filtered:
               # print "PI ", h.PI_Identification_Code.pi_identification_code, "HEADER ", self.pi_header
                if(h.PI_Identification_Code.pi_identification_code == self.pi_header):
                    self.rec.append(h.id)

            #query filtered min
            #print "RECT ", self.rec 
            self.pi_institute = datamodels.PARTICIPATING_INSTITUTION.objects.get(id=min(self.rec))

            #dictify
            self.d = {}
            self.d[self.pi_institute.id]=self.pi_institute.Institution_Name
            return self.d
        except:
            raise
            
            

class SavePiDetails(View):
    def get(self, request):
        return HttpResponse("Your request has been fullfiled.")

    def get_post_piform(self):
        return bforms.PIIdentificationCodeForm
        
    def post(self, request):
        """
        Save the PI details.
        """
        try:
            self.piform = self.get_post_piform()
            self.pi_insert = self.piform(request.POST)
            
            if(self.pi_insert.is_valid()):
                self.pi_insert.save()
                return HttpResponseRedirect("/home/dashboard/")
            else:
                print "A couple of errors ", self.pi_insert.errors
                self.datasetrecords = self.get_datarecords()
                self._piforms = self.get_post_piform()
                self.context = RequestContext(request, {"basetitle":"Data processing system", "datasetrecords":self.datasetrecords,
                                                            "user":request.user, "basetitle":"Cred Stat", "emailform":None,
                                                            "sftp_forms":None, "headersettings":None,
                                                            "hset":None,"piforms":self._piforms,
                                                            "settingserrors":self.pi_insert.errors
                                                        })

                self.template = loader.get_template("admindashboard.html")
                return HttpResponse(self.template.render(self.context))
                    
        except Exception as e:
            self.datasetrecords = self.get_datarecords()
            self.context = RequestContext(request, {"basetitle":"Data processing system", "datasetrecords":self.datasetrecords,
                                            "user":request.user, "basetitle":"Cred Stat", "emailform":None,
                                            "sftp_forms":None, "headersettings":None,
                                            "hset":None,
                                            "settingserrors":e
                                        })

            self.template = loader.get_template("admindashboard.html")
            return HttpResponse(self.template.render(self.context))
            
    def get_datarecords(self):
        """
        Return all available dataset records.
        """
        try:
            return record_models.Dataset.objects.all()
        except:
            raise

class QueryPiInformation(View):
    def get(self, request):
        try:
            if(request.is_ajax()):
                try:
                   self.ID = request.GET.get("pivalue")
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
                   self.ID = request.GET.get("pivalue")
                   self.query = self.query_pi_name(self.ID)
                   ##self.PI = self.filtere_pi(self.query)
                   return HttpResponse(simplejson.dumps(self.query), content_type="application/json")
                   
                except Exception as e:
                    self.errordict = {}
                    self.msg = "ERROR: %s " % e.message 
                    self.errordict[self.msg]=self.msg 
                    return HttpResponse(simplejson.dumps(self.errordict), content_type="application/json") 
        except Exception as e:
            self.error_msg = "SYS ERROR '%' " % str(e.message)
            return HttpResponse(simplejson.dumps(self.error_msg), content_type="application/json")

    def query_pi_name(self, pivalue):
        """
        Query the pi return value.
        """
        try:
            self.D = {}
            print "VALUE IS ", pivalue 
            self.pi_code = branchmodels.PIIdentificationCode.objects.get(pi_identification_code=pivalue)
            self.D["PIVALUE"]=self.pi_code.insitution_Name
            return self.D
        except:
            raise  
