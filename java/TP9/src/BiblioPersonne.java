import java.util.Collections;
import java.util.List;

public class BiblioPersonne {
    public static void trierParPRenom(List<Personne> l){
        Collections.sort(l);
    }
    
    public static Personne plusAgee(List<Personne> l){
        CompPersonneAge cpa = new CompPersonneAge();
        return Collections.max(l,cpa);
    }

    public static int ecartMinAge(List<Personne> l){
        int ecartMin = l.get(0).getAge() - l.get(1).getAge();
        Collections.sort(l);
        for(int i=0; i<l.size()-1;++i){
            if(l.get(i).getAge() - l.get(i+1).getAge() >= ecartMin){
                ecartMin = l.get(i).getAge() - l.get(i+1).getAge();
            }
        }
        return ecartMin;
    }
}
