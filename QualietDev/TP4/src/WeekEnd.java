import java.util.ArrayList;
import java.util.List; 

public class WeekEnd{
    private List<Personne> listeAmis;
    private List<Depense> listeDepenses;

    public WeekEnd(){
		this.listeAmis = new ArrayList<>();
		this.listeDepenses = new ArrayList<>();
    }
	
    public List<Personne> getAmis() {
		return this.listeAmis;
    }

    public List<Depense> getDepenses() {
		return this.listeDepenses;
    }
    
    public void ajouterPersonne(Personne p){this.listeAmis.add(p);}
    
	public void ajouterDepense(Depense d){this.listeDepenses.add(d); }
    
	// totalDepensesPersonne prend en entrée une personne et renvoie la somme des depenses de cette personne.
    public double totalDepensesPersonne(Personne p){
		double s = 0.0;
		for(Depense d : this.listeDepenses) {
			if((p.getNom()).equals(d.getPersonne().getNom()))
			s += d.getMontant();
		}
		return s;
    }

    // totalDepenses renvoie la somme de toutes les dépenses. 
    public double totalDepenses(){
		double s = 0.0; 
		for(Depense d : this.listeDepenses) 
			s += d.getMontant();
		return s;
    }

    // depensesMoyenne renvoie la moyenne des dépenses pour une personne 
    public double depensesMoyenne(){
		double s = totalDepenses(); 
		int nb = this.listeAmis.size(); 
		if(nb != 0) 
			return s/nb;
		else 
			return s; 
    }

    //depenseProduit prend en entrée un produit, et renvoie la somme des dépenses pour ce produit. (par exemple du pain peut avoir été acheté plusieurs fois..)
    public double depenseProduit(String p){
		double s = 0.0; 
		for(Depense d : this.listeDepenses) 
			if (p.equals(d.getProduit()))
			s+= d.getMontant();
		return s;
    } 

    // avoirPersonne prend en entrée une personne et renvoie l'avoir de cette personne pour le week end.
    public double avoirPersonne(Personne p){
		double m = depensesMoyenne(); 
		double avoir = m - totalDepensesPersonne(p); 
		return avoir; 
    }
}

