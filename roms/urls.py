from django.conf.urls import include, url

from roms.views import RomListJson, RomDetailViewJson, RomList, RomDetailView, RomCreateView

urlpatterns = [
    url(r'^json/list/$', RomListJson.as_view()),
    url(r'^json/list/(?P<tag>[a-zA-Z0-9-]+)/$', RomListJson.as_view()),
    url(r'^json/details/(?P<id>[0-9]+)/$', RomDetailViewJson.as_view()),

    url(r'^list/$', RomList.as_view(), name = 'romlist'),
    url(r'^list/(?P<tag>[a-zA-Z0-9-]+)/$', RomList.as_view(), name = 'romlist'),
    url(r'^details/(?P<id>[0-9]+)/$', RomDetailView.as_view(), name = 'romdetails'),
    url(r'^new/$', RomCreateView.as_view(), name = 'romcreate')
]
