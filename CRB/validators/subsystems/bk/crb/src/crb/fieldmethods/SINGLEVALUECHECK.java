/*  1:   */ package crb.fieldmethods;
/*  2:   */ 
/*  3:   */ public class SINGLEVALUECHECK<T>
/*  4:   */ {
/*  5:   */   T value_type_to_be_validated;
/*  6:   */   
/*  7:   */   public SINGLEVALUECHECK(T value_type_to_be_validated)
/*  8:   */   {
/*  9: 7 */     this.value_type_to_be_validated = value_type_to_be_validated;
/* 10:   */   }
/* 11:   */   
/* 12:   */   public T getValue_type_to_be_validated()
/* 13:   */   {
/* 14:13 */     Object snsn = new Object();
/* 15:   */     
/* 16:15 */     return this.value_type_to_be_validated;
/* 17:   */   }
/* 18:   */   
/* 19:   */   public void setValue_type_to_be_validated(T value_type_to_be_validated)
/* 20:   */   {
/* 21:19 */     this.value_type_to_be_validated = value_type_to_be_validated;
/* 22:   */   }
/* 23:   */ }


/* Location:           D:\Crb Java\
 * Qualified Name:     crb.fieldmethods.SINGLEVALUECHECK
 * JD-Core Version:    0.7.0.1
 */