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

    


    
}