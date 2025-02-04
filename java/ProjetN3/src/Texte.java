import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Texte {
    private List<Lettre> ListeLettre;
    
    public Texte (String lettre){
        for(int i=0; i<lettre.length(); i++){
            this.ListeLettre.add(new Lettre(lettre.charAt(i)));
        }
    }
}  
