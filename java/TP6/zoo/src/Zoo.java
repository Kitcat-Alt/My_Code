import java.util.List;
import java.util.ArrayList;

public class Zoo {
    private String nom;
    private List<Enclos> enclos;
    private List<Animal> animaux;

    public Zoo(String nom){
        this.nom = nom;
        this.enclos = new ArrayList<>();
        this.animaux = new ArrayList<>();
    }

    public String getNom(){
        return this.nom;
    }

    public void ajouteEnclos(Enclos enclosAdd){
      if(!(enclos.contains(enclosAdd))){
            this.enclos.add(enclosAdd);
        }  
    }

    public void ajouteAnimal(Animal animal){
        if(!(animaux.contains(animal))){
            this.animaux.add(animal);
        }
    }

    @Override
    public String toString(){
        String res = " ";
        for(Animal animal : this.animaux){
            res += " " + animal.getNom() + " pèse " + animal.getPoid() + " kg,";
        }
        return "Le Zoo " + this.nom + " contient ces animaux :" + res; 
    }
}
