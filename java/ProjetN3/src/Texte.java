import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Texte {
    private List<Lettre> ListeLettre;
    
    public Texte (String lettre){
        this.ListeLettre = new ArrayList<>();
        for(int i=0; i<lettre.length(); i++){
            this.ListeLettre.add(new Lettre(lettre.charAt(i)));
        }
    }

    public String toString(){
        String chaine = "";
        for(int i=0; i<this.ListeLettre.size(); i++){
            chaine = chaine + this.ListeLettre.get(i).toChar();
        }
        return chaine;
    }

    public String toMorse(){
        String chaine = "";
        for(int i=0; i<this.ListeLettre.size(); i++){
            chaine = chaine + this.ListeLettre.get(i).toMorse();
        }
        return chaine;
    }
}  
