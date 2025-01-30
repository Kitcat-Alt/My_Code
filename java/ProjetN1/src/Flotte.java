import java.util.ArrayList;
import java.util.List;

public class Flotte {
    private String nom;
    private List<Vaisseau> vaisseaux;   

    public Flotte(){
        this.nom = "Nouvelle Flotte";
        this.vaisseaux = new ArrayList<>();
    }

    public Flotte(String nom){
        this.nom = nom;
        this.vaisseaux = new ArrayList<>();
    }

    public void ajoute(Vaisseau vaisseau){
        this.vaisseaux.add(vaisseau);
    }

    public void ajoute(String nom, int puissance){
        this.vaisseaux.add(new Vaisseau(nom, puissance));

    }

    public void ajoute(String nom, int puissance, int passagers){
        this.vaisseaux.add(new Vaisseau(nom, puissance, passagers));
    }

    public int totalPuissance(){
        int totalPuissance = 0;
        for(int i=0; i<this.vaisseaux.size(); i++){
             totalPuissance += this.vaisseaux.get(i).getPuissance();
        }
        return totalPuissance;
    }

    public int nombreVaisseaux(){
        return this.vaisseaux.size();
    }

    public String getNom(){
        return this.nom;
    }

    public int nombreDeVaisseauxSansPassagers(){
        int vaisseauxSansPassagers = 0;
        for(int i=0; i<this.vaisseaux.size(); i++){
            if (this.vaisseaux.get(i).getNombrePassagers() == 0){
                vaisseauxSansPassagers++;
            }
        }
        return vaisseauxSansPassagers;
    }

    public int puissanceDeFeuMax(){
        int puissanceDeFeuMaxCpt = 0;
        for(int i=0; i<this.vaisseaux.size(); i++){
            if(puissanceDeFeuMaxCpt <= this.vaisseaux.get(i).getPuissance()){
                puissanceDeFeuMaxCpt = this.vaisseaux.get(i).getPuissance();
            }
        }
        return puissanceDeFeuMaxCpt;
    }
}
