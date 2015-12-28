# -*-  coding: utf-8 -*-
"""
"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.
from collections import defaultdict

from ulakbus.lib.convert import tl_curreny
from ulakbus.models import *
from ulakbus.views.reports.base import Reporter
from zengine.lib.utils import *


class OgrenciByGender(Reporter):
    TITLE = 'Cinsiyete göre öğrenci sayıları'

    def get_objects(self):
        choices = self.convert_choices(Ogrenci().get_choices_for('cinsiyet'))
        result = []
        for val, num in Ogrenci.objects.distinct_values_of('cinsiyet').items():
            try:
                val = int(val)
            except:
                pass
            result.append((choices.get(val, val), num))
        return result


class OgrenciByBrithPlace(Reporter):
    TITLE = 'Doğum yerine göre öğrenci sayıları'

    def get_objects(self):
        return [(val, num) for val, num in
                Ogrenci.objects.distinct_values_of('dogum_yeri').items()]


class OgrenciByBrithDate(Reporter):
    TITLE = 'Doğum tarihine göre öğrenci sayıları'

    def get_objects(self):
        dates = defaultdict(lambda: 0)
        for val, num in Ogrenci.objects.distinct_values_of('dogum_tarihi').items():
            dates[solr_to_year(val)] += int(num)
        return dates.items()


class OgrenciHarc(Reporter):
    TITLE = 'Harç Bilgileri'

    def get_objects(self):
        # choices = self.convert_choices(Borc().get_choices_for('sebep'))
        result = defaultdict(lambda: 0)
        for b in Borc.objects.filter():
            result["%s %s" % (b.get_sebep_display(), 'Borç')] += int(b.miktar or 0)
            result["%s %s" % (b.get_sebep_display(), 'Ödenen')] += int(b.odenen_miktar or 0)

        return [(k, tl_curreny(v)) for k, v in result.items()]


class RoomCapacities(Reporter):
    TITLE = 'Kapasitesine Göre Mekanlar'

    def get_objects(self):
        return [{'Kapasite': k, 'Oda Sayısı': v} for k, v in
                     Room.objects.distinct_values_of('capacity').items()]
        # return Room.objects.distinct_values_of('capacity').items()
