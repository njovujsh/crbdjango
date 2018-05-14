
class Appendix15(object):
    def __init__(self):
        self.values = ["Hire Purchase", "Leasing", "Letter of Credit", "Line of Credit",
                        "Mortage" "Overdraft", "Bond", "Revolving Credit Facility",
                        "Unsecured Loan", "Secured Loan"
                        ]

        self.classification = {"Loan":1, "Loan":2, "Facility":3,  "Facility":4, "Loan":6,
                                "Facility":7, "Facility":8, "Facility":9, "Loan":10, "Loan":11
                               }
                               
        self.product_classification = {"1":"HP", "2":"L", "11":"SL",  "10":"UL", "4":"LC",
                                "9":"RCF", "6":"M", "7":"OD", "3":"LOC", "8":"B"
                               }

        self.classification2 = {"Hire Purchase":{"Loan":'1'}, "Leasing":{"Loan":'2'},
                                "Letter of Credit":{"Facility":'3'},  "Line of Credit":{"Facility":'4'},
                                "Mortage":{"Loan":'6'}, "Overdraft":{"Facility":'7'},
                                "Bond":{"Facility":'8'}, "Revolving Credit Facility":{"Facility":'9'},
                                "Unsecured Loan":{"Loan":'10'}, "Secured Loan":{"Loan":'11'}
                               }


        self.dict_values = {}

    def associated(self):
        try:
            for keys in self.classification.keys():
                for value in self.values:
                    self.dict_values[value] = {keys:self.classification[keys]}
        except:
            raise
        else:
            return self.dict_values

    def make_tuple_of_two(self, value, index):
        if (value and index):
            return (value, index)
        else:
            return None

    def get_values_tuple(self):
        self.made_tuple = []
        for s in self.get_classification2().keys():
            for x in self.get_classification2()[s].values():
                if(self.make_tuple_of_two(str(s), str(x)) in self.made_tuple):
                    pass
                else:
                    self.made_tuple.append(self.make_tuple_of_two(str(x), str(s)))
        return tuple(self.made_tuple)

    def get_values(self):
        return self.values

    def get_classification(self):
        return self.classification

    def get_classification2(self):
        return self.classification2

    def get_dict_values(self):
        if(not len(self.dict_values)):
            return self.associated()
        else:
            return self.dict_values

    def value_2_key(self, dicts):
        """
        Given the dictionary convert the values into keys.
        """
        self.DT = {}
        if(isinstance(dicts, dict)):
            try:
                for k in dicts.keys():
                    self.DT[dicts[k]]=k
            except:
                raise
            else:
                return self.DT
        else:
            return None

    def get_value_gen(self):
        """
        Return a generator instead.
        """
        for k in self.get_classification2().values():
            yield k

    def find_value(self, key):
        for k in self.get_value_gen():
            if self.value_2_key(k).get(key):
                return True

    def get_productclassification(self, code):
        try:
            if(code):
                return self.product_classification.get(code)
        except:
            raise
            
def get_apnx():
    A = Appendix15()
    return A.get_classification2()

