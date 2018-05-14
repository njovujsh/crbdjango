from datasetrecords import models
from validators.subsystems import enforcement
from validators.subsystems import picode
from validators.subsystems import enforcement as enfs

class CBACode(picode.PICode):
    def __init__(self, bsmodel, datacode):
        super(CBACode, self).__init__(bsmodel, datacode)

        self.modelstatus = True

    def join_field_rule(self, ret_all=False):
        self.results = {}
        self.ret_field = None

        self.pi_code = self.make_code(self.datacode)

        for field in self.extract():
            if(field == "PI_Identification_Code"):
                self.ret_field = [enfs.data_status()["mandatory"], "A6",
                                       enfs.get_enf_by_number(68)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)

            elif(field == "Branch_Identification_Code"):
                self.ret_field = [enfs.data_status()["mandatory"], "N3",
                                       enfs.get_enf_by_number(14)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Borrowers_Client_Number"):
                self.ret_field = [enfs.data_status()["mandatory"], "AS30",
                                       enfs.get_enf_by_number(14)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)

            elif(field == "Borrower_Classification"):
                self.ret_field = [enfs.data_status()["mandatory"], "N1",
                                       enfs.get_enf_by_number(71)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)

            elif(field == "Credit_Account_Reference"):
                self.ret_field = [enfs.data_status()["mandatory"], "A30",
                                       enfs.get_enf_by_number(14)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Credit_Account_Date"):
                self.ret_field = [enfs.data_status()["mandatory"], "N8",
                                       {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(7)]}
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Credit_Amount"):
                self.ret_field = [enfs.data_status()["conditional"], "N21",
                                       enfs.get_enf_by_number(30)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Facility_Amount_Granted"):
                self.ret_field = [enfs.data_status()["conditional"], "N21",
                                       enfs.get_enf_by_number(29)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Credit_Account_Type"):
                self.ret_field = [enfs.data_status()["mandatory"], "N2",
                                       enfs.get_enf_by_number(61)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Group_Identification_Joint_Account_Number"):
                self.ret_field = [enfs.data_status()["conditional"], "A30",
                                       enfs.get_enf_by_number(25)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Transaction_Date"):
                self.ret_field = [enfs.data_status()["mandatory"], "N8",
                                       {"ENF":[enfs.get_enf_by_number(6), enfs.get_enf_by_number(7)]}
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Currency"):
                self.ret_field = [enfs.data_status()["mandatory"], "A3",
                                       {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(50)]}
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Opening_Balance_Indicator"):
                self.ret_field = [enfs.data_status()["mandatory"], "N1",
                                       enfs.get_enf_by_number(72)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Maturity_Date"):
                self.ret_field = [enfs.data_status()["mandatory"], "N8",
                                      {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(7)]}
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Type_of_Interest"):
                self.ret_field = [enfs.data_status()["mandatory"], "N1",
                                       enfs.get_enf_by_number(73)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Interest_Calculation_Method"):
                self.ret_field = [enforcement.data_status()["mandatory"], "N1",
                                       enfs.get_enf_by_number(74)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Annual_Interest_Rate_at_Disbursement"):
                self.ret_field = [enfs.data_status()["mandatory"], "D6.2",
                                       enfs.get_enf_by_number(14)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Annual_Interest_Rate_at_Reporting"):
                self.ret_field = [enfs.data_status()["mandatory"], "D6.2",
                                       enfs.get_enf_by_number(14)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Date_of_First_Payment"):
                self.ret_field = [enfs.data_status()["conditional"], "N8",
                                       {"ENF":[enfs.get_enf_by_number(6), enfs.get_enf_by_number(39),enfs.get_enf_by_number(7)]}
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Credit_Amortization_Type"):
                self.ret_field = [enfs.data_status()["mandatory"], "N1",
                                       enfs.get_enf_by_number(75)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Credit_Payment_Frequency"):
                self.ret_field = [enforcement.data_status()["conditional"], "N2",
                                       enfs.get_enf_by_number(58)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Number_of_Payments"):
                self.ret_field = [enforcement.data_status()["conditional"], "N4",
                                       enfs.get_enf_by_number(28)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Monthly_Instalment_Amount"):
                self.ret_field = [enforcement.data_status()["conditional"], "N21",
                                       enfs.get_enf_by_number(28)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Current_Balance_Amount"):
                self.ret_field = [enforcement.data_status()["mandatory"], "N21",
                                       {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(112)]}
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Current_Balance_Indicator"):
                self.ret_field = [enforcement.data_status()["mandatory"], "N1",
                                       enfs.get_enf_by_number(76)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Last_Payment_Date"):
                self.ret_field = [enforcement.data_status()["conditional"], "N8",
                                       {"ENF":[enfs.get_enf_by_number(13), enfs.get_enf_by_number(6), enfs.get_enf_by_number(40),enfs.get_enf_by_number(10), enfs.get_enf_by_number(7)]}
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Last_Payment_Amount"):
                self.ret_field = [enforcement.data_status()["conditional"], "N21",
                                       {"ENF":[enfs.get_enf_by_number(8), enfs.get_enf_by_number(32)]}
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Credit_Account_Status"):
                self.ret_field = [enforcement.data_status()["mandatory"], "N1",
                                       {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(4), enfs.get_enf_by_number(2), enfs.get_enf_by_number(3), enfs.get_enf_by_number(1), enfs.get_enf_by_number(44)]}
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
                
            elif(field == "Last_Status_Change_Date"):
                self.ret_field = [enforcement.data_status()["mandatory"], "N8",
                                      {"ENF":[enfs.get_enf_by_number(14), enfs.get_enf_by_number(5),enfs.get_enf_by_number(7)]}
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field =="Credit_Account_Risk_Classification"):
                self.ret_field = [enforcement.data_status()["mandatory"], "N1",
                                       enfs.get_enf_by_number(45)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Credit_Account_Arrears_Date"):
                self.ret_field = [enforcement.data_status()["conditional"], "N8",
                                       {"ENF":[enfs.get_enf_by_number(5), enfs.get_enf_by_number(6), enfs.get_enf_by_number(9),enfs.get_enf_by_number(7), enfs.get_enf_by_number(91)]}
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Number_of_Days_in_Arrears"):
                self.ret_field = [enforcement.data_status()["conditional"], "N10",
                                       enfs.get_enf_by_number(17)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Balance_Overdue"):
                self.ret_field = [enforcement.data_status()["conditional"], "N21",
                                       enfs.get_enf_by_number(18)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Flag_for_Restructured_Credit"):
                self.ret_field = [enforcement.data_status()["mandatory"], "N1",
                                       enfs.get_enf_by_number(77)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Old_Branch_Code"):
                self.ret_field = [enforcement.data_status()["conditional"], "N3",
                                       enfs.get_enf_by_number(23)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Old_Account_Number"):
                self.ret_field = [enforcement.data_status()["conditional"], "A30",
                                       enfs.get_enf_by_number(24)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Old_Client_Number"):
                self.ret_field = [enforcement.data_status()["optional"], "A30",
                                       enfs.get_enf_by_number(15)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Balance_Overdue_Indicator"):
                self.ret_field = [enforcement.data_status()["conditional"], "N1",
                                       {"ENF":[enfs.get_enf_by_number(22), enfs.get_enf_by_number(19)]}
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Credit_Account_Closure_Date"):
                self.ret_field = [enforcement.data_status()["conditional"], "N8",
                                       {"ENF":[enfs.get_enf_by_number(5), enfs.get_enf_by_number(20), enfs.get_enf_by_number(7), enfs.get_enf_by_number(34)]}
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Credit_Account_Closure_Reason"):
                self.ret_field = [enforcement.data_status()["conditional"], "N1",
                                       {"ENF":[enfs.get_enf_by_number(46), enfs.get_enf_by_number(33),enfs.get_enf_by_number(62)]}
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Specific_Provision_Amount"):
                self.ret_field = [enforcement.data_status()["conditional"], "N21",
                                       { }
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Client_Consent_Flag"):
                self.ret_field = [enforcement.data_status()["mandatory"], "A1",
                                       enfs.get_enf_by_number(78)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Client_Advice_Notice_Flag"):
                self.ret_field = [enforcement.data_status()["mandatory"], "A1",
                                       enfs.get_enf_by_number(78)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Term"):
                self.ret_field = [enforcement.data_status()["conditional"], "N5",
                                       enfs.get_enf_by_number(38)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
            elif(field == "Loan_Purpose"):
                self.ret_field = [enforcement.data_status()["mandatory"], "N5",
                                       enfs.get_enf_by_number(14)
                                       ]
                self.update_result(self.results, self.pi_code.next(), self.ret_field, field)
        yield self.results
