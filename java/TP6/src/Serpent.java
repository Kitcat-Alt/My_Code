public class Serpent extends Animal{
    private String nom;
    private double poid;
    private String nomEnclos;
    private boolean venimeux; 

    public Serpent(String nom, double poid, String nomEnclos){
        super(nom, poid,nomEnclos);
        this.venimeux = false;
    }
}
