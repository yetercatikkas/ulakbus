# -*-  coding: utf-8 -*-
"""
"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.

import random
from pyoko import form,exceptions
from zengine.lib.forms import JsonForm
from zengine.views.crud import CrudView
from ulakbus.models.ogrenci import Ogrenci
from ulakbus.services.zato_wrapper import MernisKimlikBilgileriGetir

class KimlikBilgileriForm(JsonForm):
    class Meta:
        include = ['tckn',"ogrenci_no","ad","soyad","dogum_tarihi","dogum_yeri","uyruk","medeni_hali"]

    kaydet = form.Button("Kaydet", "save")
    mernis_sorgula = form.Button("Mernis Sorgula", cmd="mernis_sorgula")

class IletisimBilgileriForm(JsonForm):
    class Meta:
        include = ["ikamet_adresi","e_posta","tel_no"]

    kaydet = form.Button("Kaydet","save")

class KimlikIletisim(CrudView):
    class Meta:
        model = "Ogrenci"

    def kimlik_bilgileri(self):
        self.form_out(KimlikBilgileriForm(self.object, current = self.current))

    def mernis_sorgula(self):
        servis = MernisKimlikBilgileriGetir(tckn=self.object.tckn)
        kimlik_bilgisi = servis.zato_request()
        self.object(**kimlik_bilgisi)
        self.object.save()