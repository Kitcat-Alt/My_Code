import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Lettre {
    private char lettre;
    static List<String> alphabetMorse = Arrays.asList("=_===", 
            "===_=_=_=", "===_===_=", "===_=_=", "=", "=_=_===_=",
            "===_===_=", "=_=_=_=", "=_=", "=_===_===_===", "===_=_===",
            "=_===_=_=", "===_===", "===_=", "===_===_===", "=_===_===_=",
            "===_===_=_===", "=_===_=", "=_=_=", "===", "=_=_===",
            "=_=_=_===", "=_===_===", "===_=_=_===", "===_=_===_===",
            "===_===_=_=", "_");
    
    private List<Character> alphabet = Arrays.asList('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ');


    public Lettre(char lettre){
        this.lettre = lettre;
    }

    public Lettre(String morse){
        this.lettre = alphabet.get(alphabetMorse.indexOf(morse));
    }

    public int toNumero(){
        return alphabet.indexOf(this.lettre);
    }

    public char toChar(){
        return this.lettre;
    }

    public String toMorse(){
        return alphabetMorse.get(alphabet.indexOf(this.lettre));
    }

    @Override
    public String toString(){
        return "";
    }

    @Override
    public boolean equals(Object objet){
        if (objet == null) {return false;}
        if(objet == this) {return true;}
        if(!(objet instanceof Lettre)) {return false;}
        Lettre tmp = (Lettre) objet;
        return tmp.toChar() == this.lettre;
     }

}

