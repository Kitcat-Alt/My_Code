public class Sorcier{
    private String nom;
    private int sagesse;
    private int courage;

    public Sorcier(String nom, int sagesse, int courage){
        this.nom = nom;
        this.sagesse = sagesse;
        this.courage = courage;
    }

    public String getNom(){
        return this.nom;
    }

    public int getCourage(){
        return this.courage;
    }

    public int getSagesse(){
        return this.sagesse;
    }

    public boolean estCourageux(){
        return this.courage > 8;
    }

    public boolean equals(Object obj){
        if(obj == null){return false;}
        if(obj == this){return true;}
        if(!(obj instanceof Sorcier)){return false;}
        Sorcier sorcier = (Sorcier) obj;
        return sorcier.getNom().equals(this.getNom()) && sorcier.getCourage() == this.getCourage() && sorcier.getSagesse() == this.getSagesse();
    }
}