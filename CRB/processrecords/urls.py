from django.conf.urls import  include, url
from django.contrib import admin
from processrecords import views 

urlpatterns = [
    url(r"^data/existing/$", views.GetVersionNumber.as_view(), name="selectversion"),
    url(r"^sending/headerfiles/version/$", views.GetSelectedVersion.as_view(), name="processbyheaders"),
    url(r"^data/existing/byID/(?P<headerID>\d+)/$", views.GetSelectedVersion.as_view(), name="selectedheader"),
    url(r"^requesting/information/searching/", views.ProcessOutput.as_view(), name="processoutput"),
    url(r"^displayprocessed/sheets/$", views.ExtractedSheets.as_view(), name="displaysheet"),
    url(r"^processinguploadedfiles/$", views.InsertLegacyRecords.as_view(), name="excelinsert"),

]
"""
To make recovery in case of failure easier, an additional sshd will 
be started on port '1022'. If anything goes wrong with the running 
ssh you can still connect to the additional one. 
If you run a firewall, you may need to temporarily open this port. As 
this is potentially dangerous it's not done automatically. You can 
open the port with e.g.: 
'iptables -I INPUT -p tcp --dport 1022 -j ACCEPT' 
"""
