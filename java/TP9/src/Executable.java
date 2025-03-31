import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Executable {
    public static void main(String[] args){
        Personne p1 = new Personne("Frieren", 1000);
        Personne p2 = new Personne("Thomas", 30);
        Personne p3 = new Personne("Deku", 18);

        List<Personne> personnes = Arrays.asList(p2,p1,p3);

        System.out.println(personnes);
        //Collections.sort(personnes);
        Collections.sort(personnes,new CompPersonneAge());
        System.out.println(personnes);

        System.out.println(BiblioPersonne.plusAgee(personnes));

        System.out.println(BiblioPersonne.ecartMinAge(personnes));
    }    
}
