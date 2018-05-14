package crb.datasets;

import java.util.Date;

import crb.inherited.HEADER;
import crb.inherited.PCI;

public class PI extends HEADER {

	public PI(String pi_identification_code, String institution_name,
			String submission_date, String version_number,
			String creation_date, String file_identifier) {
		super(pi_identification_code, institution_name, submission_date,
				version_number, creation_date, file_identifier);
	}

	String pi_identification_code;
	String institution_type;
	String institution_name;
	Date license_issuing_date;
	PCI primary_contact_information;

	public String getPi_identification_code() {
		return this.pi_identification_code;
	}

	public void setPi_identification_code(String pi_identification_code) {
		this.pi_identification_code = pi_identification_code;
	}

	public String getInstitution_type() {
		return this.institution_type;
	}

	public void setInstitution_type(String institution_type) {
		this.institution_type = institution_type;
	}

	public String getInstitution_name() {
		return this.institution_name;
	}

	public void setInstitution_name(String institution_name) {
		this.institution_name = institution_name;
	}

	public Date getLicense_issuing_date() {
		return this.license_issuing_date;
	}

	public void setLicense_issuing_date(Date license_issuing_date) {
		this.license_issuing_date = license_issuing_date;
	}

	public PCI getPrimary_contact_information() {
		return this.primary_contact_information;
	}

	public void setPrimary_contact_information(PCI primary_contact_information) {
		this.primary_contact_information = primary_contact_information;
	}

	public static void main(String... strings) {
	}
}
