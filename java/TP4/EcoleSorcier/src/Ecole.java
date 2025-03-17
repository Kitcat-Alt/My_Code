import java.util.List;
import java.util.ArrayList;

public class Ecole{
    private String nom;
    private List<Maison> maisons;

    public Ecole(String nom){
        this.nom = nom;
        this.maisons = new ArrayList<>();
    }

    /**
     * @param Maison
     */
    public void ajouter(Maison maison){
        this.maisons.add(maison);
    }

    /**
     * @return Maison : la maison avec le plus d'élèves
     */
    public Maison plusGrandeMaison(){
        Maison plusGrande = null;
        for(int i=0; i<this.maisons.size(); ++i){
            if(plusGrande == null || plusGrande.nombreEleve() < this.maisons.get(i).nombreEleve()){
                plusGrande = this.maisons.get(i);
            }
        }
        return plusGrande;
    }

    public static List lesCourageux(){
        List<Sorcier> courageux = new ArrayList<>();
        for(Sorcier sorcier : Maison.sorciers){
            if(sorcier.estCourageux()){
                courageux.add(sorcier);
            }
        }
        return courageux;
    }

    
}