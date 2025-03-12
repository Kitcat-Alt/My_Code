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
        Maison plusGrande = this.maisons.get(0);
        for(int i=0; i<this.maisons.size(); ++i){
            if(plusGrande.nombreEleve() < this.maisons.get(i).nombreEleve()){
                plusGrande = this.maisons.get(i);
            }
        }
        return plusGrande;
    }

    //public List lesCourageux(){
    //    List courageux = new ArrayList<>();
    //    List lescourageux = new ArrayList<>();
    //    for(int i=0; i<this.maisons.size(); ++i){
    //        courageux = this.maisons.get(i);
    //        for(int j = 0; j<courageux.size(); ++i){
    //            if(courageux.get(i).estCourageux()){
    //                lescourageux.add(courageux.get(i));
    //            }
    //        }
    //    }
    //    return lescourageux;
    //}
}