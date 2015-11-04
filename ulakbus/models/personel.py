# -*-  coding: utf-8 -*-
"""
"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.

from pyoko.model import Model, Node
from pyoko import field
from .auth import Unit


class Personel(Model):
    tckn = field.String("TC No", index=True)
    ad = field.String("Adı", index=True)
    soyad = field.String("Soyadı", index=True)
    cinsiyet = field.String("Cinsiyet", index=True)
    uyruk = field.String("Uyruk", index=True)
    ikamet_il = field.String("İkamet Il", index=True)
    ikamet_ilce = field.String("İkamet Ilce", index=True)
    ikamet_adresi = field.String("İkamet Adresi", index=True)
    adres_2 = field.String("Adres 2", index=True)
    adres_2_posta_kodu = field.String("Adres 2 Posta Kodu", index=True)
    oda_no = field.Integer("Oda Numarası", index=True)
    oda_tel_no = field.String("Oda Telefon Numarası", index=True)
    cep_telefonu = field.String("Cep Telefonu", index=True)
    e_posta = field.String("E-Posta", index=True)
    e_posta_2 = field.String("E-Posta 2", index=True)
    e_posta_3 = field.String("E-Posta 3", index=True)
    web_sitesi = field.String("Web Sitesi", index=True)
    yayinlar = field.String("Yayınlar", index=True)
    projeler = field.String("Projeler", index=True)
    kan_grubu = field.String("Kan Grubu", index=True)
    ehliyet = field.String("Ehliyet", index=True)
    verdigi_dersler = field.String("Verdiği Dersler", index=True)
    unvan = field.String("Unvan", index=True)
    biyografi = field.Text("Biyografi")
    notlar = field.Text("Notlar")
    engelli_durumu = field.String("Engellilik", index=True)
    engel_grubu = field.String("Engel Grubu", index=True)
    engel_derecesi = field.String("Engel Derecesi")
    engel_orani = field.Integer("Engellilik Orani")

    class Meta:
        app = 'Personel'
        verbose_name = "Personel"
        verbose_name_plural = "Personeller"
        list_fields = ['ad', 'soyad', 'tckn', 'durum']
        search_fields = ['ad', 'soyad', 'cep_telefonu', 'tckn']

    def durum(self):
        return self.NufusKayitlari.durum

    durum.title = "Durum"

    def __unicode__(self):
        return "%s %s (%s | %s)" % (self.ad, self.soyad, self.tckn,
                                    self.NufusKayitlari.emekli_sicil_no)

    class KimlikBilgileri(Node):
        cuzdan_seri = field.String("Seri", index=True)
        cuzdan_seri_no = field.String("Seri No", index=True)
        baba_adi = field.String("Ana Adi", index=True)
        ana_adi = field.String("Baba Adi", index=True)
        dogum_tarihi = field.Date("Doğum Tarihi", index=True, format="%d.%m.%Y")
        dogum_yeri = field.String("Doğum Yeri", index=True)
        medeni_hali = field.String("Medeni Hali", index=True)
        kayitli_oldugu_il = field.String("Il", index=True)
        kayitli_oldugu_ilce = field.String("Ilce", index=True)
        kayitli_oldugu_mahalle_koy = field.String("Mahalle/Koy")
        kayitli_oldugu_cilt_no = field.String("Cilt No")
        kayitli_oldugu_aile_sira_no = field.String("Aile Sira No")
        kayitli_oldugu_sira_no = field.String("Sira No")
        kimlik_cuzdani_verildigi_yer = field.String("Cuzdanin Verildigi Yer")
        kimlik_cuzdani_verilis_nedeni = field.String("Cuzdanin Verilis Nedeni")
        kimlik_cuzdani_kayit_no = field.String("Cuzdan Kayit No")
        kimlik_cuzdani_verilis_tarihi = field.String("Cuzdan Kayit Tarihi")

    class NufusKayitlari(Node):
        tckn = field.String("Sigortalının TC Kimlik No", index=True)
        ad = field.String("Adi", index=True)
        soyad = field.String("Soyadi", index=True)
        ilk_soy_ad = field.String("Memuriyete Girişteki İlk Soyadı", index=True)
        dogum_tarihi = field.Date("Dogum Tarihi", index=True, format="%d.%m.%Y")
        cinsiyet = field.String("Cinsiyet", index=True)
        emekli_sicil_no = field.Integer("Emekli Sicil No", index=True)
        memuriyet_baslama_tarihi = field.Date("Memuriyete Ilk Baslama Tarihi", index=True,
                                              format="%d.%m.%Y")
        kurum_sicil = field.String("Kurum Sicili", index=True)
        maluliyet_kod = field.Integer("Malul Kod", index=True)
        yetki_seviyesi = field.String("Yetki Seviyesi", index=True)
        aciklama = field.String("Aciklama", index=True)
        kuruma_baslama_tarihi = field.Date("Kuruma Baslama Tarihi", index=True, format="%d.%m.%Y")
        gorev_tarihi_6495 = field.Date("Emeklilik Sonrası Göreve Başlama Tarihi", index=True,
                                       format="%d.%m.%Y")
        emekli_sicil_6495 = field.Integer("2. Emekli Sicil No", index=True)
        durum = field.Boolean("Durum", index=True)
        sebep = field.Integer("Sebep", index=True)
        sync = field.Integer("Senkronize", index=True)

        class Meta:
            verbose_name = "Nüfus Bilgileri"


class AdresBilgileri(Model):
    ad = field.String("Adres Adı", index=True)
    adres = field.String("Adres", index=True)
    ilce = field.String("İlçe", index=True)
    il = field.String("İl", index=True)
    personel = Personel()

    class Meta:
        verbose_name = "Adres Bilgisi"
        verbose_name_plural = "Adres Bilgileri"


class KurumIciGorevlendirmeBilgileri(Model):
    gorev_tipi = field.String("Görev Tipi", index=True)
    kurum_ici_gorev_baslama_tarihi = field.Date("Baslama Tarihi", index=True, format="%d.%m.%Y")
    kurum_ici_gorev_bitis_tarihi = field.Date("Bitiş Tarihi", index=True, format="%d.%m.%Y")
    birim = Unit()
    aciklama = field.String("Aciklama")
    resmi_yazi_sayi = field.String("Resmi Yazi Sayi")
    resmi_yazi_tarih = field.Date("Resmi Yazi Tarihi", index=True, format="%d.%m.%Y")
    personel = Personel()

    class Meta:
        verbose_name = "Kurum Ici Gorevlendirme"
        verbose_name_plural = "Kurum Ici Gorevlendirmeler"
        form_grouping = [
            {
                "group_title": "Gorev",
                "items": ["gorev_tipi", "kurum_ici_gorev_baslama_tarihi", "kurum_ici_gorev_bitis_tarihi", "birim",
                          "aciklama"],
                "layout": "4",
                "collapse": False
            },
            {
                "group_title": "Resmi Yazi",
                "items": ["resmi_yazi_sayi", "resmi_yazi_tarih"],
                "layout": "2",
                "collapse": False
            }
        ]


class KurumDisiGorevlendirmeBilgileri(Model):
    gorev_tipi = field.Integer("Görev Tipi", index=True, choices="askerlik_nevi")
    kurum_disi_gorev_baslama_tarihi = field.Date("Baslama Tarihi", index=True, format="%d.%m.%Y")
    kurum_disi_gorev_bitis_tarihi = field.Date("Bitiş Tarihi", index=True, format="%d.%m.%Y")
    aciklama = field.Text("Aciklama")
    resmi_yazi_sayi = field.String("Resmi Yazi Sayi")
    resmi_yazi_tarih = field.Date("Resmi Yazi Tarihi", index=True, format="%d.%m.%Y")
    maas = field.Boolean("Maas")
    yevmiye = field.Boolean("Yevmiye", default=False)
    yolluk = field.Boolean("Yolluk", default=False)
    ulke = field.Integer("Ulke", default="90")
    personel = Personel()

    class Meta:
        verbose_name = "Kurum Disi Gorevlendirme"
        verbose_name_plural = "Kurum Disi Gorevlendirmeler"
        form_grouping = [
            {
                "layout": "4",
                "groups": [
                    {
                        "group_title": "Gorev",
                        "items": ["gorev_tipi", "kurum_disi_gorev_baslama_tarihi", "kurum_disi_gorev_bitis_tarihi",
                                  "ulke",
                                  "aciklama"],
                        "collapse": False
                    }
                ]

            },
            {
                "layout": "2",
                "groups": [
                    {
                        "group_title": "Resmi Yazi",
                        "items": ["resmi_yazi_sayi", "resmi_yazi_tarih"],
                        "collapse": False
                    },
                    {
                        "items": ["maas", "yevmiye", "yolluk"],
                        "collapse": False
                    }
                ]

            },
        ]


class Kadro(Model):
    kadro_no = field.Integer("Kadro No")
    unvan = field.String("Unvan", index=True)
    derece = field.Integer("Derece", index=True)
    durum = field.Integer("Durum", index=True)
    birim = Unit("Birim")

    class Meta:
        verbose_name = "Kadro"
        verbose_name_plural = "Kadrolar"

    def __unicode__(self):
        return "%s %s %s" % (self.unvan, self.derece, self.durum)


class Atama(Model):
    personel = Personel("Personel")
    kadro = Kadro("Kadro")
    notlar = field.String("Aciklama", index=True)

    class Meta:
        verbose_name = "Atama"
        verbose_name_plural = "Atamalar"

    def __unicode__(self):
        return "%s %s" % (self.personel, self.kadro)
