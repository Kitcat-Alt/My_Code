import java.util.List;
import java.util.ArrayList;


public class WeekEnd {
    private String dateDuWeekEnd;
    private List<Personne> personnes;
    private List<Depense> depenses;

    public WeekEnd(String date){
        this.dateDuWeekEnd = date;
        this.personnes = new ArrayList<>();
        this.depenses = new ArrayList<>();
    }

    public void ajoutePerticipant(String prenom, int age){
        Personne personne = new Personne(prenom, age);
        if(!(personnes.contains(personne))){
            this.personnes.add(personne);
        }
    }

    public void ajouteDepense(double montant, String produit, String prenom){
            for(Personne pers : personnes){
                if(pers.getPrenom().equals(prenom)){
                    this.depenses.add(new Depense(pers, montant, produit));
                }
            }
    }

    public double totalDepense(Personne personne){
        for(Depense dep : depenses){
            if(dep)
        }
    }

}
