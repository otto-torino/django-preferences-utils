# -*- coding: utf-8 -*-
from django.contrib import admin
from preferences_utils.admin import PreferencesUtilsAdmin
from .models import Preferences, Preferences2

@admin.register(Preferences)
class PreferencesAdmin(PreferencesUtilsAdmin):
    list_display = ('id', )

    fieldsets = (
        ('Main', {
            'fields': ("site_title",),
        }),
    )

@admin.register(Preferences2)
class Preferences2Admin(PreferencesUtilsAdmin):
    list_display = ('id', )

    fieldsets = (
        ('Main', {
            'fields': ("site_title2",),
        }),
    )
