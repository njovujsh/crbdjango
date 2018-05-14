# 2015.06.10 14:46:16 EAT
#Embedded file name: /var/www/CRB/branchcode/urls.py
from django.conf.urls import  include, url
from branchcode import views
from datasets import views as dataviews

urlpatterns = [
    url('^sendingemail/newmail/', views.EmailSending.as_view(), name='sendmail'), 
    url('^sftpsendmail/sftp/', views.SendingSFTP.as_view(), name='sftp'), 
    url('^settingsheaders/', views.HeaderSettings.as_view(), name='headers'), 
    url('^parseregiondistricts/', views.ParseRegions.as_view(), name='regionhandler'), 
    url('^parseselectedistricts/', views.ParseCountyInDistrict.as_view(), name='countyhandler'), 
    url('^getparishes/', views.ParseParishesInDistrict.as_view(), name='parishhandler'), 
    url('^settingsheaderss/update/(?P<settingPID>\\d+)/$', views.UpdateHeaderSettings.as_view(), name='headers'),
    url('^getinstitution/$', views.SearchInstitution.as_view(), name='searchpi'),
    url('^pisettings/saving/$', views.SavePiDetails.as_view(), name='savepi'),
    url('^searchpiinformation/$', views.QueryPiInformation.as_view(), name='savemorepi'),
    url('^searchbranchinformation/$', dataviews.QueryBranchInformation.as_view(), name='savebranch'),
    #branchpi/searchpiinformation
    #pisettings/saving/
]
