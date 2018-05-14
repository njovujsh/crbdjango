/*  1:   */ package crb.datasets;
/*  2:   */ 
/*  3:   */ import crb.constantvalues.BRANCHTYPE;
/*  4:   */ import crb.inherited.HEADER;
/*  5:   */ import crb.inherited.PCI;
/*  6:   */ import java.util.Date;
/*  7:   */ 
/*  8:   */ public class IB
/*  9:   */   extends HEADER
/* 10:   */ {
/* 11:   */   String pi_identification_code;
/* 12:   */   String branch_identification_code;
/* 13:   */   String branch_name;
/* 14:   */   BRANCHTYPE branchtype;
/* 15:   */   Date date_opened;
/* 16:   */   PCI primary_contact_information;
/* 17:   */   
/* 18:   */   public IB(String pi_identification_code, String institution_name, String submission_date, String version_number, String creation_date, String file_identifier)
/* 19:   */   {
/* 20:37 */     super(pi_identification_code, institution_name, submission_date, version_number, creation_date, "IB");
/* 21:   */   }
/* 22:   */ }


/* Location:           D:\Crb Java\
 * Qualified Name:     crb.datasets.IB
 * JD-Core Version:    0.7.0.1
 */