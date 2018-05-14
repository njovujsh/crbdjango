from CRB import settings
import datetime
#sub =  now + dateutil.relativedelta.relativedelta(months=-1)
#from dateutil.relativedelta import relativedelta

def timify(l):
    """
    Convert the list into an understandable datetime.
    """
    if(len(l) == 3):
        return datetime.date(l[0], l[1], l[2])


def get_first_filter_date():
    return timify(settings.FIRST_DAY_DATE_FILTER)

def get_last_filter_date():
    return timify(settings.LAST_DAY_DATE_FILTER)
    
"""
Many.objects.filter(one=one).update(one=None)
more=Many.objects.filter(one=one)
for m in more
    m.one=None
    m.save()
#and finally:
one.delete()
"""
