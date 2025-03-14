public class Executable {
    public static void main(String [] args) {
	    Personne pierre = new Personne("Durand","Pierre"); 
	    System.out.println(pierre.getNom()); 
	    Personne paul = new Personne("Dupond","Paul"); 
	    Personne marie = new Personne("Dumond","Marie");
	    Personne anne = new Personne("Dunon","Anne");  
	    Depense d1 = new Depense(pierre, 12, "pain"); 	
	    Depense d2 = new Depense(paul, 100, "pizza"); 
	    Depense d3 = new Depense(pierre, 70, "essence");
	    Depense d4 = new Depense(marie, 15, "vin");  
	    Depense d5 = new Depense(paul, 10, "vin"); 
	    WeekEnd we = new WeekEnd();  
	    we.ajouterPersonne(pierre); 
	    we.ajouterPersonne(paul);
	    we.ajouterPersonne(marie);
	    we.ajouterPersonne(anne); 
	    we.ajouterDepense(d1);   
	    we.ajouterDepense(d2); 
	    we.ajouterDepense(d4);   
	    we.ajouterDepense(d3);
	    we.ajouterDepense(d5);
	    System.out.println("total des dépenses "+we.totalDepenses()) ;
	    System.out.println("moyenne des dépenses "+we.depensesMoyenne()) ;
	    System.out.println("total des dépenses de Pierre "+ we.totalDepensesPersonne(pierre)) ;
	    System.out.println("total des dépenses de Paul "+ we.totalDepensesPersonne(paul)) ;
	    System.out.println("total des dépenses de Marie "+ we.totalDepensesPersonne(marie)) ;
	    System.out.println("total des dépenses de Anne "+ we.totalDepensesPersonne(anne)) ;
	    System.out.println("depenses vin "+we.depenseProduit("vin"));
	    System.out.println("avoir de pierre "+we.avoirPersonne(pierre));
	    System.out.println("avoir de paul "+we.avoirPersonne(paul));	
	    System.out.println("avoir de marie "+we.avoirPersonne(marie));
    }
}
