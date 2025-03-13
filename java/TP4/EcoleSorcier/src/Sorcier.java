public class Sorcier{
    private String nom;
    private int sagesse;
    private int courage;

    public Sorcier(String nom, int courage, int sagesse){
        this.nom = nom;
        this.sagesse = sagesse;
        this.courage = courage;
    }

    /**
     * 
     * @return String : le nom du sorcier
     */
    public String getNom(){
        return this.nom;
    }

    /**
     * 
     * @return int : le courage du sorcier
     */
    public int getCourage(){
        return this.courage;
    }

    /**
     * 
     * @return int : la sagesse du sorcier
     */
    public int getSagesse(){
        return this.sagesse;
    }

    /**
     * 
     * @return boolean : true si le sorcier a un
     * courage supérieur à 8 false sinon
     */
    public boolean estCourageux(){
        return this.courage > 8;
    }

    @Override
    public boolean equals(Object obj){
        if(obj == null){return false;}
        if(obj == this){return true;}
        if(!(obj instanceof Sorcier)){return false;}
        Sorcier sorcier = (Sorcier) obj;
        return sorcier.getNom().equals(this.getNom()) && sorcier.getCourage() == this.getCourage() && sorcier.getSagesse() == this.getSagesse();
    }

    @Override
    public String toString(){
        return "Nom: "+this.nom+" Courage: "+this.courage+" Sagesse: "+this.sagesse;
    }
}