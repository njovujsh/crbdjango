from util import models as utilmodels
#from datasetrecords import models

def all_districts():
    """
    Get and return all districts in tuple.
    """
    dis_list = []
    try:
        districts = utilmodels.Districts.objects.all()
        
        if(districts):
            for d in districts:
                dis_list.append((d.name, d.name))
            return tuple(dis_list)
        else:
            return tuple(dis_list)
    except Exception as e:
        return dis_list 
        
def all_subcounties():
    """
    Get and return all districts in tuple.
    """
    sub_list = []
    try:
        subcounties = utilmodels.Subcounties.objects.all()
        
        if(subcounties):
            for s in subcounties:
                sub_list.append((s.name, s.name))
            return tuple(sub_list)
        else:
            return tuple(sub_list)
    except Exception as e:
        return sub_list
        
def all_parishes():
    """
    Get and return all districts in tuple.
    """
    par_list = []
    try:
        parishes = utilmodels.Parishes.objects.all()
        if(parishes):
            for p in parishes:
                par_list.append((p.name, p.name))
            return tuple(par_list)
        else:
            return tuple(par_list)
    except Exception as e:
        return par_list


def get_cba_referencenumber():
    """
    Returns only reference number of cba.
    """
    cba_ref_list = []
    allrec = models.CREDITBORROWERACCOUNT.objects.all()
    if( not len(allrec)):
        cba_ref_list.append(("", ""))
        return cba_ref_list
    else:
        for a in allrec:
            cba_ref_list.append((a.Credit_Account_Reference, a.Credit_Account_Reference))
        return tuple(cba_ref_list)
