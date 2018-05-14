from django.conf.urls import include, url
from validators import views 
from validators import saveview 
#192.168.2.2

urlpatterns = [
    url(r"^datavalidation/rules/", views.ValidationRules.as_view(), name="vrules"),
    url(r"^beginvalidation/validatedata/", views.BeginValidation.as_view(), name="bvalidation"),
    url(r"^recentvalidation/successful/", views.SuccessfulValidation.as_view(), name="successful"),
    url(r"^recentfailure/unsuccessful/", views.FailedValidation.as_view(), name="unsuccessful"),
    url(r"^begindata/selected/", views.ValidateDatesetsAJAX.as_view(), name="validatedatasets"),
    url(r"^importrecords/(?P<record_slug>[-\w]+)/$", views.ImportRecords.as_view(), name="handlimport"),
    url(r"^firstvalidate/(?P<record_slug>[-\w]+)/$", views.ValidateAndImport.as_view(), name="firstvalidate"),
    url(r"^validatesave/(?P<record_slug>[-\w]+)/", saveview.ValidateAndSave.as_view(), name="validatesave"),
    url(r"^showsaved/andvalidated/$", saveview.ShowSavedValidated.as_view(), name="showvalidated"),
    url(r"^begindata/recordsvalidation/$", views.ValidateDatesetsAJAX.as_view(), name="validattion"),
    url(r"^recentvalidation/getbyid/$", saveview.GetValidationRecordsStatus.as_view(), name="svalidation"),
    url(r"^downloadsaved/(?P<FID>\d+)/$", saveview.DownloadSaved.as_view(), name="downloadsaved"),
    #url(r"^/searchbyclient/selectedroot/?clientRoot=350830.0
    url(r"^searchbyclient/selectedroot/$", saveview.SearchClientRootDetails.as_view(), name="searchclientroot"),
    url(r"^renewsearchcba/cba/$", saveview.SearchDetailedInformation.as_view(), name="searchclientrootcba"),
]
#/processing/requesting/information/searching/
