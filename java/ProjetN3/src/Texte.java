import java.util.ArrayList;
import java.util.List;

public class Texte {
    private List<Lettre> listeLettre;
    
    public Texte (String lettre){
        this.listeLettre = new ArrayList<>();
        for(int i=0; i<lettre.length(); i++){
            this.listeLettre.add(new Lettre(lettre.charAt(i)));
        }
    }

    public String toString(){
        String chaine = "";
        for(int i=0; i<this.listeLettre.size(); i++){
            chaine = chaine + this.listeLettre.get(i).toChar();
        }
        return chaine;
    }

    public String toMorse(){
        String chaine = "";
        for(int i=0; i<this.listeLettre.size(); i++){
            if(i+1 == this.listeLettre.size()){
                return chaine + this.listeLettre.get(i).toMorse();
            }
            if(this.listeLettre.get(i).toNumero() == 27){
                chaine = chaine + this.listeLettre.get(i).toMorse() + "_______";
            }
            else{
                chaine = chaine + this.listeLettre.get(i).toMorse() + "___";
            }

        }
        return chaine;
    }

    public boolean contient(Lettre lettre){
        return listeLettre.contains(lettre);
    }

    public static String decode(String texteMorse){
        String texte = "";
        for(String motMorse:texteMorse.split("_______")){
            for(String lettreMorse:motMorse.split("___")){
                texte += new Lettre(lettreMorse);
                System.out.println(texte);
            }
            texte += " ";
        }
        return texte;
    }
}  
