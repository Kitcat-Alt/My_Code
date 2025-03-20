public class Lion extends Animal{
    private boolean criniere;
    private String nom;
    private double poid;
    private String nomEnclos;

    public Lion(String nom, double poid, String nomEnclos){
        super(nom,poid,nomEnclos);
        this.criniere = false;
    }
}
