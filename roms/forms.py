from dal import autocomplete

from django.forms import ModelForm
from django.urls import reverse_lazy

from roms.models import Rom



class RomCreateForm(ModelForm):
    class Meta:
        model = Rom
        fields = ['name', 'description', 'cover', 'low_binary', 'high_binary', 'tags']

        widgets = {
            'tags': autocomplete.TaggitSelect2(reverse_lazy('tag-autocomplete'))
        }



class RomUpdateForm(ModelForm):
    class Meta:
        model = Rom
        fields = ['description', 'cover', 'low_binary', 'high_binary', 'tags']

        widgets = {
            'tags': autocomplete.TaggitSelect2(reverse_lazy('tag-autocomplete'))
        }
