from django.conf.urls import include, url
from datasetrecords import views 
from datasetrecords import updateview 
from datasetrecords import searchingview
from datasetrecords import updateib 
from datasetrecords import multipleupdate 
from datasetrecords import pispiupdate
from datasetrecords import singletoneupdate
from datasetrecords import bouncedview 
from datasetrecords import recordpurge  

#/app/basehomepage/superuser
urlpatterns =[
    url(r"^basehomepage/(?P<is_superuser>[-\w]+)/$", views.BaseHomepage.as_view(), name="basehome"),
    url(r"^process/datasetrecord/(?P<record_slug>[-\w]+)/$",views.NewDataRecords.as_view(), name="newdata"),
    url(r"^process/datasetrecord/existing/(?P<record_slug>[-\w]+)/$", bouncedview.BouncedExisting.as_view(), name="there"),
    url(r"^data/entered/(?P<record_slug>[-\w]+)/$", views.NewDataRecords.as_view(), name="newdata"),
    url(r"^update/entered/(?P<record_slug>[-\w]+)/(?P<dataID>\d+)/(?P<pciID>\d+)/(?P<sciID>\d+)/$", updateview.NewDataUpdate.as_view(), name="newdata"),
    url(r"^dataview/request/(?P<record_slug>[-\w]+)/$", views.RequestViewData.as_view(), name="viewdata"),
    url(r"^dashboard/$", views.AppendixView.as_view(), name="dashboard"),
    url(r"^redo/$", views.AppendixView.as_view(), name="dashboard"),
    url(r"^searching/(?P<record>[-\w]+)/$", searchingview.RecordSearching.as_view(), name="searching"),
    url(r"^deletingrecords/(?P<record>[-\w]+)/$", searchingview.APTPurge.as_view(), name="aptpurge"),
    url(r"^searchingbyajax/(?P<record>[-\w]+)/$", searchingview.RecordSearchingAJAX.as_view(), name="searchingajax"),
    url(r"^process/bynumber/existing/$", bouncedview.BouncedExisting.as_view(), name="there"),

    url(r"^updating/indentification/(?P<record_slug>[-\w]+)/(?P<recordID>\d+)/$", multipleupdate.GeneralUpdate.as_view(), name="update"),
    url(r"^update/indentification/(?P<record_slug>[-\w]+)/(?P<recordID>\d+)/$", multipleupdate.GeneralUpdate.as_view(), name="update"),
    url(r"^update/indentification/(?P<record_slug>[-\w]+)/(?P<recordID>\d+)/(?P<pciID>\d+)/(?P<sciID>\d+)/(?P<ieid>\d+)/(?P<idi>\d+)/(?P<gsid>\d+)/$", multipleupdate.GeneralUpdate.as_view(), name="update"),
    url(r"^updating/indentification/institution_branch/(?P<dataset>[-\w]+)/(?P<recordID>\d+)/$", updateib.UpdateIB.as_view(), name="update"),
    url(r"^update/indentification/institution_branch/(?P<record_slug>[-\w]+)/(?P<ibID>\d+)/(?P<pciID>\d+)/$", updateib.UpdateIB.as_view(), name="update"),
    #url(r"^updating/indentification/participatinginstitutionstakeholder/(?P<dataset>[-\w]+)/(?P<recordID>\d+)/$", pispiupdate.PIPISUpdate.as_view(), name="update"),
    url(r"^updating/indentification/participating_institution/(?P<dataset>[-\w]+)/(?P<recordID>\d+)/$", pispiupdate.PIPISUpdate.as_view(), name="update"),
    url(r"^update/indentification/participatinginstitutionstakeholder/(?P<record_slug>[-\w]+)/(?P<recordID>\d+)/(?P<pciID>\d+)/(?P<sciID>\d+)/$", pispiupdate.PIPISUpdate.as_view(), name="update"),
    url(r"^update/indentification/participating_institution/(?P<record_slug>[-\w]+)/(?P<recordID>\d+)/(?P<pciID>\d+)/$", pispiupdate.PIPISUpdate.as_view(), name="update"),
    url(r"^viewdetails/(?P<record_slug>[-\w]+)/(?P<recordID>\d+)/(?P<clientID>\d+(?:\.\d+)?)/(?P<status>\w+)/", searchingview.ClientDetailsSearching.as_view(), name="searchview"),
    url(r"^viewhistory/borrowing/(?P<record_slug>[-\w]+)/(?P<recordID>\d+)/(?P<clientID>\d+(?:\.\d+)?)/$", searchingview.ViewBorrowingHistory.as_view(), name="borrowinghistory"),
    url(r"^runaptpurge/bydatatype/(?P<record_slug>[-\w]+)/(?P<ID>\d+)/(?P<clientID>\d+(?:\.\d+)?)/$", recordpurge.PermanentDelete.as_view(), name="deleterecords"),
]
