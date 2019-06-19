# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from import_export.admin import ImportExportModelAdmin


from .models import Person
from .resources import PersonResource





class PersonAdmin(ImportExportModelAdmin):
    resource_class=PersonResource


admin.site.register(Person,PersonAdmin)

