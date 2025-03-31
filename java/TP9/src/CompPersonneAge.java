import java.util.Comparator;

public class CompPersonneAge implements Comparator<Personne>{
    @Override
    public int compare(Personne p1, Personne p2){
        return p1.getAge() - p2.getAge();
    }
}
