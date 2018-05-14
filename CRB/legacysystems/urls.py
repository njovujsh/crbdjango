from django.conf.urls import include, url
from legacysystems import views 
from legacysystems import view1 


urlpatterns = [
    #url(r"^category/(?P<category>[-\w]+)/$", views.HandleCategory.as_view(), name='category'),
    #url(r"^category/(?P<fraudtype>\w{0,50})/$", views.HandleCategory.as_view(), name='category'),
    url(r"^$", views.LegacySystem.as_view(), name='legacy'),
    url(r"^sync/$", views.BranchSystem.as_view(), name='legacy'),
    url(r"^rview/$", views.ViewBranchSystem.as_view(), name='vlegacy'),
    url(r"^rupdate/(?P<PID>\d+)/$", views.UpdateSystems.as_view(), name='vupdatelegacy'),
    url(r"^delete/purge/(?P<PID>\d+)/$", views.PurgeUpdateSystems.as_view(), name='vdeletelegacy'),
    url(r"^lview/$", views.ViewLegacy.as_view(), name='vlegacy'),
    url(r"^mupdate/rulesid/(?P<PID>\d)/$", view1.UpdateReplicationZone.as_view(), name='vlupdateegacy'),
    url(r"^mdelete/purge/(?P<PID>\d)/$", view1.PurgeReplicactionZone.as_view(), name='vlupdateegacy'),
]

