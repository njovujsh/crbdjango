package main;

import crb.fieldmethods.FIELDS;

public class Main {
	FIELDS validate_fileds = new FIELDS();

	public String csvfilewriter(Object pi_identification_code, Object pi_name,
			Object submission_date, Object version, Object date_of_creation,
			Object file_identifier) {
		String string_formated = "\"H\"|\"" + pi_identification_code + "\""
				+ "|" + "\"" + pi_name + "\"" + "|" + "\"" + submission_date
				+ "\"" + "|" + "\"" + version + "\"" + "|" + "\""
				+ date_of_creation + "\"" + "|" + "\"" + file_identifier + "\"";
		return string_formated;
	}

	public static void main(String[] paramArrayOfString) {
//		MESSAGES msg = MESSAGES.ENF021.namexx(MESSAGES.values());
		System.out.println();
	}
}
