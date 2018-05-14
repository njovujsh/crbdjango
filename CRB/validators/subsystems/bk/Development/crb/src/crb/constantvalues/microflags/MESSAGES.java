package crb.constantvalues.microflags;

public enum MESSAGES {

	NONENFORCMENT(new String[] {
			"There is no enforcment rule attached to this filed",
			"The Values is clear of enforcments" }),
   ENF007(
			new String[] { "Must be Date Authentic, with format YYYYMMDD(e.g. 20103102 is invalid, 20100115 is valid)" }), 
   ENF129(
			new String[] {
					"Field’s characters must be composed of only alphabetic-numeric and non-ASCII characters",
					"These are defined in section 3. Dataset Submission Status and Data Field Formats." }), 
   ENF014(
			new String[] { "Field must not be empty" }), 
			ENF069(new String[] {
			"Must be equal to one of the following",
			"CB, MDI, PI, CP, PSB, MEB, MOB, AH, FH, DH" }), 
			
   ENF068(
			new String[] {
					"Must be equal to one of the following",
					" CB001, CB002, CB003, CB004, CB005, CB006, CB007, CB008, CB009, CB010, CB011, CB013, CB014, CB015, CB016, CB017, CB018, CB019, CB020, CB021, CB022, CB023, CB024, CB025, CB026, CB027, CB028,CI001, CI002, CI003, CI004, CI005, CB006MDI001, MDI002, MDI003, MDI004, MDI005, MDI006, MDI007" }), invalid(
			new String[] { "" }), invalid_space(new String[] { "" }), invalid_empty(
			new String[] { "" }), valid(new String[] { "" }), format(
			new String[] { "This Field's Format Must Be" }), invalid_null(
			new String[] { "" }), mandatory(
			new String[] { "This Field Must Not Be Null" }), invalid_condition_mandatory(
			new String[] { "" }), invalid_unknownstatus(new String[] { "" }), ENF049(
			new String[] {
					"Field must match APPENDIX 1.18 UGANDA REGION/DISTRICT/COUNTY/SUB-COUNTY/PARISH/LOCAL COUNCIL NAMES.",
					"Check Appendix in the accompanying DSS document" }), ENF036(
			new String[] { "The PCI Country Code == UG ",
					"Thus Field must not be empty" }), ENF021(
			new String[] {
					"If entity's primary address is within a complex/building, then Field must not be empty",
					"Priority 3", "Action=Inform Submitting PI" }), ENF054(
			new String[] {
					"Field must be among Uganda Regions As Specified  in Data Submission Document.",
					"Check APPENDIX 1.26 UGANDA REGIONS in Accompaning DSS(Data Submission Specification) Document" }), ENF116(
			new String[] {
					"Field is Numeric or Decimal, and is not a Date by definition",
					"Field must be equal to or greater than 0 (negative values are not acceptable)" }), ENF065(
			new String[] {
					"Field must  be equal to one of the  Country's ISO CODES As Specified  in Data Submission Document.",
					"Check  APPENDIX 1.19 COUNTRY ISO CODES in Accompaning DSS(Data Submission Specification) Document" }), ENF084(
			new String[] {
					"Place  must be Owned, Living in as a Tenant or Others",
					"Field must be equal to either:O (for Owner) or T (for Tenant) or R (for Other)" }), ENF085(
			new String[] {
					"Person must be either Formaly Employed , Informally Employed or Self Employed",
					"Field must be equal to either:0 (for Formal Employment) or  1 (for Informal Employment) or 2 (for Self Employed) or 3 (for Unemployed)" }), ENF056(
			new String[] {
					"Field must equal to one of the INTERNATIONAL DIALLING CODES  As Specified  in Data Submission Document.",
					"Field must match APPENDIX 1.28 INTERNATIONAL DIALLING CODES in the accompanying DSS document." });

	String[] message;

	public String[] getMessage() {
		return this.message;
	}

	public void setMessage(String[] message) {
		this.message = message;
	}

	private MESSAGES(String... message) {
		this.message = message;
	}

//	public MESSAGES namexx(MESSAGES... messages) {
//		return null;
//	}
}
