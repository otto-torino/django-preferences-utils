#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_django-preferences-utils
------------

Tests for `django-preferences-utils` admin module.
"""

from django.test import TestCase, RequestFactory

from django.contrib.admin.sites import AdminSite
from django.views.generic.base import HttpResponseRedirect
from tests.admin import PreferencesAdmin
from tests.models import Preferences


class PreferencesUtilsAdminTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_changelist_view(self):
        request = self.factory.get('/admin/tests/preferences/')
        admin = PreferencesAdmin(model=Preferences, admin_site=AdminSite())
        res: HttpResponseRedirect = admin.changelist_view(request)
        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.url, '/admin/tests/preferences/1/change/?readonly=1')

    def test_has_change_permission_readonly(self):
        request = self.factory.get('/admin/tests/preferences/1/change/?readonly=1')
        admin = PreferencesAdmin(model=Preferences, admin_site=AdminSite())
        self.assertEqual(admin.has_change_permission(request), False)

    def test_has_change_permission_not_readonly(self):
        request = self.factory.get('/admin/tests/preferences/1/change/')
        admin = PreferencesAdmin(model=Preferences, admin_site=AdminSite())
        self.assertEqual(admin.has_change_permission(request), True)

    def test_has_add_permission(self):
        request = self.factory.get('/admin/tests/preferences/')
        admin = PreferencesAdmin(model=Preferences, admin_site=AdminSite())
        self.assertEqual(admin.has_add_permission(request), False)
