package crb.constantvalues.enf;

public enum ENF086 {
	Male(0), Female(1);

	int gender;

	private ENF086(int gender) {
		this.gender = gender;
	}
}
