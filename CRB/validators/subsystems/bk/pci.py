#  pci.py
#  
#  Copyright 2015 wangolo joel <wangolo@wangolo-3020>
#  
#  self program is free software you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation either version 2 of the License, or
#  (at your option) any later version.
#  
#  self program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with self program if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
class PCI(object):
    """
    Object for holding the pci field/attributes.
    """
    def __init__(self, *modelfiels):
        self.field_dict =  { }
        if(modelfiels):
            self.handle_modelfields(modelfiels)
            
        self.pci_building_unit_number = ""
        self.pci_building_name = ""
        self.pci_floor_number = ""
        self.pci_plot_or_street_number = ""
        self.pci_lc_or_street_name = ""
        self.pci_parish = ""
        self.pci_suburb = ""
        self.pci_village = ""
        self.pci_county_or_town = ""
        self.pci_district = ""
        self.pci_region = ""
        self.pci_po_box_number = ""
        self.pci_post_office_town = ""
        self.pci_country_code = ""
        self.pci_period_at_address = ""
        self.pci_flag_of_ownership = ""
        self.pci_primary_number_country_dialling_code = ""
        self.pci_primary_number_telephone_number = ""
        self.pci_other_number_country_dialling_code = ""
        self.pci_other_number_telephone_number = ""
        self.pci_mobile_number_country_dialling_code = ""
        self.pci_mobile_number_telephone_number = ""
        self.pci_facsimile_country_dialling_code = ""
        self.pci_facsimile_number = ""
        self.pci_email_address = ""
        self.pci_web_site = ""
        
        
    def  getPci_building_unit_number(self): 
        return self.pci_building_unit_number
   
    def  setPci_building_unit_number(self, pci_building_unit_number): 
        self.pci_building_unit_number = pci_building_unit_number
    
    def  getPci_building_name(self): 
        return self.pci_building_name
    

    def  setPci_building_name(self, pci_building_name): 
        self.pci_building_name = pci_building_name
    
    def  getPci_floor_number(self): 
        return self.pci_floor_number
    
    def  setPci_floor_number(self, pci_floor_number): 
        self.pci_floor_number = pci_floor_number
    
    def  getPci_plot_or_street_number(self): 
        return self.pci_plot_or_street_number
    
    def  setPci_plot_or_street_number(self, pci_plot_or_street_number): 
        self.pci_plot_or_street_number = pci_plot_or_street_number
    

    def  getPci_lc_or_street_name(self): 
        return self.pci_lc_or_street_name
    
    def  setPci_lc_or_street_name(self, pci_lc_or_street_name): 
        self.pci_lc_or_street_name = pci_lc_or_street_name
    
    def  getPci_parish(self): 
        return self.pci_parish
    

    def  setPci_parish(self, pci_parish): 
        self.pci_parish = pci_parish
    
    def  getPci_suburb(self): 
        return self.pci_suburb
    
    def  setPci_suburb(self, pci_suburb): 
        self.pci_suburb = pci_suburb
    

    def  getPci_village(self): 
        return self.pci_village
    
    def  setPci_village(self, pci_village): 
        self.pci_village = pci_village
    

    def  getPci_county_or_town(self): 
        return self.pci_county_or_town
    
    def  setPci_county_or_town(self, pci_county_or_town): 
        self.pci_county_or_town = pci_county_or_town
    
    def  getPci_district(self): 
        return self.pci_district
    
    def  setPci_district(self, pci_district): 
        self.pci_district = pci_district
    
    def  getPci_region(self): 
        return self.pci_region
    
    def  setPci_region(self, pci_region): 
        self.pci_region = pci_region
    
    def  getPci_po_box_number(self): 
        return self.pci_po_box_number
    
    def  setPci_po_box_number(self, pci_po_box_number): 
        self.pci_po_box_number = pci_po_box_number
    
    def  getPci_post_office_town(self): 
        return self.pci_post_office_town
    
    def  setPci_post_office_town(self, pci_post_office_town): 
        self.pci_post_office_town = pci_post_office_town
    
    def  getPci_country_code(self): 
        return self.pci_country_code
    
    def  setPci_country_code(self, pci_country_code): 
        self.pci_country_code = pci_country_code
    

    def  getPci_period_at_address(self):
        return self.pci_period_at_address
    
    def  setPci_period_at_address(self, pci_period_at_address):
        self.pci_period_at_address = pci_period_at_address
    
    def  getPci_flag_of_ownership(self):
        return self.pci_flag_of_ownership

    def  setPci_flag_of_ownership(self, pci_flag_of_ownership):
        self.pci_flag_of_ownership = pci_flag_of_ownership

    def  getPci_primary_number_country_dialling_code(self):
        return self.pci_primary_number_country_dialling_code

    def  setPci_primary_number_country_dialling_code(self, pci_primary_number_country_dialling_code):
        self.pci_primary_number_country_dialling_code = pci_primary_number_country_dialling_code

    def  getPci_primary_number_telephone_number(self):
        return self.pci_primary_number_telephone_number

    def  setPci_primary_number_telephone_number(self, pci_primary_number_telephone_number):
        self.pci_primary_number_telephone_number = pci_primary_number_telephone_number

    def  getPci_other_number_country_dialling_code(self):
        return self.pci_other_number_country_dialling_code

    def  setPci_other_number_country_dialling_code(self, pci_other_number_country_dialling_code):
        self.pci_other_number_country_dialling_code = pci_other_number_country_dialling_code

    def  getPci_other_number_telephone_number(self):
        return self.pci_other_number_telephone_number

    def  setPci_other_number_telephone_number(self, pci_other_number_telephone_number):
        self.pci_other_number_telephone_number = pci_other_number_telephone_number

    def  getPci_mobile_number_country_dialling_code(self):
        return self.pci_mobile_number_country_dialling_code

    def  setPci_mobile_number_country_dialling_code(self, pci_mobile_number_country_dialling_code):
        self.pci_mobile_number_country_dialling_code = pci_mobile_number_country_dialling_code

    def  getPci_mobile_number_telephone_number(self):
        return self.pci_mobile_number_telephone_number

    def  setPci_mobile_number_telephone_number(self, pci_mobile_number_telephone_number):
        self.pci_mobile_number_telephone_number = pci_mobile_number_telephone_number

    def  getPci_facsimile_country_dialling_code(self):
        return self.pci_facsimile_country_dialling_code

    def  setPci_facsimile_country_dialling_code(self, pci_facsimile_country_dialling_code):
        self.pci_facsimile_country_dialling_code = pci_facsimile_country_dialling_code

    def  getPci_facsimile_number(self):
        return self.pci_facsimile_number

    def  setPci_facsimile_number(self, pci_facsimile_number):
        self.pci_facsimile_number = pci_facsimile_number

    def  getPci_email_address(self):
        return self.pci_email_address

    def  setPci_email_address(self, pci_email_address):
        self.pci_email_address = pci_email_address

    def  getPci_web_site(self):
        return self.pci_web_site

    def  setPci_web_site(self, pci_web_site):
        self.pci_web_site = pci_web_site
