import os
import uuid

from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

from taggit.managers import TaggableManager

from stdimage.models import StdImageField
from stdimage.validators import MinSizeValidator

from users.models import User

def upload_cover_to(instance, filename):
    _, ext = os.path.splitext(filename)
    return "covers/%s%s" % (uuid.uuid4(), ext)

def upload_binary_to(instance, filename):
    return "roms/%s.bin" % uuid.uuid4()


class Rom(models.Model):
    name = models.CharField("name", max_length = 128, unique=True)
    description = models.TextField("Beschreibung", max_length=1024)
    cover = StdImageField("cover-Bild",
                                 upload_to = upload_cover_to,
                                 validators = [MinSizeValidator(300,300)],
                                 variations = {'large': {'width': 600, 'height': 600, 'crop': True},
                                             'small': {'width': 300, 'height': 300, 'crop': True}})
    low_binary = models.FileField("low binary", upload_to = upload_binary_to)
    high_binary = models.FileField("high binary", upload_to = upload_binary_to)
    approved = models.BooleanField("approved", default=False)
    tags = TaggableManager(blank = True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT)
    download_count = models.IntegerField(default = 0)
    creation_time = models.DateTimeField("creation time", auto_now_add = True)
    edit_time = models.DateTimeField("edit time", auto_now = True)

    def get_absolute_url(self):
        return reverse('romdetails', kwargs={'id' : self.pk})

    def tag_list(self):
        return [t.name for t in self.tags.all()]

    def to_json(self):
        json = {
            'id' : self.pk,
            'name' : self.name,
            'user' : self.user.username,
            'description' : self.description,
            'tags' : self.tag_list(),
            'low_binary' : self.low_binary.url,
            'high_binary' : self.high_binary.url,
            'download_count' : self.download_count,
            'creation_time' : self.creation_time,
            'edit_time' : self.edit_time
        }

        return json

    def __str__(self):
        return self.name
