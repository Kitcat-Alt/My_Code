import java.util.List;
import java.util.ArrayList;

public class CaseIntelligente extends Case{
    private List<Case> lesVoisines;

    public CaseIntelligente(){
        super();
        this.lesVoisines = new ArrayList<>();
    }

    public void ajouteVoisine(Case uneCase){

    }

    public int nombreBombesVoisines(){
        return 0;
    }

    public String toString(){
        return " ";
    }
}
