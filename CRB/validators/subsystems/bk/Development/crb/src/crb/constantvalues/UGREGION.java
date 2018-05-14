package crb.constantvalues;

public enum UGREGION {
	zero(

	"CENTRAL"), one("WESTERN"), two("EASTERN"), four("KARAMOJA"), five(
			"ACHOLI(NORTHAN)"), six("LANGO(NORTHAN)"), seven("WEST NILE");

	String ugregion;

	private UGREGION(String ugregion) {
		this.ugregion = ugregion;
	}
}
