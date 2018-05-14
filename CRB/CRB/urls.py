"""CRB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from CRB import settings 
from django.contrib.staticfiles.views import serve
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^grappelli/", include("grappelli.urls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^$", include("userlogin.urls")),
    url(r"^baseuser/", include("userlogin.urls")),
    url(r"^app/", include("datasetrecords.urls")),
    url(r"^dataset/",include("datasetrecords.urls")),
    url(r"^view/", include("datasetrecords.urls")),
    url(r"^home/", include("datasetrecords.urls")),
    url(r"^purge/", include("datasetrecords.urls")),
    url(r"^addnew/", include("datasets.urls")),
    url(r"^dssh/", include("datasets.urls")),
    #url(r"^uploading/", include("datasetrecords.urls")),
    url(r"^purgebulk/", include("datasetrecords.urls")),
    url(r"^file/", include("fileprocessor.urls")),
    url(r"^processing/", include("processrecords.urls")),
    url(r"^user/", include("userlogin.urls")),
    url(r"^data/", include("datasetrecords.urls")),
    url(r"^record/", include("creditanalysis.urls")),
    url(r"^analysis/", include("creditanalysis.urls")),
    url(r"^validation/", include("validators.urls")),
    url(r"^help/", include("manual.urls")),
    url(r"^importdata/", include("validators.urls")),
    url(r"^fraudster/", include("fraudcategory.urls")),
    url(r"^sendmail/", include("branchcode.urls")),
    url(r"^rscheduler/", include("schedulers.urls")),
    url(r"^creport/", include("creditreports.urls")),
    url(r"^rlegacy/", include("legacysystems.urls")),
    url(r"^srules/", include("securityrules.urls")),
    url(r"^branch/", include("branchcode.urls")),
    url(r"^branchpi/", include("branchcode.urls")),
    #url(r"^search/", include("branchcode.urls")),
    url(r"^regionhandler/", include("branchcode.urls")),
    url(r"^importedrecords/", include("processrecords.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

