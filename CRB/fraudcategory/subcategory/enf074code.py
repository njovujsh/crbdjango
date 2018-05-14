from fraudcategory.subcategory import stakeholdercategory


class ENF074Code(object):
    def __init__(self):
        self.status = (
                    ('0',"Declining Balance"), 
                    ('1',"Flat"),
                    )
                    
    def get_status(self):
        return self.status 
        

def get_class_status():
    credit = ENF074Code()
    return credit.get_status()

