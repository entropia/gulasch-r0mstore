from django.conf.urls import include, url

from roms.views import RomListJson, RomDetailViewJson

urlpatterns = [
    url(r'json/$', RomListJson.as_view()),
    url(r'json/(?P<id>[0-9]+)/$', RomDetailViewJson.as_view())
]
