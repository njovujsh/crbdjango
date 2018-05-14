from validators.subsystems.enforcements import enf001 
from validators.subsystems import startswithnum 


class ENF069(enf001.ENF001):
    def __init__(self,mobject, field, priority, action):
        super(ENF069, self).__init__(mobject, field, priority, action)
        
        self.status = None 
        self.equal_to = ['CB', 'MDI', 'PI', 'CP', 'PSB', 'MEB', 'MOB', 'AH', 'FH', 'DH','ACP','CI']
        
    def validate_field(self, field):
        try:
            return field in self.equal_to 
            #return self.equal_to_field(field)
        except:
            raise 
    
    def equal_to_field(self, field):
        return field in self.equal_to 
