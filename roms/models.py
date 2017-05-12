import os
import uuid

from django.db import models
from django.core.exceptions import ValidationError

from taggit.managers import TaggableManager

from stdimage.models import StdImageField
from stdimage.validators import MinSizeValidator

def upload_cover_to(instance, filename):
    _, ext = os.path.splitext(filename)
    return "covers/%s%s" % (uuid.uuid4(), ext)

def upload_binary_to(instance, filename):
    return "roms/%s.bin" % uuid.uuid4()


class Rom(models.Model):
    name = models.CharField("name", max_length = 128, unique=True)
    description = models.TextField("description")
    cover = StdImageField("cover image",
                                 upload_to = upload_cover_to,
                                 validators = [MinSizeValidator(300,300)],
                                 variations = {'large': {'width': 600, 'height': 600, 'crop': True},
                                             'small': {'width': 300, 'height': 300, 'crop': True}})
    low_binary = models.FileField("low binary", upload_to = upload_binary_to)
    high_binary = models.FileField("high binary", upload_to = upload_binary_to)
    approved = models.BooleanField("approved")
    tags = TaggableManager(blank = True)
    creation_time = models.DateTimeField("creation time", auto_now_add = True)
    edit_time = models.DateTimeField("edit time", auto_now = True)


    def tag_list(self):
        return [t.name for t in self.tags.all()]

    def to_json(self):
        json = {
            'id' : self.pk,
            'name' : self.name,
            'description' : self.description,
            'tags' : self.tag_list(),
            'low_binary' : self.low_binary.url,
            'high_binary' : self.high_binary.url,
            'creation_time' : self.creation_time,
            'edit_time' : self.edit_time
        }

        return json

    def __str__(self):
        return self.name
