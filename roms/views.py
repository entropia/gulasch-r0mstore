from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse

from roms.models import Rom


class RomListJson(ListView):
    def get_queryset(self):
        return Rom.objects.all().filter(approved = True)

    def render_to_response(self, context, **response_kwargs):
        queryset = self.get_queryset()

        json = {}
        for rom in queryset:
            json[rom.id] = rom.name

        return JsonResponse(json, **response_kwargs, safe=False)



class RomDetailViewJson(DetailView):
    model = Rom
    pk_url_kwarg = 'id'

    def render_to_response(self, context, **response_kwargs):
        rom = self.get_object()
        return JsonResponse(rom.to_json(), **response_kwargs, safe=False)
