from django.conf.urls import include, url

from roms.views import RomListJson, RomDetailViewJson, RomList, RomDetailView, RomCreateView, RomUpdateView

urlpatterns = [
    url(r'^json/list/$', RomListJson.as_view()),
    url(r'^json/list/(?P<tag>[-\w]+)/$', RomListJson.as_view()),
    url(r'^json/details/(?P<id>[0-9]+)/$', RomDetailViewJson.as_view()),

    url(r'^list/$', RomList.as_view(), name = 'romlist'),
    url(r'^list/(?P<tag>[-\w]+)/$', RomList.as_view(), name = 'romlist'),
    url(r'^details/(?P<id>[0-9]+)/$', RomDetailView.as_view(), name = 'romdetails'),

    url(r'^new/$', RomCreateView.as_view(), name = 'romcreate'),
    url(r'^edit/(?P<id>[0-9]+)/$', RomUpdateView.as_view(), name = 'romupdate')
]
