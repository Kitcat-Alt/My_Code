public class Serpent extends Animal{
    private String nom;
    private double poid;
    private String nomEnclos;
    private boolean venimeux; 

    public Serpent(String nom, double poid, String nomEnclos, boolean venimeux){
        super(nom, poid,nomEnclos);
        this.venimeux = venimeux;
    }

    @Override
    public String  toString(){
        String res = "non venimeux";
        if(this.venimeux){
            res = "est venimeux";
        }
        return "Serpent " + this.nom + " pèse : " + this.poid + res;
    }
}
