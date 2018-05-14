package crb.constantvalues.microflags;

import crb.constantvalues.ENF2;

public enum DVR {
	PC1001("allTheTen", "PCI Unit_Number", STATUS.C, FORMAT.AS10, MESSAGES.ENF021, new ENF2[] { ENF2.ENF021 }),
	PCI002("allTheTen", "PCI Unit Name",STATUS.C, FORMAT.AS50, MESSAGES.ENF021, new ENF2[] { ENF2.ENF021 }),
	PCI003("allTheTen", "PCI Floor Number", STATUS.C, FORMAT.AS10, MESSAGES.ENF021, new ENF2[] { ENF2.ENF021 }),
	
	PCI004("allTheTen","PCI Plot or Street Number", STATUS.O, FORMAT.A10, MESSAGES.NONENFORCMENT, new ENF2[] { ENF2.NONENFORCMENT }), 
	
	PCI005("allTheTen", "PCI LC or Street Name", STATUS.O, FORMAT.A50, MESSAGES.NONENFORCMENT, new ENF2[] { ENF2.NONENFORCMENT }), 
	PCI006("allTheTen", "PCI Parish", STATUS.C, FORMAT.A50, MESSAGES.ENF049,new ENF2[] { ENF2.ENF036, ENF2.ENF049 }), 
	PCI007("allTheTen","PCI Suburb", STATUS.O, FORMAT.A50, MESSAGES.NONENFORCMENT,new ENF2[] { ENF2.NONENFORCMENT }), 
	PCI008("allTheTen","PCI Village", STATUS.O, FORMAT.A50, MESSAGES.NONENFORCMENT,new ENF2[] { ENF2.NONENFORCMENT }), PCI009("allTheTen","PCI County or Town", STATUS.C, FORMAT.A50, MESSAGES.ENF036,new ENF2[] { ENF2.ENF036, ENF2.ENF049 }), 
	PCI010("allTheTen","PCI District", STATUS.C, FORMAT.A50, MESSAGES.ENF036, new ENF2[] {ENF2.ENF036, ENF2.ENF049 }), 
	PCI011("allTheTen","PCI Region", STATUS.C, FORMAT.N1, MESSAGES.ENF036, new ENF2[] {ENF2.ENF036, ENF2.ENF054, ENF2.ENF116 }), 
	PCI012("allTheTen", "PCI PO Box Number", STATUS.C, FORMAT.A10,MESSAGES.ENF014, new ENF2[] { ENF2.ENF014 }), 
	PCI013("allTheTen","PCI Post Office Town", STATUS.C, FORMAT.A20, MESSAGES.ENF014,new ENF2[] { ENF2.ENF014 }), 
	PCI014("allTheTen","PCI Country Code", STATUS.M, FORMAT.A2, MESSAGES.ENF014,new ENF2[] { ENF2.ENF065, ENF2.ENF014 }), PCI015("allTheTen","PCI Period At Address", STATUS.M, FORMAT.N3, MESSAGES.ENF014, new ENF2[] { ENF2.ENF014, ENF2.ENF116 }), 
	
	PCI016("allTheTen", "PCI Flag of Ownership", STATUS.M, FORMAT.A1, MESSAGES.ENF084, new ENF2[] { ENF2.ENF084 }), 
	PCI017("allTheTen","PCI Primary Number Country Dialling Code", STATUS.M, FORMAT.N5,MESSAGES.ENF056, new ENF2[] { ENF2.ENF056, ENF2.ENF116 }), 
	PCI018("allTheTen", "PCI Primary Number Telephone Number", STATUS.M, FORMAT.N10, MESSAGES.ENF116, new ENF2[] { ENF2.ENF116 }), 
	PCI019("allTheTen", "PCI Other Number Country Dialling Code", STATUS.C,FORMAT.N5, MESSAGES.ENF116, new ENF2[] { ENF2.ENF116, ENF2.ENF056 }), 
	PCI020("allTheTen", "PCI Other Number Telephone Number", STATUS.C,FORMAT.N10, MESSAGES.ENF116, new ENF2[] { ENF2.ENF116 }), 
	PCI021("allTheTen", "PCI Mobile Number Country Dialling Code", STATUS.C,FORMAT.N5, MESSAGES.ENF056, new ENF2[] { ENF2.ENF116, ENF2.ENF056 }), 
	PCI022("allTheTen", "PCI Mobile Number Telephone Number", STATUS.C,FORMAT.N10, MESSAGES.ENF116, new ENF2[] { ENF2.ENF116 }), 
	PCI023("allTheTen", "PCI Facsimile Country Dialling Code", STATUS.C,FORMAT.N5, MESSAGES.ENF116, new ENF2[] { ENF2.ENF116, ENF2.ENF056 }), 
	PCI024("allTheTen", "PCI Facsimile Number", STATUS.C, FORMAT.N10,MESSAGES.ENF116, new ENF2[] { ENF2.ENF116 }), 
	PCI025("allTheTen","PCI Email Address", STATUS.C, FORMAT.AS50, MESSAGES.ENF129,new ENF2[] { ENF2.ENF129 }), 
	PCI026("allTheTen", "PCI Website",STATUS.C, FORMAT.AS50, MESSAGES.ENF129, new ENF2[] { ENF2.ENF129 }), 
	PI001("PI", "PI Identification Code", STATUS.M, FORMAT.A6,MESSAGES.ENF068, new ENF2[] { ENF2.ENF068 }), 
	PI002("PI","Institution Type", STATUS.M, FORMAT.A3, MESSAGES.ENF069,new ENF2[] { ENF2.ENF069 }), 
	PI003("PI", "Institution Name",STATUS.M, FORMAT.AS100, MESSAGES.ENF129, new ENF2[] { ENF2.ENF014,ENF2.ENF129 }), 
	PI004("PI", "License Issuing Date",STATUS.M, FORMAT.N8, MESSAGES.ENF007, new ENF2[] { ENF2.ENF014,ENF2.ENF007 });

	String allTheTen = "allTheTen";
	String dataset;
	String data_filed;
	STATUS status;
	FORMAT format;
	MESSAGES reasons;
	ENF2[] enforcmentcodes;

	private DVR(String dataset, String data_filed, STATUS status,
			FORMAT format, MESSAGES reasons, ENF2... enforcmentcodes) {
		this.dataset = dataset;
		this.data_filed = data_filed;
		this.status = status;
		this.format = format;
		this.reasons = reasons;
		this.enforcmentcodes = enforcmentcodes;
	}

	public String getDataset() {
		return this.dataset;
	}

	public void setDataset(String dataset) {
		this.dataset = dataset;
	}

	public String getData_filed() {
		return this.data_filed;
	}

	public void setData_filed(String data_filed) {
		this.data_filed = data_filed;
	}

	public STATUS getStatus() {
		return this.status;
	}

	public void setStatus(STATUS status) {
		this.status = status;
	}

	public FORMAT getFormat() {
		return this.format;
	}

	public void setFormat(FORMAT format) {
		this.format = format;
	}

	public MESSAGES getReasons() {
		return this.reasons;
	}

	public void setReasons(MESSAGES reasons) {
		this.reasons = reasons;
	}

	public ENF2[] getEnforcmentcodes() {
		return this.enforcmentcodes;
	}

	public void setEnforcmentcodes(ENF2[] enforcmentcodes) {
		this.enforcmentcodes = enforcmentcodes;
	}
}
