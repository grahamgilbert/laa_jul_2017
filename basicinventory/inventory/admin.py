# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Machine
class MachineAdmin(admin.ModelAdmin):
    readonly_fields=('created_date','modified_date',)

admin.site.register(Machine, MachineAdmin)
