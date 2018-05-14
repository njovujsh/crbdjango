#  pivalidate.py
#
#  Copyright 2015 Wangolo Joel <wangolo@developer>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
from validators.subsystems import picode
from datasetrecords import models
from validators.subsystems import checkstatus
from validators.subsystems import checkformat
from validators.subsystems import checkenforcements
from validators.subsystems.csvwriters  import writers
from validators.subsystems.datasets import validationstatus
from collections import defaultdict

class PIValidate(object):
    def __init__(self, code="PI"):
        self.running = True
        self._model = models.PARTICIPATING_INSTITUTION
        self.all_records = models.PARTICIPATING_INSTITUTION.objects.all()
        self.code = code
        self.pi_c_code = picode.PICode(self._model, self.code)
        self.dict_list = []
        self.real_passed = {}
        self.record_writer = writers.ExcelWriter()

        self.fileobj = self.record_writer.openfilename("newcsv.csv")
        self.csvwrite = self.record_writer.create_csvobject(self.fileobj)

    def begin_validation(self):
        try:

            self.all_fields = self.pi_c_code.extract()
            self.examine_field(self.all_fields)
        except Exception as e:
            # Log 
            pass 

    def examine_field(self, field):
        try:
            for f in field:
                try:
                    self.ret_require = self.get_field_requirement(f).next()
                    self.real_passed[f]=self.v_lid(f, self.ret_require)
                except StopIteration as error:
                    pass
        except Exception as e:
            pass 
        
    def get_field_requirement(self, field):
        try:
            for all_field in self.pi_c_code.join_field_rule():
                for v_field in all_field.values():
                    f = v_field.get(field)
                    if(f == None):
                        pass
                    else:
                        yield f
        except Exception as e:
            pass

    def check_data_in_field(self, f, rules):
        self.passed = { }

    def v_picode(self, f, rules):
        self.passed = { }
        if(f == "PI_Identification_Code"):
            self.pass_pi = {}
            self.final_result = {}
            for records in self.all_records:
                for r in rules:
                    if r == "M":
                        if(records.PI_Identification_Code.pi_identification_code):
                            self.passed[records.PI_Identification_Code.pi_identification_code]={"Mandatory":True}
                        else:
                            self.passed[records.PI_Identification_Code.pi_identification_code]={"Mandatory":False}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.PI_Identification_Code.pi_identification_code, priority=r.get(key))
                            self.passed[records.PI_Identification_Code.pi_identification_code]["ENF"]=self.statuss.validate_field(records.PI_Identification_Code.pi_identification_code)
                    else:
                        if(len(records.PI_Identification_Code.pi_identification_code) == 6):
                            self.passed[records.PI_Identification_Code.pi_identification_code]["FORMAT"]=checkformat.is_alapnumeric(records.PI_Identification_Code.pi_identification_code)
                        else:
                            self.passed[records.PI_Identification_Code.pi_identification_code]["FORMAT"]=False
        
        if(not len(self.passed)):
            pass 
        else:
            return self.passed 
        
    def v_it(self, f, rules):
        self.passed = { }
        if(f == "Institution_Type"):
            self.pass_it = { }
            for records in self.all_records:
                for r in rules:
                    if r == "M":
                        if(records.Institution_Type):
                            self.passed[records.Institution_Type]={"Mandatory":True}
                        else:
                            self.passed[records.Institution_Type]={"Mandatory":True}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Institution_Type, priority=r.get(key))
                            self.passed[records.Institution_Type]["ENF"]=self.statuss.validate_field(records.Institution_Type)
                    else:
                        if(len(records.Institution_Type) == 3):
                            self.passed[records.Institution_Type]["FORMAT"]=checkformat.is_alapnumeric(records.Institution_Type)
                        else:
                            self.passed[records.Institution_Type]["FORMAT"]=False

        if(not len(self.passed)):
            pass 
        else:
            return self.passed 

    def v_in(self, f, rules):
        self.passed = { }
        if(f == "Institution_Name"):
            self.pass_in = {}
            for records in self.all_records:
                for r in rules:
                    if r == "M":
                        if(records.Institution_Name):
                            self.passed[records.Institution_Name]={"Mandatory":True}
                        else:
                            self.passed[records.Institution_Name]={"Mandatory":True}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.Institution_Name, priority=r.get(key))
                            self.passed[records.Institution_Name]["ENF"]=self.statuss.validate_field(records.Institution_Name)
                    else:
                        if(len(records.Institution_Name) > 100):
                            self.passed[records.Institution_Name]["FORMAT"]=False
                        else:
                            self.passed[records.Institution_Name]["FORMAT"]=checkformat.sub_alphanumeric(records.Institution_Name)

        if(not len(self.passed)):
            pass 
        else:
            return self.passed 

    def v_lid(self, f, rules):
        self.passed = { }
        if(f == "License_Issuing_Date"):
            self.pass_lid = {}
            for records in self.all_records:
                for r in rules:
                    if r == "M":
                        if(records.License_Issuing_Date):
                            self.passed[records.License_Issuing_Date]={"Mandatory":True}
                        else:
                            self.passed[records.License_Issuing_Date]={"Mandatory":True}

                    elif(isinstance(r, dict)):
                        for key in r:
                            self.statuss = checkenforcements.check_enforcements(key, self._model, records.License_Issuing_Date.replace("-", "",10), priority=r.get(key))
                            self.passed[records.License_Issuing_Date]["ENF"]=self.statuss.validate_field(records.License_Issuing_Date.replace("-","",10))

                    else:
                        if(len(records.License_Issuing_Date.replace("-", "", 10)) == 8):
                            self.passed[records.License_Issuing_Date]["FORMAT"]=checkformat.is_numeric(records.License_Issuing_Date.replace("-", "",10))
                        else:
                            self.passed[records.License_Issuing_Date]["FORMAT"]=False

        if(not len(self.passed)):
            pass 
        else:
            return self.passed 
        
    def set_code(self, dc_code):
        self.pi_c_code = dc_code

    def openfiles(self, filename="testouput.txt"):
        try:
            return open(filename, "w")
        except Exception as e:
            pass 

    def merged_dict(self):
        return defaultdict(list)

    def add_dict_to_list(self, newdict):
        if(newdict):
            try:
                self.dict_list.append(newdict)
            except:
                raise
        else:
            return False

    def merged_dictionary(self, dictlist):
        self.merged = self.merged_dict()
        try:
            if(dictlist):
                for dict_items in dictlist:
                    if(isinstance(dict_items, int)):
                        pass
                    else:
                        for k, v in dict_items.items():
                            self.merged[k].append(v)
            else:
                return None
        except:
            raise
        else:
            return self.merged


    def get_dict_list(self, in_tuple=False):
        if(in_tuple):
            return tuple(self.dict_list)
        else:
            return self.dict_list

    def get_real_dict(self):
        return self.real_passed

    def add_dict_to_list(self, dic, in_tuple=False):
        if(in_tuple):
            return tuple([dic])
        else:
            return [dic]

    def write_to_file(self, filepath=None):
        try:
            self.fileobject = self.record_writer.openfilename("wangolo.csv")
            self.csv_record_writers = self.record_writer.create_csvobject(self.fileobject)

            for data in self.add_dict_to_list(self.get_real_dict(), in_tuple=True):
                for k, v in data.iteritems():
                    print k, v
                    self.csv_record_writers.writerow([v,k])
            self.fileobject.close()
        except:
            raise

    def get_record_keys(self, validated_record):
        try:
            
            if validated_record == None:
                pass 
            else:
                for key in validated_record.keys():
                    yield key
        except:
            raise

    def validation_status(self, validated_record):
        try:
            final_status = []
            for rec_key in self.get_record_keys(validated_record):
                if(self.get_format(validated_record[rec_key]) and self.get_condition(validated_record[rec_key]) and self.get_format(validated_record[rec_key])):
                    #print "CALLED VSTATUS ", rec_key
                    yield rec_key

                elif(get_enf(validated_record[rec_key]) == False):
                    yield -1 #for failed enforcements

                elif(get_condition(validated_record[rec_key]) == False):
                    yield -2 #for valied conditions

                elif(get_format(validated_record[rec_key]) == False):
                    yield -3 #for falied format

                else:
                    yield False

            #yield final_status
        except:
            raise

    def get_format(self, validated_record):
        try:
            return validated_record.get("FORMAT")
        except:
            raise

    def get_enf(self,validated_record):
        try:
            return validated_record.get("ENF")
        except:
            raise

    def get_condition(self, validated_record):
        try:
            return validated_record.get("Mandatory")
        except:
            raise

