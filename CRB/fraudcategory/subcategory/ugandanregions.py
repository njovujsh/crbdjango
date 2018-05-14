from fraudcategory.subcategory import stakeholdercategory

class UgandanRegions(object):
    def __init__(self):
        self.regions = (
                    ('0',"Central Region"), 
                    ('1',"Western Region"),
                    ('2',"Eastern Region"),
                    ("8","Northern Region"),
                    )
        self.regions_dict = {
                    '0':"Central Region", 
                    '1':"Western Region",
                    '2':"Eastern Region",
                    "8":"Northern Region",
                      }
                    
    def get_region(self):
        return self.regions 
        
    
    def search_region(self, code):
        return self.regions_dict.get(code)
        
def get_class_region():
    regions = UgandanRegions()
    return regions.get_region()
