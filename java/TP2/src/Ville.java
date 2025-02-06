import java.util.ArrayList;
import java.util.List;

public class Ville {
    private String nom;
    private List<Magasin> magasins;
    /**
     * 
     * @param nom
     */
    public Ville(String nom){
        this.nom = nom;
        this.magasins = new ArrayList<>();
    }

    /**
     * 
     * @param nom
     * @param lundi
     * @param dimanche
     */
    public void ajouteMagasin(String nom, boolean lundi, boolean dimanche){
        this.magasins.add(new Magasin(nom, lundi, dimanche));
    }

    /**
     * 
     * @return la liste des magasins ouvert le lundi
     */
    public List<Magasin> ouvertsLeLundi(){
        List<Magasin> magasin = new ArrayList<>();
        for(int i=0; i<this.magasins.size(); i++){
            if(this.magasins.get(i).getOuvertLundi()){
                magasin.add(this.magasins.get(i));
            }
        } 
        return magasin;
    }

    @Override
    public String toString(){
        String res = "Liste des Magasins de " + this.nom + " :";
        for(int i = 0; i<this.magasins.size(); i++){
            res += this.magasins.get(i) +  "";
        }
        res += "\n";
        return res;
    }
}
