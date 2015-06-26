# -*-  coding: utf-8 -*-
"""General Core views"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.
from zaerp.lib.views import SimpleView

from falcon.errors import HTTPBadRequest

# from zaerp.modules.forms import get_form
# from zaerp.modules.auth.student import authenticate


class Dashboard(SimpleView):

    def _do(self):
        self._show()

    def _show(self):
        self.current.request.context['result']['dashboard'] = "Dashboard"
