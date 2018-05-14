package crb.constantvalues.enf;

public enum ENF085
{
  FormalEmployment(0, "Formal Employment"),  InformalEmployment(1, 
    "Informal Employment"),  SelfEmployed(2, "Self Employed"),  Unemployed(
    3, "Unemployed");
  
  String employmentstatus;
  int employmentstatuscode;
  
  private ENF085(int employmentstatuscode, String employmentstatus) {}
}
