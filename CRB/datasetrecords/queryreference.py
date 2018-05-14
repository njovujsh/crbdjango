import datasetrecords

def get_cba_referencenumber():
    """
    Returns only reference number of cba.
    """
    cba_ref_list = []
    allrec = datasetrecords.models.CREDITBORROWERACCOUNT.objects.all()
    if( not len(allrec)):
        cba_ref_list.append(("", ""))
        return cba_ref_list
    else:
        for a in allrec:
            cba_ref_list.append((a.Credit_Account_Reference, a.Credit_Account_Reference))
        return tuple(cba_ref_list)
