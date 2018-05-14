package crb.pojos;

import crb.constantvalues.microflags.MESSAGES;

public class TestingConcepts {
	String[] mytrings;
	Object hdh;

	public static void main(String[] args) {
		TestingConcepts bsbs = new TestingConcepts();

		// ADDRESSBUILDING.YESNO.setYesno("YES");
		// System.out.println(ADDRESSBUILDING.YESNO.getYesno() + " ");
		// System.out.println(ADDRESSBUILDING.YESNO);
		String[] msg = MESSAGES.ENF021.getMessage();
		System.out.print(msg[1]);
//		for (String string : msg) {
//			System.out.println(string);
//		}

	}

	public void field_validator(String data_dss_dvr, Object value) {
		this.hdh = null;
		if (this.hdh.toString().equals(null)) {
			System.out.print("haaa");
		}
	}
}
