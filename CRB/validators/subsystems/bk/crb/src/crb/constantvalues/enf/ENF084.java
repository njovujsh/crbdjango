package crb.constantvalues.enf;

public enum ENF084 {
	O("Ownership"), T("Tenant"), R("Other");

	String ownership;

	private ENF084(String ownership) {
		this.ownership = ownership;
	}
}
