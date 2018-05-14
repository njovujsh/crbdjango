from fraudcategory.subcategory import stakeholdercategory


class OpenBalanceIndicator(object):
    def __init__(self):
        self.status = (
                    ('0',"Credit Limit"), 
                    ('1',"Opening Balance"),
                    )
                    
    def get_status(self):
        return self.status 
        

def get_class_status():
    credit = OpenBalanceIndicator()
    return credit.get_status()



