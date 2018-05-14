class EmployementInformation(object):
    def __init__(self):
        self.values = (
                        ('0', "Formal Employment"),
                       ('1', "Informal Employment"),
                       ('2', "Self Employed"),
                       ('3', "Unemployed"),
                        )
                        
        self.values_dict = {'0':"Formal Employment",
                       '1':"Informal Employment",
                       '2':"Self Employed",
                       '3':"Unemployed"
                        }
        
        
    def get_employement(self):
        return self.values
        
    def search_value(self, value):
        try:
            return self.values_dict.get(value)
        except:
            raise  
    
def get_employement():
    E = EmployementInformation()
    return E.get_employement()    

