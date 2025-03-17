import java.util.ArrayList;
import java.util.List;
import java.util.Random;

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
        for(int i=0; i<this.cases.size(); ++i){
            for(int j=0; j<this.cases.size(); ++j){
                for(int x=i-1; x<i+1; ++x){
                    for(int y=j-1; y<j+1; ++y){
                        this.cases.get(i).get(j).ajouteVoisine(this.cases.get(x).get(y));
                    }
                }
            }
        }
    }

    protected void poseDesBombesAleatoirement(){
        Random rand = new Random();
        int borneMax = 100;
        for(int i=0; i<this.cases.size(); ++i){
            for(int j=0; j<this.cases.size(); ++j){
                if(rand.nextInt(borneMax) < this.pourcentageDeBombe){
                    this.cases.get(i).get(j).poseBombe();
                }    
            }
        }
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
        return this.cases.get(numLigne).get(numColonne);

    }

    public int getNbCasesMarquees(){
        int nbCasesMarquees = 0;
        for(int i=0; i<this.cases.size(); ++i){
            for(int j=0; j<this.cases.size(); ++j){
                if(this.cases.get(i).get(j).estMarquee()){
                    nbCasesMarquees++;
                }
            }
        }
        return nbCasesMarquees;
    }

    public void poseBombe(int x, int y){
        this.cases.get(x).get(y).poseBombe();
    }

    public void reset(){
        for(int i=0; i<this.cases.size(); ++i){
            for(int j=0; j<this.cases.size(); ++j){
                this.cases.get(i).get(j).reset();
            }
        }
        this.nbBombes = 0;  
    }
}