import java.util.ArrayList;
import java.util.List;

public class Plateau{
    private int nbLignes;
    private int nbColonnes;
    private int pourcentageDeBombe;
    private int nbBombes;
    private List<List<CaseIntelligente>> cases;

    public Plateau(int nbLignes, int nbColonnes, int pourcentage){
        this.nbLignes = nbLignes;
        this.nbColonnes = nbColonnes;
        this.pourcentageDeBombe = pourcentage;
        this.nbBombes = 0;
        this.cases = new ArrayList<>();
        for(int i = 0; i<this.nbColonnes; ++i){
            this.cases.add(new ArrayList<>());
        }
    }

    private void creerLesCasesVides(){
        for(int i = 0; i<this.nbColonnes; ++i){
            for(int j = 0; j<this.nbLignes; ++j){
                this.cases.get(i).add(new CaseIntelligente());
            }
        }
    }

    private void rendLesCasesIntelligentes(){
        
    }

    protected void poseDesBombesAleatoirement(){

    }

    public int getNbLignes() {
        return this.nbLignes;
    }

    public int getNbColonnes(){
        return this.nbColonnes;
    }

    public int getNbTotalBombes(){
        return this.nbBombes;
    }

    public CaseIntelligente getCase(int numLigne, int numColonne){
        return null;

    }

    public int getNbCasesMarquees(){
        return 0;
    }

    public void poseBombe(int x, int y){
        
    }

    public void reset(){

    }
}