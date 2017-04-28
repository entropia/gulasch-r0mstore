import os
import uuid

from django.db import models
from django.core.exceptions import ValidationError

from taggit.managers import TaggableManager

def upload_cover_to(instance, filename):
    _, ext = os.path.splitext(filename)
    return "covers/%s.%s" % (uuid.uuid4(), ext)

def upload_binary_to(instance, filename):
    return "roms/%s.bin" % uuid.uuid4()


class Rom(models.Model):
    name = models.CharField("name", max_length = 128)
    description = models.TextField("description")
    cover = models.ImageField("cover image", upload_to=upload_cover_to)
    binary = models.FileField("binary", upload_to=upload_binary_to)
    approved = models.BooleanField("approved")
    tags = TaggableManager()

    def tag_list(self):
        return [t.name for t in self.tags.all()]

    def to_json(self):
        json = {
            'id' : self.pk,
            'name' : self.name,
            'description' : self.description,
            'tags' : self.tag_list(),
            'cover' : self.cover,
            'binary' : self.binary
        }

        return json

    def __str__(self):
        return "Rom %s" % self.name
