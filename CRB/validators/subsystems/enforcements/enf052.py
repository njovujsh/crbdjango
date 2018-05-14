from validators.subsystems.enforcements import enf001 
from fraudcategory.subsystems import allmodules

class ENF052(enf001.ENF001):
    def __init__(self, mobject, field, priority, action):
        super(ENF052, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        
    def validate_field(self, field):
        try:
            self.module = self.load_module_by_id(field)
            #print "MODULE ", self.module, field 
            if(self.module):
                try:
                    v = self.module.get_subcategory_by_dict().values()
                    for sub in self.module.get_subcategory_by_dict().values():
                        if str(field) in sub.values():
                            return True
                        else:
                            return False 

                except:
                    raise 
            
        except:
            raise 
    
    def load_module_by_id(self, ID):
        try:
            if(ID):
                try:
                    return allmodules.get_module_by_id(int(ID))
                except:
                    raise 
            else:
                return False 
        except:
            raise 


