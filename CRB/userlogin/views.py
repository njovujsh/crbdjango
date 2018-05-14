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
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

BASE_TITLE="Welcome to Cred-Start  | Record, Validate, Analyse, Visualize"

#-----------View will be called directly from the url---------#

def parse_model_fields(model_data):
    """
    Returns the fields coresponding to particular models.
    """
    fields = [ ]
    mfields = model_data._meta.fields

    for field in mfields:
        if field.name in fields:
            pass
        else:
            if("_" in field.name):
                fields.append(field.name.replace("_", "", len(field.name)))
            else:
                fields.append(field.name)

    #return the model fields
    return fields
        
class UserLoginPage(View):
    """
    subclass of View.
    """
    
    def get(self, request):
        """
        Will be called from the url. automatically.
        """
        #return HttpResponse("It has worked like a charm!!!")
        try:
            self.template = self.get_base_template()
            #self.context = self.render_context(request, self.template)  #Context({"basetitle":"Welcome to our title system"})
            return render(request, "baselogin.html", {"basetitle":"Welcome to our title system"})
        except:
            raise
        else:
            #rendered = self.template.render(self.context)
            return HttpResponse(self.context)

    def get_base_template(self, *template):
        """
        return the loader template.
        """
        if(template):
            return loader.get_template(template)
        else:
            #return loader.get_template("baselogin.html")
            return loader.get_template("baselogin.html")

    def render_context(self, request, template, errormsg=None):
        """
        Render the needed context vars.
        """
        try:
            if(errormsg):
                self.context = RequestContext(request, {"basetitle":BASE_TITLE,
                                                        "incorrect":errormsg

                                                })
                self.rendered = template.render(self.context)
                return self.rendered
            else:
                self.context = RequestContext(request, {"basetitle":BASE_TITLE,

                                                })
                self.rendered = template.render(self.context)
                return self.rendered
        except:
            raise

    def post(self, request):
        """
        Authenticate user.
        """
        try:
            if(self._as_superuser(request)):
                try:
                    self.verify_user = self.authenticate_user(request)
                    if(self.verify_user):
                        if(self.verify_user.is_superuser):
                            login(request, self.verify_user)
                            return HttpResponseRedirect("/app/basehomepage/superuser")
                        else:
                            login(request, self.verify_user)
                            return HttpResponseRedirect("/app/basehomepage/notsuperuser")
                    else:
                        self.template = self.get_base_template()
                        return HttpResponse(self.render_context(request, 
                                            self.template, 
                                            "Incorrect username or password"
                                            ))
                except:
                    raise 
            else:
                self.verify_user = self.authenticate_user(request)
                if(self.verify_user):
                    if(self.verify_user.is_superuser):
                        login(request, self.verify_user)
                        return HttpResponseRedirect("/app/basehomepage/superuser")
                    else:
                        login(request, self.verify_user)
                        return HttpResponseRedirect("/app/basehomepage/notsuperuser")
                else:
                    self.template = self.get_base_template()
                    return HttpResponse(self.render_context(request, 
                                            self.template, 
                                            "Incorrect username or password"
                                            )) 
        except:
            raise 
      
    def _as_superuser(self, request):
        """
        Find out if the user is logging in as a super user
        """
        try:
            if(request):
                if(request.POST.get("superuser", "")):
                    return True 
                else:
                    return False 
            else:
                return None 
        except:
            raise 
     
    def authenticate_user(self, request):
        """
        The user is logging in as superuser.
        """
        try:
            if(request):
                self.username = request.POST.get("username", "")
                self.password = request.POST.get("password", "")
                self.athenticated_user = auth.authenticate(username=self.username, password=self.password)
                
                if(self.athenticated_user):
                    return self.athenticated_user
                else:
                    return False 
            else:
                return None 
        except:
            raise 
            
            
class LogoutUser(View):
    def get(self, request):
        try:
            if(request.user.is_authenticated()):
                logout(request)
                return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("/")
        except:
            raise


class AddNewStaff(View):
    @method_decorator(login_required)
    def get(self, request):
        try:
            if(request.user.is_authenticated()):
                self.rendered_context = self.process_context(request)
                if(self.rendered_context):
                    try:
                        return HttpResponse(self.rendered_context)
                    except:
                        return HttpResponseServerError("ERROR please try againlater")
                else:
                    return HttpResponseServerError("ERROR please try to clear cookies")
            else:
                return HttpResponseRedirect("/")
        except:
            raise 
            
    
    def load_new_usertemplate(self, *custom_template):
        """
        Given the template attempt to load and return it.
        """
        try:
            if(custom_template):
                try:
                    return loader.get_template(custom_template)
                except:
                    raise 
            else:
                try:
                    return loader.get_template("newstaff.html")
                except:
                    raise 
        except:
            raise
            
    def process_context(self, request):
        """
        Process and return the context.
        """
        try:
            self.template = self.load_new_usertemplate()
            if(self.template):
                try:
                    self.datasetrecords = self.get_datarecords()
                    self.userforms = self.get_registrationform()
                    self.user_stateform = self.get_userforms()
                    
                    self.context = RequestContext(request, {"basetitle":BASE_TITLE,"datasetrecords":self.datasetrecords,
                                                            "useraddforset":self.userforms, "userforms":self.user_stateform
                                                    })
                    return self.template.render(self.context)
                except:
                    raise 
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
            
    
    def get_registrationform(self, prefix="useradding"):
        """
        Return the forms which shall be used for 
        adding ne users.
        """
        try:
            return userloginforms.UserLoginForms(prefix=prefix)
        except:
            raise 

    
    def get_userforms(self, prefix="userforms"):
        try:
            return userloginforms.UserForms(prefix=prefix)
        except:
            raise 
            
    def get_userform_insert(self):
        return userloginforms.UserForms
        
    def get_regform_insert(self):
        return userloginforms.UserLoginForms
        
    @method_decorator(login_required)
    def post(self, request):
        try:
            self.datasetrecords = self.get_datarecords()
            self.user_insertform = self.get_userform_insert()
            self.user_regform = self.get_regform_insert()
            
            self.registration = self.user_regform(request.POST, prefix="useradding")
            self.userforms = self.user_insertform(request.POST, prefix="userforms")
            
            if(self.userforms.is_valid()):
                if(self.registration.is_valid()):
                    self.ret_code = self.userforms.save()
                    self.ret_code.set_password(self.ret_code.password)
                    self.ret_code.save()
                    
                    self.reg_retcode = self.registration.save(commit=False)
                    self.reg_retcode.username = self.ret_code
                    self.reg_retcode.save()
                    self.registration.save_m2m()
                    return HttpResponseRedirect("/user/view/existingstaff/")
                else:
                    try:
                        self.errordict = {"basetitle":BASE_TITLE, "error1":self.registration.errors,
                                    "datasetrecords":self.datasetrecords, "useraddforset":self.registration,
                                    "userforms":self.userforms, "error2":self.userforms.errors
                                    }
                        return HttpResponse(self.render_with_errors(request, self.errordict))
                   
                    except:
                        raise 
            else:
                try:
                    self.errordict = {"basetitle":BASE_TITLE, "error1":self.registration.errors,
                                    "datasetrecords":self.datasetrecords, "useraddforset":self.registration,
                                    "userforms":self.userforms, "error2":self.userforms.errors
                                    }
                    return HttpResponse(self.render_with_errors(request, self.errordict))
                   
                except:
                    raise 
        except:
            raise 
                
        
    def render_with_errors(self, request, errors):
        try:
            self.template = self.load_new_usertemplate()
            self.context = RequestContext(request, (errors))
            return self.template.render(self.context)
        except:
            raise 
            
class ViewAvailableUsers(View):
    @method_decorator(login_required)
    def get(self, request):
        try:
            if(request.user.is_authenticated()):
                self.rendered_context = self.process_context(request)
                if(self.rendered_context):
                    try:
                        return HttpResponse(self.rendered_context)
                    except:
                        return HttpResponseServerError("ERROR please try againlater")
                else:
                    return HttpResponseServerError("ERROR please try to clear cookies")
            else:
                return HttpResponseRedirect("/")
        except:
            raise 
            
    
    def load_view_usertemplate(self, *custom_template):
        """
        Given the template attempt to load and return it.
        """
        try:
            if(custom_template):
                try:
                    return loader.get_template(custom_template)
                except:
                    raise 
            else:
                try:
                    return loader.get_template("viewstaff.html")
                except:
                    raise 
        except:
            raise
            
    def process_context(self, request):
        """
        Process and return the context.
        """
        try:
            self.template = self.load_view_usertemplate()
            if(self.template):
                try:
                    self.datasetrecords = self.get_datarecords()
                    
                    self.available_staffs = self.load_allstaffs()
                    
                    self.paginated_staff = Paginator(self.available_staffs, 5)
                    
                    self.next_page = request.GET.get("page")
                    try:
                        self.staff_page = self.paginated_staff.page(self.next_page)
                    except PageNotAnInteger:
                        self.staff_page = self.paginated_staff.page(1) 
                    except EmptyPage:
                        self.staff_page = self.paginated_staff.page(self.paginated_staff.num_pages)
                        
                    self.model_headers = parse_model_fields(usermodels.CreditInstitutionStaff)
                    
                    self.context = RequestContext(request, {"basetitle":BASE_TITLE,"datasetrecords":self.datasetrecords,
                                                            "staffs":self.staff_page,"user_headers":self.model_headers
                                                    })
                    return self.template.render(self.context)
                except:
                    raise 
            else:
                return False 
        except:
            raise 
    
    def load_allstaffs(self):
        """
        Load and return all staffs.
        """
        try:
            return usermodels.CreditInstitutionStaff.objects.all()
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

class UpdateUser(View):
    @method_decorator(login_required)
    def get(self, request, userID):
        try:
            self._user_infor = self.request_user_info(userID) 
            self.updated = self.perform_update(request, userID, self._user_infor)
            if(self.updated):
                return HttpResponse(self.updated)
            else:
                return HttpResponse("Internal server error")
                
        except:
            raise 
            
    def request_user_info(self, userID):
        try:
            if(userID):
                try:
                    return usermodels.CreditInstitutionStaff.objects.get(id=int(userID))
                except:
                    raise 
            else:
                return False 
        except:
            raise 
        
    def load_update_form(self):
        return userloginforms.UserLoginForms
        
    def load_cred_form(self):
        return userloginforms.UserForms
        
    def user_form_instance(self, forms, userdetails, prefix):
        try:
            if(forms and userdetails):
                try:
                    return forms(instance=userdetails, prefix=prefix)
                except:
                    raise 
            else:
                return False
        except:
            raise        
            
        
    def perform_update(self, request, userid, userdetails):
        try:
            self.update_template = self.load_new_usertemplate()
            
            self.detailsform = self.load_update_form()
            self.credform = self.load_cred_form()
            
            self.details_formset = self.user_form_instance(self.detailsform, userdetails, prefix="useradding")
            self.cred_formset = self.user_form_instance(self.credform, userdetails.username, prefix="userforms")
            self.datasetrecords = self.get_datarecords()
            
            self.context = RequestContext(request, {"basetitle":BASE_TITLE,"datasetrecords":self.datasetrecords,
                                                        "useraddforset":self.details_formset, 
                                                        "userforms":self.cred_formset, "userid":userid,
                                                        "nameid":userdetails.username.id
                                                    })
                                                    
            return self.update_template.render(self.context)
        except:
            raise 
            
    def load_new_usertemplate(self, *custom_template):
        """
        Given the template attempt to load and return it.
        """
        try:
            if(custom_template):
                try:
                    return loader.get_template(custom_template)
                except:
                    raise 
            else:
                try:
                    return loader.get_template("updatestaff.html")
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
    
    def exception_handler(self):
        pass 
        
    @method_decorator(login_required)
    def post(self, request, userID, usernameID):
        try:
            self.usernameupdated = request.POST.get("userforms-username", "")
            self.password = request.POST.get('userforms-password', "")
            self.datasetrecords= self.get_datarecords()
            self.username_details = self.load_username_byid(usernameID)
            self.staff_details = self.load_staff_details(userID)
            self.update_form = self.load_update_form()
            self.cred_form = self.load_cred_form()
            
            try:
                self.username_details.username=self.usernameupdated
                if(self.password):
                    self.username_details.set_password(self.password)
                    self.username_details.save()
                else:
                    self.username_details.save()
                #self.update_cred_update = self.cred_form(request.POST, instance=self.username_details, prefix='userforms')
                self.update_staff_details = self.update_form(request.POST, instance=self.staff_details, prefix="useradding")

                if(self.usernameupdated):
                    #self._cred_instance = self.update_cred_update.save()
                    if(self.update_staff_details.is_valid()):
                        self.update_instance = self.update_staff_details.save(commit=False)
                        self.update_instance.username = self.username_details
                        self.update_instance.save()
                        self.update_staff_details.save_m2m()
                        return HttpResponseRedirect("/user/view/existingstaff/")
                    else:
                        try:
                            self.errordict = {
                                            "basetitle":BASE_TITLE, "error1":self.update_staff_details.errors,
                                            "datasetrecords":self.datasetrecords,"userforms":self.update_cred_update,
                                            "useraddforset":self.update_staff_details,"userid":userID,
                                            "nameid":usernameID
                                            }
                            return HttpResponse(self.render_with_errors(request, self.errordict))
                        except:
                            raise
                else:
                    try:
                        self.errordict = {"basetitle":BASE_TITLE, "error1":self.update_cred_update.errors,
                                        "datasetrecords":self.datasetrecords,"useraddforset":self.update_staff_details,
                                        "userforms":self.update_cred_update, "userid":userID,
                                        "nameid":usernameID
                                        }
                        return HttpResponse(self.render_with_errors(request, self.errordict))
                    except:
                        raise 
            except:
                raise 
        except:
            raise 
                
    def load_username_byid(self, usernameID):
        try:
            if(usernameID):
                return User.objects.get(id=int(usernameID))
            else:
                return False 
        except:
            raise 
            
    def load_staff_details(self, staffid):
        try:
            if(staffid):
                return usermodels.CreditInstitutionStaff.objects.get(id=int(staffid))
            else:
                return False 
        except:
            raise 
            
    def render_with_errors(self, request, errors):
        try:
            self.template = self.load_new_usertemplate()
            self.context = RequestContext(request, (errors))
            return self.template.render(self.context)
        except:
            raise 
