import java.util.List;
import java.util.ArrayList;

public class CaseIntelligente extends Case{
    private List<Case> lesVoisines;

    public CaseIntelligente(){
        super();
        this.lesVoisines = new ArrayList<>();
    }

    public void ajouteVoisine(Case uneCase){
        this.lesVoisines.add(uneCase);
    }

    public int nombreBombesVoisines(){
        int nbBombesVoisines = 0;
        for(int i = 0; i<this.lesVoisines.size(); ++i){
            if(this.lesVoisines.get(i).contientUneBombe()){
                nbBombesVoisines++;
            }
        }
        return nbBombesVoisines;
    }

    public String toString(){
        if(this.estMarquee() == false && this.estDecouverte() == false){
            return " ";

        }else if(this.estMarquee()){
            return "?";
        }else if(this.estDecouverte()){
            if(this.contientUneBombe()){
                return "@";
            }

            if(this.contientUneBombe() == false && this.nombreBombesVoisines() == 0){
                return "0";
            }

            if(this.contientUneBombe() == false && this.nombreBombesVoisines() > 0){
                return "" + this.nombreBombesVoisines();
            }
    
        }
        return "";
    }

}