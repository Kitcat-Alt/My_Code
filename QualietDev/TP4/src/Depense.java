class Depense{
    private Personne pers;
    private double montant; 
    private String produit;
    public Depense(Personne p, double mont, String prod ){
	this.pers = p; this.montant = mont; this.produit = prod;
    }
    public Personne getPersonne() {return this.pers;}
    public double getMontant() {return this.montant;}
    public String getProduit() {return this.produit;}

    public String toString(){
        return this.produit + " " + this.montant + " euros " + this.pers;
    }
}
