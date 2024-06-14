#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_django-preferences-utils
------------

Tests for `django-preferences-utils` templatetags module.
"""

from django.test import TestCase
from preferences_utils.templatetags.preferences_utils import get_dict_item

class PreferencesUtilsModelTagsTest(TestCase):
    def test_get_dict_key(self):
        mydict = {
            'key1': 'value1',
            'key2': 'value2',
        }
        self.assertEqual(get_dict_item(mydict, 'key1'), 'value1')
        self.assertEqual(get_dict_item(mydict, 'key2'), 'value2')
        self.assertEqual(get_dict_item(mydict, 'key3'), None)
