from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .dso import *
from .views import testView
# from .loadCSV import LoadRelationsCSV

urlpatterns = {
    url(r'^create/$', ReadnWriteView.as_view(), name="readWrite"),
    url(r'^readA/$', ReadAllView.as_view(), name="readAll"),
    url(r'^readO/(?P<id>\d+)/$', ReadOneView.as_view(), name="readOne"),
    url(r'^update/(?P<id>\d+)/$', UpdateView.as_view(), name="update"),
    url(r'^delete/(?P<id>\d+)/$', DeleteView.as_view(), name="delete"),
    url(r'^readU/(?P<id>\d+)/$', ReadnUpdateView.as_view(), name="readOne"),
    url(r'^readD/(?P<id>\d+)/$', ReadnDeleteView.as_view(), name="readOne"),
    url(r'^readUD/(?P<id>\d+)/$', ReadnUpdatenDeleteView.as_view(), name="readOne"),
    # url(r'^loadCSV/', LoadRelationsCSV.as_view(), name="loadCSV"),
    url(r'^test/$', testView.p_req, name="readAll"),

}




urlpatterns = format_suffix_patterns(urlpatterns)