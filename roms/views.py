from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse

from taggit.models import Tag

from roms.models import Rom


class RomList(ListView):
    template_name = 'roms/list.html'
    context_object_name = 'roms'


    def get_queryset(self):
        tag = self.kwargs.get('tag', None)

        queryset = Rom.objects.all().filter(approved = True)
        if tag != None:
            queryset = queryset.filter(tags__slug = tag)

        return queryset


    def get_context_data(self, **kwargs):
        context = super(RomList, self).get_context_data(**kwargs)

        context['filter_tag'] = self.kwargs.get('tag', None)
        context['tags'] = Tag.objects.all()

        return context


class RomDetailView(DetailView):
    pk_url_kwarg = 'id'
    template_name = 'roms/details.html'
    context_object_name = 'rom'

    def get_queryset(self):
        queryset = Rom.objects.all().filter(approved = True)
        return queryset


class RomListJson(ListView):

    def get_queryset(self):
        tag = self.kwargs.get('tag', None)

        queryset = Rom.objects.all().filter(approved = True)
        if tag != None:
            queryset = queryset.filter(tags__slug = tag)

        return queryset


    def render_to_response(self, context, **response_kwargs):
        queryset = self.get_queryset()

        filter_tag = self.kwargs.get('tag', '')

        json = {
            'filter_tag' : filter_tag,
            'tags': {},
            'roms' : {},
        }
        for tag in Tag.objects.all():
            json['tags'][tag.slug] = tag.name

        for rom in queryset:
            json['roms'][rom.id] = rom.name

        return JsonResponse(json, **response_kwargs, safe=False)


class RomDetailViewJson(DetailView):
    pk_url_kwarg = 'id'

    def get_queryset(self):
        queryset = Rom.objects.all().filter(approved = True)
        return queryset

    def render_to_response(self, context, **response_kwargs):
        rom = self.get_object()
        return JsonResponse(rom.to_json(), **response_kwargs, safe=False)
