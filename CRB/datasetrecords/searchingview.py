from django.shortcuts import render, render_to_response
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
#from datasetsystem import processcsvs
from reportlab.pdfgen import canvas
import datetime
import time
from django.forms.models import inlineformset_factory
import importlib
from datasets import models as record_models
from datasetrecords import models as datamodels
from datasetrecords import formsdisabled as dataset_forms 
from datasetrecords import loadmodels
import simplejson

import forms

mytitle = "CRB Data"

def get_datarecords():
        """
        Return all available dataset records.
        """
        try:
            return record_models.Dataset.objects.all()
        except:
            raise
            
class RecordSearching(View):
    def get(self, request,record):
        try:
            self.rendered_context = self.process_context(request, record)
            if(self.rendered_context):
                try:
                    return HttpResponse(self.rendered_context)
                except:
                    raise 
            else:
                return HttpResponseServerError("FAILURE")
        except:
            raise 
    
    def load_search_template(self, template):
        if(len(template)):
            try:
                return loader.get_template(template)
            except:
                raise 
        else:
            return False 

    def process_context(self, request, record):
        try:
            self.template = self.load_search_template("searchpage.html")
            if(self.template):
                try:
                    self.datasetrecords = get_datarecords()
                    
                    self.context = RequestContext(request, {"basetitle":mytitle,"datasetrecords":self.datasetrecords,
                                                            "records_to_search":record 
                                                            })
                    return self.template.render(self.context)
                except:
                    raise 
            else:
                return None 
        except:
            raise 
                
                
class RecordSearchingAJAX(View):
    def get(self, request, record):
        try:
            self.search_records = request.GET.get("dataset", "")
            self.model = self.load_module_modules(record)
            if(self.model == None):
                pass 
            else:
                self.allrecords = self.load_records_in_model(self.model)
            return HttpResponse("works")
        except:
            raise 
    
    
    def load_search_template(self, template):
        if(len(template)):
            try:
                return loader.get_template(template)
            except:
                raise 
        else:
            return False 

    def process_context(self, request, record):
        try:
            self.template = self.load_search_template("searchpage.html")
            if(self.template):
                try:
                    self.datasetrecords = get_datarecords()
                    
                    self.context = RequestContext(request, {"basetitle":mytitle,"datasetrecords":self.datasetrecords,
                                                            "records_to_search":record 
                                                            })
                    return self.template.render(self.context)
                except:
                    raise 
            else:
                return None 
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
                

class ClientDetailsSearching(View):
    def get(self, request, record_slug, recordID, clientID, status):
        try:
            return HttpResponse(self.process_context(request, record_slug, recordID, clientID, status))
        except:
            raise 
    
    def load_search_template(self, template):
        if(len(template)):
            try:
                return loader.get_template(template)
            except:
                raise 
        else:
            return False 

    def process_context(self, request, record_slug, recordID, clientID, status):
        self.datasetrecords = get_datarecords()
        try:
            if(record_slug == "credit_application"):
                self.record_details = self.load_record_information(record_slug)
                self.forms = self.get_insert_forms(self.record_details.dataset_record.replace("_", " ", len(self.record_details.dataset_record)))
                self.model = self.get_models(self.record_details.dataset_record.replace("_", " ", len(self.record_details.dataset_record)))
                self.updating_instance = self.get_model_data(self.model, recordID)
                self.formset = self.load_form_instance(self.forms, self.updating_instance, prefix="standard_forms")
                
                self.pciform = self.get_PCIForms()
                self.sciform = self.get_SCIForms()
                self.ieform = self.get_EIForms()
                self.idform = self.get_IDForms()
                self.gscafbforms = self.get_GSCAFBForms()
                self.client_detailsformset = self.get_clientforms()

                self.pciformset = self.load_form_instance(self.pciform, self.updating_instance.pci, prefix="PCI_Forms")
                self.sciformset = self.load_form_instance(self.sciform, self.updating_instance.sci, prefix="SCI_Forms")
                self.ieformset = self.load_form_instance(self.ieform, self.updating_instance.ei, prefix="EIForms")
                self.idformset = self.load_form_instance(self.idform, self.updating_instance.idi, prefix="IDForms")
                self.gscafbformsset = self.load_form_instance(self.gscafbforms, self.updating_instance.gscafb, prefix="GSCAFBForms")
                self.user_detailsformset = self.load_form_instance(self.client_detailsformset, self.updating_instance.client_details, prefix="ClientDForms")

                #if(self.updating_instance.gscafb.id)
                try:
                    self.pcid = self.updating_instance.pci.id
                    self.sciid = self.updating_instance.sci.id
                    self.ieid = self.updating_instance.ei.id
                    self.idi = self.updating_instance.idi.id
                    self.gsid = self.updating_instance.gscafb.id
                    self.clientupdatid = self.updating_instance.client_details.id
                except Exception as e:
                    self.template = loader.get_template('datasetrecordsupdate.html')
                    self.context = RequestContext(request, {"generrors":e})
                    return HttpResponse(self.template.render(self.context)) 
                try:
                    self.context = RequestContext(request, {"datasetforms":self.formset, "datasetrecords":self.datasetrecords,
                                                            "dataid":recordID, "datasetupdate":"Updating Records",
                                                            'pciforms':self.pciformset, 'sciforms':self.sciformset,
                                                            'ieforms':self.ieformset, 'idforms':self.idformset,
                                                            'gscafbforms':self.gscafbformsset,"dataset_active":record_slug,
                                                            "pciID":self.pcid, "sciID":self.sciid, "ieid":self.ieid,
                                                            "idi":self.idi, "gsid":self.gsid, "title":"CRB",
                                                            "clientform":self.user_detailsformset, "clientupdatingID":self.clientupdatid,
                                                            "updating_instance":self.updating_instance, "viewtype":status
                                                  })
                except Exception as e:
                    self.template = loader.get_template('datasetrecordsupdate.html')
                    self.context = RequestContext(request, {"generrors":e})
                    return HttpResponse(self.template.render(self.context)) 
                else:
                    self.template = self.get_template()
                    return self.template.render(self.context)
                    
            else: #(record_slug == "creditborroweraccount"):
                self.record_details = self.load_record_information(record_slug)
                self.forms = self.get_insert_forms(self.record_details.dataset_record.replace("_", " ", len(self.record_details.dataset_record)))
                self.model = self.get_models(self.record_details.dataset_record.replace("_", " ", len(self.record_details.dataset_record)))
                self.updating_instance = self.get_model_data(self.model, recordID)
                self.formset = self.load_form_instance(self.forms, self.updating_instance, prefix="standard_forms")
                
                self.pciform = self.get_PCIForms()
                self.sciform = self.get_SCIForms()
                self.ieform = self.get_EIForms()
                self.idform = self.get_IDForms()
                self.gscafbforms = self.get_GSCAFBForms()
                self.client_detailsformset = self.get_clientforms()

                self.pciformset = self.load_form_instance(self.pciform, self.updating_instance.Borrowers_Client_Number.pci, prefix="PCI_Forms")
                self.sciformset = self.load_form_instance(self.sciform, self.updating_instance.Borrowers_Client_Number.sci, prefix="SCI_Forms")
                self.ieformset = self.load_form_instance(self.ieform, self.updating_instance.Borrowers_Client_Number.ei, prefix="EIForms")
                self.idformset = self.load_form_instance(self.idform, self.updating_instance.Borrowers_Client_Number.idi, prefix="IDForms")
                self.gscafbformsset = self.load_form_instance(self.gscafbforms, self.updating_instance.Borrowers_Client_Number.gscafb, prefix="GSCAFBForms")
                self.user_detailsformset = self.load_form_instance(self.client_detailsformset, self.updating_instance.Borrowers_Client_Number.client_details, prefix="ClientDForms")

                #if(self.updating_instance.gscafb.id)
                try:
                    self.pcid = self.updating_instance.Borrowers_Client_Number.pci.id
                    self.sciid = self.updating_instance.Borrowers_Client_Number.sci.id
                    self.ieid = self.updating_instance.Borrowers_Client_Number.ei.id
                    self.idi = self.updating_instance.Borrowers_Client_Number.idi.id
                    self.gsid = self.updating_instance.Borrowers_Client_Number.gscafb.id
                    self.clientupdatid = self.updating_instance.Borrowers_Client_Number.client_details.id
                except Exception as e:
                    self.template = loader.get_template('datasetrecordsupdate.html')
                    self.context = RequestContext(request, {"generrors":e})
                    return HttpResponse(self.template.render(self.context)) 
                try:
                    self.context = RequestContext(request, {"datasetforms":self.formset, "datasetrecords":self.datasetrecords,
                                                            "dataid":recordID, "datasetupdate":"Updating Records",
                                                            'pciforms':self.pciformset, 'sciforms':self.sciformset,
                                                            'ieforms':self.ieformset, 'idforms':self.idformset,
                                                            'gscafbforms':self.gscafbformsset,"dataset_active":record_slug,
                                                            "pciID":self.pcid, "sciID":self.sciid, "ieid":self.ieid,
                                                            "idi":self.idi, "gsid":self.gsid, "title":"CRB",
                                                            "clientform":self.user_detailsformset, "clientupdatingID":self.clientupdatid,
                                                            "updating_instance":self.updating_instance, "viewtype":status
                                                  })
                except Exception as e:
                    self.template = loader.get_template('datasetrecordsupdate.html')
                    self.context = RequestContext(request, {"generrors":e})
                    return HttpResponse(self.template.render(self.context)) 
                else:
                    self.template = self.get_template()
                    return self.template.render(self.context)
        except:
            raise

    def indexer(self, records_to_index):
        """
        Given a bunch of recordds successfuly index,
        them.
        """
        try:
            self.appendlist = {}
            
            self.firstindex = records_to_index.index(",")
            self.recordtype = records_to_index[:self.firstindex]
            self.appendlist["recordtype"]=(self.recordtype.strip("[").strip("").lstrip().rstrip())
            
            #Save the new records
            self.records_to_index = records_to_index[self.firstindex:]

            #Strip the first ,
            self.records_to_index = self.records_to_index.strip(",")

            #Perform the second index
            self.second_indx = self.records_to_index.index(",")
            self.userid = self.records_to_index[:self.second_indx]
            self.appendlist["ID"]=(self.userid)
            
            # Save our current saving index
            self.records_to_index = self.records_to_index[self.second_indx:]
            self.appendlist["REF"]=(self.records_to_index.strip("]").strip(",").lstrip().rstrip())
            return self.appendlist
        except:
            raise

    def loadgscafbinstance(self, form, gscafb):
        try:
            return form(instance=gscafb.gscafb)
        except:
            raise 
            
    def loadidinstance(self,form, idi):
        try:
            return form(instance=idi.idi)
        except:
            raise 
            
    def loadieinstance(self, form, ei):
        try:
            return form(instance=ei.ei)
        except:
            raise 
            
    def loadsciinstance(self, form, sci):
        try:
            return form(instance=sci.sci)
        except:
            raise 
            
    def loadpciinstance(self, form, pci):
        try:
            return form(instance=pci.pci)
        except:
            raise 
                
    def load_form_instance(self, form, dataupdating, prefix):
        try:
            #print "FORM IS ", form 
            return form(instance=dataupdating, prefix=prefix)
        except:
            raise

    def getforms(self, dataset):
        try:
            if(dataset == "FINANCIAL MALPRACTICE DATA"):
                return dataset_forms.FRA_Forms(prefix="standard_forms")
            elif(dataset == "COLLATERAL CREDIT GUARANTOR"):
                return dataset_forms.CCG_Forms(prefix="standard_forms")
            elif(dataset == "COLLATERAL MATERIAL COLLATERAL"):
                return dataset_forms.CMC_Forms(prefix="standard_forms")
            elif(dataset == "BORROWERSTAKEHOLDER"):
                return dataset_forms.BS_Forms(prefix="standard_forms")
            elif(dataset.upper() == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return dataset_forms.PIS_Forms(prefix="standard_forms")
            elif(dataset == "BOUNCEDCHEQUES"):
                return dataset_forms.BC_Forms(prefix="standard_forms")
            elif(dataset == "CREDIT APPLICATION"):
                return dataset_forms.CAP_Forms(prefix="standard_forms")
            elif(dataset == "CREDITBORROWERACCOUNT"):
                return dataset_forms.CBA_Forms(prefix="standard_forms")
            elif(dataset == "INSTITUTION BRANCH"):
                return dataset_forms.IB_Forms(prefix="standard_forms")
            elif(dataset == "PARTICIPATING INSTITUTION"):
                return dataset_forms.PI_Forms(prefix="standard_forms")
            else:
                return None

        except:
            raise
            
    def get_template(self, *template):
        try:
            if(template):
                try:
                    return loader.get_template(template)
                except TemplateDoesNotExists:
                    raise
            else:
                #return loader.get_template("datasetrecordview.html")
                return loader.get_template("datasetrecordsupdate.html")
        except:
            raise

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
            elif(dataset == "BOUNCEDCHEQUES"):
                return datamodels.BOUNCEDCHEQUES
            elif(dataset == "CREDIT APPLICATION"):
                return datamodels.CREDIT_APPLICATION
            elif(dataset == "CREDITBORROWERACCOUNT"):
                return datamodels.CREDITBORROWERACCOUNT
            elif(dataset == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return datamodels.PARTICIPATINGINSTITUTIONSTAKEHOLDER
           
        except:
            raise

    def load_forms_insert(self, record_info):
        """
        Return the forms which will be used.
        """
        try:
            if(record_info.dataset_record == "COLLATERAL_MATERIAL_COLLATERAL"):
                return dataset_forms.CMC_Forms
            elif(record_info.dataset_record == "BORROWERSTAKEHOLDER"):
               return dataset_forms.BS_Forms
            elif(record_info.dataset_record == "BOUNCEDCHEQUES"):
                return dataset_forms.BC_Forms 
            elif(record_info.dataset_record == "COLLATERAL_CREDIT_GUARANTOR"):
                return dataset_forms.CCG_Forms
            elif(record_info.dataset_record == "CREDITBORROWERACCOUNT"):
                return dataset_forms.CBA_Forms 
            elif(record_info.dataset_record == "CREDIT_APPLICATION"):
                return dataset_forms.CAP_Forms
            elif(record_info.dataset_record == "FINANCIAL_MALPRACTICE_DATA"):
                return dataset_forms.FRA_Forms
            elif(record_info.dataset_record == "INSTITUTION_BRANCH"):
                return dataset_forms.IB_Forms
            elif(record_info.dataset_record == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return dataset_forms.PIS_Forms
            elif(record_info.dataset_record == "PARTICIPATING_INSTITUTION"):
                return dataset_forms.PI_Forms
            else:
                return False
        except:
            raise

    def query_pci_sci_byID(self, pci_sci_model, ID):
        """
        Return the pcidata record given the ID
        """
        try:
            if(pci_sci_model and ID):
                try:
                    return pci_sci_model.objects.get(id=int(ID))
                except:
                    raise 
            else:
                return False 
        except:
            raise

    def get_PCIModel(self):
        return datamodels.PCI

    def get_clientModel(self):
        return datamodels.ClientInformation
        
    def get_SCIModel(self):
        return datamodels.SCI
        
    def get_PCIForms(self):
        return dataset_forms.PCIForms

    def get_clientforms(self):
        return dataset_forms.ClientInformation_Forms
              
    def get_SCIForms(self):
        return dataset_forms.SCIForms
        
    def get_EIForms(self):
        return dataset_forms.EIForms
        
    def get_IDForms(self):
        return dataset_forms.IDForms
    
    def get_GSCAFBForms(self):
        return dataset_forms.GSCAFBForms
        
    def get_GSCAFB(self):
        return datamodels.GSCAFB_INFORMATION
        
    def get_EImodels(self):
        return datamodels.EMPLOYMENT_INFORMATION
        
    def get_IDmodel(self):
        return datamodels.IDENTIFICATION_INFORMATION

    def load_record_information(self, slug):
        """
        Load and return the information of any
        record.
        """
        try:
            return record_models.Dataset.objects.get(slug=slug)
        except:
            raise

    def get_insert_forms(self, dataset):
        try:
            if(dataset == "FINANCIAL MALPRACTICE DATA"):
                return dataset_forms.FRA_Forms
            elif(dataset == "COLLATERAL CREDIT GUARANTOR"):
                return dataset_forms.CCG_Forms
            elif(dataset == "COLLATERAL MATERIAL COLLATERAL"):
                return dataset_forms.CMC_Forms
            elif(dataset == "BORROWERSTAKEHOLDER"):
                return dataset_forms.BS_Forms
            elif(dataset == "BOUNCEDCHEQUES"):
                return dataset_forms.BC_Forms
            elif(dataset == "CREDIT APPLICATION"):
                return dataset_forms.CAP_Forms
            elif(dataset == "CREDITBORROWERACCOUNT"):
                return dataset_forms.CBA_Forms
            elif(dataset == "PARTICIPATINGINSTITUTIONSTAKEHOLDER"):
                return dataset_forms.PIS_Forms
        except:
            raise

    def get_model_data(self, model, ID):
        try:
            if(model):
                if(ID):
                    self.model_data = model.objects.get(id=ID)
                    if(self.model_data):
                        return self.model_data
                    else:
                        return False
                else:
                    return None
            else:
                return None
        except:
            raise   

class ViewBorrowingHistory(View):
    def get(self, request, record_slug, recordID, clientID):
        try:
            return HttpResponse(self.rendered_details(request, record_slug, recordID, clientID))
        except:
            raise

    def rendered_details(self, request, record_slug, recordID, clientID):
        try:
            self.datasetrecords = get_datarecords()
            self.template = loader.get_template("borrowerhistory.html")
            self.queryhistory = self.query_record(recordID)
            self.context = RequestContext(request, {"basetitle":"Borrower History", "datasetrecords":self.datasetrecords,
                                                    "clientID":clientID, "bhistory":self.queryhistory
                                                    })
            return self.template.render(self.context)
         
        except:
            raise 

    def query_record(self, record_id):
        try:
            return datamodels.CREDIT_APPLICATION.objects.get(id=int(record_id))
        except:
            raise

"""
gscafb = models.OneToOneField(GSCAFB_INFORMATION, blank=True, null=True, unique=False)
idi = models.OneToOneField(IDENTIFICATION_INFORMATION, blank=True, null=True, unique=False)
ei = models.OneToOneField(EMPLOYMENT_INFORMATION, blank=True, null=True, unique=False)
pci = models.OneToOneField(PCI,blank=True, null=True, unique=False)
sci = models.OneToOneField(SCI,blank=True, null=True, unique=False)
history = models.ManyToManyField(BorrowerHistory, blank=False)
howmanytimes = models.OneToOneField(BorrowingTimes, blank=True, null=True)
""" 
class APTPurge(View):
    def get(self, request, record):
        try:
            self.record_details = self.load_module_modules(record)
            #return HttpResponse("Wangolo")
            if(record == "credit_application"):
                self.all_records = self.record_details.objects.all()
                try:
                    for records in self.all_records:
                        try:
                            records.delete()
                            records.gscafb.delete()
                            records.idi.delete()
                            records.ei.delete()
                            records.pci.delete()
                            records.sci.delete()
                            if(records.history):
                                allmany = records.history.all()
                                if(allmany):
                                    for m in allmany:
                                        records.history.remove(m)
                            records.howmanytimes.delete()
                        except ValueError as error:
                            continue
                            
                    return HttpResponseRedirect(self.record_view_path(record))
                except ValueError as error:
                    print error
                    pass 
                    
            elif(record == "bouncedcheques"):
                self.all_records = self.record_details.objects.all()
                for records in self.all_records:
                    records.delete()
                return HttpResponseRedirect(self.record_view_path(record))
                
            elif(record == "creditborroweraccount"):
                self.all_records = self.record_details.objects.all()
                for records in self.all_records:
                    records.delete()
                return HttpResponseRedirect(self.record_view_path(record))
            else:
                return HttpResponse("Records do not support deleting.")
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

    def record_view_path(self, record):
        return "/view/dataview/request/%s/" % record 
