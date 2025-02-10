import java.util.ArrayList;
import java.util.List;

public class Cave{
    private List<Bouteille> cave;

    public Cave(){
        this.cave = new ArrayList<>();
    }

    public void ajouteBouteille(String region, String appellation, int millesime){
        this.cave.add(new Bouteille(region, appellation, millesime));
    }

    public int nbBouteilles(){
        return this.cave.size();
    }

    public int nbBouteillesDeRegion(String region){
        int cpt = 0;
        for(int i=0; i<this.cave.size(); i++){
            if(this.cave.get(i).getRegion().equals(region)){
                cpt++;
            }
        }
        return cpt;
    }

    public Bouteille plusVielleBouteille(){
        Bouteille plusVielle = this.cave.get(0);
        int annee = this.cave.get(0).getMillesime();
        
        for(int i=0; i<this.cave.size(); i++){
            if(this.cave.get(i).getMillesime() <= annee){
                plusVielle = this.cave.get(i);
                annee = this.cave.get(i).getMillesime();
            }
        }
        return plusVielle;
    }
}