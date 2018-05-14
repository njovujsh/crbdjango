/*  1:   */ package crb.constantvalues.microflags;
/*  2:   */ 
/*  3:   */ public enum ACTIONONRULE
/*  4:   */ {
/*  5: 4 */   RR("Reject Record"),  ISP("Inform Submitting PI"),  CL("Clear");
/*  6:   */   
/*  7:   */   String actiontaken;
/*  8:   */   
/*  9:   */   public String getActiontaken()
/* 10:   */   {
/* 11: 6 */     return this.actiontaken;
/* 12:   */   }
/* 13:   */   
/* 14:   */   public void setActiontaken(String actiontaken)
/* 15:   */   {
/* 16:10 */     this.actiontaken = actiontaken;
/* 17:   */   }
/* 18:   */   
/* 19:   */   private ACTIONONRULE(String actiontaken)
/* 20:   */   {
/* 21:16 */     this.actiontaken = actiontaken;
/* 22:   */   }
/* 23:   */ }

