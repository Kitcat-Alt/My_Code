import java.util.List;
import java.util.ArrayList;

public class  Maison{
    private String nom;
    private List<Sorcier> sorciers;

    public Maison(String nomMaison){
        this.nom = nomMaison;
        this.sorciers = new ArrayList<>();
    }

    /**
     * 
     * @return String : le nom de la maison
     */
    public String getNom(){
        return this.nom;
    }

    /**
     * 
     * @param nomSorcier
     * @param courage
     * @param sagesse
     * @return boolean : retourne true si le sorcier a été ajouté
     * à la maison false sinon
     */
    public boolean ajouter(String nomSorcier, int courage, int sagesse){
        Sorcier sorcier = new Sorcier(nomSorcier, courage, sagesse);
        if(this.sorciers.contains(sorcier) == false){
            this.sorciers.add(sorcier);
            return true;
        }
        else{
            return false;
        }
    }

    /**
     * 
     * @return int : le nombre d'élève dans la maison
     */
    public int nombreEleve(){
        return this.sorciers.size();
    }

    /**
     * 
     * @return boolean : renvoi true si la maison contient
     * un sorcier courageux (courage > 8)
     */
    public boolean contientCourageux(){
        for(int i = 0; i<this.sorciers.size(); ++i){
            if(this.sorciers.get(i).estCourageux() == true){
                return true;
            }
        }
        return false;
    }

    /**
     * 
     * @return Sorcier : le sorcier le moins courageux
     * de la maison
     */
    public Sorcier leMoinsCourageux(){
        Sorcier moinsCourageux = this.sorciers.get(0);
        for(int i=0; i<this.sorciers.size(); ++i){
            if(moinsCourageux.getCourage() >= this.sorciers.get(i).getCourage())
            moinsCourageux = this.sorciers.get(i);
        }
        return moinsCourageux;
    }

    /**
     * 
     * @return Sorcier : le sorcier le plus sage de 
     * la maison
     */
    public Sorcier lePlusSage(){
        Sorcier plusSage = this.sorciers.get(0);
        for(int i=0; i<this.sorciers.size(); ++i){
            if(plusSage.getSagesse() <= this.sorciers.get(i).getSagesse()){
                plusSage = this.sorciers.get(i);
            }
        }
        return plusSage;
    }

    @Override
    public boolean equals(Object obj){
        if(obj == null){return false;}
        if(obj == this){return true;}
        if(!(obj instanceof Maison)){return false;}
        Maison maison = (Maison) obj;
        return this.nom.equals(maison.getNom());
    }

    

    //public void trierParCourage(){
    //    List<Sorcier> trieParCourage = new ArrayList<>();
    //    int courage = this.sorciers.get(i).getCourage(0);
    //    trieParCourage = this.sorciers.sort(courage<? super int> c);
    // List<Sorcier> copie = new Arraylist<>(this.sorciers);
    //}
}