import java.util.List;
import java.util.ArrayList;


public class Depense {
    private double montant;
    private String produit;
    private Personne payeur;

    public Depense(Personne personne, double montant, String produit){
        this.payeur = personne;
        this.montant = montant;
        this.produit = produit;
    }

    public String getProduit(){
        return this.produit;
    }

    public double getMontant(){
        return this.montant;
    }
}
