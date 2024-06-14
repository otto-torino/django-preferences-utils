#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_django-preferences-utils
------------

Tests for `django-preferences-utils` models module.
"""

from django.test import TransactionTestCase

from preferences_utils.models import PreferencesUtilsModel
from .models import Preferences, Preferences2


class PreferencesUtilsModelTest(TransactionTestCase):
    def test_creation(self):
        item = Preferences(
            site_title='Meow',
        )
        item.save()
        item2 = Preferences(
            site_title='Meow',
        )
        item2.save()
        self.assertEqual(item2.id, 1)
        self.assertEqual(str(item2), 'Preferences')

    def test_get_instance_from_derived(self):
        item = Preferences(
            site_title='Meow',
        )
        item.save()
        instance = Preferences.instance()
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.site_title, 'Meow')

    def test_get_instance_from_base(self):
        item = Preferences(
            site_title='Meow',
        )
        item.save()
        item2 = Preferences2(
            site_title2='Meow',
        )
        item2.save()
        instance = PreferencesUtilsModel.instance('pref')
        instance2 = PreferencesUtilsModel.instance('pref2')
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.site_title, 'Meow')
        self.assertEqual(instance2.id, 1)
        self.assertEqual(instance2.site_title2, 'Meow')

    def test_get_instance_from_base_without_name(self):
        item = Preferences(
            site_title='Meow',
        )
        item.save()
        try:
            instance = PreferencesUtilsModel.instance()
            self.fail()
        except Exception as e:
            self.assertRaises(Exception)
