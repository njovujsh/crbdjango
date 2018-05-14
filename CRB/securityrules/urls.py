from django.conf.urls import include, url
from securityrules import views 
from validators import saveview 
#192.168.2.2

urlpatterns =[
    url(r"^$", views.SecurityRules.as_view(), name="srules"),
    url(r"sview/$", views.ViewRules.as_view(), name="svrules"),
    url(r"update/rulesid/(?P<PID>\d+)/$", views.UpdateRules.as_view(), name="svrules"),
    url(r"delete/purge/(?P<PID>\d+)/$", views.DeleteRule.as_view(), name="svrules"),
]
#/processing/requesting/information/searching/
