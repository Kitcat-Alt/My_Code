public class Case {
    private boolean contientUneBombe;
    private boolean estDecouverte;
    private boolean estMarquee;

    public Case(){
        this.contientUneBombe = false;
        this.estDecouverte = false;
        this.estMarquee = false;
    }

    public void reset(){
        this.contientUneBombe = false;
        this.estDecouverte = false;
        this.estMarquee = false;
    }

    public void poseBombe(){
        this.contientUneBombe = true;
    }

    public boolean contientUneBombe(){
        return this.contientUneBombe;
    }

    public boolean estDecouverte(){
        return this.estDecouverte();
    }

    public boolean estMarquee(){
        return this.estMarquee();
    }

    public boolean reveler(){
        if(this.estDecouverte){
            return false;
        }
        this.estDecouverte = true;
        return true;
    }

    public void marquer(){
        this.estMarquee = true;
    }
}
