from django.forms import Field, Widget, ModelForm
from django.forms.models import BaseInlineFormSet

from roms.models import RomFile

class ReadOnlyWidget(Widget):
    def render(self, name, value, attrs):
        final_attrs = self.build_attrs(attrs, name=name)
        if hasattr(self, 'initial'):
            value = self.initial
        return "%s" % (value or '')

    def _has_changed(self, initial, data):
        return False


class ReadOnlyField(Field):
    widget = ReadOnlyWidget
    def __init__(self, widget=None, label=None, initial=None, help_text=None):
        super(ReadOnlyField, self).__init__(self, label=label, initial=initial,
            help_text=help_text, widget=widget)

    def clean(self, value, initial):
        self.widget.initial = initial
        return initial


class RomFileForm(ModelForm):
    slot = ReadOnlyField()
    class Meta:
        model = RomFile
        fields = ['binary']


class RomFileInlineFormSet(BaseInlineFormSet):

    def __init__(self, *args, **kwargs):
        super(RomFileInlineFormSet, self).__init__(*args, **kwargs)
        # Check that the data doesn't already exist
        if not kwargs['instance'].romfile_set.all():
            self.initial = [{'slot' : i} for i in range(1, SLOT_COUNT+1)]
            self.extra = SLOT_COUNT
