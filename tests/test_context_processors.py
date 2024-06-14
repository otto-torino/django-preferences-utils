# -*- coding: utf-8 -*-
import importlib

"""
test_django-preferences-utils
------------

Tests for `django-preferences-utils` context processors
"""

from django.test import TestCase, RequestFactory

class PreferencesUtilsContextProcessorTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_context(self):
        request = self.factory.get('/')
        cls = importlib.import_module("preferences_utils.context_processors.preferences")
        pref = cls.pref(request).get('pref')
        self.assertEqual(pref.site_title, "Site Title")
