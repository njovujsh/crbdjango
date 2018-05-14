class Gender(object):
    def __init__(self):
        self.gender = (
                        ('0', "Male"),
                       ('1', "Female"),
                        )
                        
        self.gender_dict = {'0':"Male",
                       '1':"Female",
                        }
        
        
    def get_gender(self):
        return self.gender
        
    def search_gender(self, value):
        try:
            return self.gender_dict.get(value)
        except:
            raise  
    
def get_gender():
    G = Gender()
    return G.get_gender()    

