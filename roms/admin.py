from django.contrib import admin

from taggit_helpers.admin import TaggitListFilter, TaggitTabularInline

from roms.models import Rom


class RomAdmin(admin.ModelAdmin):
    list_display = ('name', 'approved', 'tag_list')
    list_filter = [TaggitListFilter]
    actions = ['mark_approved', 'mark_disapproved']

    inlines = [
        TaggitTabularInline
    ]

    def tag_list(self, obj):
        return u", ".join(obj.tag_list())

    def mark_approved(self, request, queryset):
        rows_updated = queryset.update(approved=True)
        if rows_updated == 1:
            message_bit = "One rom was"
        else:
            message_bit = "%d roms were" % rows_updated
        self.message_user(request, "%s successfully marked as approved." % message_bit)
    mark_approved.short_description = "Mark selected roms as approved"

    def mark_disapproved(self, request, queryset):
        rows_updated = queryset.update(approved=False)
        if rows_updated == 1:
            message_bit = "One rom was"
        else:
            message_bit = "%d roms were" % rows_updated
        self.message_user(request, "%s successfully marked as disapproved." % message_bit)
    mark_disapproved.short_description = "Mark selected roms as disapproved"


admin.site.register(Rom, RomAdmin)
