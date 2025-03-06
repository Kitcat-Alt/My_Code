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

    public Sorcier leMoinsCourageux(){
        Sorcier moinsCourageux = this.sorciers.get(0);
        for(int i=0; i<this.sorciers.size(); ++i){
            if(moinsCourageux.getCourage() > this.sorciers.get(i).getCourage())
            moinsCourageux = this.sorciers.get(i);
        }
        return moinsCourageux;
    }

    public Sorcier lePlusSage(){
        Sorcier plusSage = this.sorciers.get(0);
        for(int i=0; i<this.sorciers.size(); ++i){
            if(plusSage.getSagesse() < this.sorciers.get(i).getSagesse()){
                plusSage = this.sorciers.get(i);
            }
        }
        return plusSage;
    }
}