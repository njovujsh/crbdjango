from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError,JsonResponse
from django.template import Context, loader, RequestContext
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.views import login
from datasets import models as record_models
from userlogin import forms as userloginforms
from userlogin import models as usermodels
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from fraudcategory.subsystems import allmodules
import simplejson
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class HandleCategory(View):
    @method_decorator(login_required)
    def get(self, request):
        if(request.is_ajax()):
            self.fraud_type = request.GET.get("fraudtype", "")
            try:
                self.fraud_module = self.load_module_by_type(self.fraud_type)
                if(self.fraud_module):
                    try:
                        self.load_fraud_category = self.load_sub_category(self.fraud_module)
                        if(self.load_fraud_category):
                            try:
                                self.module_category = self.load_fraud_category.get(str(self.fraud_type))
                            except KeyError as error:
                                raise
                            else:
                                return HttpResponse(simplejson.dumps(self.module_category), content_type="application/json")
                        else:
                            return HttpResponse(simplejson.dumps({"error":"None"}),content_type="application/json")
                    except:
                        return HttpResponse(simplejson.dumps({"ERROR":"Unable to load module"}),content_type="application/json")
                else:
                    return HttpResponse(simplejson.dumps({"ERROR":"Module not found"}), content_type="application/json")
            except:
                return HttpResponse(simplejson.dumps({"ERROR":"System related error"}),content_type="application/json")

        else:
            self.fraud_type = request.GET.get("fraudtype", "")
            try:
                self.fraud_module = self.load_module_by_type(self.fraud_type)
                if(self.fraud_module):
                    try:
                        self.load_fraud_category = self.load_sub_category(self.fraud_module)
                        if(self.load_fraud_category):
                            try:
                                self.module_category = self.load_fraud_category.get(str(self.fraud_type))
                            except KeyError as error:
                                raise
                            else:
                                return HttpResponse(simplejson.dumps(self.module_category), content_type="application/json")
                        else:
                            return HttpResponse(simplejson.dumps({"error":"None"}),content_type="application/json")
                    except:
                        return HttpResponse(simplejson.dumps({"ERROR":"Unable to load module"}),content_type="application/json")
                else:
                    return HttpResponse(simplejson.dumps({"ERROR":"Module not found"}), content_type="application/json")
            except:
                return HttpResponse(simplejson.dumps({"ERROR":"System related error"}),content_type="application/json")

    def load_module_by_type(self, modtype):
        """
        given the requested module dynamically load it.
        """
        try:
            if(modtype):
                return allmodules.get_module(str(self.fraud_type))
            else:
                return None
        except:
            raise

    def load_sub_category(self, module):
        """
        Given the module load the avaiable sub category.
        """
        try:
            if(module):
                try:
                    return module.make_subcategory()
                except:
                    raise
            else:
                return None
        except:
            raise
