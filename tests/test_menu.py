# -*-  coding: utf-8 -*-
"""

"""
# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.
from time import sleep
from .base_test_case import BaseTestCase
import pytest
import falcon


class TestCase(BaseTestCase):
    def test_authorized_in_menu(self):
        self.prepare_client('/menu')
        resp = self.client.post()
        resp.raw()
        # Kullaniciya izinler ekliyor
        self.client.user.role_set[0].role.add_permission_by_name('Atama', True)
        self.client.user.role_set[0].role.add_permission_by_name('Borc', True)
        sleep(1)
        # Kullanicinin izin desgisikliklerini gormesi icin cikis yapmasi gerekiyor
        self.client.set_path('/logout')
        self.client.post()
        # Login'e true atayip varolan kullaniciyi direkt login yaptiriyor.
        self.prepare_client('/menu', login=True)
        resp = self.client.post()
        resp.raw()
        lst = ['other', 'personel', 'ogrenci']
        # Ciktinin asagida tanimlanmis keylere sahip olup olmadigini kontrol ediyor
        assert set(lst).issubset(resp.json.keys())
        for key in lst:
            for value in resp.json[key]:
                assert set(value.keys()).issubset({'kategori', 'param', 'text', 'url', 'wf', 'model'})

    def test_authorisation_in_menu(self):
        # setup workflow
        self.prepare_client('/menu')
        resp = self.client.post()
        resp.raw()
        self.client.user.role_set[0].role.add_permission_by_name('Atama', True)
        self.client.user.role_set[0].role.add_permission_by_name('Borc', True)
        sleep(1)
        self.client.set_path('/logout')
        self.client.post()
        self.prepare_client('/menu', login=True)
        resp = self.client.post()
        resp.raw()

        assert set(resp.json.keys()) == set(['other', 'personel', 'ogrenci', 'is_login'])
        for content in resp.json.keys():
            try:
                for i in range(len(resp.json[content])):
                    assert set(resp.json[content][i].keys()) == set(['url', 'text', 'kategori', 'param'])
                    assert resp.json[content][i]['url'] in ["crud/Borc", "/yeni_personel", "crud/HizmetBorclanma",
                                                            "crud/Atama"]
            except TypeError:
                assert content

        lst = ['other', 'personel', 'ogrenci']
        # Ciktinin asagida tanimlanmis keylere sahip olup olmadigini kontrol ediyor
        assert set(lst).issubset(resp.json.keys())
        for key in lst:
            for value in resp.json[key]:
                assert set(value.keys()).issubset({'kategori', 'param', 'text', 'url', 'wf', 'model'})
                assert value['url'] in ["crud/Borc", "/yeni_personel", "crud/HizmetBorclanma",
                                        "crud/Atama"]

    def test_unauthorized_in_menu(self):
        self.client.set_path('/logout')
        self.client.post()
        with pytest.raises(falcon.errors.HTTPUnauthorized):
            self.prepare_client('/menu')
            self.client.post()
