from django.db import models

from taggit.managers import TaggableManager

class Rom(models.Model):
    name = models.CharField("name", max_length = 128)
    description = models.TextField("description")
    cover = models.ImageField("cover image")
    tags = TaggableManager()


class RomFile(models.Model):
    SLOT_CHOICES = [(i, "Slot %d" % i) for i in range(1,7)]
    rom = models.ForeignKey(Rom, verbose_name = "rom")
    slot = models.IntegerField("slot", choices=SLOT_CHOICES)
    binary = models.FileField("binary")

    class Meta:
        unique_together = ('rom', 'slot')
