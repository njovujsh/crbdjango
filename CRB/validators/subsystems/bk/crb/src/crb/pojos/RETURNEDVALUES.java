package crb.pojos;

import crb.constantvalues.microflags.DVR;
import crb.constantvalues.microflags.MESSAGES;

public class RETURNEDVALUES {
	MESSAGES[] value;
	DVR infornation_of_returned_value;

	public Object getValue() {
		return this.value;
	}

	public void setValue(MESSAGES... value) {
		this.value = value;
	}

	public DVR getInfornation_of_returned_value() {
		return this.infornation_of_returned_value;
	}

	public void setInfornation_of_returned_value(
			DVR infornation_of_returned_value) {
		this.infornation_of_returned_value = infornation_of_returned_value;
	}
}
