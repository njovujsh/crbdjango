from django.conf.urls import include, url
from fileprocessor import views 
#firmware-linux firmware-linux-free firmware linux-nonfree broadcom-sta-dkms
urlpatterns = [
    url(r"^uploading/newupload/formater/$", views.FileUploader.as_view(), name="fileuploader"),
    url(r"^display/success/url/upload/$", views.DisplayFiles.as_view(), name="displayfiles"),
    url(r"^filehandler/processfiles/byid/(?P<fileID>\d+)/$", views.ProcessFiles.as_view(), name="processfiles"),
    url(r"^processid/requested/(?P<fileID>\d+)/$", views.ProcessFiles.as_view(), name="processfiles"),
    
]

