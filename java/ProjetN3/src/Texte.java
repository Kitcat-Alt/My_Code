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
            if(i+1 == this.ListeLettre.size()){
                return chaine + this.ListeLettre.get(i).toMorse();
            }
            if(this.ListeLettre.get(i).toNumero() == 27){
                chaine = chaine + this.ListeLettre.get(i).toMorse() + "_______";
            }
            else{
                chaine = chaine + this.ListeLettre.get(i).toMorse() + "___";
            }

        }
        return chaine;
    }

    public boolean contient(Lettre lettre){
        return ListeLettre.contains(lettre);
    }
}  
