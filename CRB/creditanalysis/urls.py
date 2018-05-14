from django.conf.urls import include, url
from creditanalysis import views 


urlpatterns =[
    url(r"^searching/(?P<record>[-\w]+)/$", views.RecordSearching.as_view(), name="searching"),
    url(r"^arecords/(?P<record>[-\w]+)/$", views.RecordSearching.as_view(), name="searching"),
]

