from django.conf.urls import  include, url
from django.contrib import admin
from userlogin import views 

urlpatterns = [
    url(r'^$', views.UserLoginPage.as_view(), name="basepage"),
    url(r"^authentication/", views.UserLoginPage.as_view(), name="basepage"),
    url(r"^logout/$", views.LogoutUser.as_view(), name="logout"),
    url(r"^new/userstaff/$", views.AddNewStaff.as_view(), name="addnewstaff"),
    url(r"^view/existingstaff/$", views.ViewAvailableUsers.as_view(), name="viewusers"),
    url(r"^addnew/dssh/$", views.AddNewStaff.as_view(), name="addnewstaff"),
    url(r"^update/userid/(?P<userID>\d+)/$", views.UpdateUser.as_view(), name="updateuser"),
    url(r"^addnew/updated/(?P<userID>\d+)/(?P<usernameID>\d+)/$", views.UpdateUser.as_view(), name="updateuser"),
]
