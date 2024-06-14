# -*- coding: utf-8 -*-
from django.db import models
from preferences_utils.models import PreferencesUtilsModel

@PreferencesUtilsModel.register("pref")
class Preferences(PreferencesUtilsModel):
    site_title = models.CharField(max_length=100, default="Site Title", blank=True)

    class Meta:
        verbose_name = "preferences"
        verbose_name_plural = "preferences"

@PreferencesUtilsModel.register("pref2")
class Preferences2(PreferencesUtilsModel):
    site_title2 = models.CharField(max_length=100, default="Site Title 2", blank=True)

    class Meta:
        verbose_name = "preferences2"
        verbose_name_plural = "preferences2"
