from django.conf.urls import  include, url
from creditreports import views 
from creditreports import viewreport


urlpatterns = [
    #url(r"^category/(?P<category>[-\w]+)/$", views.HandleCategory.as_view(), name='category'),
    url(r"^instantview/(?P<record_slug>[-\w]+)/$", viewreport.ViewValidationReport.as_view(), name='viewcreport'),
    #url(r"^category/(?P<fraudtype>\w{0,50})/$", views.HandleCategory.as_view(), name='category'),
    url(r"^$", views.CreditReporter.as_view(), name='creporter'),
]

