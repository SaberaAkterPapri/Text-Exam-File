from django.contrib import admin
# from django.contrib.auth.models import SearchAdmin
# from django.contrib.auth.admin import SearchAdmin
from .models import SearchEngine 


class SearchEngineAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'user', 'time', 'location', 'device', 'created', 'modified')
    search_fields = ('keyword', 'user')
    readonly_field = ('device', 'created')

    # filter_horizontal = ()
    list_filter = ('keyword', 'user', 'time', 'location', 'device', 'created', 'modified')
    # fieldsets = ()

admin.site.register(SearchEngine, SearchEngineAdmin)


# Register your models here.
