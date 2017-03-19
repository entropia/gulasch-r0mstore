import os
import uuid

from django.db import models
from django.core.exceptions import ValidationError

from taggit.managers import TaggableManager

from gulashromstore.settings import SLOT_COUNT

def upload_cover_to(instance, filename):
    _, ext = os.path.splitext(filename)
    return "covers/%s.%s" % (uuid.uuid4(), ext)

def upload_binary_to(instance, filename):
    return "roms/%s.bin" % uuid.uuid4()


class Rom(models.Model):
    name = models.CharField("name", max_length = 128)
    description = models.TextField("description")
    cover = models.ImageField("cover image", upload_to=upload_cover_to)
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
            'roms' : {romfile.slot : romfile.binary.url for romfile in self.romfile_set.all()}
        }

        return json



class RomFile(models.Model):
    SLOT_CHOICES = [(i, "Slot %d" % i) for i in range(1, SLOT_COUNT+1)]
    rom = models.ForeignKey(Rom, verbose_name = "rom")
    slot = models.IntegerField("slot", choices=SLOT_CHOICES)
    binary = models.FileField("binary", upload_to=upload_binary_to)

    class Meta:
        unique_together = ('rom', 'slot')
