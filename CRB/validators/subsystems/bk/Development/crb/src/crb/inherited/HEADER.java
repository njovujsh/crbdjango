package crb.inherited;

public class HEADER {
	String pi_identification_code;
	String institution_name;
	String submission_date;
	String version_number;
	String creation_date;
	String file_identifier;

	public String getPi_identification_code() {
		return this.pi_identification_code;
	}

	public void setPi_identification_code(String pi_identification_code) {
		this.pi_identification_code = pi_identification_code;
	}

	public String getInstitution_name() {
		return this.institution_name;
	}

	public void setInstitution_name(String institution_name) {
		this.institution_name = institution_name;
	}

	public String getSubmission_date() {
		return this.submission_date;
	}

	public void setSubmission_date(String submission_date) {
		this.submission_date = submission_date;
	}

	public String getVersion_number() {
		return this.version_number;
	}

	public void setVersion_number(String version_number) {
		this.version_number = version_number;
	}

	public String getCreation_date() {
		return this.creation_date;
	}

	public void setCreation_date(String creation_date) {
		this.creation_date = creation_date;
	}

	public String getFile_identifier() {
		return this.file_identifier;
	}

	public void setFile_identifier(String file_identifier) {
		this.file_identifier = file_identifier;
	}

	public HEADER(String pi_identification_code, String institution_name,
			String submission_date, String version_number,
			String creation_date, String file_identifier) {
		this.pi_identification_code = pi_identification_code;
		this.institution_name = institution_name;
		this.submission_date = submission_date;
		this.version_number = version_number;
		this.creation_date = creation_date;
		this.file_identifier = file_identifier;
	}
}
