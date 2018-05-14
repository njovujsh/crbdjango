#  datasetmatch.py
#  
#  Copyright 2015 wangolo joel <wangolo@wangolo-3020>
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

_MODULE_NAME={
    "BORROWERSTAKEHOLDER":"BS",
    "BOUNCEDCHEQUES":"BC",
    "COLLATERAL CREDIT GUARANTOR":"CCG",
    "COLLATERAL MATERIAL COLLATERAL":"CMC",
    "CREDITBORROWERACCOUNT":"CBA",
    "CREDIT APPLICATION":"CAP",
    "FINANCIAL MALPRACTICE DATA":"FRA",
    "INSTITUTION BRANCH":"IB",
    "PARTICIPATINGINSTITUTIONSTAKEHOLDER":"PIS",
    "PARTICIPATING INSTITUTION":"PI"
}


def load_file_extension(dataset):
    """
    Given the data set search for the
    given extension.
    """
    try:
        return _MODULE_NAME.get(str(dataset).upper().replace("_", " ", len(str(dataset))))
    except:
        raise 
