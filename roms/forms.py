from django.forms import ModelForm

from roms.models import Rom


class RomUploadForm(ModelForm)
    class Meta:
        model = Rom
        fields = ['name', 'description', 'cover', 'low_binary', 'high_binary', 'tags']
