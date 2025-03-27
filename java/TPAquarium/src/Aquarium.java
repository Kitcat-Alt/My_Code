import java.util.List;
import java.util.ArrayList;

public class Aquarium {
    private List<PetitPoisson> petitspoissons;
    private List<GrosPoisson> grospoissons;
    private List<Algue> algues;
    private List<Bulle> bulles;

    public Aquarium(){
        this.petitspoissons = new ArrayList<>();
        this.grospoissons = new ArrayList<>();
        this.algues = new ArrayList<>();
        this.bulles = new ArrayList<>();

    }

    public int getHauteur(){
        return 50;
    }

    public int getLargeur(){
        return 120;
    }

    public Dessin getDessin(){
        PetitPoisson possion = new PetitPoisson(10, 10, 2);
        Dessin aquarium = new Dessin();
        String couleur = "0x0000F0";
        aquarium.ajouteChaine(10, 10, "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", couleur);
        return aquarium;
    }

    public void evolue(){
        
    }

}
