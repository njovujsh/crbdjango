import reportstatus 

DATA = {
            1L: {u'CRB001': {'ENF': True, 'FORMAT': True, 'Mandatory': False}},
            2L: {u'CRB001': {'ENF': True, 'FORMAT': True, 'Mandatory': True}},
            3L: {u'CRB001': {'ENF': True, 'FORMAT': True, 'Mandatory': True}},
            4L: {u'CRB001': {'ENF': True, 'FORMAT': True, 'Mandatory': True}},
            5L: {u'CRB001': {'ENF': True, 'FORMAT': True, 'Mandatory': True}},
            6L: {u'CRB001': {'ENF': True, 'FORMAT': True, 'Mandatory': True}},
            7L: {u'CRB001': {'ENF': True, 'FORMAT': True, 'Mandatory': True}},
            8L: {u'CRB001': {'ENF': True, 'FORMAT': True, 'Mandatory': True}},
            9L: {u'CRB001': {'ENF': True, 'FORMAT': True, 'Mandatory': True}},
            10L: {u'CRB001': {'ENF': True, 'FORMAT': True, 'Mandatory': True}},
            11L: {u'CRB001': {'ENF': True, 'FORMAT': True, 'Mandatory': True}},
            12L: {u'CRB001': {'ENF': True, 'FORMAT': True, 'Mandatory': True}},
            13L: {u'CRB001': {'ENF': True, 'FORMAT': True, 'Mandatory': True}},
            14L: {u'CRB001': {'ENF': False, 'FORMAT': True, 'Mandatory': True}},
            15L: {u'CRB001': {'ENF': True, 'FORMAT': True, 'Mandatory': True}},
            16L: {u'CRB001': {'ENF': True, 'FORMAT': True, 'Mandatory': True}},
            17L: {u'CRB001': {'ENF': True, 'FORMAT': True, 'Mandatory': True}},
            18L: {u'CRB001': {'ENF': True, 'FORMAT': True, 'Mandatory': True}},
            19L: {u'CRB001': {'ENF': False, 'FORMAT': True, 'Mandatory': True}},
            20L: {u'CRB001': {'ENF': True, 'FORMAT': True, 'Mandatory': True}},
            21L: {u'CRB001': {'ENF': True, 'FORMAT': True, 'Mandatory': True}},
            22L: {u'CRB001': {'ENF': True, 'FORMAT': True, 'Mandatory': True}},
            23L: {u'CRB001': {'ENF': False, 'FORMAT': True, 'Mandatory': True}},
            24L: {u'CRB001': {'ENF': True, 'FORMAT': True, 'Mandatory': True}}
}

S = reportstatus.ReportStatus(True, True)
print "PASSED ", S.get_passed()
print "FAILED ", S.get_failed()

S.analyse_failed_passed(DATA)
print "\n-------------------------\n"
print "PASSED ", S.get_passed()
print "FAILED ", S.get_failed()
