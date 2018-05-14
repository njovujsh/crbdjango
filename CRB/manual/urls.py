from django.conf.urls import include, url
from django.contrib import admin
from manual import views 

urlpatterns = [
    url(r"^usermanual/$", views.UserManual.as_view(), name="manual"),
    url(r"^maintainers/$", views.Maintainers.as_view(), name="maintainers"),
]
