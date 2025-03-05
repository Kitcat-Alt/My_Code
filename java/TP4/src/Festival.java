import java.util.List;
import java.util.ArrayList;

public class Festival {
    private String nom;
    private String adresse;
    private List<Concert> concerts;
    private List<Billet> billets;

    public Festival(String nom){
        this.nom = nom;
    }
    
    public Festival(String nom, String adresse){
        this.nom = nom;
        this.adresse = adresse;
        this.concerts = new ArrayList<>();
        this.billets = new ArrayList<>();
    }

    public List getConcert(){
        return this.concerts;
    }

    public void reserver(Spectateur spectateur, Concert concert, int prix){
        this.billets.add(new Billet(concert, spectateur, prix));
    }

    public int nombreBilletConcert(Concert concert){
        int nbBillets = 0;
        for(int i=0; i<this.billets.size(); ++i){
            if(this.billets.get(i).getConcert().equals(concert)){
                ++nbBillets;
            }
        }
        return nbBillets;
    }

    public int nombreConcert(){
        return this.concerts.size();
    }

    


    
}