from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.db.models import Q

from taggit.models import Tag
from dal import autocomplete

from roms.models import Rom
from roms.forms import RomCreateForm, RomUpdateForm


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
        queryset = Rom.objects.all().filter(Q(approved = True) | Q(user__id = self.request.user.id))
        return queryset


class RomCreateView(LoginRequiredMixin, CreateView):
    model = Rom
    form_class = RomCreateForm
    template_name = 'roms/create.html'

    def form_valid(self, form):
        res = super(RomCreateView, self).form_valid(form)

        self.object.user = self.request.user
        self.object.save()

        return res


class RomUpdateView(LoginRequiredMixin, UpdateView):
    model = Rom
    pk_url_kwarg = 'id'
    form_class = RomUpdateForm
    template_name = 'roms/update.html'

    def get_queryset(self):
        return Rom.objects.filter(user__id = self.request.user.id)


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Tag.objects.none()

        qs = Tag.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


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

        response_kwargs['safe'] = False
        return JsonResponse(json, **response_kwargs)


class RomDetailViewJson(DetailView):
    pk_url_kwarg = 'id'

    def get_queryset(self):
        queryset = Rom.objects.all().filter(approved = True)
        return queryset

    def render_to_response(self, context, **response_kwargs):
        rom = self.get_object()

        response_kwargs['safe'] = False
        return JsonResponse(rom.to_json(), **response_kwargs)
