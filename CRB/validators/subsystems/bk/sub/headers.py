import string 


headers = { }

def populate_headers(dicts):
    if(isinstance(dicts, dict)):
        try:
            dicts["Delimeter"]="|"
        except:
            raise 
        else:
            return dicts 
    else:
        return None 
        
        
p = populate_headers(headers)
print p
print p.get("Delimeter")
