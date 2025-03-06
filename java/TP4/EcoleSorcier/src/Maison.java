import java.util.List;
import java.util.ArrayList;

public class  Maison{
    private String nom;
    private List<Sorcier> sorciers;

    public Maison(String nomMaison){
        this.nom = nomMaison;
        this.sorciers = new ArrayList<>();
    }

    public boolean ajouter(String nomSorcier, int courage, int sagesse){
        Sorcier sorcier = new Sorcier(nomSorcier, sagesse, courage);
        if(this.sorciers.contains(sorcier) == false){
            this.sorciers.add(sorcier);
            return true;
        }
        else{
            return false;
        }
    }

    public int nombreEleve(){
        return this.sorciers.size();
    }

    public boolean contientCourageux(){
        for(int i = 0; i<this.sorciers.size(); ++i){
            if(this.sorciers.get(i).estCourageux() == true){
                return true;
            }
        }
        return false;
    }
}