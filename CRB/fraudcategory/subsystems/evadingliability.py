#  evadingliability.py
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
from fraudcategory.subsystems import falseid 


class EvadingLiability(falseid.FalseID):
    def __init__(self,category,code=6, length=15):
        super(EvadingLiability, self).__init__(category, code=5,length=length)
        
        self.subcategory = ["FALSE REPORT FINANCIAL DOCS LOST", "FALSE REPORT OF ATM MISUSE",
                            "SIGNIFICANT MISUSE OF ACCOUNT", "GOODS RETURNED (REFUNDS)",
                            "DEBIT/STOP ORDER", "MULTILE ENCASHMENT", "CHEQUE","CREDIT CARD",
                            "PERSONAL LOAN", "MORTAGE FINANCE", "CAR LOAN", "RETAIL  CREDIT",
                            "INTERNET BANKING", "INTERNET SHOPPING", "OTHERS"
                            ]
