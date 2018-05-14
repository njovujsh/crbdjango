package crb.constantvalues.microflags;

/*  3:   */public enum ADDRESSBUILDING
/* 4: */{
	/* 5: 4 */YESNO("NO");
	/* 6: */
	/* 7: */String yesno;

	/* 8: */
	/* 9: */private ADDRESSBUILDING(String yesno)
	/* 10: */{
		/* 11: 8 */this.yesno = yesno;
		/* 12: */}

	/* 13: */
	/* 14: */public String getYesno()
	/* 15: */{
		/* 16:12 */return this.yesno;
		/* 17: */}

	/* 18: */
	/* 19: */public void setYesno(String yesno)
	/* 20: */{
		/* 21:16 */this.yesno = yesno;
		/* 22: */}
	/* 23: */
}
