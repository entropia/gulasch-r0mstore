from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from gulashromstore.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    url(r'^roms/', include('roms.urls')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
