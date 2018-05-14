package crb.fieldmethods;

import java.util.ArrayList;
import java.util.List;

import crb.constantvalues.ENF2;
import crb.constantvalues.enf.ENF068;
import crb.constantvalues.enf.ENF069;
import crb.constantvalues.microflags.ADDRESSBUILDING;
import crb.constantvalues.microflags.DVR;
import crb.constantvalues.microflags.MESSAGES;
import crb.constantvalues.microflags.STATUS;
import crb.pojos.RETURNEDVALUES;

public class FIELDS {
	public List<RETURNEDVALUES> field_validator(DVR data_dss_dvr, Object value) {
		List<RETURNEDVALUES> report_value_status_list_of_issues = new ArrayList();
		RETURNEDVALUES report_value_status = new RETURNEDVALUES();
		try {
			switch (data_dss_dvr.getStatus()) {
			case C:
				if (value.equals(null)) {
					report_value_status
							.setValue(new MESSAGES[] { MESSAGES.mandatory });
					report_value_status
							.setInfornation_of_returned_value(data_dss_dvr);

					report_value_status_list_of_issues.add(report_value_status);
				} else {
					formatChecker(data_dss_dvr, report_value_status);
				}
				break;
			case M:
				condition_checker(value, new ENF2[] { ENF2.ENF001 });
			default:
				break;
			}
		} catch (Exception e) {
			report_value_status.setValue(new MESSAGES[] { MESSAGES.mandatory });
			report_value_status.setInfornation_of_returned_value(data_dss_dvr);
			report_value_status_list_of_issues.add(report_value_status);
		}
		return report_value_status_list_of_issues;
	}

	private DVR enformentChecker(ENF2 enforcement, Object value) {
		DVR dvr_dss = null;

		ENF068 enf68 = ENF068.CB001;

		ENF069 enf69 = ENF069.AH;
		if (!enforcement.equals(ENF2.ENF001)) {
			if (!enforcement.equals(ENF2.ENF002)) {
				if (!enforcement.equals(ENF2.ENF007)) {
					if (!enforcement.equals(ENF2.ENF014)) {
						if (enforcement.equals(ENF2.ENF068)) {
							switch (enf68) {
							case CB001:
								dvr_dss.setReasons(MESSAGES.valid);
								break;
							case CB002:
								dvr_dss.setReasons(MESSAGES.valid);
							default:
								dvr_dss.setReasons(MESSAGES.ENF068);

								break;
							}
						} else if (dvr_dss.getEnforcmentcodes().equals(
								ENF2.ENF069)) {
							switch (enf69) {
							case MOB:
								dvr_dss.setReasons(MESSAGES.valid);
								break;
							case AH:
								dvr_dss.setReasons(MESSAGES.valid);
								break;
							default:
								dvr_dss.setReasons(MESSAGES.ENF069);

								break;
							}
						} else if (dvr_dss.getEnforcmentcodes().equals(
								ENF2.ENF021)) {
							if (ADDRESSBUILDING.YESNO.name().equals("NO")) {
								dvr_dss.setStatus(STATUS.O);
								field_validator(dvr_dss, value);
							} else if (ADDRESSBUILDING.YESNO.name().equals(
									"YES")) {
								dvr_dss.setStatus(STATUS.M);
								field_validator(dvr_dss, value);
							}
						} else if (!dvr_dss.getEnforcmentcodes().equals(
								ENF2.ENF129)) {
							dvr_dss.getEnforcmentcodes().equals(ENF2.ENF025);
						}
					}
				}
			}
		}
		return dvr_dss;
	}

	private MESSAGES condition_checker(Object value, ENF2... enforcment) {
		ENF2 enformet_rule1 = null;
		ENF2 enformet_rule2 = null;
		ENF2 enformet_rule3 = null;
		ENF2 enformet_rule4 = null;

		ENF2[] list_of_enforcement_codes = enforcment;
		int number_of_enforcement_codes = list_of_enforcement_codes.length;
		switch (number_of_enforcement_codes) {
		case 2:
			enformet_rule1 = list_of_enforcement_codes[0];
			enformet_rule2 = list_of_enforcement_codes[1];
			if (enformet_rule1.getPriolity() <= enformet_rule2.getPriolity()) {
				enformentChecker(enformet_rule1, "value");
			} else {
				enformentChecker(enformet_rule2, "value");
			}
			break;
		case 3:
			enformet_rule1 = list_of_enforcement_codes[0];
			enformet_rule2 = list_of_enforcement_codes[1];
			enformet_rule3 = list_of_enforcement_codes[2];
			if (enformet_rule1.getPriolity() <= enformet_rule2.getPriolity()) {
				if (enformet_rule1.getPriolity() <= enformet_rule3
						.getPriolity()) {
					enformentChecker(enformet_rule1, "value");
					break;
				}
			}
			if (enformet_rule2.getPriolity() <= enformet_rule1.getPriolity()) {
				if (enformet_rule2.getPriolity() <= enformet_rule3
						.getPriolity()) {
					enformentChecker(enformet_rule2, "value");

					break;
				}
			}
			if (enformet_rule3.getPriolity() <= enformet_rule1.getPriolity()) {
				if (enformet_rule3.getPriolity() <= enformet_rule2
						.getPriolity()) {
					enformentChecker(enformet_rule3, "value");

					break;
				}
			}
			String error_value = "method @condition_checker in *FIELDS";
			enformentChecker(enformet_rule3, "value");

			break;
		case 4:
			enformet_rule1 = list_of_enforcement_codes[0];
			enformet_rule2 = list_of_enforcement_codes[1];
			enformet_rule3 = list_of_enforcement_codes[2];
			enformet_rule4 = list_of_enforcement_codes[3];
			if (enformet_rule1.getPriolity() <= enformet_rule2.getPriolity()) {
				if (enformet_rule1.getPriolity() <= enformet_rule3
						.getPriolity()) {
					if (enformet_rule1.getPriolity() <= enformet_rule4
							.getPriolity()) {
						enformentChecker(enformet_rule1, "value");
						break;
					}
				}
			}
			if (enformet_rule2.getPriolity() <= enformet_rule1.getPriolity()) {
				if (enformet_rule2.getPriolity() <= enformet_rule3
						.getPriolity()) {
					if (enformet_rule2.getPriolity() <= enformet_rule4
							.getPriolity()) {
						enformentChecker(enformet_rule2, "value");

						break;
					}
				}
			}
			if (enformet_rule3.getPriolity() <= enformet_rule1.getPriolity()) {
				if (enformet_rule3.getPriolity() <= enformet_rule2
						.getPriolity()) {
					if (enformet_rule3.getPriolity() <= enformet_rule4
							.getPriolity()) {
						enformentChecker(enformet_rule3, "value");

						break;
					}
				}
			}
			if (enformet_rule4.getPriolity() <= enformet_rule1.getPriolity()) {
				if (enformet_rule4.getPriolity() <= enformet_rule2
						.getPriolity()) {
					if (enformet_rule4.getPriolity() <= enformet_rule3
							.getPriolity()) {
						enformentChecker(enformet_rule4, "value");
						break;
					}
				}
			}
			error_value = "method @condition_checker in *FIELDS";
			enformentChecker(enformet_rule4, "value");

			break;
		default:
			enformet_rule1 = list_of_enforcement_codes[0];
		}
		return null;
	}

	public List<RETURNEDVALUES> formatChecker(DVR data_dss_dvr, Object value) {
		RETURNEDVALUES report_value_status = new RETURNEDVALUES();
		List<RETURNEDVALUES> report_value_status_list_of_issues = new ArrayList();
		switch (data_dss_dvr.getFormat()) {
		case A20:
			if (value.equals("No")) {
				report_value_status
						.setValue(new MESSAGES[] { MESSAGES.format });
				report_value_status
						.setInfornation_of_returned_value(data_dss_dvr);

				report_value_status_list_of_issues.add(report_value_status);
			}
			break;
		case A2:
			break;
		case A50:
			break;
		}
		return report_value_status_list_of_issues;
	}

	public static void main(String[] args) {
		FIELDS feilds = new FIELDS();

		feilds.field_validator(DVR.PI001, "HSGFTTFF");
	}
}
