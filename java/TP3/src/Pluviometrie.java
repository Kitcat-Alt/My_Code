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
    public int quantiteTotale(){
        int totalQuantite = 0;
        for(int i=0; i<this.precipitations.size(); i++){
            if(this.precipitations.get(i) != null){
                totalQuantite += (int) this.precipitations.get(i);
            }
        }
        return totalQuantite;
    }

    /**
     * 
     * @return
     */
    public int quantiteMax(){
        int maxQuantite = 0;
        for(int i = 0; i<this.precipitations.size(); i++){
            if(this.precipitations.get(i) != null && this.precipitations.get(i) > maxQuantite){
                maxQuantite = this.precipitations.get(i);
            }
        }
        return maxQuantite;
    }

    /**
     * 
     * @return
     */
    public boolean estPluvieuse(){
        boolean semainePluvieuse = false;
        for(int i = 0; i<this.precipitations.size()-1; i++){
            if(this.precipitations.get(i) != null && this.precipitations.get(i+1) != null){
                if(this.precipitations.get(i) != 0 && this.precipitations.get(i+1) != 0){
                    return true;
                }
            }
        }
        return semainePluvieuse;
    }
}
