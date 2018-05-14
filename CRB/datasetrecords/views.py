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
#from validators.subsystems picode 
from userlogin import models as usermodels 
from datasetrecords import accreference 

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from processrecords import forms as processforms
from datasetrecords import searchfilters

mytitle = "Credit-Start | Record, Validate, Analyse, Report"

# Create your views here.
#-----view for the appendix----

def load_exception_template():
    return loader.get_template("exceptiontemplate.html")
    
def get_PI():
    """
    Return the participating instutition.
    """
    try:
        return datamodels.PARTICIPATING_INSTITUTION.objects.all().count()
    except:
        raise 
   
def get_IB():
    try:
        return datamodels.INSTITUTION_BRANCH.objects.all().count()
    except:
        raise 
  #cbapath

def get_CBA():
    try:
        return datamodels.CREDITBORROWERACCOUNT.objects.all().count()
    except:
        raise 
#cappath

def get_CAP():
    try:
        return datamodels.CREDIT_APPLICATION.objects.all().count()
    except:
        raise 

def get_BC():
    try:
        #bcpath
        return datamodels.BOUNCEDCHEQUES.objects.all().count()
    except:
        raise  
        
#pispath
def get_PIS():
    try:
        return datamodels.PARTICIPATINGINSTITUTIONSTAKEHOLDER.objects.all().count()
    except:
        raise 
        
#get_CMC
def get_CMC():
    try:
        return datamodels.COLLATERAL_MATERIAL_COLLATERAL.objects.all().count()
    except:
        raise 
        
#ccgpath
def get_CCG():
    try:
        return datamodels.COLLATERAL_CREDIT_GUARANTOR.objects.all().count()
    except:
        raise  

#fmdpath

def get_FMD():
    try:
        return datamodels.FINANCIAL_MALPRACTICE_DATA.objects.all().count()
    except:
        raise 

#bspath
def get_BS():
    try:
        return datamodels.BORROWERSTAKEHOLDER.objects.all().count()
    except:
        raise 
                                             
class BaseHomepage(View):
    def get(self, request, is_superuser):
        try:
            if(request.user.is_authenticated()):
                if(is_superuser == "superuser"):
                    self.admin_template = self.load_superuser_template()
                    if(self.admin_template):
                        self.codeform = self.load_branchcode_forms()
                        self.emailform = self.get_email_form()
                        self._sftp_forms = self.sftp_forms()
                       
                        self.rendered = self.render_appendix_context(request, self.admin_template, request.user, codeform=self.codeform, emailform=self.emailform,
                                                                        sftp_forms=self.sftp_forms)
                        if(self.rendered):
                            return HttpResponse(self.rendered)
                        else:
                            return HttpResponseServerError("Failed to perform request")
                    else:
                        return HttpResponseServerError("An error occured while processing data")
                        
                elif(is_superuser == "notsuperuser"):
                    self.users =  self.load_user_creds(request) 
                    self.data_rights = self.users.data_access_rights.all()
                    self.emailform = self.get_email_form()
                    self._sftp_forms = self.sftp_forms()
                    self.codeform = self.load_branchcode_forms()
                    self.templates = self.get_appendix_template()
                    
                    self.rendered = self.render_appendix_context(request, self.templates, self.data_rights, staff=self.users,
                                                        codeform=self.codeform, emailform=self.emailform, sftp_forms=self.sftp_forms
                                                )
                    if(self.rendered):
                        return HttpResponse(self.rendered)
                    else:
                        return HttpResponseServerError("Failed to perform request")
                else:
                    return HttpResponseServerError("Attempted failure")
            else:
                return HttpResponseRedirect("/")
        except:
            raise

    def load_superuser_template(self):
        try:
            return loader.get_template("admindashboard.html")
        except:
            raise
            
    def sftp_forms(self):
        try:
            return bforms.SFTPForm()
        except:
            raise 
            
    def load_branchcode_forms(self):
        try:
            return bforms.BranchCodeForms()
        except:
            raise 
             
    def parse_model_fields(self, data):
        self.fields = [ ]
        self.mfields = data._meta.fields

        for model_fields in self.mfields:
                if(model_fields.name in self.fields):
                    pass
                else:
                    self.fields.append(model_fields.name)

        return self.fields
    
    def load_user_creds(self, request):
        try:
            return usermodels.CreditInstitutionStaff.objects.get(username=request.user)
        except:
            raise 
            
    def get_appendix_template(self, *template):
        """
        Load the template for the appendix
        """
        try:
            if(template):
                return loader.get_template(template)
            else:
                return loader.get_template("nonsuperuserdashboard.html")
        except:
            raise
    
    def get_email_form(self):
        try:
            return bforms.EmailForm()
        except:
            raise 
            
    def load_default_settings(self):
        return branchmodels.DefaultHeaders.objects.all()
        
    def render_appendix_context(self, request, template, user_rights, staff=None, codeform=None, emailform=None, sftp_forms=None):
        """
        Load the contexts and return the rendered.
        """
        try:
            self.headersettingsnew = True
            try:
                self.datasetrecords = self.get_datarecords()                
                
                self._piforms = self.filter_settings_ret_piform()
                self.context = RequestContext(request, {"basetitle":"Data processing system", "datasetrecords":self.datasetrecords,
                                                        "user":request.user, "codeform":codeform, "userrights":user_rights,
                                                        "emailform":emailform,"sftp_forms":sftp_forms,"staff":staff,
                                                        "piforms":self._piforms
                                })

                return template.render(self.context)
            except IndexError as error:
                raise
        except:
            raise

    def filter_settings_ret_piform(self):
        """
        """
        self.ids = []
        self.all_rec = branchmodels.PIIdentificationCode.objects.all()
        if(self.all_rec):
            for rec in self.all_rec:
                self.ids.append(rec.id)

            # Query
            self.all_id = branchmodels.PIIdentificationCode.objects.get(id=min(self.ids))
            return bforms.PIIdentificationCodeForm(instance=self.all_id)
        else:
            return bforms.PIIdentificationCodeForm()
            
    def get_pi_form(self):
        return bforms.PIIdentificationCodeForm()
        
    def filter_modeldata(self, model):
        try:
            if(model):
                try:
                    availabledata = model.objects.all().count()
                    return availabledata
                except:
                    pass
            else:
                pass
        except:
            pass

    def get_navs(self, ids):
        """
        get the ide.
        """
        try:
            if(ids <  1):
                return None
            else:
                try:
                    self.name = models.DataSetRecords.objects.get(id=ids)
                    return self.name
                except:
                    pass
        except:
            pass

    def get_models(self, dataset):
        try:
            if(dataset == "FINANCIAL MALPRACTICE DATA"):
                return datamodels.FINANCIAL_MALPRACTICE_DATA
            elif(dataset == "COLLATERAL CREDIT GUARANTOR"):
                return datamodels.COLLATERAL_CREDIT_GUARANTOR
            elif(dataset == "COLLATERAL MATERIAL COLLATERAL"):
                return datamodels.COLLATERAL_MATERIAL_COLLATERAL
            elif(dataset == "BORROWERSTAKEHOLDER"):
                return datamodels.BORROWERSTAKEHOLDER
            elif(dataset == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return datamodels.PARTICIPATINGINSTITUTIONSTAKEHOLDER
            elif(dataset == "BOUNCEDCHEQUES"):
                return datamodels.BOUNCEDCHEQUES
            elif(dataset == "CREDIT APPLICATION"):
                return datamodels.CREDIT_APPLICATION
            elif(dataset == "CREDITBORROWERACCOUNT"):
                return datamodels.CREDITBORROWERACCOUNT
            elif(dataset == "INSTITUTION BRANCH"):
                self.template = "IB_dataview.html"
                return datamodels.INSTITUTION_BRANCH
            elif(dataset == "PARTICIPATING INSTITUTION"):
                return datamodels.PARTICIPATING_INSTITUTION
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

class NewDataRecords(View):
    @method_decorator(login_required)
    def get(self, request, record_slug):
        try:
            self.dataset_infor = self.load_record_information(record_slug)
            self.template = self.load_template()
            if(self.dataset_infor):
                context_var  = self.process_context(request, self.template, self.dataset_infor)
                #return HttpResponse(self.rendered)
                return context_var
            else:
                return HttpResponse("Failure")
        except Exception as e:
            self.datasetrecords = self.get_datarecords()
            self.template = load_exception_template()
            self.context = RequestContext(request, {"datasetrecords":self.datasetrecords, "Error":e,
                                                    "internalserver":"Internal Server Error!"
                                          })
            return HttpResponse(self.template.render(self.context))
            
    def load_user_creds(self, request):
        try:
            if(request.user.is_superuser):
                return True
            else:
                return usermodels.CreditInstitutionStaff.objects.get(username=request.user)
        except Exception as e:
            self.datasetrecords = self.get_datarecords()
            self.template = load_exception_template()
            self.context = RequestContext(request, {"datasetrecords":self.datasetrecords, "Error":e,
                                                    "internalserver":"Internal Server Error!"
                                          })
            return HttpResponse(self.template.render(self.context))
            
    def load_record_information(self, slug):
        """
        Load and return the information of any
        record.
        """
        try:
            return record_models.Dataset.objects.get(slug=slug)
        except Exception as e:
            self.datasetrecords = self.get_datarecords()
            self.template = load_exception_template()
            self.context = RequestContext(request, {"datasetrecords":self.datasetrecords, "Error":e,
                                                    "internalserver":"Internal Server Error!"
                                          })
            return HttpResponse(self.template.render(self.context))

    def load_template(self, custom_template=None):
        try:
            if(custom_template):
                return loader.get_template(custom_template)
            else:
                return loader.get_template("datasetrecords.html")
        except Exception as e:
            self.datasetrecords = self.get_datarecords()
            self.template = load_exception_template()
            self.context = RequestContext(request, {"datasetrecords":self.datasetrecords, "Error":e,
                                                    "internalserver":"Internal Server Error!"
                                          })
            return HttpResponse(self.template.render(self.context))

    def process_context(self, request, template, dataset_slug):
        try:
            if(template):
                self.datasetforms = self.load_forms_by_slug(dataset_slug)
                self.pciforms = self.get_PCIForms()
                self.sciforms = self.get_SCIForms()
                self.gscafbforms = self.get_GSCAFBForms()
                self.idforms = self.get_IDForms()
                self.getieforms = self.get_EIForms()
                self.clientform = self.get_clientforms()
                #
                self.process_forms = processforms.ExcelLegacyForms()
                self.datasetrecords = self.get_datarecords()
                self.data_rights = None
                self.userdetails = self.load_user_creds(request)
                
                if(self.userdetails == True):
                    pass
                else:
                    self.data_rights = self.userdetails.data_access_rights.all()
                    
                self.errorsession = request.session.get("errormsg")
                self.context  = render(request, "datasetrecords.html", {"datasetforms":self.datasetforms,"datasetrecords":self.datasetrecords,
                                                        "datasetinput":dataset_slug.dataset.upper().replace("_", " ", len(str(dataset_slug.dataset))),
                                                        "pciforms":self.pciforms,"sciforms":self.sciforms, "dataset_active":dataset_slug.dataset,
                                                        "gscafbforms":self.gscafbforms, "idforms":self.idforms,
                                                        "ieforms":self.getieforms, "userrights":self.data_rights, "fileimporterror":self.errorsession,
                                                        "process_forms":self.process_forms, "clientform":self.clientform,
                                                        })
                if(self.errorsession):
                    request.session["errormsg"]=None
                #return template.render(self.context)
                return self.context 
            else:
                return None
        except:
            raise

    def get_clientforms(self):
        return forms.ClientInformation_Forms(prefix="clientdetails")

    def get_PCIForms(self):
        return forms.PCIForms(prefix="PCI_Forms")

    def get_SCIForms(self):
        return forms.SCIForms(prefix="SCI_Forms")
    
    def get_GSCAFBForms(self, post=False):
        if(post):
            return forms.GSCAFBForms
        else:
            return forms.GSCAFBForms(prefix="GSCAFBForms")
        
    def get_IDForms(self, post=False):
        if(post):
            return forms.IDForms
        else:
            return forms.IDForms(prefix="IDForms")
        
    def get_EIForms(self, post=False):
        if(post):
            return forms.EIForms
        else:
            return forms.EIForms(prefix="EIForms")
        
    def load_forms_by_slug(self, record_info):
        """
        Return the forms which will be used.
        """
        try:
            if(record_info.dataset_record == "COLLATERAL_MATERIAL_COLLATERAL"):
                return forms.CMC_Forms(prefix="standard_forms")
            elif(record_info.dataset_record == "BORROWERSTAKEHOLDER"):
               return forms.BS_Forms(prefix="standard_forms")
            elif(record_info.dataset_record == "BOUNCEDCHEQUES"):
                return forms.BC_Forms(prefix="standard_forms")
            elif(record_info.dataset_record == "COLLATERAL_CREDIT_GUARANTOR"):
                return forms.CCG_Forms(prefix="standard_forms")
            elif(record_info.dataset_record == "CREDITBORROWERACCOUNT"):
                return forms.CBA_Forms(prefix="standard_forms")
            elif(record_info.dataset_record == "CREDIT_APPLICATION"):
                return forms.CAP_Forms(prefix="standard_forms")
            elif(record_info.dataset_record == "FINANCIAL_MALPRACTICE_DATA"):
                return forms.FRA_Forms(prefix="standard_forms")
            elif(record_info.dataset_record == "INSTITUTION_BRANCH"):
                return forms.IB_Forms(prefix="standard_forms")
            elif(record_info.dataset_record == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return forms.PIS_Forms(prefix="standard_forms")
            elif(record_info.dataset_record == "PARTICIPATING_INSTITUTION"):
                return forms.PI_Forms(prefix="standard_forms")
            else:
                return False
        except:
            raise
            
    def load_forms_insert(self, record_info):
        """
        Return the forms which will be used.
        """
        try:
            if(record_info.dataset_record == "COLLATERAL_MATERIAL_COLLATERAL"):
                return forms.CMC_Forms
            elif(record_info.dataset_record == "BORROWERSTAKEHOLDER"):
               return forms.BS_Forms
            elif(record_info.dataset_record == "BOUNCEDCHEQUES"):
                return forms.BC_Forms 
            elif(record_info.dataset_record == "COLLATERAL_CREDIT_GUARANTOR"):
                return forms.CCG_Forms
            elif(record_info.dataset_record == "CREDITBORROWERACCOUNT"):
                return forms.CBA_Forms 
            elif(record_info.dataset_record == "CREDIT_APPLICATION"):
                return forms.CAP_Forms
            elif(record_info.dataset_record == "FINANCIAL_MALPRACTICE_DATA"):
                return forms.FRA_Forms
            elif(record_info.dataset_record == "INSTITUTION_BRANCH"):
                return forms.IB_Forms
            elif(record_info.dataset_record == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return forms.PIS_Forms
            elif(record_info.dataset_record == "PARTICIPATING_INSTITUTION"):
                return forms.PI_Forms
            else:
                return False
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
    
    def get_pci_formpost(self):
        return forms.PCIForms
        
    def get_sci_formpost(self):
        return forms.SCIForms
        
    def get_stakeholder_formpost(self):
        return forms.BorrowersStakeDetails_Forms
        
    @method_decorator(login_required)  
    def post(self, request, record_slug):
        if(request.POST):
            try:
                self.dataset_infor = self.load_record_information(record_slug)
                if(record_slug.upper() == 'INSTITUTION_BRANCH'):
                    self.return_response = self.insert_ib(request, self.dataset_infor, record_slug)
                    return self.return_response
                    
                elif(record_slug.upper() == 'CREDITBORROWERACCOUNT'):
                    self.return_response = self.insert_all(request, self.dataset_infor, record_slug)
                    return self.return_response
                     
                elif(record_slug.upper() == 'CREDIT_APPLICATION'):
                    self.return_response = self.insert_cap(request, self.dataset_infor, record_slug)
                    return self.return_response
                    
                elif(record_slug.upper() == 'BOUNCEDCHEQUES'):
                    self.return_response = self.insert_all(request, self.dataset_infor, record_slug)
                    return self.return_response
                    
                elif(record_slug.upper() == 'BORROWERSTAKEHOLDER'):
                    self.return_response = self.insert_bs(request, self.dataset_infor, record_slug)
                    return self.return_response
                    
                elif(record_slug.upper() == 'COLLATERAL_MATERIAL_COLLATERAL'):
                    self.return_response = self.insert_cmc(request, self.dataset_infor, record_slug)
                    return self.return_response
                    
                elif(record_slug.upper() == 'COLLATERAL_CREDIT_GUARANTOR'):
                    self.return_response = self.insert_ccg(request, self.dataset_infor, record_slug)
                    return self.return_response
                    
                elif(record_slug.upper() == 'FINANCIAL_MALPRACTICE_DATA'):
                    self.return_response = self.insert_fmd(request, self.dataset_infor, record_slug)
                    return self.return_response
                    
                elif(record_slug.upper() == 'PARTICIPATINGINSTITUTIONSTAKEHOLDER'):
                    self.return_response = self.insert_all(request, self.dataset_infor, record_slug)
                    return self.return_response
                    
                elif(record_slug.upper() == 'PARTICIPATING_INSTITUTION'):
                    self.return_response = self.insert_pi(request, self.dataset_infor, record_slug)
                    return self.return_response
                else:
                    return HttpResponse("Working like a charm")
            except:
                raise 

    def insert_bs(self, request, dataset_infor, record_slug):
        
        try:
            self.pci_insert = self._form_instance(request, self.get_pci_formpost(), prefix="PCI_Forms")
            self.sci_insert = self._form_instance(request, self.get_sci_formpost(), prefix="SCI_Forms")
            self.idi_insert = self._form_instance(request, self.get_IDForms(True), prefix="IDForms")
            self.ie_insert = self._form_instance(request, self.get_EIForms(True), prefix="EIForms")
            self.gscafb_insert = self._form_instance(request, self.get_GSCAFBForms(True), prefix="GSCAFBForms")
            
            try:
                self.standard_form = self.load_forms_insert(dataset_infor)
                self.standard_insert = self._form_instance(request, self.standard_form, prefix="standard_forms")
                
            except Exception as e:
                self.context_dict["dataerrors"]=e
                self.context = RequestContext(request, self.context_dict)
                return HttpResponse(self.template.render(self.context)) 
                
            else:
                self.datasetrecords = self.get_datarecords()
                self.context_dict = {"datasetforms":self.standard_insert,"datasetrecords":self.datasetrecords,
                                                        "datasetinput":dataset_infor,
                                                        "pciforms":self.pci_insert,"sciforms":self.sci_insert, "dataset_active":record_slug,
                                                        "gscafbforms":self.gscafb_insert, "idforms":self.idi_insert,
                                                        "ieforms":self.ie_insert, "userrights":self.dataset_infor
                                    }
                                    
                self.template =  loader.get_template("datasetrecords.html")
                
                #Beginning testing the records if they are valid
                if(self.pci_insert.is_valid()):
                    self.pci_ret_instance = self.pci_insert.save()
                    
                    if(self.sci_insert.is_valid()):
                        self.sci_ret_instance = self.sci_insert.save()
                        
                        if(self.idi_insert.is_valid()):
                            self.id_ret_instance = self.idi_insert.save()
                            
                            if(self.ie_insert.is_valid()):
                                self.ie_ret_instance = self.ie_insert.save()
                                
                                if(self.gscafb_insert.is_valid()):
                                    self.gscafb_ret_instance = self.gscafb_insert.save()
                                    
                                    #Check the final standard form
                                    if(self.standard_insert.is_valid()):
                                        self.ret_standard_intance = self.standard_insert.save(commit=False) #Don't save the changs
                                        
                                        #Save all other following fields
                                        self.ret_standard_intance.pci=self.pci_ret_instance
                                        self.ret_standard_intance.sci=self.sci_ret_instance
                                        self.ret_standard_intance.idi=self.id_ret_instance
                                        self.ret_standard_intance.ei=self.ie_ret_instance
                                        self.ret_standard_intance.gscafb=self.gscafb_ret_instance
                                        
                                        #Finally save all together and and perform the commit
                                        self.ret_standard_intance.save()
                                        
                                        if("submitsquit" in request.POST):
                                            return HttpResponseRedirect("/home/redo/")
                                        elif("submitviews" in request.POST):
                                            url = "/view/dataview/request/%s/" % str(self.dataset_infor.slug)
                                            return HttpResponseRedirect(url)
                                            
                                        elif("submitsagain" in request.POST):
                                            self.path = request.get_full_path()
                                            return HttpResponseRedirect(self.path)
                    
                                    else:
                                        self.context_dict["dataerrors"]=self.standard_insert.errors 
                                        self.context = RequestContext(request, self.context_dict)
                                        return HttpResponse(self.template.render(self.context))
                                else:
                                    self.context_dict["dataerrors"]=self.gscafb_insert.errors 
                                    self.context = RequestContext(request, self.context_dict)
                                    return HttpResponse(self.template.render(self.context))
                            else:
                                self.context_dict["dataerrors"]=self.ie_insert.errors 
                                self.context = RequestContext(request, self.context_dict)
                                return HttpResponse(self.template.render(self.context))
                        else:
                            self.context_dict["dataerrors"]=self.idi_insert.errors 
                            self.context = RequestContext(request, self.context_dict)
                            return HttpResponse(self.template.render(self.context))
                    else:
                        self.context_dict["dataerrors"]=self.sci_insert.errors 
                        self.context = RequestContext(request, self.context_dict)
                        return HttpResponse(self.template.render(self.context))
                else:
                    self.context_dict["dataerrors"]=self.pci_insert.errors 
                    self.context = RequestContext(request, self.context_dict)
                    return HttpResponse(self.template.render(self.context))
                    
        except Exception as e:
            self.context_dict["dataerrors"]=e
            self.context = RequestContext(request, self.context_dict)
            return HttpResponse(self.template.render(self.context))  
            
    def insert_fmd(self, request, dataset_infor, record_slug):
        
        self.standard_form = self.load_forms_insert(dataset_infor)
        self.insert_standard = self.standard_form(request.POST, prefix="standard_forms")

        #Following for error handling
        self.datasetrecords = self.get_datarecords()
        #print "TYPE IS ", type(dataset_infor), dataset_infor
        self.context_dict = {"datasetforms":self.insert_standard,"datasetrecords":self.datasetrecords,"dataset_active":record_slug
                            }
        self.template =  loader.get_template("datasetrecords.html")

        try:
            if(self.insert_standard.is_valid()):
                try:
                    self.insert_standard.save()
                    
                    if("submitsquit" in request.POST):
                        return HttpResponseRedirect("/home/redo/")
                        
                    elif("submitviews" in request.POST):
                        url = "/view/dataview/request/%s/" % str(self.dataset_infor.slug)
                        return HttpResponseRedirect(url)
                        
                    elif("submitsagain" in request.POST):
                        self.path = request.get_full_path()
                        return HttpResponseRedirect(self.path)
                        
                except Exception as e:
                    self.context_dict["dataerrors"]=e
                    self.context = RequestContext(request, self.context_dict)
                    return HttpResponse(self.template.render(self.context)) 
                        
            else:
                self.context_dict["dataerrors"]=self.insert_standard.errors 
                self.context = RequestContext(request, self.context_dict)
                return HttpResponse(self.template.render(self.context))
                    
        except Exception as e:
            self.context_dict["dataerrors"]=e
            self.context = RequestContext(request, self.context_dict)
            return HttpResponse(self.template.render(self.context))
            
            
    def insert_ccg(self, request, dataset_infor, record_slug):
        
        try:
            self.pci_insert = self._form_instance(request, self.get_pci_formpost(), prefix="PCI_Forms")
            self.sci_insert = self._form_instance(request, self.get_sci_formpost(), prefix="SCI_Forms")
            self.idi_insert = self._form_instance(request, self.get_IDForms(True), prefix="IDForms")
            self.ie_insert = self._form_instance(request, self.get_EIForms(True), prefix="EIForms")
            self.gscafb_insert = self._form_instance(request, self.get_GSCAFBForms(True), prefix="GSCAFBForms")
            
            try:
                self.standard_form = self.load_forms_insert(dataset_infor)
                self.standard_insert = self._form_instance(request, self.standard_form, prefix="standard_forms")
                
            except Exception as e:
                self.context_dict["dataerrors"]=e
                self.context = RequestContext(request, self.context_dict)
                return HttpResponse(self.template.render(self.context)) 
                
            else:
                self.datasetrecords = self.get_datarecords()
                self.context_dict = {"datasetforms":self.standard_insert,"datasetrecords":self.datasetrecords,
                                                        "datasetinput":dataset_infor,
                                                        "pciforms":self.pci_insert,"sciforms":self.sci_insert, "dataset_active":record_slug,
                                                        "gscafbforms":self.gscafb_insert, "idforms":self.idi_insert,
                                                        "ieforms":self.ie_insert, "userrights":self.dataset_infor
                                    }
                                    
                self.template =  loader.get_template("datasetrecords.html")
                
                #Beginning testing the records if they are valid
                if(self.pci_insert.is_valid()):
                    self.pci_ret_instance = self.pci_insert.save()
                    
                    if(self.sci_insert.is_valid()):
                        self.sci_ret_instance = self.sci_insert.save()
                        
                        if(self.idi_insert.is_valid()):
                            self.id_ret_instance = self.idi_insert.save()
                            
                            if(self.ie_insert.is_valid()):
                                self.ie_ret_instance = self.ie_insert.save()
                                
                                if(self.gscafb_insert.is_valid()):
                                    self.gscafb_ret_instance = self.gscafb_insert.save()
                                    
                                    #Check the final standard form
                                    if(self.standard_insert.is_valid()):
                                        self.ret_standard_intance = self.standard_insert.save(commit=False) #Don't save the changs
                                        
                                        #Save all other following fields
                                        self.ret_standard_intance.pci=self.pci_ret_instance
                                        self.ret_standard_intance.sci=self.sci_ret_instance
                                        self.ret_standard_intance.idi=self.id_ret_instance
                                        self.ret_standard_intance.ei=self.ie_ret_instance
                                        self.ret_standard_intance.gscafb=self.gscafb_ret_instance
                                        
                                        #Finally save all together and and perform the commit
                                        self.ret_standard_intance.save()
                                        
                                        if("submitsquit" in request.POST):
                                            return HttpResponseRedirect("/home/redo/")
                                        elif("submitviews" in request.POST):
                                            url = "/view/dataview/request/%s/" % str(self.dataset_infor.slug)
                                            return HttpResponseRedirect(url)
                                            
                                        elif("submitsagain" in request.POST):
                                            self.path = request.get_full_path()
                                            return HttpResponseRedirect(self.path)
                    
                                    else:
                                        self.context_dict["dataerrors"]=self.standard_insert.errors 
                                        self.context = RequestContext(request, self.context_dict)
                                        return HttpResponse(self.template.render(self.context))
                                else:
                                    self.context_dict["dataerrors"]=self.gscafb_insert.errors 
                                    self.context = RequestContext(request, self.context_dict)
                                    return HttpResponse(self.template.render(self.context))
                            else:
                                self.context_dict["dataerrors"]=self.ie_insert.errors 
                                self.context = RequestContext(request, self.context_dict)
                                return HttpResponse(self.template.render(self.context))
                        else:
                            self.context_dict["dataerrors"]=self.idi_insert.errors 
                            self.context = RequestContext(request, self.context_dict)
                            return HttpResponse(self.template.render(self.context))
                    else:
                        self.context_dict["dataerrors"]=self.sci_insert.errors 
                        self.context = RequestContext(request, self.context_dict)
                        return HttpResponse(self.template.render(self.context))
                else:
                    self.context_dict["dataerrors"]=self.pci_insert.errors 
                    self.context = RequestContext(request, self.context_dict)
                    return HttpResponse(self.template.render(self.context))
                    
        except Exception as e:
            self.context_dict["dataerrors"]=e
            self.context = RequestContext(request, self.context_dict)
            return HttpResponse(self.template.render(self.context))  
            
    def insert_pi(self, request, dataset_infor, record_slug):
        self.pci_form = self.get_pci_formpost()
       
        self.pci_insert = self.pci_form(request.POST, prefix="PCI_Forms")
        #self.sci_insert = self.sci_form(request.POST, prefix="SCI_Forms")
        
        self.standard_form = self.load_forms_insert(dataset_infor)
        self.insert_standard = self.standard_form(request.POST, prefix="standard_forms")
        
        #Following for error handling
        self.datasetrecords = self.get_datarecords()
        #print "TYPE IS ", type(dataset_infor), dataset_infor
        self.context_dict = {"datasetforms":self.insert_standard,"datasetrecords":self.datasetrecords,
                                "datasetinput":dataset_infor, "pciforms":self.pci_insert,"dataset_active":record_slug
                            }
        self.template =  loader.get_template("datasetrecords.html")
        
        try:
            if(self.pci_insert.is_valid()):
                try:
                    self.pci_returncode = self.pci_insert.save()
                    #self.sci_returncode = self.sci_insert.save()
                except Exception as e:
                    self.context_dict["dataerrors"]=e
                    self.context = RequestContext(request, self.context_dict)
                    return HttpResponse(self.template.render(self.context))
                    #raise 
            else:
                alls = str(self.pci_insert.errors) #+ str(self.sci_insert.errors)
                self.context_dict["dataerrors"]=self.pci_insert.errors
                self.context = RequestContext(request, self.context_dict)
                #print 'He is not validating', self.pic_insert.errors
                return HttpResponse(self.template.render(self.context))

            if(self.insert_standard.is_valid()):
                try:
                    self.instance_field = self.insert_standard.save(commit=False)
                    self.instance_field.pci=self.pci_returncode                    
                    self.instance_field.save()
                    
                    if("submitsquit" in request.POST):
                        return HttpResponseRedirect("/home/redo/")
                        
                    elif("submitviews" in request.POST):
                        url = "/view/dataview/request/%s/" % str(self.dataset_infor.slug)
                        return HttpResponseRedirect(url)
                        
                    elif("submitsagain" in request.POST):
                        self.path = request.get_full_path()
                        return HttpResponseRedirect(self.path)
                        
                except Exception as e:
                    self.context_dict["dataerrors"]=e
                    self.context = RequestContext(request, self.context_dict)
                    return HttpResponse(self.template.render(self.context))
                    #raise 
                    
            else:
                self.context_dict["dataerrors"]=self.insert_standard.errors 
                self.context = RequestContext(request, self.context_dict)
                return HttpResponse(self.template.render(self.context))
                
        except Exception as e:
            self.context_dict["dataerrors"]=e
            self.context = RequestContext(request, self.context_dict)
            return HttpResponse(self.template.render(self.context))
            #raise 
            
    def insert_cba(self, request, record_slug):
        self.pci_form = self.get_pci_formpost()
        self.sci_form = self.get_sci_formpost()
       
        self.pci_insert = self.pci_form(request.POST, prefix="PCI_Forms")
        self.sci_insert = self.sci_form(request.POST, prefix="SCI_Forms")
        self.gscaform = self.get_GSCAFBForms(post=True) #()
        self.idform = self.get_IDForms(post=True) #(request.POST, prefix="IDForms")
        self.eiform = self.get_EIForms(post=True) #(request.POST, prefix="EIForms")
        
        self.gscaform_insert = self.gscaform(request.POST, prefix="GSCAFBForms")
        self.idform_insert = self.idform(request.POST, prefix="IDForms")
        self.eiform_insert = self.eiform(request.POST, prefix="EIForms")
        self.insert_standard = self.standard_form(request.POST, prefix="standard_forms")
        
        self.datasetrecords = self.get_datarecords()
        self.context_dict = {"datasetforms":self.insert_standard,"datasetrecords":self.datasetrecords,
                                "datasetinput":dataset_infor,
                                "pciforms":self.pci_insert,"sciforms":self.sci_insert, "dataset_active":record_slug,
                                "gscafbforms":self.gscafb_insert, "idforms":self.idform_insert,
                                "ieforms":self.eiform_insert, "userrights":self.dataset_infor
                            }
        self.template =  loader.get_template("datasetrecords.html")
        
        try:
            if(self.pci_insert.is_valid() and self.sci_insert.is_valid()):
                try:
                    self.pci_returncode = self.pci_insert.save()
                    self.sci_returncode = self.sci_insert.save()
                except Exception as e:
                    self.context_dict["dataerrors"]=e
                    self.context = RequestContext(request, self.context_dict)
                    return HttpResponse(self.template.render(self.context))
            else:
                alls = str(self.pci_insert.errors) + str(self.sci_insert.errors)
                self.context_dict["dataerrors"]=alls
                self.context = RequestContext(request, self.context_dict)
                return HttpResponse(self.template.render(self.context))
                
            if(self.gscaform_insert.is_valid() and self.idform_insert.is_valid()):
                self.ret_gscafbform = self.gscaform_insert.save()
                self.ret_idform = self.idform_insert.save()
            else:
                self.context_dict["dataerrors"]=self.gscaform_insert.errors 
                self.context = RequestContext(request, self.context_dict)
                return HttpResponse(self.template.render(self.context))
                
            if(self.eiform_insert.is_valid()):
                self.ret_eiform = self.eiform_insert.save()
            else:
                self.context_dict["dataerrors"]=self.eiform_insert.errors 
                self.context = RequestContext(request, self.context_dict)
                return HttpResponse(self.template.render(self.context))
                
            if(self.insert_standard.is_valid()):
                try:
                    self.instance_field = self.insert_standard.save(commit=False)
                    self.instance_field.pci=self.pci_returncode
                    self.instance_field.sci=self.sci_returncode
                    
                    self.instance_field.save()
                    
                    if("submitsquit" in request.POST):
                        return HttpResponseRedirect("/home/redo/")
                    elif("submitviews" in request.POST):
                        url = "/view/dataview/request/%s/" % str(self.dataset_infor.slug)
                        return HttpResponseRedirect(url)
                    
                    elif("submitsagain" in request.POST):
                        self.path = request.get_full_path()
                        return HttpResponseRedirect(self.path)
                        
                except Exception as e:
                    self.context_dict["dataerrors"]=e
                    self.context = RequestContext(request, self.context_dict)
                    return HttpResponse(self.template.render(self.context)) 
            else:
                self.context_dict["dataerrors"]=self.insert_standard.errors 
                self.context = RequestContext(request, self.context_dict)
                return HttpResponse(self.template.render(self.context))
                
        except Exception as e:
            self.context_dict["dataerrors"]=e 
            self.context = RequestContext(request, self.context_dict)
            return HttpResponse(self.template.render(self.context)) 
                            
    def insert_ib(self, request, dataset_infor, record_slug):
        self.pci_form = self.get_pci_formpost()
        self.pci_insert = self.pci_form(request.POST, prefix="PCI_Forms")
        self.standard_form = self.load_forms_insert(dataset_infor)
        self.insert_standard = self.standard_form(request.POST, prefix="standard_forms")
        
        #print "ACTIVE ", dataset_infor
        self.datasetrecords = self.get_datarecords()
        self.context_dict = {"datasetforms":self.insert_standard,"datasetrecords":self.datasetrecords,
                                "datasetinput":dataset_infor,
                                "pciforms":self.pci_insert,"dataset_active":record_slug,
                            }
        self.template =  loader.get_template("datasetrecords.html")
                    
        if(self.pci_insert.is_valid()):
            try:
                self.pci_returncode = self.pci_insert.save()
            except Exception as e:
                self.context_dict["dataerrors"]=e 
                self.context = RequestContext(request, self.context_dict)
                return HttpResponse(self.template.render(self.context)) 
                #raise
                
            if(self.insert_standard.is_valid()):
                try:
                    self.instance_field = self.insert_standard.save(commit=False)
                    self.instance_field.pci=self.pci_returncode
                    self.instance_field.save()
                    
                    if("submitsquit" in request.POST):
                        return HttpResponseRedirect("/home/redo/")
                        
                    elif("submitviews" in request.POST):
                        url = "/view/dataview/request/%s/" % str(self.dataset_infor.slug)
                        return HttpResponseRedirect(url)
                        
                    elif("submitsagain" in request.POST):
                        self.path = request.get_full_path()
                        return HttpResponseRedirect(self.path)
                        
                except Exception as e:
                    self.context_dict["dataerrors"]=e 
                    self.context = RequestContext(request, self.context_dict)
                    return HttpResponse(self.template.render(self.context))
                    #raise 
            else:
                self.context_dict["dataerrors"]=self.insert_standard.errors 
                self.context = RequestContext(request, self.context_dict)
                return HttpResponse(self.template.render(self.context))
                #raise 
        else:
            self.context_dict["dataerrors"]=self.pci_insert.errors 
            self.context = RequestContext(request, self.context_dict)
            return HttpResponse(self.template.render(self.context))
            #raise 
    
    def insert_cmc(self, request, dataset_infor, record_slug):
        self.standard_form = self.load_forms_insert(dataset_infor)
        self.datasetrecords = self.get_datarecords()
        self.insert = self.standard_form(request.POST, prefix="standard_forms")
        self.context_dict = {"datasetforms":self.insert,"datasetrecords":self.datasetrecords,
                                "datasetinput":dataset_infor,"dataset_active":record_slug,
                            }
        self.template =  loader.get_template("datasetrecords.html")
        try:
            if(self.standard_form):
                try:                   
                    if(self.insert.is_valid()):
                        self.insert.save() 
                        
                        if("submitsquit" in request.POST):
                            return HttpResponseRedirect("/home/dashboard/")
                        elif("submitviews" in request.POST):
                            url = "/view/dataview/request/%s/" % str(self.dataset_infor.slug)
                            return HttpResponseRedirect(url)
                            
                        elif("submitsagain" in request.POST):
                            self.path = request.get_full_path()
                            return HttpResponseRedirect(self.path)
                    else:
                        self.context_dict["dataerrors"]=self.insert.errors 
                        self.context = RequestContext(request, self.context_dict)
                        return HttpResponse(self.template.render(self.context))
                        
                except Exception as e:
                    self.context_dict["dataerrors"]=e
                    self.context = RequestContext(request, self.context_dict)
                    return HttpResponse(self.template.render(self.context))
                    
            else:
                self.context_dict["dataerrors"]="THIS IS A SYSTEM BUG/GLITCH : Report to developers"
                self.context = RequestContext(request, self.context_dict)
                return HttpResponse(self.template.render(self.context))
                
        except Exception as e:
            self.context_dict["dataerrors"]=e
            self.context = RequestContext(request, self.context_dict)
            return HttpResponse(self.template.render(self.context))
            
    def insert_all(self, request, dataset_infor, record_slug):
        try:
            self.pci_insert = self._form_instance(request, self.get_pci_formpost(), prefix="PCI_Forms")
            self.sci_insert = self._form_instance(request, self.get_sci_formpost(), prefix="SCI_Forms")
            self.idi_insert = self._form_instance(request, self.get_IDForms(True), prefix="IDForms")
            self.ie_insert = self._form_instance(request, self.get_EIForms(True), prefix="EIForms")
            self.gscafb_insert = self._form_instance(request, self.get_GSCAFBForms(True), prefix="GSCAFBForms")
            
            try:
                self.standard_form = self.load_forms_insert(dataset_infor)
                self.standard_insert = self._form_instance(request, self.standard_form, prefix="standard_forms")
                
            except Exception as e:
                self.context_dict["dataerrors"]=e
                self.context = RequestContext(request, self.context_dict)
                return HttpResponse(self.template.render(self.context)) 
                
            else:
                self.datasetrecords = self.get_datarecords()
                self.context_dict = {"datasetforms":self.standard_insert,"datasetrecords":self.datasetrecords,
                                                        "datasetinput":dataset_infor,
                                                        "pciforms":self.pci_insert,"sciforms":self.sci_insert, "dataset_active":record_slug,
                                                        "gscafbforms":self.gscafb_insert, "idforms":self.idi_insert,
                                                        "ieforms":self.ie_insert, "userrights":self.dataset_infor
                                    }
                                    
                self.template =  loader.get_template("datasetrecords.html")
                
                #Beginning testing the records if they are valid
                if(self.pci_insert.is_valid()):
                    self.pci_ret_instance = self.pci_insert.save()
                    
                    if(self.sci_insert.is_valid()):
                        self.sci_ret_instance = self.sci_insert.save()
                        
                        if(self.idi_insert.is_valid()):
                            self.id_ret_instance = self.idi_insert.save()
                            
                            if(self.ie_insert.is_valid()):
                                self.ie_ret_instance = self.ie_insert.save()
                                
                                if(self.gscafb_insert.is_valid()):
                                    self.gscafb_ret_instance = self.gscafb_insert.save()
                                    
                                    #Check the final standard form
                                    if(self.standard_insert.is_valid()):
                                        self.ret_standard_intance = self.standard_insert.save(commit=False) #Don't save the changs
                                        
                                        #Save all other following fields
                                        self.ret_standard_intance.pci=self.pci_ret_instance
                                        self.ret_standard_intance.sci=self.sci_ret_instance
                                        self.ret_standard_intance.idi=self.id_ret_instance
                                        self.ret_standard_intance.ei=self.ie_ret_instance
                                        self.ret_standard_intance.gscafb=self.gscafb_ret_instance
                                        
                                        #Finally save all together and and perform the commit
                                        self.ret_standard_intance.save()
                                        
                                        if("submitsquit" in request.POST):
                                            return HttpResponseRedirect("/home/redo/")
                                        elif("submitviews" in request.POST):
                                            url = "/view/dataview/request/%s/" % str(self.dataset_infor.slug)
                                            return HttpResponseRedirect(url)
                                            
                                        elif("submitsagain" in request.POST):
                                            self.path = request.get_full_path()
                                            return HttpResponseRedirect(self.path)
                    
                                    else:
                                        self.context_dict["dataerrors"]=self.standard_insert.errors 
                                        self.context = RequestContext(request, self.context_dict)
                                        return HttpResponse(self.template.render(self.context))
                                else:
                                    self.context_dict["dataerrors"]=self.gscafb_insert.errors 
                                    self.context = RequestContext(request, self.context_dict)
                                    return HttpResponse(self.template.render(self.context))
                            else:
                                self.context_dict["dataerrors"]=self.ie_insert.errors 
                                self.context = RequestContext(request, self.context_dict)
                                return HttpResponse(self.template.render(self.context))
                        else:
                            self.context_dict["dataerrors"]=self.idi_insert.errors 
                            self.context = RequestContext(request, self.context_dict)
                            return HttpResponse(self.template.render(self.context))
                    else:
                        self.context_dict["dataerrors"]=self.sci_insert.errors 
                        self.context = RequestContext(request, self.context_dict)
                        return HttpResponse(self.template.render(self.context))
                else:
                    self.context_dict["dataerrors"]=self.pci_insert.errors 
                    self.context = RequestContext(request, self.context_dict)
                    return HttpResponse(self.template.render(self.context))
                    
        except Exception as e:
            self.context_dict["dataerrors"]=e
            self.context = RequestContext(request, self.context_dict)
            return HttpResponse(self.template.render(self.context))  
            
    def insert_cap(self, request, dataset_infor, record_slug):
        try:
            self.pci_insert = self._form_instance(request, self.get_pci_formpost(), prefix="PCI_Forms")
            self.sci_insert = self._form_instance(request, self.get_sci_formpost(), prefix="SCI_Forms")
            self.idi_insert = self._form_instance(request, self.get_IDForms(True), prefix="IDForms")
            self.ie_insert = self._form_instance(request, self.get_EIForms(True), prefix="EIForms")
            self.gscafb_insert = self._form_instance(request, self.get_GSCAFBForms(True), prefix="GSCAFBForms")
            self.datasetforms = self.load_forms_by_slug(dataset_infor) #self.datasetforms =
            
            try:
                self.standard_form = self.load_forms_insert(dataset_infor)
                self.standard_insert = self._form_instance(request, self.standard_form, prefix="standard_forms")
            except:
                raise 
            else:
                self.datasetrecords = self.get_datarecords()
                self.context_dict = {"datasetforms":self.standard_insert,"datasetrecords":self.datasetrecords,
                                                        "datasetinput":dataset_infor,
                                                        "pciforms":self.pci_insert,"sciforms":self.sci_insert, "dataset_active":record_slug,
                                                        "gscafbforms":self.gscafb_insert, "idforms":self.idi_insert,
                                                        "ieforms":self.ie_insert, "userrights":self.dataset_infor
                                    }
                                    
                self.template =  loader.get_template("datasetrecords.html")

                #Beginning testing the records if they are valid
                if(self.pci_insert.is_valid()):
                    self.pci_ret_instance = self.pci_insert.save()
                    
                    if(self.sci_insert.is_valid()):
                        self.sci_ret_instance = self.sci_insert.save()
                        
                        if(self.idi_insert.is_valid()):
                            self.id_ret_instance = self.idi_insert.save()
                            
                            if(self.ie_insert.is_valid()):
                                self.ie_ret_instance = self.ie_insert.save()
                                
                                if(self.gscafb_insert.is_valid()):
                                    self.gscafb_ret_instance = self.gscafb_insert.save()
                                    
                                    if(self.standard_insert.is_valid()):
                                        self.ret_standard_intance = self.standard_insert.save(commit=False) #Don't save the changs
                                        
                                        #Save all other following fields
                                        self.ret_standard_intance.pci=self.pci_ret_instance
                                        self.ret_standard_intance.sci=self.sci_ret_instance
                                        self.ret_standard_intance.idi=self.id_ret_instance
                                        self.ret_standard_intance.ei=self.ie_ret_instance
                                        self.ret_standard_intance.gscafb=self.gscafb_ret_instance                                        
                                        
                                        #Finally save all together and and perform the commit
                                        self.ret_standard_intance.save()
                                        self.reference = self.get_acc_reference(self.ret_standard_intance)
                                        if(self.reference):
                                            self.ret_standard_intance.Credit_Application_Reference=self.reference
                                            self.ret_standard_intance.save()
                                        else:
                                            self.ret_standard_intance.Credit_Application_Reference = str(self.ret_standard_intance.id) + self.ret_standard_intance.Credit_Account_or_Loan_Product_Type  
                                   
                                        if("submitsquit" in request.POST):
                                            return HttpResponseRedirect("/home/redo/")
                                        elif("submitviews" in request.POST):
                                            url = "/view/dataview/request/%s/" % str(self.dataset_infor.slug)
                                            return HttpResponseRedirect(url)
                                            
                                        elif("submitsagain" in request.POST):
                                            self.path = request.get_full_path()
                                            return HttpResponseRedirect(self.path)
                                    else:
                                        self.context_dict["dataerrors"]=self.standard_insert.errors 
                                        self.context = RequestContext(request, self.context_dict)
                                        return HttpResponse(self.template.render(self.context))
                                else:
                                    self.context_dict["dataerrors"]=self.gscafb_insert.errors 
                                    self.context = RequestContext(request, self.context_dict)
                                    return HttpResponse(self.template.render(self.context))
                            else:
                                self.context_dict["dataerrors"]=self.ie_insert.errors 
                                self.context = RequestContext(request, self.context_dict)
                                return HttpResponse(self.template.render(self.context))
                        else:
                            self.context_dict["dataerrors"]=self.idi_insert.errors 
                            self.context = RequestContext(request, self.context_dict)
                            return HttpResponse(self.template.render(self.context))
                    else:
                        self.context_dict["dataerrors"]=self.sci_insert.errors 
                        self.context = RequestContext(request, self.context_dict)
                        return HttpResponse(self.template.render(self.context))
                else:
                    self.context_dict["dataerrors"]=self.pci_insert.errors 
                    self.context = RequestContext(request, self.context_dict)
                    return HttpResponse(self.template.render(self.context))
        except:
            raise  
          
    def get_acc_reference(self,saved):
        try:
            return accreference.get_reference_number(saved.id, saved.Credit_Account_or_Loan_Product_Type)
        except:
            raise     
        
    def _form_instance(self, request, form, prefix):
        try:
            if(request and form and prefix):
                try:
                    return form(request.POST, prefix=prefix)
                except:
                    raise 
            else:
                return False 
        except:
            raise 
            
class RequestViewData(View):
    @method_decorator(login_required)
    def get(self, request, record_slug, mode=None):

        try:
            #IB_dataview
            if(request.user.is_authenticated()):
                self.record_details = self.load_record_information(record_slug)
                self.models = self.get_models(self.record_details.dataset_record.replace("_", " ", len(self.record_details.dataset_record)))
                self.templates = self.get_model_templates(self.record_details.dataset_record.replace("_", " ", len(self.record_details.dataset_record)))
               
                if(self.templates is None):
                    self.data_view_template = self.load_template()
                else:
                    self.data_view_template = self.load_template(self.templates)

                if(self.data_view_template):

                    if(self.models is not None):
                        self.rendered = self.process_data_context(request, self.data_view_template, self.models, record_slug, mode)
                        return HttpResponse(self.rendered)
                    else:
                        self.rendered = self.process_data_context(request, self.data_view_template, self.models, record_slug, mode)
                        return HttpResponse(self.rendered)
                else:
                    pass
            else:
                return HttpResponseRedirect("/")
        except Exception as e:
            self.datasetrecords = self.get_datarecords()
            self.template = load_exception_template()
            self.context = RequestContext(request, {"datasetrecords":self.datasetrecords, "Error":e,
                                                    "internalserver":"Internal Server Error!"
                                          })
            return HttpResponse(self.template.render(self.context))

    def load_template(self, template):
        try:

            if(template):
                return loader.get_template(template)
            else:
                return loader.get_template("dataview.html")
        except:# TemplateDoesNotExists:
            raise
            
    def load_user_creds(self, request):
        try:
            if(request.user.is_superuser):
                return True
            else:
                return usermodels.CreditInstitutionStaff.objects.get(username=request.user)
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
            
    def load_record_information(self, slug):
        """
        Load and return the information of any
        record.
        """
        try:
            return record_models.Dataset.objects.get(slug=slug)
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

    def _filter_records(self, model_db_records, get_new=True):
        """
        Filter and return new or old records.
        """
        if(get_new):
            test_all = model_db_records.objects.all()
            if(test_all):
                return model_db_records.objects.filter(date__gte=searchfilters.get_first_filter_date(), date__lte=searchfilters.get_last_filter_date())
            else:
                return test_all
        else:
            return model_db_records.objects.filter(date__lte=searchfilters.get_first_filter_date())
                
    def process_data_context(self, request, template, datamodel, record_slug, mode=None):
        self.delete_mode = True
        self.datasetrecords = self.get_datarecords()
        self.error_context = {"datasetrecords":self.datasetrecords, "datasetview":record_slug,
                                "basetitle":mytitle, "who":record_slug
                             }
        try:
            if(mode == "True"):
                self.delete_mode=True
            else:
                self.delete_mode=False
                
            self.parsed_fields = self.parse_model_fields(datamodel)
            #self.data_available = datamodel.objects.all()
            self.data_available = self._filter_records(datamodel)
            self.datasetrecords = self.get_datarecords()
            self.get_modelcount = self.get_models(self.record_details.dataset_record.replace("_", " ", len(self.record_details.dataset_record)))
            self.available_data = self.data_available.count() #self.get_modelcount.objects.all().count()
            self.now = time.ctime()
            '''
            self.paginatator = Paginator(self.data_available, self.available_data)
            self.now = time.ctime()
            self.next_page = request.GET.get("page")
            
            try:
                self.page_obj = self.paginatator.page(self.next_page)
            except PageNotAnInteger:
                self.page_obj = self.paginatator.page(1)
            except EmptyPage:
                self.page_obj = self.paginatator.page(self.paginatator.num_pages)
            '''
            self.data_rights = None 
            #remove the underscore on data
            self.remove_underscore = self.exclude_pci_sci(self.parsed_fields)
            self.userdetails = self.load_user_creds(request)
            
            if(self.userdetails == True):
                pass 
            else:
                self.data_rights = self.userdetails.data_access_rights.all()

            
            # COUNT OLD RECORDS
            self.old_records = self._filter_records(datamodel, get_new=False)
            self.count_old = self.old_records.count()
            self.context = RequestContext(request,{"modelfields":self.remove_underscore, "availabledata":self.data_available,
                                    "view":False, "displaytimes":self.now, "datacount":self.available_data,
                                    "datasetrecords":self.datasetrecords, "who":record_slug, "basetitle":mytitle,
                                    "nextpage":self.available_data, "deletemode":self.delete_mode,"datasetview":record_slug,
                                    "user":request.user, "userrights":self.data_rights, "oldrecordscount":self.count_old,
                                    "oldrecords":self.old_records
                                   })

            try:
                return template.render(self.context)
            except Exception as e:
                self.error_context["viewerror"]=e
                return template.render(self.error_context)
                #raise 

        except Exception as e:
            self.error_context["viewerror"]=e
            return HttpResponse(template.render(self.error_context))
    
    def exclude_pci_sci(self, model_data):
        self.cleaned_field = [ ]
        for m in model_data:
            if m == "pci":
                pass 
            elif(m == "sci"):
                pass 
            elif(m == "slug"):
                pass 
            elif(m == "gscafb"):
                pass 
            elif(m == "Branch_Identification_Code"):
                pass
            elif(m == "Client_Consent_flag"):
                pass 
            elif(m == "Credit_Application_Status"):
                pass 
            elif(m == "Credit_Amount"):
                pass 
            elif(m == "Credit_Account_Date"):
                pass 
            elif(m == "Cheque_Account_Opened_Date"):
                pass 
            elif(m == "Cheque_Account_Classification"):
                pass 
            elif(m == "Guarantee_Type"):
                pass 
            elif(m == "Guarantor_Type"):
                pass 
            elif(m == "Collateral_Type_Identification"):
                pass 
            elif(m == "Collateral_Reference_Number"):
                pass 
            elif(m == "validated"):
                pass 
            elif(m == "borrower_stake_details"):
                pass 
            elif(m == "Stakeholder_Category"):
                pass 
            elif(m == "Cheque_Account_Reference_Number"):
                pass 
            elif(m == "Cheque_Account_Reference_Number"):
                pass 
            elif(m == "PI_Identification_Code"):
                pass 
           
            elif(m == "borrower_stake"):
                pass 
            elif(m == "Sub_Category_Code"):
                pass 
            elif(m == "Incident_Date"):
                pass 
            elif(m == "idi"):
                pass 
            elif(m == "ei"):
                pass 
            elif(m == "date"):
                pass 
            else:
                self.cleaned_field.append(m)        
        return self.cleaned_field
        
    def parse_model_fields(self, model_data):
        """
        Returns the fields coresponding to particular models.
        """
        self.fields = [ ]
        self.mfields = model_data._meta.fields

        for field in self.mfields:
            if field.name in self.fields:
                pass
            else:
                if(len(self.fields) == 8):
                    pass 
                else:
                    self.fields.append(field.name)

        #return the model fields
        return self.fields

    def get_models(self, dataset):
        try:
            if(dataset == "FINANCIAL MALPRACTICE DATA"):
                return datamodels.FINANCIAL_MALPRACTICE_DATA
            elif(dataset == "COLLATERAL CREDIT GUARANTOR"):
                return datamodels.COLLATERAL_CREDIT_GUARANTOR
            elif(dataset == "COLLATERAL MATERIAL COLLATERAL"):
                return datamodels.COLLATERAL_MATERIAL_COLLATERAL
            elif(dataset == "BORROWERSTAKEHOLDER"):
                return datamodels.BORROWERSTAKEHOLDER
            elif(dataset == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return datamodels.PARTICIPATINGINSTITUTIONSTAKEHOLDER
            elif(dataset == "BOUNCEDCHEQUES"):
                return datamodels.BOUNCEDCHEQUES
            elif(dataset == "CREDIT APPLICATION"):
                return datamodels.CREDIT_APPLICATION
            elif(dataset == "CREDITBORROWERACCOUNT"):
                return datamodels.CREDITBORROWERACCOUNT
            elif(dataset == "INSTITUTION BRANCH"):
                self.template = "IB_dataview.html"
                return datamodels.INSTITUTION_BRANCH
            elif(dataset == "PARTICIPATING INSTITUTION"):
                return datamodels.PARTICIPATING_INSTITUTION
        except:
            raise

    def get_model_templates(self, dataset):
        try:
            if(dataset == "FINANCIAL MALPRACTICE DATA"):
                return "fmd_dataview.html"
            elif(dataset == "COLLATERAL CREDIT GUARANTOR"):
                return "ccg_dataview.html"
            elif(dataset == "COLLATERAL MATERIAL COLLATERAL"):
                return "cmc_dataview.html"
            elif(dataset == "BORROWERSTAKEHOLDER"):
                return "bs_dataview.html"
            elif(dataset == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return "pis_dataview.html"
            elif(dataset == "BOUNCEDCHEQUES"):
                return "bc_dataview.html"
            elif(dataset == "CREDIT APPLICATION"):
                return "cp_dataview.html"
            elif(dataset == "CREDITBORROWERACCOUNT"):
                return "cba_dataview.html"
            elif(dataset == "INSTITUTION BRANCH"):
                self.templates = "IB_dataview.html"
                return self.templates
            elif(dataset == "PARTICIPATING INSTITUTION"):
                return "pi_dataview.html"
        except:
            raise

#-----view for the appendix----
class AppendixView(View):
    @method_decorator(login_required)
    def get(self, request):
        try:
            if(request.user.is_authenticated()):
                if(request.user.is_superuser):
                    self.admin_template = self.load_superuser_template()
                    if(self.admin_template):
                        self.code = self.load_branchcode_forms()
                        self.emailform = self.get_email_form()
                        self._sftp_forms = self.sftp_forms()
                        self.rendered = self.render_appendix_context(request, self.admin_template, code=self.code, 
                                                emailform=self.emailform, sftp_forms=self.sftp_forms)
                        if(self.rendered):
                            return HttpResponse(self.rendered)
                        else:
                            return HttpResponseServerError("Failed to perform request")
                    else:
                        return HttpResponseServerError("An error occured while processing data")
                else:
                    self.templates = self.get_appendix_template()
                    self.users =  self.load_user_creds(request) 
                    self.data_rights = self.users.data_access_rights.all()
                    self.code = self.load_branchcode_forms()
                    self.emailform = self.get_email_form()
                    self._sftp_forms = self.sftp_forms()
                    
                    self.rendered = self.render_appendix_context(request, self.templates, staff=self.users,
                                                code=self.code, emailform=self.emailform, sftp_forms=self.sftp_forms)
                    if(self.rendered):
                        return HttpResponse(self.rendered)
            else:
                return HttpResponseRedirect("/")
        except:
            self.datasetrecords = self.get_datarecords()
            self.template = load_exception_template()
            self.context = RequestContext(request, {"datasetrecords":self.datasetrecords, "Error":e,
                                                    "internalserver":"Internal Server Error!"
                                          })
            return HttpResponse(self.template.render(self.context))

    def get_pi_form(self):
        return bforms.PIIdentificationCodeForm()
        
    def get_email_form(self):
        try:
            return bforms.EmailForm()
        except:
            raise 
            
    def sftp_forms(self):
        try:
            return bforms.SFTPForm()
        except:
            raise 
            
    def load_default_settings(self):
        return branchmodels.DefaultHeaders.objects.all()
        
    def load_branchcode_forms(self):
        try:
            return bforms.BranchCodeForms()
        except:
            raise
            
    def load_superuser_template(self):
        try:
            return loader.get_template("admindashboard.html")
        except:
            raise 
            
    def parse_model_fields(self, data):
        self.fields = [ ]
        self.mfields = data._meta.fields

        for model_fields in self.mfields:
                if(model_fields.name in self.fields):
                    pass
                else:
                    self.fields.append(model_fields.name)

        return self.fields

    def get_appendix_template(self, *template):
        """
        Load the template for the appendix
        """
        try:
            if(template):
                return loader.get_template(template)
            else:
                return loader.get_template("nonsuperuserdashboard.html")
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
            
    def render_appendix_context(self, request, template, staff=None, code=None, emailform=None, sftp_forms=None):
        """
        Load the contexts and return the rendered.
        """
        try:
            self.headersettingsnew = True 
            self.user = request.user
            self.datasetrecords = self.get_datarecords()
            self.headerforms = None 
            self.userdetails = self.load_user_creds(request)
            self.rights = None 
            #self.branchsetting = bforms.DefaultHeadersForms()
            self.hset = 0 
            
            if(self.userdetails == True):
                pass 
            else:
                self.rights = self.userdetails.data_access_rights.all()
                
          
            try:
                self._piforms = self.filter_settings_ret_piform() #.get("Form")
                self._piformsid = self.filter_settings_ret_piform() #.get("ID")
                #print "FORM ", self._piforms
                if(isinstance(self._piforms, dict)):
                    self._piforms = self._piforms.get("Form")

                if(isinstance(self._piformsid, dict)):
                    self._piformsid = self._piformsid.get("ID")
                    
                self.context = RequestContext(request, {"basetitle":"Data processing system", "datasetrecords":self.datasetrecords,
                                                        "user":self.user, "basetitle":mytitle, 
                                                        "userrights":self.rights, "codeform":code, "emailform":emailform,
                                                        "sftp_forms":sftp_forms, "staff":staff,
                                                        "piforms":self._piforms, "PIFORMID":self._piformsid
                                                    })
                                
                return template.render(self.context)
            except IndexError as error:
                raise 
                
        except:
            raise
            
    def filter_settings_default(self):
        """
        Default settings.
        """
        self.idlist = []
        self.default = branchmodels.DefaultHeaders.objects.all() #.filter(testfield=12).order_by('-id')[0]
        self.hides = []
        if(self.default):
            for ids in self.default:
                self.idlist.append(ids.id)
                self.hides.append(ids.default_headers.id)
                
            self.hset = branchmodels.DefaultHeaders.objects.get(id=min(self.idlist))
            return {"Form":bforms.DefaultHeadersForms(instance=self.hset), "ID":min(self.idlist), "DEFAULTID":min(self.hides)}
        else:
            #return {"Form":None, "ID":None, "DEFAULTID":None}
            return self.bforms.DefaultHeadersForms()
                            
    def filter_settings_ret_piform(self):
        """
        """
        self.ids = []
        self.all_rec = branchmodels.PIIdentificationCode.objects.all()
        if(self.all_rec):
            for rec in self.all_rec:
                self.ids.append(rec.id)
            self.all_id = branchmodels.PIIdentificationCode.objects.get(id=min(self.ids))
            return {"Form":bforms.PIIdentificationCodeForm(instance=self.all_id), "ID":min(self.ids)}
        else:
            #return {"Form":None, "ID":None}
            return bforms.PIIdentificationCodeForm()
            
    def filter_modeldata(self, model):
        try:
            if(model):
                try:
                    availabledata = model.objects.all().count()
                    return availabledata
                except:
                    pass
            else:
                pass
        except:
            pass
            
            
    def get_models(self, dataset):
        try:
            if(dataset == "FINANCIAL MALPRACTICE DATA"):
                return datamodels.FINANCIAL_MALPRACTICE_DATA
            elif(dataset == "COLLATERAL CREDIT GUARANTOR"):
                return datamodels.COLLATERAL_CREDIT_GUARANTOR
            elif(dataset == "COLLATERAL MATERIAL COLLATERAL"):
                return datamodels.COLLATERAL_MATERIAL_COLLATERAL
            elif(dataset == "BORROWERSTAKEHOLDER"):
                return datamodels.BORROWERSTAKEHOLDER
            elif(dataset == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return datamodels.PARTICIPATINGINSTITUTIONSTAKEHOLDER
            elif(dataset == "BOUNCEDCHEQUES"):
                return datamodels.BOUNCEDCHEQUES
            elif(dataset == "CREDIT APPLICATION"):
                return datamodels.CREDIT_APPLICATION
            elif(dataset == "CREDITBORROWERACCOUNT"):
                return datamodels.CREDITBORROWERACCOUNT
            elif(dataset == "INSTITUTION BRANCH"):
                return datamodels.INSTITUTION_BRANCH
            elif(dataset == "PARTICIPATING INSTITUTION"):
                return datamodels.PARTICIPATING_INSTITUTION
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
