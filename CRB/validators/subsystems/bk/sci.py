#  sci.py
#  
#  Copyright 2015 wangolo joel <wangolo@wangolo-3020>
#  
#  self. program is free software = "" you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation = "" either version 2 of the License, or
#  (at your option) any later version.
#  
#  self. program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY = "" without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with self. program = "" if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

class SCI(object):
    """
    Object for handling the sci fields
    """
    def __init__(self, *fields):
        self.fields_dict = { }
        if(self.fields):
            self.process_fields(fields)
            
        self.sci_building_unit_number = ""
        self.sci_building_name = ""
        self.sci_floor_number = ""
        self.sci_plot_or_street_number = ""
        self.sci_lc_or_street_name = ""
        self.sci_parish = ""
        self.sci_suburb = ""
        self.sci_village = ""
        self.sci_county_or_town = ""
        self.sci_district = ""
        self.sci_region = ""
        self.sci_po_box_number = ""
        self.sci_post_office_town = ""
        self.sci_country_code = ""
        self.sci_period_at_address = ""
        self.sci_flag_of_ownership = ""
        self.sci_primary_number_country_dialling_code = ""
        self.sci_primary_number_telephone_number = ""
        self.sci_other_number_country_dialling_code = ""
        self.sci_other_number_telephone_number = ""
        self.sci_mobile_number_country_dialling_code = ""
        self.sci_mobile_number_telephone_number = ""
        self.sci_facsimile_country_dialling_code = ""
        self.sci_facsimile_number = ""
        self.sci_email_address = ""
        self.sci_web_site = ""
        
    def  getSci_building_unit_number():
        return self.sci_building_unit_number
    
    def  setSci_building_unit_number(self, sci_building_unit_number):
        self.sci_building_unit_number = sci_building_unit_number
    
    def  getSci_building_name():
        return self.sci_building_name
    
    def  setSci_building_name(self, sci_building_name):
        self.sci_building_name = sci_building_name
    
    def  getSci_floor_number():
        return self.sci_floor_number
    
    def  setSci_floor_number(self, sci_floor_number):
        self.sci_floor_number = sci_floor_number
    
    def  getSci_plot_or_street_number():
        return self.sci_plot_or_street_number
    
    def  setSci_plot_or_street_number(self, sci_plot_or_street_number):
        self.sci_plot_or_street_number = sci_plot_or_street_number
    
    def  getSci_lc_or_street_name():
        return self.sci_lc_or_street_name
    
    def  setSci_lc_or_street_name(self, sci_lc_or_street_name):
        self.sci_lc_or_street_name = sci_lc_or_street_name
    
    def  getSci_parish():
        return self.sci_parish
    
    def  setSci_parish(self, sci_parish):
        self.sci_parish = sci_parish
    
    def  getSci_suburb():
        return self.sci_suburb
    
    def  setSci_suburb(self, sci_suburb):
        self.sci_suburb = sci_suburb
    
    def  getSci_village():
        return self.sci_village
    
    def  setSci_village(self, sci_village):
        self.sci_village = sci_village
   
    def  getSci_county_or_town():
        return self.sci_county_or_town
    
    def  setSci_county_or_town(self, sci_county_or_town):
        self.sci_county_or_town = sci_county_or_town
    
    def  getSci_district():
        return self.sci_district
    
    def  setSci_district(self, sci_district):
        self.sci_district = sci_district
    
    def  getSci_region():
        return self.sci_region
    
    def  setSci_region(self, sci_region):
        self.sci_region = sci_region
    
    def  getSci_po_box_number():
        return self.sci_po_box_number
    
    def  setSci_po_box_number(self, sci_po_box_number):
        self.sci_po_box_number = sci_po_box_number
    
    def  getSci_post_office_town():
        return self.sci_post_office_town
    
    def  setSci_post_office_town(self, sci_post_office_town):
        self.sci_post_office_town = sci_post_office_town
   
    def  getSci_country_code():
        return self.sci_country_code
    
    def  setSci_country_code(self, sci_country_code):
        self.sci_country_code = sci_country_code
    
    def  getSci_period_at_address():
        return self.sci_period_at_address
    
    def  setSci_period_at_address(self, sci_period_at_address):
        self.sci_period_at_address = sci_period_at_address
    
    def  getSci_flag_of_ownership():
        return self.sci_flag_of_ownership
    
    def  setSci_flag_of_ownership(self, sci_flag_of_ownership):
        self.sci_flag_of_ownership = sci_flag_of_ownership
   
    def  getSci_primary_number_country_dialling_code():
        return self.sci_primary_number_country_dialling_code
    
    def  setSci_primary_number_country_dialling_code(self, sci_primary_number_country_dialling_code) :
        self.sci_primary_number_country_dialling_code = sci_primary_number_country_dialling_code
    
    def  getSci_primary_number_telephone_number() :
        return self.sci_primary_number_telephone_number
    
    def  setSci_primary_number_telephone_number(self, sci_primary_number_telephone_number) :
        self.sci_primary_number_telephone_number = sci_primary_number_telephone_number
    
    def  getSci_other_number_country_dialling_code() :
        return self.sci_other_number_country_dialling_code
    
    def  setSci_other_number_country_dialling_code(self, sci_other_number_country_dialling_code) :
        self.sci_other_number_country_dialling_code = sci_other_number_country_dialling_code
    
    def  getSci_other_number_telephone_number() :
        return self.sci_other_number_telephone_number
    
    def  setSci_other_number_telephone_number(self, sci_other_number_telephone_number):
        self.sci_other_number_telephone_number = sci_other_number_telephone_number
    
    def  getSci_mobile_number_country_dialling_code():
        return self.sci_mobile_number_country_dialling_code
    
    def  setSci_mobile_number_country_dialling_code(self, sci_mobile_number_country_dialling_code):
        self.sci_mobile_number_country_dialling_code = sci_mobile_number_country_dialling_code
    
    def  getSci_mobile_number_telephone_number():
        return self.sci_mobile_number_telephone_number
    
    def  setSci_mobile_number_telephone_number(self, sci_mobile_number_telephone_number) :
        self.sci_mobile_number_telephone_number = sci_mobile_number_telephone_number
    
    def  getSci_facsimile_country_dialling_code():
        return self.sci_facsimile_country_dialling_code
    
    def  setSci_facsimile_country_dialling_code(self, sci_facsimile_country_dialling_code):
        self.sci_facsimile_country_dialling_code = sci_facsimile_country_dialling_code
    
    def  getSci_facsimile_number():
        return self.sci_facsimile_number
    
    def  setSci_facsimile_number(self, sci_facsimile_number):
        self.sci_facsimile_number = sci_facsimile_number
    
    def  getSci_email_address() :
        return self.sci_email_address
    
    def  setSci_email_address(self, sci_email_address):
        self.sci_email_address = sci_email_address
    
    def  getSci_web_site():
        return self.sci_web_site
    
    def  setSci_web_site(self, sci_web_site):
        self.sci_web_site = sci_web_site
