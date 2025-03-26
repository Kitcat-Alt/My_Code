public class Lion extends Animal{
    private boolean criniere;
    private String nom;
    private double poid;
    private String nomEnclos;

    public Lion(String nom, double poid, String nomEnclos, boolean criniere){
        super(nom,poid,nomEnclos);
        this.criniere = criniere;
    }

    @Override
    public String  toString(){
        String res = "sans crinière";
        if(this.criniere){
            res = "possede une crinière";
        }
        return "Lion " + this.nom + " pèse : " + this.poid + res;
    }
}
