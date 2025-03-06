import java.util.List;
import java.util.ArrayList;

public class Ecole{
    private String nom;
    private List<Maison> maisons;

    public Ecole(String nom){
        this.nom = nom;
        this.maisons = new ArrayList<>();
    }

    public void ajouter(Maison maison){
        this.maisons.add(maison);
    }

    public Maison plusGrandeMaison(){
        Maison plusGrande = this.maisons.get(0);
        for(int i=0; i<this.sorciers.size(); ++i){
            if(plusGrande.nombreEleve() < this.maisons.get(i).nombreEleve()){
                plusGrande = this.maisons.get(i);
            }
        }
        return plusGrande;
    }

    public List lesCourageux(){
        List<Sorciers> courageux = new ArrayList<>();
        for(int i=0; i<this.maisons.size(); ++i){
            for()
        }
    }
}