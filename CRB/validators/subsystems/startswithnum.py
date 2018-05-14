import re 

def startswith_alpha(s):
    try:
        re_alpha_checker = re.compile(r"^[a-zA-Z]+.*")
        if(re_alpha_checker):
            if(re_alpha_checker.match(s)):
                return True
            else:
                return False 
        else:
            return False 
    except:
        raise 
        

def endswith_number(s):
    try:
        re_num_ends = re.compile(r"\d+$")
        if(re_num_ends):
            if(re_num_ends.search(s)):
                return True
            else:
                return False 
    except:
        return False 


#s = re.compile(r"^[a-zA-Z]+.*\d+$")
#print s.match("131WANGOLO JOEL123")
