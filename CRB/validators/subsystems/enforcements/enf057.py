#  enf057.py
#
#  Copyright 2015 Wangolo Joel <wangolo@developer>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

from validators.subsystems.enforcements import enf001
from fraudcategory.subcategory import chequebounceresons


class ENF057(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF057, self).__init__(mobject, field, priority, action)

        self.status = None
    def validate_field(self, field, re_enfor=None):
        try:
            for reason in self.get_b_reasons():
                if field in reason:
                    return True
                else:
                    return False
        except:
            raise

    def get_b_reasons(self):
        return chequebounceresons.get_all()
