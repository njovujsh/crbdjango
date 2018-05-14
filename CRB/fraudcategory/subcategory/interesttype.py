from fraudcategory.subcategory import stakeholdercategory


class InterestType(object):
    def __init__(self):
        self.status = (
                    ('0',"Fixed"), 
                    ('1',"Floating"),
                    )
                    
    def get_status(self):
        return self.status 
        

def get_class_status():
    credit = InterestType()
    return credit.get_status()


