import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Pluviometrie {
    private int annee;
    private int semaine;
    static List<Integer> precipitations = Arrays.asList(null, null, null, null, null, null, null);

    /**
     * 
     * @param annee
     * @param semaine
     */
    Pluviometrie(int annee, int semaine){
        this.annee = annee;
        this.semaine = semaine;
    }

    /**
     * 
     * @param jour
     * @param pluie
     */
    public void setPrecipitation(int jour, int pluie) {
       this.precipitations.set(jour, pluie);
    }

    /**
     * 
     * @param jour
     * @return
     */
    public Integer getPluie(int jour){
        return this.precipitations.get(jour);
    }

    /**
     * 
     * @return
     */
    public Integer quantiteTotale(){
        Integer totalQuantite = 0;
        for(int i=0; i<this.precipitations.size(); i++){
            if(this.precipitations.get(i) != null){
                totalQuantite += this.precipitations.get(i).getPluie(i);
            }
        }
        return totalQuantite;
    }

    /**
     * 
     * @return
     */
    public int quantiteMax(){
        return 0;
    }

    /**
     * 
     * @return
     */
    public boolean estPluvieuse(){
        return false;
    }
}
