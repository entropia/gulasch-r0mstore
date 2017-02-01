from django.contrib import admin

from taggit_helpers.admin import TaggitListFilter, TaggitTabularInline

from roms.models import Rom, RomFile

class RomFileInline(admin.TabularInline):
    model = RomFile

class RomAdmin(admin.ModelAdmin):
    list_filter = [TaggitListFilter]

    inlines = [
        RomFileInline,
        TaggitTabularInline
    ]

admin.site.register(Rom, RomAdmin)
