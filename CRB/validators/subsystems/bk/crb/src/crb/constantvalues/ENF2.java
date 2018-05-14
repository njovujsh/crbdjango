package crb.constantvalues;

import crb.constantvalues.microflags.ACTIONONRULE;

public enum ENF2 {
    ENF007(2, ACTIONONRULE.RR), 
    ENF001(1, ACTIONONRULE.RR), 
    ENF002(2,ACTIONONRULE.RR),
    ENF068(2, ACTIONONRULE.RR), 
    ENF069(2,ACTIONONRULE.RR), 
    ENF129(1, ACTIONONRULE.RR), 
    ENF014(2,ACTIONONRULE.RR), 
    ENF025(3, ACTIONONRULE.ISP), 
    ENF021(3,ACTIONONRULE.ISP), 
    ENF036(2, ACTIONONRULE.RR), 
    ENF049(3,ACTIONONRULE.ISP), 
    ENF054(2, ACTIONONRULE.RR), 
    ENF116(2,ACTIONONRULE.RR), 
    ENF065(2, ACTIONONRULE.RR), 
    ENF084(2,ACTIONONRULE.RR), 
    ENF085(2, ACTIONONRULE.RR), 
    ENF086(2,ACTIONONRULE.RR), 
    ENF056(2, ACTIONONRULE.RR), 
    NONENFORCMENT(0,ACTIONONRULE.CL);

    int priolity;
    ACTIONONRULE action_onrule;

    public ACTIONONRULE getAction_onrule() {
        return this.action_onrule;
    }

    public void setAction_onrule(ACTIONONRULE action_onrule) {
        this.action_onrule = action_onrule;
    }

    public int getPriolity() {
        return this.priolity;
    }

    public void setPriolity(int priolity) {
        this.priolity = priolity;
    }

    private ENF2(int priolity, ACTIONONRULE action_onrule) {
        this.priolity = priolity;
        this.action_onrule = action_onrule;
    }
}
