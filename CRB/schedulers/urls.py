from django.conf.urls import include, url
from schedulers import views 


urlpatterns = [
    #url(r"^category/(?P<category>[-\w]+)/$", views.HandleCategory.as_view(), name='category'),
    #url(r"^category/(?P<fraudtype>\w{0,50})/$", views.HandleCategory.as_view(), name='category'),
    url(r"^$", views.DataScheduler.as_view(), name='scheduler'),
]

