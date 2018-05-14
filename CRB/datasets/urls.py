from django.conf.urls import include, url
from django.contrib import admin
from datasets import views 

urlpatterns = [
    url(r"^dssh/", views.AddNewDSS.as_view(), name="addssh"),
    url(r"^uploadbranchcodes/$", views.UploadBranchCode.as_view(), name="uploadbranchcode"),
    url(r"^submission/new/dssh/", views.AddNewDSS.as_view(), name="addsshpost"),
    url(r"^view/dsshe/", views.ViewDSS.as_view(), name="viewdssh"),
    url(r"^updating/dss/", views.ViewDSS.as_view(), name="viewdssh"),
    url(r"^edit/dsshid/(?P<dsshID>\d+)/$", views.UpdateHeaderFiles.as_view(), name="updatedssh"),
    url(r"^upheaders/dsshupdatedversion/(?P<updatingID>\d+)/$", views.UpdateHeaderFiles.as_view(), name="updatedssh"),
]
