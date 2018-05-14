from django import template
from django.forms import Select, ModelChoiceField
register = template.Library()
from django.template.defaultfilters import stringfilter
from django.template.defaultfilters import filesizeformat

@register.filter(name="is_selectbox")
def is_selectbox(field):
    if(field):
        try:
            return field.__class__.__name__  == Select().__class__.__name__
        except:
            raise 
    else:
        return None

@register.filter(name="get_labeltag")
@stringfilter
def get_labeltag(label):
    if(label):
        if("pci:" in label.lower()):
            return "/add/pci/"
        elif("sci:" in label.lower()):
            return "/add/sci/"
        else:
            return "/add/none/"
    else:
        return False 
  
  
@register.filter(name="purge_underscore")
@stringfilter
def purge_underscore(text):
    if(len(text)):
        try:
            #purge andremove the underscore
            if("_" in text):
                return str(text.replace("_", " ", len(text))).title()
            else:
                return str(text).title()
        except:
            return False 
    else:
        return None       

@register.filter(name="justpass")
@stringfilter
def justpass(text):
    """
    Custom pass implementation in django,
    this is because django does not give us
    just a filter, so we do it our self.
    """
    try:
        if(len(text)):
            return ""
        else:
            pass 
    except:
        raise 

@register.filter(name="parsefilesize")
@stringfilter
def parsefilesize(filesize):
    try:
        return filesizeformat(int(filesize))
    except:
        pass

@register.filter(name="putspaces")
@stringfilter
def putspaces(strings):
    try:
        if(strings == "Bouncedcheques"):
            return "Bounced Cheques"
        elif(strings == "Creditborroweraccount"):
            return "Credit Borrower Account"
            
        elif(strings == "Borrowerstakeholder"):
            return "Borrower Stakeholder"
            
        elif(strings == "Participatinginstitutionstakeholder"):
            return "Participating Institution Stakeholder"
        else:
            return strings
    except:
        raise  

@register.filter(name="check_classification")
def check_classification(string):
    if(string == "0"):
        return "Individual"
    elif(string == "1"):
        return "Non Individual"
    else:
        return string 
