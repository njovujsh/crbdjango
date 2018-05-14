package crb.constantvalues;

public enum TYPEOFINSTITUTION {
	CB("COMMERCIAL BANK"), MDI("MICROFINACE DEPOSIT TAKING INSTITUTION"), CI(
			"CREDIT INSTITUTION"), ACP("ACCREDITED CREDIT PROVIDERS"), PSB(
			"POST OFFICE SAVING BANK"), MEB("MERCHANT BANK"), MOB(
			"MORTGAGE BANK"), AH("ACCEPTANCE HOUSES"), FH("FINANCE HOUSES"), DH(
			"DISCOUNT HOUSE");

	String institution_type_codes;

	private TYPEOFINSTITUTION(String institution_type_codes) {
		this.institution_type_codes = institution_type_codes;
	}
}
